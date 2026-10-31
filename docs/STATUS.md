# STATUS — SchoolLA

**Обновлено:** 2026-10-31 (сессия Cowork «Maryland», правки сайта по просьбе Эдварда — см. JOURNAL)

## Что сейчас на live
- https://tosmedia.github.io/schoolLA/ собирается из `main`.
- `index.html` в `main` совпадает с файлом в `~/Documents/Claude/Maryland` (сверка по blob-sha после каждого пуша).
- Рабочая папка на Маке: `~/Documents/Claude/Maryland`. `~/Desktop/SchoolLA` — устаревшая копия.
- Страница сейчас: шапка (оранжевый логотип Fredoka, номер +1 (747) 744-7888, кнопка «Send a message»),
  hero из трёх строк, фото дома, расписание с иконками, фото двора, FAQ (8 вопросов), фото крючков,
  контакты (номер, «Please call before 12 noon or after 6 p.m.», SMS, окно письма), подвал (часы Mon–Fri 12:00–6:00 p.m.).
- Дни без школы — по договорённости с Анной минимум за 2 дня.

## Проверки
`python3 tools/check_site.py`: 23 проверки. **FAIL 1, WARN 1**:
- FAIL: 5 хот-линков на `d8j0ntlcm91z4.cloudfront.net` (см. проблему 1).
- WARN: email `hello@poghosyanchildcare.com` не соответствует бренду.

## Открытые проблемы
1. **5 картинок хот-линкуются с Higgsfield CDN.** Если CDN удалит файлы, они пропадут с сайта.
   Готовые jpg лежат только в артефакте https://claude.ai/artifact/XDVwcWf8Z2Zqb73SRPfdw8.
   Нужны в `photos/`: homework-table, homework-three-kids, notebook-hands, backyard-golden-hour, backpacks-hooks
   (таблица CDN-имя → файл — в JOURNAL за 2026-10-03 и в истории STATUS). Бинарные файлы — push только с Мака.
2. **Email для формы.** Письма из окна «Send a message» уходят на `hello@poghosyanchildcare.com` — неизвестно, работает ли ящик. Нужен адрес от Эдварда.
3. **Окно обратного звонка `contactModal`** больше ничем не открывается (кнопку «Come see the house» убрали). Удалить или вернуть кнопку — решает Эдвард.
4. **DBA** «Maryland Family Child Care» не зарегистрировано.
5. **Логотип:** на знаке 6 точек при вместимости 8.
6. **Мусор на Маке:** `~/Desktop/SchoolLA/_to_delete/`, старые `poghosyan-*.html` в Загрузках (копии есть в `_archive/`).

## Следующие шаги
1. Получить адрес email и заменить его в форме и подвале.
2. Перенести 5 фото в репо.
3. Решить судьбу `contactModal`.
