#!/usr/bin/env python3
"""Проверки сайта Maryland Family Child Care (SchoolLA).

Запуск из корня проекта:  python3 tools/check_site.py
Код выхода 0 — всё зелёное, 1 — есть FAIL. WARN не роняет прогон.

Правило: каждая починка добавляет сюда проверку, которая ловит именно эту поломку.
"""
import os
import re
import sys
from html.parser import HTMLParser

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
INDEX = os.path.join(ROOT, "index.html")

PHONE_MAIN = "+17477447888"          # (747) 744-7888 — телефон для родителей
PHONE_LICENSING = "+13239813350"     # CDSS Monterey Park Regional Office — не наш, но легитимен
ALLOWED_EXTERNAL = ("https://fonts.googleapis.com", "https://fonts.gstatic.com")

results = []


def check(name, ok, detail="", warn=False):
    status = "PASS" if ok else ("WARN" if warn else "FAIL")
    results.append((status, name, detail))


class Collector(HTMLParser):
    def __init__(self):
        super().__init__()
        self.imgs, self.refs, self.text = [], [], []
        self._skip = 0

    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        if tag in ("style", "script"):
            self._skip += 1
        if tag == "img":
            self.imgs.append(a)
        for key in ("src", "href", "poster"):
            if a.get(key):
                self.refs.append((tag, key, a[key]))
        if a.get("srcset"):
            for part in a["srcset"].split(","):
                self.refs.append((tag, "srcset", part.strip().split(" ")[0]))

    def handle_endtag(self, tag):
        if tag in ("style", "script") and self._skip:
            self._skip -= 1

    def handle_data(self, data):
        if not self._skip:
            self.text.append(data)


def main():
    if not os.path.exists(INDEX):
        print("FAIL  index.html не найден в", ROOT)
        return 1
    html = open(INDEX, encoding="utf-8").read()
    p = Collector()
    p.feed(html)
    text = re.sub(r"\s+", " ", " ".join(p.text))

    # 1. Внешние ресурсы: только Google Fonts. Картинки — только из репо (решение 2026-09-13).
    css_urls = re.findall(r"url\(\s*['\"]?([^'\")]+)", html)
    external = [r for _, k, r in p.refs if r.startswith(("http://", "https://"))
                and not r.startswith(ALLOWED_EXTERNAL) and k != "href"]
    external += [u for u in css_urls if u.startswith(("http://", "https://"))]
    check("нет хот-линков картинок/ресурсов на внешние CDN", not external,
          f"{len(external)} внешних: " + ", ".join(sorted({re.sub(r'^https?://([^/]+).*', r'\1', u) for u in external})))

    # 2. Все локальные файлы, на которые ссылается страница, существуют.
    local = [r for _, k, r in p.refs if not re.match(r"^(https?:|mailto:|tel:|sms:|#|data:)", r)]
    local += [u for u in css_urls if not re.match(r"^(https?:|data:|#)", u)]
    missing = sorted({r for r in local if not os.path.exists(os.path.join(ROOT, r.split("#")[0].split("?")[0]))})
    check("все локальные картинки/файлы на месте", not missing, ", ".join(missing))

    # 3. У каждой картинки есть alt.
    no_alt = [i.get("src", "?") for i in p.imgs if "alt" not in i]
    check("у всех <img> есть alt", not no_alt, ", ".join(no_alt))

    # 4. Телефоны: родительский есть, чужих нет.
    tels = set(re.findall(r'(?:tel|sms):([+\d]+)', html))
    check("телефон (747) 744-7888 есть в tel:/sms:", PHONE_MAIN in tels)
    check("нет посторонних телефонов", tels <= {PHONE_MAIN, PHONE_LICENSING},
          ", ".join(sorted(tels - {PHONE_MAIN, PHONE_LICENSING})))

    # 5. Вместимость 8, возраст 5–13 (решение 2026-08-27, «не шесть»).
    check("вместимость 8 указана", re.search(r"\b(8|eight)\b", text, re.I) is not None)
    check("возраст 5–13 указан", re.search(r"5\s*(–|-|&ndash;|to)\s*13", text) is not None)
    check("нигде не написано «six children / up to 6»",
          re.search(r"\b(six|6)\s+(children|kids)\b|up to (six|6)\b", text, re.I) is None)

    # 6. Цен на сайте нет (решение 2026-08-27).
    prices = re.findall(r"\$\s?\d[\d,]*", text)
    check("на странице нет цен", not prices, ", ".join(prices[:5]))

    # 7. Утром в школу не отвозим — нигде не обещаем.
    bad = [m.group(0) for m in re.finditer(
        r"[^.]*\b(?:drop(?:-| )off at school|take (?:them|your child) to school|before[- ]school care)\b[^.]*",
        text, re.I)]
    bad = [b for b in bad if not re.search(r"\b(not|no|don't|do not)\b", b, re.I)]
    check("нет обещаний утреннего ухода / отвоза в школу", not bad)

    # 8. Название бренда.
    check("бренд «Maryland Family Child Care» на странице", "Maryland Family Child Care" in text)
    check("старое имя SPARK не всплыло", "SPARK" not in html)

    # 9. GitHub Pages: .nojekyll на месте.
    check(".nojekyll в корне", os.path.exists(os.path.join(ROOT, ".nojekyll")))

    # 10. Файлы состояния проекта на месте.
    for f in ("PROJECT_CONTEXT.md", "STATUS.md", "JOURNAL.md", "WORKFLOW.md"):
        check(f"docs/{f} существует", os.path.exists(os.path.join(ROOT, "docs", f)))

    # WARN — известные, но не решённые вопросы.
    check("email на сайте соответствует бренду", "poghosyanchildcare.com" not in html,
          "всё ещё hello@poghosyanchildcare.com", warn=True)

    width = max(len(n) for _, n, _ in results)
    for status, name, detail in results:
        print(f"{status:4}  {name.ljust(width)}  {detail}".rstrip())
    fails = sum(1 for s, _, _ in results if s == "FAIL")
    warns = sum(1 for s, _, _ in results if s == "WARN")
    print(f"\nИтого: {len(results)} проверок, FAIL {fails}, WARN {warns}")
    return 1 if fails else 0


if __name__ == "__main__":
    sys.exit(main())
