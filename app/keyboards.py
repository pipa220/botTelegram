from aiogram.types import (ReplyKeyboardMarkup , KeyboardButton ,
                           InlineKeyboardButton , InlineKeyboardMarkup)

# reg_button = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text='5 класс', callback_data='')],[InlineKeyboardButton(text='6 класс')],
#                                               [InlineKeyboardButton(text='7 класс')],[InlineKeyboardButton(text='8 класс')],
#                                               [InlineKeyboardButton(text='9 класс')],[InlineKeyboardButton(text='10 класс')],
#                                               [InlineKeyboardButton(text='11 класс')],[InlineKeyboardButton(text='я учитель')]])

# class_button = InlineKeyboardMarkup(row_width=3)
# for i in range (5,12):
#     class_button.insert(InlineKeyboardButton(text=f'{i} класс', callback_data=f'grade_{i}'))
# class_button.add(InlineKeyboardButton(text='я учитель',callback_data='teacher'))
#
# letter_button = InlineKeyboardMarkup(row_width=7)
# for letter_buttonin in ["А","Б","В","Г","Д","Е","Ж","З"]:
#     letter_button.insert(InlineKeyboardButton(text='letter' , callback_data=f'latter_{'letter'}'))

main = ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text='🤖Узнать о "бот-121" школы!🤖'),
                                     KeyboardButton(text='Связь с парламентом📞')],
                                     [KeyboardButton(text='1️⃣Расписание уроков для первой смены📚'),
                                      KeyboardButton(text='2️⃣Расписание уроков для второй смены📚')],
                                     [KeyboardButton(text='все соц-сети школы📱'),
                                      KeyboardButton(text='Помощи с выбором !плейлиста! для дискотеки🪩💗')]
                                     ], input_field_placeholder='Что вас интересует...')