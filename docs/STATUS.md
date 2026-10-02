# STATUS — SchoolLA

**Обновлено:** 2026-10-03 (сессия Cowork «Контекст проекта»)

## Что сейчас на live
- https://tosmedia.github.io/schoolLA/ собирается из `main`.
- **Последний коммит, менявший сайт:** `171516c` (2026-09-02), «Rework the page: bigger brand lockup…».
  После него в `main` идут только коммиты с документацией (`docs/`, `tools/`, `CLAUDE.md`), их список в JOURNAL.
- `index.html` в `main`: blob `87ee1a0c`, 45 760 байт. На Маке в папке SchoolLA лежит **тот же файл**
  (сверено 2026-10-03 по blob-sha).
- В репо: `index.html`, `.nojekyll`, `logo/`, `photos/house.webp`, `docs/`, `tools/check_site.py`, `CLAUDE.md`.

## Проверки
`python3 tools/check_site.py`: 18 проверок. На версии из `main` **FAIL 1, WARN 1**:
- FAIL: 7 хот-линков на `d8j0ntlcm91z4.cloudfront.net` (см. проблему 1).
- WARN: email `hello@poghosyanchildcare.com` не соответствует бренду.

## Открытые проблемы

1. **7 картинок хот-линкуются с Higgsfield CDN** (`d8j0ntlcm91z4.cloudfront.net`).
   Если CDN удалит файлы, картинки на сайте пропадут.
   - Исправление готово с 2026-09-13, но лежит **только в артефакте**
     https://claude.ai/artifact/XDVwcWf8Z2Zqb73SRPfdw8. Это 7 jpg и index.html с локальными путями.
   - На Маке этих фото нет. Архив `maryland-photos-and-index.zip`, упомянутый 2026-09-13, в папке не найден.
   - `index.html` из артефакта обёрнут в каркас артефакта, поэтому как файл сайта он не годится.
     Правильный путь: взять `index.html` из `main` и заменить в нём 7 URL по таблице ниже.
     Проверка `check_site.py` на такой версии проходит без FAIL (проверено 2026-10-03).

   | имя файла на CDN (`…/user_38tNbATsxTeaW5Nh2B2p2zEj7iM/<имя>`) | локальный файл |
   |---|---|
   | hf_20260821_153757_65bfcff3-5688-4a8d-9401-381964503143.png | photos/homework-table.jpg |
   | hf_20260821_160459_f0bdc4fc-b47b-405c-ae06-6a9bd5bccb4d.png | photos/homework-three-kids.jpg |
   | hf_20260821_153757_bc4fd702-c6f9-4a91-97c9-3ea4709ecf8f.png | photos/notebook-hands.jpg |
   | hf_20260821_160459_ce383585-0cd4-4021-a2c5-e34d821ac993.png | photos/reading-armchair.jpg |
   | hf_20260821_153757_da29e7c7-17ce-4945-90ab-795f19051dba.png | photos/reading-corner.jpg |
   | hf_20260821_160459_d5841188-1bf4-4f48-9f84-e3ca87899c58.png | photos/backyard-golden-hour.jpg |
   | hf_20260821_153757_b6909401-6d47-4d9d-9cbc-bf49f6b1f449.png | photos/backpacks-hooks.jpg |

   Порядок замены совпадает с порядком появления URL в `index.html` (сверено с артефактом).
2. **Email** `hello@poghosyanchildcare.com` не соответствует бренду. Нужен новый адрес от Эдварда.
3. **DBA** «Maryland Family Child Care» не зарегистрировано. Это вне сайта, но имя на сайте висит.
4. **Логотип:** на знаке 6 точек при вместимости 8. Вариант с 8 точками не выбран.
5. **Мусор в папке на Маке:**
   - `maryland-schoolla-project.zip` (2026-09-13) устарел, в нём старый PROJECT_CONTEXT.
   - `_to_delete/ziNqxbek` — копия того же архива (тот же размер). Ждёт удаления Эдвардом.

## Следующие шаги
1. Перенести 7 фото из артефакта в репо: скачать их из артефакта, положить в `photos/` на Маке,
   заменить URL в `index.html`, прогнать проверки, запушить (фото — бинарные, push с Мака).
2. Решить вопрос с email.
3. Удалить `_to_delete/` и устаревший zip, если Эдвард согласен.
