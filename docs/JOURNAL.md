# JOURNAL — SchoolLA

Хронологический журнал. Записи только дописываются снизу.
Формат записи: дата, сессия, что сделано и почему, коммиты, что осталось.

Записи до 2026-10-03 восстановлены по истории коммитов `main`, по PROJECT_CONTEXT от 2026-09-13
и по памяти проекта.

---

## 2026-08-21 — картинки
- По именам файлов (`hf_20260821_*`) иллюстрации сгенерированы в Higgsfield.
  Сайт подключал их хот-линками с `d8j0ntlcm91z4.cloudfront.net`.

## 2026-08-22 — первый выпуск и ребрендинг
- `bf2a0ba` Add Poghosyan Family Child Care site.
- `11b1094` Light background for the "What this isn't" section.
- `516083f` Rebrand to Maryland Family Child Care: new wordmark, house-and-six mark, favicon.
- Репо сделан публичным, потому что Pages на free-плане не работает с приватными репо.

## 2026-08-27 — контент и бренд
- `3a39921` Capacity up to 8, school pickup only, 5pm clubs, drop rates and form, phone contact.
- `d77fe6f` New hero headline: «The hours after school are the ones that build a child».
- Решения: название Maryland (SPARK отклонён), вместимость 8, возраст 5–13, без цен и формы,
  контакт по телефону (747) 744-7888. Локальный файл переименован в `index.html`.

## 2026-08-28 — фото дома
- `d762af2` Фото дома отдаётся из репо (`photos/house.webp`).
- `38f8c97` На мобильных фото дома показывается целиком, в своих пропорциях.

## 2026-09-02 — переработка страницы
- `171516c` Rework the page: bigger brand lockup with phone and address, house photo up top,
  no roster, no licence details, no timetable clock, **pickup by car**, contact modal.
- Это последний коммит, который менял сайт (на 2026-10-03).

## 2026-09-13 — потеря чата и восстановление
- Чат «SchoolLA» в Claude.ai был потерян. Контекст восстановили из папки SchoolLA и репо.
  Создан `PROJECT_CONTEXT.md` и архив `maryland-schoolla-project.zip`.
- Сессия Cowork «Сайт Maryland»: опубликован артефакт https://claude.ai/artifact/XDVwcWf8Z2Zqb73SRPfdw8.
  7 картинок с CDN вытащены через Groover, переведены в JPEG и переименованы,
  `index.html` переписан на локальные пути.
- Решение Эдварда: всё лежит в GitHub, без хот-линков.
- В репо это **не попало**: коннектор не пишет бинарные файлы, а git push из облака режет прокси.

## 2026-09-15
- Контекст проекта импортирован в память проекта Claude.

## 2026-10-03 — система сохранения контекста (сессия Cowork «Контекст проекта»)
- В `PROJECT_CONTEXT.md` на Маке дописан блок «Обновление 2026-09-13», копия положена в проект Claude.
- По просьбе Эдварда заведена система из трёх мест хранения.
  Файлы `docs/STATUS.md`, `docs/JOURNAL.md`, `docs/PROJECT_CONTEXT.md`, `docs/WORKFLOW.md`
  лежат в репо, в проекте Claude и в папке на Маке. Корневой `CLAUDE.md` указывает на них.
- `PROJECT_CONTEXT.md` переписан по фактам, сверенным с `index.html`:
  - забирают из школы **на машине**, а не пешком (так с 171516c);
  - второй телефон (323) 981-3350 принадлежит CDSS;
  - добавлены часы работы;
  - ограничения GitHub-коннектора уточнены.
- Добавлен `tools/check_site.py` на 18 проверок. Каждая проверка, ловящая поломку
  (цены, «six», утренний отвоз), испытана на подставленной поломке.
  Результат на `main`: FAIL 1 (7 хот-линков на CDN), WARN 1 (email).
- Сверено: `index.html` на Маке совпадает с `main` (blob `87ee1a0c`).
- Найдено: фото из артефакта 09-13 на Маке отсутствуют, архива `maryland-photos-and-index.zip` нет.
  Восстановлена таблица соответствия CDN-URL и локальных имён (в STATUS).
- Осталось: залить 7 фото в репо, решить вопрос с email, убрать мусорные архивы.
