# Задача: поддержка OG/Twitter-превью для страниц p.knotta.ru

## Проблема
Страница публикуется как `srcdoc` песочного `<iframe>` внутри оболочки `https://p.knotta.ru/<slug>`. Соцсети-краулеры (Telegram, VK, Facebook, X, WhatsApp) читают мета-теги из **внешней страницы оболочки**, а не из HTML внутри iframe (в iframe они не заходят и JS не исполняют).

Сейчас оболочка отдаёт в `<head>`:
- `<title>` = общий «p.knotta.ru» (не per-page);
- **ни одного** `og:*` / `twitter:*` тега;
- сохранённый `description` в `<head>` не выводится.

Итог: при шеринге любой ссылки p.knotta превью пустое/общее. Заголовок и описание, которые уже принимает `/api/publish`, на превью не влияют.

## Цель
Дать публикатору задавать соц-метаданные так, чтобы **оболочка server-side рендерила** их в первый HTML-ответ `GET /<slug>`.

## Объём работ

### 1. API `/api/publish` и `/api/page/<slug>` (+ admin-edit)
Принимать и хранить опциональные поля (всё необязательное, обратная совместимость):
- `og_title` (string, ≤ 200) — фолбэк на существующий `title`.
- `og_description` (string, ≤ 300) — фолбэк на `description`.
- `og_image` — один из вариантов:
  - **URL** на внешнюю картинку (https), ИЛИ
  - **загрузка файла** (multipart / base64), т.к. бесплатные страницы это один HTML и своего хостинга картинки у автора может не быть.
- (опц.) `og_image_alt`, `og_type` (default `website`), `theme_color`.

Если `og_image` пришёл файлом — хостить его и отдавать по стабильному URL, например `https://p.knotta.ru/api/og/<slug>.jpg` (или `/<slug>/og.jpg`).

### 2. Хранилище
Добавить колонки к записи страницы: `og_title`, `og_description`, `og_image_url`, `og_image_alt`, `theme_color`. Картинку — в тот же стораж, что и страницы.

### 3. Оболочка `GET /<slug>` — SSR мета-тегов (главное)
В серверном ответе (НЕ через JS) подставлять в `<head>`:
```html
<title>{og_title || title || "p.knotta.ru"}</title>
<meta name="description" content="{og_description || description}">
<meta property="og:type" content="{og_type || website}">
<meta property="og:title" content="{og_title || title}">
<meta property="og:description" content="{og_description || description}">
<meta property="og:url" content="https://p.knotta.ru/{slug}">
<meta property="og:image" content="{og_image_url}">
<meta property="og:image:secure_url" content="{og_image_url}">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="{og_title || title}">
<meta name="twitter:description" content="{og_description || description}">
<meta name="twitter:image" content="{og_image_url}">
```
Экранировать значения (защита от инъекций в атрибуты).

### 4. Плагин `/host-html` и `/host-edit`
Новые опциональные аргументы/флаги:
- `--og-image <path|url>` (если path — загрузить файл при публикации),
- `--og-title "<...>"`, `--og-desc "<...>"`.
При наличии — класть в тело запроса. В отчёте после публикации показывать, что og задан.

## Критерии приёмки
- `curl -s https://p.knotta.ru/<slug>` (без JS) содержит корректные `og:*` и `twitter:*` и per-page `<title>`.
- Карточка рендерится в: Telegram (`@WebpageBot`), opengraph.xyz, Facebook Sharing Debugger, VK.
- Картинка `og:image` отдаётся публично с `Content-Type: image/jpeg|png`, размер 1200×630, < 5 МБ.
- Старые страницы без og-полей работают как раньше (фолбэк на title/description, дефолтный og:image платформы — опц.).
- Значения корректно экранируются.

## Заметки
- Рекомендуемый размер og:image — 1200×630 (1.91:1), JPG/PNG. WebP некоторые краулеры (старый FB) не тянут — лучше JPG/PNG.
- Желательно дать платформенный дефолтный `og:image`, если автор не задал свой, чтобы превью не было совсем пустым.
- Пример og:image приложен: `og-cover.jpg` (1200×630).
