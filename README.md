## Лабораторна робота №3. Рівень другий

Вебзастосунок «Волинь: туристичний путівник» (Flask + Jinja2 + Tailwind CSS).

## Сторінки
- Головна (`/`)
- Про нас (`/about`)
- Місця (`/places`)
- Поради (`/tips`)

## Запуск
```bash
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
python app.py

## Запуск ngrok
.venv\Scripts\activate
python -c "from pyngrok import ngrok; print(ngrok.connect(5000)); input('Натисни Enter, щоб зупинити...')"
```
Сайт буде доступний за адресою http://127.0.0.1:5000 або адресею яку дасть ngork

## Автор
Конашук Владислав Сергійович, група ІПЗ-21