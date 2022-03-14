import re

from telethon import Button
from telethon.errors import MessageNotModifiedError
from telethon.events import CallbackQuery

from userbot import jmthon

from ..Config import Config
from ..core.logger import logging

LOGS = logging.getLogger(__name__)


@jmthon.tgbot.on(CallbackQuery(data=re.compile(r"^age_verification_true")))
async def age_verification_true(event: CallbackQuery):
    u_id = event.query.user_id
    if u_id != Config.OWNER_ID and u_id not in Config.SUDO_USERS:
        return await event.answer(
            "نظرًا لكونه قرارًا غبيًا ، فقد اخترت تجاهله",
            alert=True,
        )
    await event.answer("نعم عمري هو 18+", alert=False)
    buttons = [
        Button.inline(
            text="غير متأكد / تغير قرارك ?",
            data="chg_of_decision_",
        )
    ]
    try:
        await event.edit(
            text="يجب وضع فار `ALLOW_NSFW` = True  في قاعده بيانات الفارات لاستخدام هذه الميزه",
            file="https://telegra.ph/file/85f3071c31279bcc280ef.jpg",
            buttons=buttons,
        )
    except MessageNotModifiedError:
        pass


@jmthon.tgbot.on(CallbackQuery(data=re.compile(r"^age_verification_false")))
async def age_verification_false(event: CallbackQuery):
    u_id = event.query.user_id
    if u_id != Config.OWNER_ID and u_id not in Config.SUDO_USERS:
        return await event.answer(
            "نظرًا لكونه قرارًا غبيًا ، فقد اخترت تجاهله.",
            alert=True,
        )
    await event.answer("لا ليس كذلك", alert=False)
    buttons = [
        Button.inline(
            text="غير متأكد / تغير قرارك ?",
            data="chg_of_decision_",
        )
    ]
    try:
        await event.edit(
            text="العب بعيدا طفلي",
            file="https://telegra.ph/file/1140f16a883d35224e6a1.jpg",
            buttons=buttons,
        )
    except MessageNotModifiedError:
        pass


@jmthon.tgbot.on(CallbackQuery(data=re.compile(r"^chg_of_decision_")))
async def chg_of_decision_(event: CallbackQuery):
    u_id = event.query.user_id
    if u_id != Config.OWNER_ID and u_id not in Config.SUDO_USERS:
        return await event.answer(
            "نظرًا لكونه قرارًا غبيًا ، فقد اخترت تجاهله",
            alert=True,
        )
    await event.answer("غير متأكد", alert=False)
    buttons = [
        (
            Button.inline(text="نعم عمري هو 18+", data="age_verification_true"),
            Button.inline(text="لا لست كذلك", data="age_verification_false"),
        )
    ]
    try:
        await event.edit(
            text="**هل انت كبير بما فيه الكفاية لهذا  ؟**",
            file="https://telegra.ph/file/238f2c55930640e0e8c56.jpg",
            buttons=buttons,
        )
    except MessageNotModifiedError:
        pass

#استغفر الله العظيم 
#غير مسؤول امام الله عن استخدام الاوامر الاباحيه
# لقد قمت بالترجمه فقط لمساعده في باقي الاوامر 
# استغفر الله العظيم واتوب اليه 
