from aiogram import F, Router
from aiogram.filters import CommandStart, Command
from aiogram.types import Message, CallbackQuery, InputMediaPhoto
import keyboard as kb
from keyboard import cmd_start_t, XROS_3_Mini_t, ELFX_t, XROS_PRO_t, ELFX_PRO_t, XROS_CUBE_t, XROS_4_t, XROS_4_NANO_t

router = Router()


# ENTRY POINT

@router.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer(cmd_start_t,
                        reply_markup = kb.start_k)
    await message.delete()



# HELP

@router.message(Command('help'))
async def gef_help(message: Message):
    await message.answer('COMING SOON')



# INFOMATION

@router.message(Command('information'))
async def information(message: Message):
    await message.answer(
        f"""
    ПРИВІТ!
    Твій ID: {message.from_user.id}
    Імя: {message.from_user.first_name}
    Ці дані знадобляться тобі для замовлення.
    Замовити можна тут.
    Оплата:
    - Карта: Private, Mono
    - Готівка при отриманні
    """
    )
    await message.delete()



# CATALOG

@router.message(Command('catalog'))
async def information(message: Message):
    await  message.answer_photo(photo = 'AgACAgIAAxkBAAPEZzb_E9sB_FXDQwUozhQVfJ11m7UAAh3pMRur8bFJaSimlZ8NQXwBAAMCAAN5AAM2BA',
                                caption = 'Це каталог наших товарів😁, сподіваюсь ти знайдеш те, що тобі довподоби😃',
                                reply_markup = kb.catalog_k)
    await message.delete()


# CATALOG: BACK TO CATALOG

@router.callback_query(F.data == 'НАЗАД_catalog')
async def pods(callback: CallbackQuery):
    await callback.answer('')
    await callback.message.edit_media(
        media=InputMediaPhoto(media='AgACAgIAAxkBAAPEZzb_E9sB_FXDQwUozhQVfJ11m7UAAh3pMRur8bFJaSimlZ8NQXwBAAMCAAN5AAM2BA',
                              caption = 'Це каталог наших товарів😁, сподіваюсь ти знайдеш те, що тобі довподоби😃'),
        reply_markup=kb.catalog_k
)



# HUI

@router.message(F.text == 'Хуй')
async def hui_reply(message: Message):
    await message.reply_photo(photo = 'AgACAgIAAxkBAANxZzXyUYlm_pebnEYwiUEYUGgKaEIAApzpMRsDr7BJVa0cI_sJeEIBAAMCAAN5AAM2BA',
                               caption = 'БАЗАР ФИЛЬТРУЙ')

@router.message(F.text == 'Пошол нахуй')
async def hui_reply(message: Message):
    await message.reply_photo(photo = 'AgACAgIAAxkBAANxZzXyUYlm_pebnEYwiUEYUGgKaEIAApzpMRsDr7BJVa0cI_sJeEIBAAMCAAN5AAM2BA',
                               caption = 'БАЗАР ФИЛЬТРУЙ')

@router.message(F.text == 'Соси')
async def hui_reply(message: Message):
    await message.reply_photo(photo = 'AgACAgIAAxkBAANxZzXyUYlm_pebnEYwiUEYUGgKaEIAApzpMRsDr7BJVa0cI_sJeEIBAAMCAAN5AAM2BA',
                               caption = 'БАЗАР ФИЛЬТРУЙ')


# GET ID PHOTO

@router.message(F.photo)
async def get_photo(message: Message):
    await message.answer(f'id photo: {message.photo[-1].file_id}')



# CALLLBAKS
# show_alert = True


@router.callback_query(F.data == 'pods')
async def pods(callback: CallbackQuery):
    await callback.answer('')
    await callback.message.edit_media(
        media=InputMediaPhoto(media='AgACAgIAAxkBAAICjmdEKBx4BFGyB0Di_ScXgRxCsIQEAALA4zEbU7spSg_ARrKaMykjAQADAgADeQADNgQ',
                              caption = 'Ось весь асортимент наших подів для тебе😃'),
        reply_markup=kb.pods_k
)


@router.callback_query(F.data == 'cartriges')
async def pods(callback: CallbackQuery):
    await callback.answer('')
    await callback.message.answer_photo(photo = 'AgACAgIAAxkBAAPHZzb_E1Pe-izQxY3VXiF5KU17Nq4AAlbhMRuANLlJpxSfql7mLJ8BAAMCAAN5AAM2BA',
                                        caption = 'Я ще не вигадав текст для цієї секції🤣 тому як тільки вигадаю, одразу напишу.')

@router.callback_query(F.data == 'giga')
async def pods(callback: CallbackQuery):
    await callback.answer('')
    await callback.message.answer_photo(photo = 'AgACAgIAAxkBAAPGZzb_E5gpJCLSEeApxCsCXJiRKhIAAh_pMRur8bFJjT0XRi2Xd5wBAAMCAAN5AAM2BA',
                                        caption = 'Я ще не вигадав текст для цієї секції🤣 тому як тільки вигадаю, одразу напишу.')

# CALLBACK TO BACK

@router.callback_query(F.data == 'НАЗАД')
async def pods(callback: CallbackQuery):
    await callback.answer('НАЗАД')
    await callback.message.edit_media(
        media=InputMediaPhoto(media='AgACAgIAAxkBAAICW2c-6d5o2U7bWkZ-UyX4uu0oSCT3AALx3jEbaoP5SS6iLoyk5jTkAQADAgADeQADNgQ',
                              caption = 'Це каталог наших товарів😁, сподіваюсь ти знайдеш те, що тобі довподоби😃'),
        reply_markup=kb.pods_k
)

# CALLBACK POD

@router.callback_query(F.data == 'XROS 3 Mini')
async def pods(callback: CallbackQuery):
    await callback.answer('XROS 3 Mini')
    await callback.message.edit_media(
        media=InputMediaPhoto(media='AgACAgIAAxkBAAICUGc-41clCoiruN6eqYDR748chfcvAAIO5jEb1_v4SaOZAQw8_aokAQADAgADeQADNgQ',
                              caption = XROS_3_Mini_t),
        reply_markup=kb.pods_back_k
)


@router.callback_query(F.data == 'ELFX')
async def pods(callback: CallbackQuery):
    await callback.answer('ELFX')
    await callback.message.edit_media(
        media=InputMediaPhoto(media='AgACAgIAAxkBAAICVGc-42Fa7ARuw3lp8GYdXHYFyHE_AAIQ5jEb1_v4Sf3cGm6PGL2uAQADAgADeQADNgQ',
                              caption = ELFX_t),
        reply_markup=kb.pods_back_k
)


@router.callback_query(F.data == 'ELFX Pro')
async def pods(callback: CallbackQuery):
    await callback.answer('ELFX Pro')
    await callback.message.edit_media(
        media=InputMediaPhoto(media='AgACAgIAAxkBAAICUmc-41t9yFW2y1z4s0oEIC_DGcAYAAIP5jEb1_v4SbjikkXz2UVEAQADAgADeQADNgQ',
                              caption = ELFX_PRO_t),
        reply_markup=kb.pods_back_k
)


@router.callback_query(F.data == 'XROS Pro')
async def pods(callback: CallbackQuery):
    await callback.answer('XROS Pro')
    await callback.message.edit_media(
        media=InputMediaPhoto(media='AgACAgIAAxkBAAICSGc-40Kgg8jdFCxkXY97IjkC-Hk9AAIJ5jEb1_v4Sf2UxoYEhghgAQADAgADeAADNgQ',
                              caption = XROS_PRO_t),
        reply_markup=kb.pods_back_k
)


@router.callback_query(F.data == 'XROS Cube')
async def pods(callback: CallbackQuery):
    await callback.answer('XROS Cube')
    await callback.message.edit_media(
        media=InputMediaPhoto(media='AgACAgIAAxkBAAICSmc-40fQ0y6cNa30xehniOpZoiXOAAIL5jEb1_v4SYh56eP6akPfAQADAgADeQADNgQ',
                              caption = XROS_CUBE_t),
        reply_markup=kb.pods_back_k
)

@router.callback_query(F.data == 'XROS 4')
async def pods(callback: CallbackQuery):
    await callback.answer('XROS 4')
    await callback.message.edit_media(
        media=InputMediaPhoto(media='AgACAgIAAxkBAAICTmc-41N0iQjFmhKI7IAOX6aGNfDIAAIN5jEb1_v4SXmSsKrCVaI6AQADAgADeQADNgQ',
                              caption = XROS_4_t),
        reply_markup=kb.pods_back_k
)

@router.callback_query(F.data == 'XROS 4 Nano')
async def pods(callback: CallbackQuery):
    await callback.answer('XROS 4 Nano')
    await callback.message.edit_media(
        media=InputMediaPhoto(media='AgACAgIAAxkBAAICNGc-3rGYR4MWkAQq3LI8fnBSrzm-AAJv5TEb1_v4SbKfXZ8yTRHxAQADAgADeQADNgQ',
                              caption = XROS_4_NANO_t),
        reply_markup=kb.pods_back_k
)



#"""
# @router.callback_query(F.data == 'XROS 4 Nano')
# async def pods(callback: CallbackQuery):
#     await callback.answer('XROS 4 Nano')
#     await callback.message.edit_caption(caption = XROS_4_NANO_t,
#                                         reply_markup = kb.pods_back_20_k)
# """

#"""
# @router.callback_query(F.data == '')
# async def pods(callback: CallbackQuery):
#     await callback.answer('', show_alert = True)
#     await callback.message.answer_photo(photo = '',
#                                         caption = '')
# """

#"""
# @router.callback_query(F.data == '')
# async def pods(callback: CallbackQuery):
#     await callback.answer('')
#     await callback.message.edit_media(
#         media=InputMediaPhoto(media='',
#                               caption = ),
#         reply_markup=kb.pods_back_k
# )
# """


