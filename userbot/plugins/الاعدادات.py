import os
from asyncio.exceptions import CancelledError
from time import sleep

from userbot import jmthon

from ..core.logger import logging
from ..core.managers import edit_or_reply
from ..sql_helper.global_collection import (
    add_to_collectionlist,
    del_keyword_collectionlist,
    get_collectionlist_items,
)
from ..sql_helper.globals import addgvar, delgvar, gvarstatus
from . import BOTLOG, BOTLOG_CHATID, HEROKU_APP

LOGS = logging.getLogger(__name__)
plugin_category = "tools"


@jmthon.ar_cmd(
    pattern="اعادة تشغيل$",
    command=("اعادة تشغيل", plugin_category),
    info={
        "header": "اعادة تشغيل البوت !!",
        "usage": "{tr}اعادة تشغيل",
    },
    disable_errors=True,
)
async def _(event):
    "اعادة تشغيل البوت !!"
    if BOTLOG:
        await event.client.send_message(BOTLOG_CHATID, "#اعادة_التشغيل \n" "تم اعادة تشغيل البوت")
    sandy = await edit_or_reply(
        event,
        "تمت اعادة التشغيل بنجاح ✓\n**ارسل** `.فحص` ** او ** `.اوامري` ** للتحقق مما إذ كان البوت شغال ، يستغرق الأمر في الواقع 1-2 دقيقة لإعادة التشغيل**",
    )
    try:
        ulist = get_collectionlist_items()
        for i in ulist:
            if i == "restart_update":
                del_keyword_collectionlist("restart_update")
    except Exception as e:
        LOGS.error(e)
    try:
        add_to_collectionlist("restart_update", [sandy.chat_id, sandy.id])
    except Exception as e:
        LOGS.error(e)
    try:
        await jmthon.disconnect()
    except CancelledError:
        pass
    except Exception as e:
        LOGS.error(e)


@jmthon.ar_cmd(
    pattern="أيقاف السورس$",
    command=("ايقاف السورس", plugin_category),
    info={
        "header": "ايقاف تشغيل السورس !!",
        "description": "لإيقاف تشغيل الدينو من هيروكو. لا يمكنك تشغيل البوت ، اذا اردت تشغيله تحتاج الى تشغيله يدويا من هيروكو",
        "usage": "{tr}ايقاف السورس",
    },
)
async def _(event):
    "ايقاف تشغيل السورس"
    if BOTLOG:
        await event.client.send_message(BOTLOG_CHATID, "#ايقاف_التشغيل \n" "تم ايقاف تشغيل السورس")
    await edit_or_reply(event, "**جارٍ إيقاف تشغيل السورس الآن ... شغِّلني يدويًا لاحقًا**")
    if HEROKU_APP is not None:
        HEROKU_APP.process_formation()["worker"].scale(0)
    else:
        os._exit(143)


@jmthon.ar_cmd(
    pattern="أيقاف مؤقت( [0-9]+)?$",
    command=("ايقاف مؤقت", plugin_category),
    info={
        "header": "سوف يتوقف السورس عن العمل في الوقت المذكور.",
        "usage": "{tr}ايقاف مؤقت <عدد الثواني>",
        "examples": "{tr}ايقاف مؤقت 60",
    },
)
async def _(event):
    "لإقاف تشغيل السورس مؤقت"
    if " " not in event.pattern_match.group(1):
        return await edit_or_reply(event, "الامر : **. وقت الايقاف**")
    counter = int(event.pattern_match.group(1))
    if BOTLOG:
        await event.client.send_message(
            BOTLOG_CHATID,
            "لقد وضعت السورس في وضع السكون لمدة " + str(counter) + " ثواني",
        )
    event = await edit_or_reply(event, f"**حسنا تم ايقاف البوت لمده {counter} ثواني**")
    sleep(counter)
    await event.edit("**اهلا الان اشتغل بشكل طبيعي**")


@jmthon.ar_cmd(
    pattern="التحديثات (تشغيل|ايقاف)$",
    command=("التحديثات", plugin_category),
    info={
        "header": "⌯︙لتحديـث الدردشـة بعـد إعـادة التشغيـل  أو إعـادة التحميـل  ",
        "description": "⌔︙سيتـم إرسـال بنـك cmds ڪـرد على الرسالـة السابقـة الأخيـرة لـ (إعادة تشغيل/إعادة تحميل/تحديث cmds) 💡.",
        "usage": [
            "{tr}التحديثات <تشغيل/ايقاف",
        ],
    },
)
async def set_pmlog(event):
    "⌯︙لتحديـث الدردشـة بعـد إعـادة التشغيـل  أو إعـادة التحميـل"
    input_str = event.pattern_match.group(1)
    if input_str == "ايقاف":
        if gvarstatus("restartupdate") is None:
            return await edit_delete(event, "**⌯︙تـم تعطيـل التـحديـثات بالفعـل ❗️**")
        delgvar("restartupdate")
        return await edit_or_reply(event, "**⌔︙تـم تعطيـل التـحديـثات بنجـاح ✓**")
    if gvarstatus("restartupdate") is None:
        addgvar("restartupdate", "turn-oned")
        return await edit_or_reply(event, "**⌔︙تـم تشغيل التـحديـثات بنجـاح ✓**")
    await edit_delete(event, "**⌯︙تـم تشغيل التـحديـثات بالفعـل ❗️**")
