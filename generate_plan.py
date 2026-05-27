#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from datetime import datetime, timedelta

# Новый список книг с информацией об обязательности
# Формат: (Автор, Название, Обязательно, примерное количество слов)
books = [
    ("А.С. Пушкин", "Сказка о мертвой царевне и о семи богатырях", True, 6500),
    ("И.А. Крылов", "Волк и журавль, Квартет", False, 1500),
    ("В.Ф. Одоевский", "Городок в табакерке", False, 4000),
    ("В. Гаршин", "Сказка о жабе и розе", False, 2500),
    ("М.Ю. Лермонтов", "Ашик-Кериб", False, 5000),
    ("А.П. Чехов", "Мальчики", False, 4500),
    ("С.Т. Аксаков", "Аленький цветочек", False, 12000),
    ("Л. Андреев", "Кусака", False, 3500),
    ("В. Бианки", "Оранжевое горлышко", False, 3000),
    ("Д.Н. Мамин-Сибиряк", "Приёмыш", False, 5500),
    ("А.И. Куприн", "Барбос и Жулька", False, 4000),
    ("В.П. Астафьев", "Стрижонок Скрип", False, 4500),
    ("П.П. Ершов", "Конёк-Горбунок", True, 25000),
    ("П.П. Бажов", "Серебряное копытце", False, 6000),
    ("Е. Шварц", "Сказка о потерянном времени", False, 8000),
    ("Р. Брэдбери", "Все лето в один день", False, 4000),
    ("К.Г. Паустовский", "Корзина с еловыми шишками, Дремучий медведь", False, 9000),
    ("М.М. Зощенко", "Ёлка", False, 3500),
    ("Б.С. Житков", "Как я ловил человечков", False, 7000),
    ("Г.Х. Андерсен", "Русалочка", False, 15000),
    ("А. Сент-Экзюпери", "Маленький принц", True, 18000),
    ("В. Драгунский", "Главные реки, Что любит Мишка", False, 5000),
    ("А. Толстой", "Золотой ключик, или Приключения Буратино", True, 45000),
    ("Д. Барри", "Питер Пен", False, 35000),
    ("Ф. Баум", "Страна Оз", False, 40000),
    ("Т. Янссон", "Сказки про Муми-тролля", False, 30000),
    ("А. Линдгрен", "Малыш и Карлсон", True, 50000),
    ("Е. Велтистов", "Приключения Электроника", False, 55000),
    ("К. Булычев", "Путешествия Алисы", True, 40000),
    ("М. Твен", "Приключения Тома Сойера", True, 75000),
    ("Д. Свифт", "Путешествия Гулливера", False, 80000),
    ("Н. Носов", "Приключения Незнайки и его друзей", True, 65000),
]

# Параметры чтения
WORDS_PER_MINUTE = 90
READING_MINUTES_PER_DAY = 60  # 1 час
WORDS_PER_DAY = WORDS_PER_MINUTE * READING_MINUTES_PER_DAY  # 5400 слов в день

# Период чтения: 27 мая - 1 сентября 2026
START_DATE = datetime(2026, 5, 27)
END_DATE = datetime(2026, 9, 1)

# Расчет дней для каждой книги
reading_schedule = []
current_date = START_DATE

for author, title, required, word_count in books:
    days_needed = max(1, (word_count + WORDS_PER_DAY - 1) // WORDS_PER_DAY)
    
    for day_offset in range(days_needed):
        reading_date = current_date + timedelta(days=day_offset)
        if reading_date > END_DATE:
            break
        reading_schedule.append({
            'date': reading_date,
            'author': author,
            'title': title,
            'required': required,
            'day_in_book': day_offset + 1,
            'total_days': days_needed
        })
    
    current_date += timedelta(days=days_needed)
    if current_date > END_DATE:
        break

# Генерация HTML
def get_color_for_book(author, title, required, idx):
    colors = [
        "#e74c3c", "#3498db", "#9b59b6", "#1abc9c", "#f39c12",
        "#2ecc71", "#e67e22", "#95a5a6", "#16a085", "#d35400",
        "#7f8c8d", "#27ae60", "#8e44ad", "#c0392b", "#2980b9",
        "#f1c40f", "#34495e", "#9b59b6", "#1abc9c", "#e74c3c",
        "#3498db", "#2ecc71", "#e67e22", "#95a5a6", "#16a085",
        "#d35400", "#7f8c8d", "#27ae60", "#8e44ad", "#c0392b",
    ]
    return colors[idx % len(colors)]

# Группировка по датам
from collections import defaultdict
schedule_by_date = defaultdict(list)
for item in reading_schedule:
    schedule_by_date[item['date']].append(item)

# Генерация календаря
month_names = {
    5: "Май", 6: "Июнь", 7: "Июль", 8: "Август", 9: "Сентябрь"
}

day_names = ["Пн", "Вт", "Ср", "Чт", "Пт", "Сб", "Вс"]

html_content = '''<!DOCTYPE html>
<html lang="ru">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Летнее чтение: Переход в 3 класс</title>
    <style>
        body {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            background-color: #f4f7f6;
            color: #333;
            margin: 0;
            padding: 20px;
        }
        .container {
            max-width: 1400px;
            margin: 0 auto;
            background: white;
            padding: 30px;
            border-radius: 10px;
            box-shadow: 0 4px 15px rgba(0,0,0,0.1);
        }
        h1 {
            text-align: center;
            color: #2c3e50;
        }
        h2 {
            text-align: center;
            color: #7f8c8d;
            font-size: 1.2em;
            margin-bottom: 30px;
        }
        .info-box {
            background-color: #e8f4fd;
            border-left: 5px solid #2196F3;
            padding: 15px;
            margin-bottom: 20px;
            border-radius: 4px;
        }
        .book-list {
            margin-bottom: 30px;
        }
        .book-list h3 {
            color: #2c3e50;
            border-bottom: 2px solid #3498db;
            padding-bottom: 10px;
        }
        .book-list table {
            width: 100%;
            border-collapse: collapse;
            margin-top: 10px;
        }
        .book-list th, .book-list td {
            padding: 8px 12px;
            text-align: left;
            border-bottom: 1px solid #ddd;
        }
        .book-list th {
            background-color: #f8f9fa;
            font-weight: bold;
        }
        .book-list tr:hover {
            background-color: #f5f5f5;
        }
        .required-mark {
            color: #e74c3c;
            font-weight: bold;
        }
        .calendar-grid {
            display: grid;
            grid-template-columns: repeat(7, 1fr);
            gap: 8px;
            margin-top: 20px;
        }
        .calendar-header {
            background-color: #2c3e50;
            color: white;
            padding: 10px;
            text-align: center;
            font-weight: bold;
            border-radius: 4px;
        }
        .day-cell {
            background-color: #fff;
            border: 1px solid #ddd;
            border-radius: 4px;
            padding: 8px;
            min-height: 120px;
            display: flex;
            flex-direction: column;
        }
        .day-cell.empty {
            background-color: #f9f9f9;
            border-color: #eee;
        }
        .day-date {
            font-weight: bold;
            color: #2c3e50;
            margin-bottom: 6px;
            font-size: 0.85em;
            text-align: center;
        }
        .reading-block {
            font-size: 0.7em;
            padding: 3px 5px;
            border-radius: 3px;
            margin-bottom: 3px;
            color: #fff;
            text-shadow: 0 1px 2px rgba(0,0,0,0.3);
            flex-grow: 1;
            display: flex;
            flex-direction: column;
            justify-content: center;
            text-align: center;
        }
        .reading-title {
            font-weight: bold;
            margin-bottom: 2px;
        }
        .reading-author {
            font-size: 0.85em;
            opacity: 0.9;
        }
        .required-badge {
            display: inline-block;
            padding: 1px 4px;
            font-size: 0.7em;
            border-radius: 3px;
            background-color: rgba(255,255,255,0.3);
            color: white;
            margin-top: 2px;
            font-weight: bold;
        }
        .footer {
            margin-top: 30px;
            text-align: center;
            font-size: 0.9em;
            color: #777;
        }
        @media (max-width: 1024px) {
            .calendar-grid {
                grid-template-columns: repeat(5, 1fr);
            }
        }
        @media (max-width: 768px) {
            .calendar-grid {
                grid-template-columns: repeat(3, 1fr);
            }
        }
        @media (max-width: 480px) {
            .calendar-grid {
                grid-template-columns: 1fr;
            }
        }
    </style>
</head>
<body>

<div class="container">
    <h1>План летнего чтения: 2-3 класс</h1>
    <h2>Календарь чтения: 27 мая — 1 сентября 2026</h2>
    
    <div class="info-box">
        <p><strong>Расчет:</strong> Скорость чтения 90 слов/мин × 1 час = 5400 слов в день. Количество дней для каждой книги рассчитано исходя из её объема.</p>
    </div>

    <div class="book-list">
        <h3>Список книг</h3>
        <table>
            <tr>
                <th>№</th>
                <th>Автор</th>
                <th>Произведение</th>
                <th>Статус</th>
            </tr>
'''

# Добавляем список книг
for idx, (author, title, required, word_count) in enumerate(books, 1):
    status = '<span class="required-mark">Обязательно</span>' if required else ''
    html_content += f'''            <tr>
                <td>{idx}</td>
                <td>{author}</td>
                <td>{title}</td>
                <td>{status}</td>
            </tr>
'''

html_content += '''        </table>
    </div>

    <div class="calendar-grid">
        <div class="calendar-header">Пн</div>
        <div class="calendar-header">Вт</div>
        <div class="calendar-header">Ср</div>
        <div class="calendar-header">Чт</div>
        <div class="calendar-header">Пт</div>
        <div class="calendar-header">Сб</div>
        <div class="calendar-header">Вс</div>
'''

# Заполнение календаря
current_date = START_DATE
# Находим первый день недели (0 = понедельник)
first_weekday = START_DATE.weekday()

# Пустые ячейки до начала месяца
for i in range(first_weekday):
    html_content += '        <div class="day-cell empty"></div>\n'

book_index = 0
while current_date <= END_DATE:
    date_str = current_date.strftime("%d %B")
    # Русские названия месяцев
    month_ru = {
        'May': 'мая', 'June': 'июня', 'July': 'июля', 
        'August': 'августа', 'September': 'сентября'
    }
    month_name = current_date.strftime("%B")
    date_display = f"{current_date.day} {month_ru.get(month_name, month_name)}"
    
    readings = schedule_by_date.get(current_date, [])
    
    html_content += f'        <div class="day-cell">\n'
    html_content += f'            <div class="day-date">{date_display}</div>\n'
    
    for reading in readings:
        color = get_color_for_book(reading['author'], reading['title'], reading['required'], book_index)
        required_badge = '<div class="required-badge">Обязательно</div>' if reading['required'] else ''
        
        # Показываем только в первый день чтения книги
        if reading['day_in_book'] == 1:
            html_content += f'''            <div class="reading-block" style="background-color: {color};">
                <div class="reading-title">{reading['title']}</div>
                <div class="reading-author">{reading['author']}</div>
                {required_badge}
            </div>
'''
            book_index += 1
    
    html_content += '        </div>\n'
    
    current_date += timedelta(days=1)

html_content += '''    </div>

    <div class="footer">
        <p>Счастливого чтения!</p>
    </div>
</div>

</body>
</html>
'''

with open('/workspace/index.html', 'w', encoding='utf-8') as f:
    f.write(html_content)

print("План чтения успешно обновлен!")
print(f"Всего книг: {len(books)}")
print(f"Обязательных книг: {sum(1 for _, _, req, _ in books if req)}")
print(f"Период: {START_DATE.strftime('%d.%m.%Y')} - {END_DATE.strftime('%d.%m.%Y')}")
