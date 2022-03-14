import random
import re
import time
from datetime import datetime
from platform import python_version

from telethon import version
from telethon.errors.rpcerrorlist import (
    MediaEmptyError,
    WebpageCurlFailedError,
    WebpageMediaEmptyError,
)
from telethon.events import CallbackQuery

from userbot import StartTime, jmthon, jmthonversion

from ..Config import Config
from ..core.managers import edit_or_reply
from ..helpers.functions import jmthonalive, check_data_base_heal_th, get_readable_time
from ..helpers.utils import reply_id
from ..sql_helper.globals import gvarstatus
from . import mention

plugin_category = "utils"


@jmthon.ar_cmd(
    pattern="فحص$",
    command=("فحص", plugin_category),)
async def amireallyalive(event):
    "لعرض حاله البوت وفحص السورس"
    reply_to_id = await reply_id(event)
    uptime = await get_readable_time((time.time() - StartTime))
    start = datetime.now()
    jmthonevent = await edit_or_reply(event, "- يتم التحقق من الكليشة")
    end = datetime.now()
    ms = (end - start).microseconds / 1000
    _, check_sgnirts = check_data_base_heal_th()
    EMOJI = gvarstatus("ALIVE_EMOJI") or "  ✥ "
    ALIVE_TEXT = gvarstatus("ALIVE_TEXT") or "**✮ البـوت يعـمل بنجـاح ✮**"
    JMTHON_IMG = gvarstatus("ALIVE_PIC")
    jmthon_caption = gvarstatus("ALIVE_TEMPLATE") or temp
    caption = jmthon_caption.format(
        ALIVE_TEXT=ALIVE_TEXT,
        EMOJI=EMOJI,
        mention=mention,
        uptime=uptime,
        telever=version.__version__,
        jmver=jmthonversion,
        pyver=python_version(),
        dbhealth=check_sgnirts,
        ping=ms,
    )
    if JMTHON_IMG:
        JMTHON = [x for x in JMTHON_IMG.split()]
        PIC = random.choice(JMTHON)
        try:
            await event.client.send_file(
                event.chat_id, PIC, caption=caption, reply_to=reply_to_id
            )
            await jmthonevent.delete()
        except (WebpageMediaEmptyError, MediaEmptyError, WebpageCurlFailedError):
            return await edit_or_reply(
                jmthonevent,
                f"**الرابط غير صحيح**\n `.ضع فار ALIVE_PIC رابط صورتك`\n\n**لا يمـكن الحـصول عـلى صـورة من الـرابـط :-** `{PIC}`",
            )
    else:
        await edit_or_reply(
            jmthonevent,
            caption,
        )


temp = """{ALIVE_TEXT}
**{EMOJI} قاعدۿ البيانات :** `{dbhealth}`
**{EMOJI} أصـدار التـيليثون :** `{telever}`
**{EMOJI} أصـدار جـمثون :** `{jmver}`
**{EMOJI} الوقت:** `{uptime}` 
**{EMOJI} أصدار البـايثون :** `{pyver}`
**{EMOJI} المسـتخدم:** {mention}"""





@jmthon.ar_cmd(
    pattern="السورس$",
    command=("السورس", plugin_category),)
async def amireallyalive(event):
    " لعرض حاله البوت وفحص السورس بشكل انلاين"
    reply_to_id = await reply_id(event)
    EMOJI = gvarstatus("ALIVE_EMOJI") or "  ✥ "
    ALIVE_TEXT = gvarstatus("ALIVE_TEXT") or "**سورس جمثون شغال بنجاح**"
    jmthon_caption = f"{ALIVE_TEXT}\n"
    jmthon_caption += f"**{EMOJI} أصدار التيليثون :** `{version.__version__}\n`"
    jmthon_caption += f"**{EMOJI} أصدار سورس جمثون :** `{jmthonversion}`\n"
    jmthon_caption += f"**{EMOJI} أصدار البايثون :** `{python_version()}\n`"
    jmthon_caption += f"**{EMOJI} المالك:** {mention}\n"
    results = await event.client.inline_query(Config.TG_BOT_USERNAME, jmthon_caption)
    await results[0].click(event.chat_id, reply_to=reply_to_id, hide_via=True)
    await event.delete()


@jmthon.tgbot.on(CallbackQuery(data=re.compile(b"stats")))
async def on_plug_in_callback_query_handler(event):
    statstext = await jmthonalive(StartTime)
    await event.answer(statstext, cache_time=0, alert=True)
