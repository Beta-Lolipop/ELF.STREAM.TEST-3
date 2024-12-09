from aiogram.types import (ReplyKeyboardMarkup, KeyboardButton,
                           InlineKeyboardMarkup, InlineKeyboardButton)

# ReplyKeyboar

reg_k = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text = '/reg')]
],
                    resize_keyboard=True,
                    input_field_placeholder = 'choose in menu')

start_k = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text = '/catalog')],
    [KeyboardButton(text = '/information'), KeyboardButton(text = '/help')],
    [KeyboardButton(text = '/start')]
],
                    resize_keyboard=True,
                    input_field_placeholder = 'choose in menu')

# Inline

catalog_k = InlineKeyboardMarkup(inline_keyboard =[
[InlineKeyboardButton(text = 'PODS', callback_data = 'pods')],
[InlineKeyboardButton(text = 'CARTRIGES', callback_data = 'cartriges'),
 InlineKeyboardButton(text = 'GIGA', callback_data = 'giga')]
])

# PODS

pods_k = InlineKeyboardMarkup (inline_keyboard =[
[InlineKeyboardButton(text = 'XROS 3 Mini', callback_data = 'XROS 3 Mini')],
[InlineKeyboardButton(text = 'ELFX', callback_data = 'ELFX'),
 InlineKeyboardButton(text = 'ELFX Pro', callback_data = 'ELFX Pro')],
[InlineKeyboardButton(text = 'XROS Pro', callback_data = 'XROS Pro'),
 InlineKeyboardButton(text = 'XROS Cube', callback_data = 'XROS Cube')],
[InlineKeyboardButton(text = 'XROS 4', callback_data = 'XROS 4'),
 InlineKeyboardButton(text = 'XROS 4 Nano', callback_data = 'XROS 4 Nano')],
[InlineKeyboardButton(text = 'НАЗАД', callback_data = 'НАЗАД_catalog')]
])

pods_back_k = InlineKeyboardMarkup(inline_keyboard = [
    [InlineKeyboardButton(text = 'НАЗАД', callback_data = 'НАЗАД')]
])

pods_back_catalog_k = InlineKeyboardMarkup(inline_keyboard = [
    [InlineKeyboardButton(text = 'НАЗАД', callback_data = 'НАЗАД_catalog')]
])


cmd_start_t = """
Ти успішно мене запустив🥰
Тепер ми зможемо тобі щось підібрати.

Нижче ти можеш бачити кнопочкі😁
Перед тим як на них тицяти, ознайомся з їхнім функціоналом🤓

CATALOG - думаю тут все зрозуміло

INFORMATION - це інформація про тебе яка знадобиться тобі при отриманні замовлення.
"""

XROS_3_Mini_t = """
⚡️Vaporesso Xros 3 Mini ⚡️

Ціна: 700 ГРН💲

🔅Особливості: 
• Живі фото
• Картриджі до цього пода 
• Акумулятор: 1000 мАг
• Потужність: 11 / 16 Вт
• Опір картриджу: 0.6 Ом
• Об‘єм картриджу: 2 мл
• Компактні розміри 
• Захист від протікання



Для замовленя натисни /information
"""

ELFX_t = """
⚡️Elf Bar ELFX⚡️

Ціна: 600 ГРН💲

🔅 Особливості: 
• Акумулятор: 1000 mAh
• Регулювання затяжки 
• Неонова підсвітка корпусу 
• Верхня заправка 
• В комплекті два картриджі: 0.6 та 0.8 Ом!
• Швидка зарядка
• Потужність: до 30 Вт



Для замовленя натисни /information
"""

ELFX_PRO_t = """
⚡️Elf Bar ELFX Pro⚡️

Ціна: 900 ГРН💲

🔅 Особливості: 
• Акумулятор: 1200 mAh
• Регулювання затяжки 
• Регулювання потужності
• Верхня заправка 
• В комплекті два картриджі: 0.6 та 0.8 Ом!
• Швидка зарядка
• Потужність: 5-45 Вт



Для замовленя натисни /information
"""

XROS_PRO_t = """
⚡️Vaporesso Xros Pro⚡️ 

Ціна: 1200 ГРН💲

🔅Особливості:
• Новий тип картриджа 0.4 Ом (3 мл)
• Можливість точно регулювати потужність (тільки на 0.4 Ом) до 30 Вт з кроком 0.5 Вт
• Можливість міняти режими (від 0.6 до 1.2 Ом): 
— Еко-режим 
— Нормальний 
— Режим підвищеної потужності 
• Окрема бокова кнопка для блокування основної кнопки
• Регулювання затяжки з декількома режимами
• Акумулятор: 1200 мАг
• Повна зарядка всього за 35 хвилин



Для замовленя натисни /information
"""

XROS_CUBE_t = """
⚡️Vaporesso Xros Cube⚡️ 

Ціна: 900 ГРН💲

🔅 Особливості: 
• Акумулятор: 900 mAh
• Нові кольори
• COREX 2.0
• Два картриджі в комплекті (0.8, 1.2 Ом)
• Швидка зарядка
• Регулювання затяжки
• Потужність: ~19 Вт



Для замовленя натисни /information
"""

XROS_4_t = """
⚡️Vaporesso Xros 4⚡️

Ціна: 1000 ГРН💲

🔅 Особливості: 
• Акумулятор: 1000 mAh
• Нові кольори
• COREX 2.0
• Два картриджі в комплекті (0.4 Ом, 3 мл)
• Швидка зарядка
• Три режими паріння
• Регулювання затяжки
• Потужність: ~20-29 Вт



Для замовленя натисни /information
"""

XROS_4_NANO_t = """
⚡️Vaporesso Xros 4 Nano ⚡️

Ціна: 1250 ГРН💲

🔅 Особливості: 
• Акумулятор: 1350 mAh
• Різні теми на екранчику
• Можливість регулювати потужність
• Регулювання затяжки
• Кнопка
• Ремішок в подарунок
• COREX 2.0
• Два картриджі в комплекті 
• Швидка зарядка (за 20 хв до 80%)



Для замовленя натисни /information
"""
