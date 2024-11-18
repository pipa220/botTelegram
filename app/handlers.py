from aiogram import F , Router
import asyncio
from aiogram.types import Message, CallbackQuery
from aiogram.filters import  CommandStart , Command

import app.keyboards as kb
router = Router()

@router.message(CommandStart())
async def cmd_snart(message: Message):
    await  message.answer('Привет!\nЯ — бот школы №121🏫, и моя задача — помогать тебе в школьной жизни.Но для начала нам нужно познакомиться. Выбери свой класс:\n(‼️Просим‼️ отвечать честно, ведь сейчас вы настраиваете тг-бота под себя для удобного пользования)', reply_markup=kb.main)

@router.message(Command('help'))
async def get_help(message: Message):
    await message.answer('Если у вас возникли проблеммы с "бот-121" обращайтесь к админам:\n@na_tttily или @gorilla2233 ')

@router.callback_query(F.date == '')
async def class_button(callback: CallbackQuery):
    await callback.message.answer('спасибо вы выбрали класс, теперь нужно выбрать букву класса')

@router.message(Command('🤖Узнать о "бот-121" школы!🤖'))
async def teleg_bot(message: Message):
    await message.answer('Я — школьный телеграм-бот🤖, меня зовут Бот-121, и я был создан, чтобы сделать процесс обучения более удобным и эффективным.Я был разработан не самым опытным программистом, поэтому, возможно, в моей работе есть некоторые недочёты. Однако я не планирую останавливаться на достигнутом и буду постоянно совершенствоваться, учитывая ваши предложения и замечания.В будущем у меня большие планы. Например, я хочу подключить к себе нейронную сеть, но это пока только в разработке, так как я — лишь первая версия.'

                                               '\nПока что мой функционал ограничен, но он включает в себя:Расписание уроков и звонков; Ссылки на социальные сети; связь с парламентом; Новостной канал; Периодические опросы.'

                                             '\nЭто только начало. Если у вас есть идеи, как улучшить мои функции, пожалуйста, напишите в парламент, т.к они мои создатели (а точнее вице-президент и министр информационных технологий) с радостью рассмотрят ваши предложения.'

                                              '\nНадеюсь,я буду полезен вам')


@router.message(F.text == 'Связь с парламентом📞')
async def meet_parlament(message: Message):
     await message.answer('В нашем парламенте работает множество замечательных людей, готовых помочь и поддержать ваши идеи. Однако основной способ связи с ними :\n@na_tttily или @gorilla2233 \nОни с радостью передадим все ваши сообщения в парламент, поэтому не стесняйтесь высказываться и предлагать свои идеи. ')


@router.message('️⃣Расписание уроков для первой смены📚')
async def inquiry1(message: Message):
    await message.answer_photo(photo=)

@router.message(Command('️⃣Расписание уроков для второй смены📚'))
async def inquiry2(message: Message):
    await message.answer('')

@router.message(Command('все соц-сети школы📱'))
async def social(message: Message):
    await message.answer('Все соцсети, которые ведет школа:\nпервый аккаунт: https://www.instagram.com/school.121?igsh=MXhjNGljc2s5d2lmYQ=='
                                           '\nвторой аккаунт: https://www.instagram.com/121_mektep_shkola?igsh=ZGJ3ZWczMjFrenoy\n тгк:https://t.me/myschool_121-(тут все новости, что бы вы ничего не пропустили)')

@router.message(Command('Помощи с выбором !плейлиста! для дискотеки🪩💗'))
async def disco(message: Message):
    await message.answer('')#тут сам разбирайся с бд