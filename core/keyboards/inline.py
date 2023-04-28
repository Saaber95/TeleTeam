from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder
from core.utils.callbackdata import MacInfo

# select_macbook = InlineKeyboardMarkup(inline_keyboard=[
#     [
#         InlineKeyboardButton(
#             text='Macbook Air 13" M1 2020',
#             callback_data='apple_air_13_m1_2020'
#         )
#     ],
#     [
#         InlineKeyboardButton(
#             text='Macbook Pro 14" M1 Pro 2021',
#             callback_data='apple_pro_14_m1_2020'
#         )
#     ],
#     [
#         InlineKeyboardButton(
#             text='Apple MacBook Pro 16" 2019',
#             callback_data='apple_pro_16_i7_2019'
#         )
#     ],
#     [
#         InlineKeyboardButton(
#             text='Link',
#             url='https://nztcoder.com'
#         )
#     ],
#     [
#         InlineKeyboardButton(
#             text='Profile',
#             url='tg://user?id=660089851'
#         )
#     ]
# ])


def get_inline_keyboard():
    keyboard_builder = InlineKeyboardBuilder()
    keyboard_builder.button(text='FAQ', url='https://docs.google.com/document/d/1Rxbrr5mqoa-UlLR-RqmnhF6p8n3S3H8hwuzo0PJezWU/edit')

    keyboard_builder.button(text='Общий канал', url='https://t.me/c/1873667582/1')

#    keyboard_builder.button(text='Общий канал', callback_data=MacInfo(model='1', size=1, chip='1', year=1))

    keyboard_builder.button(text='Канал с профилями', callback_data=MacInfo(model='1', size=3, chip='1', year=1))
    keyboard_builder.button(text='Teleteam', url='https://rbc.ru')
    keyboard_builder.button(text='RandomCofee', callback_data=MacInfo(model='1', size=4, chip='1', year=1))
    keyboard_builder.button(text='СЕГОДНЯ',  callback_data=MacInfo(model='1', size=5, chip='1', year=1))
    keyboard_builder.button(text='ОПРОСЫ',  callback_data=MacInfo(model='1', size=6, chip='1', year=1))
    keyboard_builder.button(text='ФОТОСКЛАД',  callback_data=MacInfo(model='1', size=7, chip='1', year=1))
    # keyboard_builder.button(text='Profile', url='tg://user?id=660089851')

    keyboard_builder.adjust(1)
    return keyboard_builder.as_markup()


def get_inline_keyboard1():
    keyboard_builder = InlineKeyboardBuilder()

    keyboard_builder.button(text='FAQ1', callback_data=MacInfo(model='air', size=13, chip='m1', year=2020))
    keyboard_builder.button(text='FAQ2', callback_data=MacInfo(model='pro', size=14, chip='m1', year=2021))
    keyboard_builder.button(text='FAQ3', callback_data=MacInfo(model='pro', size=16, chip='i7', year=2019))

    keyboard_builder.adjust(1)
    return keyboard_builder.as_markup()

def get_inline_keyboard2():
    keyboard_builder = InlineKeyboardBuilder()

    keyboard_builder.button(text='Общий Канал1', callback_data=MacInfo(model='air', size=13, chip='m1', year=2020))
    keyboard_builder.button(text='Общий Канал2', callback_data=MacInfo(model='pro', size=14, chip='m1', year=2021))
    keyboard_builder.button(text='Общий Канал3', callback_data=MacInfo(model='pro', size=16, chip='i7', year=2019))

    keyboard_builder.adjust(1)
    return keyboard_builder.as_markup()


def get_inline_keyboard3():
    keyboard_builder = InlineKeyboardBuilder()

    keyboard_builder.button(text='FAQ1', callback_data=MacInfo(model='air', size=13, chip='m1', year=2020))
    keyboard_builder.button(text='FAQ2', callback_data=MacInfo(model='pro', size=14, chip='m1', year=2021))
    keyboard_builder.button(text='FAQ3', callback_data=MacInfo(model='pro', size=16, chip='i7', year=2019))

    keyboard_builder.adjust(1)
    return keyboard_builder.as_markup()




