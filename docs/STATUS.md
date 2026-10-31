# STATUS — SchoolLA

**Обновлено:** 2026-10-31 (сессия Cowork «Maryland», правки сайта по просьбе Эдварда — см. JOURNAL)

## Что сейчас на live
- https://tosmedia.github.io/schoolLA/ собирается из `main`.
- `index.html` в `main` совпадает с файлом в `~/Documents/Claude/Maryland` (сверка по blob-sha после каждого пуша).
- Рабочая папка на Маке: `~/Documents/Claude/Maryland`. `~/Desktop/SchoolLA` — устаревшая копия.
- Страница сейчас: шапка (оранжевый логотип Fredoka, номер +1 (747) 744-7888, кнопка «Send a message»),
  hero из трёх строк, фото дома, расписание с иконками, FAQ (6 вопросов),
  контакты (номер, «Please call before 12 noon or after 6 p.m.», кнопка «Send a message» → окно письма на annapoghos58@gmail.com), подвал (часы Mon–Fri 12:00–6:00 p.m., ссылка «Privacy & cookies»), плашка cookies с Accept и окно Privacy.
- Дни без школы — по договорённости с Анной минимум за 2 дня.

## Проверки
`python3 tools/check_site.py`: 24 проверки. **FAIL 1, WARN 0**:
- FAIL: 3 хот-линка на `d8j0ntlcm91z4.cloudfront.net` (см. проблему 1).

## Открытые проблемы
1. **3 картинки хот-линкуются с Higgsfield CDN.** Если CDN удалит файлы, они пропадут с сайта.
   Готовые jpg лежат только в артефакте https://claude.ai/artifact/XDVwcWf8Z2Zqb73SRPfdw8.
   Нужны в `photos/`: homework-table, homework-three-kids, notebook-hands
   (таблица CDN-имя → файл — в JOURNAL за 2026-10-03 и в истории STATUS). Бинарные файлы — push только с Мака.
2. **Окно обратного звонка `contactModal`** больше ничем не открывается (кнопку «Come see the house» убрали). Удалить или вернуть кнопку — решает Эдвард.
3. **DBA** «Maryland Family Child Care» не зарегистрировано.
4. **Логотип:** на знаке 6 точек при вместимости 8.
5. **Мусор на Маке:** `~/Desktop/SchoolLA/_to_delete/`, старые `poghosyan-*.html` в Загрузках (копии есть в `_archive/`).

## Следующие шаги
1. Перенести 3 фото в репо.
2. Решить судьбу `contactModal`.
