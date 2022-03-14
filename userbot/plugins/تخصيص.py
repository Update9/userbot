from urlextract import URLExtract
from validators.url import url

from userbot import jmthon
from userbot.core.logger import logging

from ..Config import Config
from ..core.managers import edit_delete, edit_or_reply
from ..sql_helper.globals import addgvar, delgvar, gvarstatus
from . import BOTLOG_CHATID

plugin_category = "utils"
LOGS = logging.getLogger(__name__)
cmdhd = Config.COMMAND_HAND_LER

extractor = URLExtract()
vlist = [
    "ALIVE_PIC",
    "ALIVE_EMOJI",
    "ALIVE_TEMPLATE",
    "ALIVE_TEXT",
    "ALLOW_NSFW",
    "IALIVE_PIC",
    "PM_PIC",
    "PM_TEXT",
    "PM_BLOCK",
    "MAX_FLOOD_IN_PMS",
    "START_TEXT",
    "CUSTOM_STICKER_PACKNAME",
]

oldvars = {
    "PM_PIC": "pmpermit_pic",
    "PM_TEXT": "pmpermit_txt",
    "PM_BLOCK": "pmblock",
}


@jmthon.ar_cmd(
    pattern="(اضف_|جلب_|حذف_)فار(?: |$)([\s\S]*)",
    command=("dv", plugin_category),)
async def bad(event):  # sourcery no-metrics
    "To manage vars in database"
    cmd = event.pattern_match.group(1).lower()
    vname = event.pattern_match.group(2)
    vnlist = "".join(f"{i}. `{each}`\n" for i, each in enumerate(vlist, start=1))
    if not vname:
        return await edit_delete(
            event, f"**📑 يجب عليك كتابة اسم الفار بشك صحيح من القائمة :\n\n**{vnlist}", time=60
        )
    vinfo = None
    if " " in vname:
        vname, vinfo = vname.split(" ", 1)
    reply = await event.get_reply_message()
    if not vinfo and reply:
        vinfo = reply.text
    if vname in vlist:
        if vname in oldvars:
            vname = oldvars[vname]
        if cmd == "اضف_":
            if not vinfo and vname == "ALIVE_TEMPLATE":
                return await edit_delete(event, f"تأكد من  @JJOTT")
            if not vinfo:
                return await edit_delete(
                    event, f"- يجب عليك وضع قيمه للفار **{vname}**"
                )
            check = vinfo.split(" ")
            for i in check:
                if (("PIC" in vname) or ("pic" in vname)) and not url(i):
                    return await edit_delete(event, "**يجب عليك وضع رابط صحيح...**")
            addgvar(vname, vinfo)
            if BOTLOG_CHATID:
                await event.client.send_message(
                    BOTLOG_CHATID,
                    f"#وضع_فار\
                    \n**{vname}** تم تحديثه بنجاح في قاعده البيانات كـ:",
                )
                await event.client.send_message(BOTLOG_CHATID, vinfo, silent=True)
            await edit_delete(
                event, f"📑 قيمة الفار **{vname}** تغيرت الى :- `{vinfo}`", time=20
            )
        if cmd == "جلب_":
            var_data = gvarstatus(vname)
            await edit_delete(
                event, f"📑 قيمة الفار **{vname}** هي `{var_data}`", time=20
            )
        elif cmd == "حذف_":
            delgvar(vname)
            if BOTLOG_CHATID:
                await event.client.send_message(
                    BOTLOG_CHATID,
                    f"#حذف_فار\
                    \n**{vname}** تم حذفه من قاعده البيانات",
                )
            await edit_delete(
                event,
                f"📑 قيمة الفار **{vname}** تم حذفها وارجاعها الى قيمتها الاصلية.",
                time=20,
            )
    else:
        await edit_delete(
            event, f"**📑 يجب عليك كتابة اسم الفار بشك صحيح من القائمة :\n\n**{vnlist}", time=60
        )


@jmthon.ar_cmd(
    pattern="تخصيص (pmpermit|pmpic|pmblock|startmsg)$",
    command=("تخصيص", plugin_category),)
async def custom_jmthonuserbot(event):
    "."
    reply = await event.get_reply_message()
    text = None
    if reply:
        text = reply.text
    if text is None:
        return await edit_delete(event, "**-يجب عليك الرد على النص او الرابط**")
    input_str = event.pattern_match.group(1)
    if input_str == "pmpermit":
        addgvar("pmpermit_txt", text)
    if input_str == "pmblock":
        addgvar("pmblock", text)
    if input_str == "startmsg":
        addgvar("START_TEXT", text)
    if input_str == "pmpic":
        urls = extractor.find_urls(reply.text)
        if not urls:
            return await edit_delete(event, "- الرابط المعطى غير مدعوم", 5)
        text = " ".join(urls)
        addgvar("pmpermit_pic", text)
    await edit_or_reply(event, f"__التخصيص الخاص بك {input_str} تم تحديثه__")
    if BOTLOG_CHATID:
        await event.client.send_message(
            BOTLOG_CHATID,
                    f"#وضع_فار\
                    \n**{input_str}** تم تحديثه بنجاح في قاعده البيانات كـ:",
                )
        await event.client.send_message(BOTLOG_CHATID, text, silent=True)


@jmthon.ar_cmd(
    pattern="ازالة (pmpermit|pmpic|pmblock|startmsg)$",
    command=("delcustom", plugin_category),)
async def custom_jmthonuserbot(event):
    "To delete costomization of your Userbot."
    input_str = event.pattern_match.group(1)
    if input_str == "pmpermit":
        if gvarstatus("pmpermit_txt") is None:
            return await edit_delete(event, "__انت لم تقم بوضع تخصيص لكليشه الحماية__")
        delgvar("pmpermit_txt")
    if input_str == "pmblock":
        if gvarstatus("pmblock") is None:
            return await edit_delete(event, "__انت لم تقم بوضع تخصيص لكليشه الحظر__")
        delgvar("pmblock")
    if input_str == "pmpic":
        if gvarstatus("pmpermit_pic") is None:
            return await edit_delete(event, "__انت لم تقم بوضع تخصيص لصورة الحماية__")
        delgvar("pmpermit_pic")
    if input_str == "startmsg":
        if gvarstatus("START_TEXT") is None:
            return await edit_delete(
                event, "__انت لم تقم بوضع تخصيص لكليشه رسالة البدء__"
            )
        delgvar("START_TEXT")
    await edit_or_reply(
        event, f"__تم بنجاح حذف التخصيص ✓.__"
    )
    if BOTLOG_CHATID:
        await event.client.send_message(
            BOTLOG_CHATID,
            f"#حذف_فار\
                    \n**{input_str}** تم حذفه من قاعده البيانات",
        )
