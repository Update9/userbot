"""
idea from lynda and rose bot
made by @JMTHON
"""
from telethon.errors import BadRequestError
from telethon.errors.rpcerrorlist import UserAdminInvalidError, UserIdInvalidError
from telethon.tl.functions.channels import EditBannedRequest
from telethon.tl.types import ChatBannedRights
from telethon.utils import get_display_name

from userbot import jmthon

from ..core.managers import edit_or_reply
from ..helpers.utils import _format
from . import BOTLOG, BOTLOG_CHATID, extract_time, get_user_from_event

plugin_category = "admin"

# =================== CONSTANT ===================
NO_ADMIN = "**أنا لست مشرفًا!**"
NO_PERM = "**ليس لدي أذونات كافية! هذا هو حزين جدا. اك باي**"


@jmthon.ar_cmd(
    pattern="كتم_مؤقت(?:\s|$)([\s\S]*)",
    command=("كتم_مؤقت", plugin_category),
    info={
        "header": "لكتم المستخدم في المجموعة مؤقتا",
        "description": "كتم المستخدم مؤقتًا لوقت معين.",
        "وحدات زمنية": {
            "s": "ثواني",
            "m": "الدقائق",
            "h": "ساعات",
            "d": "أيام",
            "w": "أسابيع",
        },
        "usage": [
            "{tr}كتم_مؤقت <ايدي/معرف/بالرد> <المدة>",
            "{tr}كتم_مؤقت <ايدي/معرف/بالرد> <المدة> <السبب>",
        ],
        "examples": ["{tr}كتم_مؤقت 2d لاختبار كتم لمدة يومين"],
    },
    groups_only=True,
    require_admin=True,
)
async def tmuter(event):  # sourcery no-metrics
    "لكتم شخص ما لوقت محدد"
    catevent = await edit_or_reply(event, "**- جاري كتم المستخدم ....**")
    user, reason = await get_user_from_event(event, catevent)
    if not user:
        return
    if not reason:
        return await catevent.edit("- عزيزي المستخدم عليك ذكر الوقت اولا..")
    reason = reason.split(" ", 1)
    hmm = len(reason)
    cattime = reason[0].strip()
    reason = "".join(reason[1:]) if hmm > 1 else None
    ctime = await extract_time(catevent, cattime)
    if not ctime:
        return
    if user.id == event.client.uid:
        return await catevent.edit("آسف ، لا يمكنني كتم نفسي")
    try:
        await catevent.client(
            EditBannedRequest(
                event.chat_id,
                user.id,
                ChatBannedRights(until_date=ctime, send_messages=True),
            )
        )
        # Announce that the function is done
        if reason:
            await catevent.edit(
                f"{_format.mentionuser(user.first_name ,user.id)} تم كتهم في {get_display_name(await event.get_chat())}\n"
                f"**مدة الكتم : **{cattime}\n"
                f"**سبب الكتم : **__{reason}__"
            )
            if BOTLOG:
                await event.client.send_message(
                    BOTLOG_CHATID,
                    "#كتم_مؤقت\n"
                    f"**المعرف : **[{user.first_name}](tg://user?id={user.id})\n"
                    f"**المحادثة : **{get_display_name(await event.get_chat())}(**{event.chat_id}**)\n"
                    f"**مدة الكتم : ****{cattime}**\n"
                    f"**سبب الكتم : ****{reason}****",
                )
        else:
            await catevent.edit(
                f"{_format.mentionuser(user.first_name ,user.id)} تم كتمه في {get_display_name(await event.get_chat())}\n"
                f"مكتوم لمدة {cattime}\n"
            )
            if BOTLOG:
                await event.client.send_message(
                    BOTLOG_CHATID,
                    "#كتم_م\n"
                    f"**المعرف : **[{user.first_name}](tg://user?id={user.id})\n"
                    f"**المحادثة : **{get_display_name(await event.get_chat())}(**{event.chat_id}**)\n"
                    f"**مدة الكتم : ****{cattime}**",
                )
        # Announce to logging group
    except UserIdInvalidError:
        return await catevent.edit("**- عزيزي المستخدم يجب عليك تحديد احد لكتمه **")
    except UserAdminInvalidError:
        return await catevent.edit(
            "**إما أنك لست مشرف أو أنك حاولت كتم مشرف لم تقم برفعه انت**"
        )
    except Exception as e:
        return await catevent.edit(f"**{e}**")


@jmthon.ar_cmd(
    pattern="حظر_مؤقت(?:\s|$)([\s\S]*)",
    command=("حظر_مؤقت", plugin_category),
    info={
        "header": "لإزالة مستخدم من المجموعة لفترة زمنية محددة.",
        "description": "يحظر مؤقتًا المستخدم لوقت معين.",
        "وحدات زمنية": {
            "s": "ثواني",
            "m": "الدقائق",
            "h": "ساعات",
            "d": "أيام",
            "w": "أسابيع",
        },
        "usage": [
            "{tr}حظر_مؤقت <ايدي/معرف/بالرد> <المدة>",
            "{tr}حظر_مؤقت <يدي/معرف/بالرد> <المدة> <السبب>",
        ],
        "examples": ["{tr}حظر_مؤقت 2d لاختبار الحظر لمدة يومين"],
    },
    groups_only=True,
    require_admin=True,
)
async def tban(event):  # sourcery no-metrics
    "لحظر شخص لفترة محددة"
    catevent = await edit_or_reply(event, "**- جاري حظر المستخدم....**")
    user, reason = await get_user_from_event(event, catevent)
    if not user:
        return
    if not reason:
        return await catevent.edit("- لم تذكر مدة الحظر.. تأكد من الامر..")
    reason = reason.split(" ", 1)
    hmm = len(reason)
    cattime = reason[0].strip()
    reason = "".join(reason[1:]) if hmm > 1 else None
    ctime = await extract_time(catevent, cattime)
    if not ctime:
        return
    if user.id == event.client.uid:
        return await catevent.edit("آسف ، لا يمكنني حظر نفسي")
    await catevent.edit("**ضرب الآفة!**")
    try:
        await event.client(
            EditBannedRequest(
                event.chat_id,
                user.id,
                ChatBannedRights(until_date=ctime, view_messages=True),
            )
        )
    except UserAdminInvalidError:
        return await catevent.edit(
            "**إما أنك لست مشرف أنك حاولت حظر مشرف لم تقم برفعه انت**"
        )
    except BadRequestError:
        return await catevent.edit(NO_PERM)
    # Helps ban group join spammers more easily
    try:
        reply = await event.get_reply_message()
        if reply:
            await reply.delete()
    except BadRequestError:
        return await catevent.edit(
            "**ليس لدي الصلاحيات الكافيه لكنه ما زال محظور في الدردشة**"
        )
    # Delete message and then tell that the command
    # is done gracefully
    # Shout out the ID, so that fedadmins can fban later
    if reason:
        await catevent.edit(
            f"{_format.mentionuser(user.first_name ,user.id)} تم حظره في {get_display_name(await event.get_chat())}\n"
            f"مده الحظر {cattime}\n"
            f"السبب:**{reason}**"
        )
        if BOTLOG:
            await event.client.send_message(
                BOTLOG_CHATID,
                "#حظر_مؤقت\n"
                f"**المعرف : **[{user.first_name}](tg://user?id={user.id})\n"
                f"**المحادثة : **{get_display_name(await event.get_chat())}(**{event.chat_id}**)\n"
                f"**محظور الى غاية : ****{cattime}**\n"
                f"**السبب : **__{reason}__",
            )
    else:
        await catevent.edit(
            f"{_format.mentionuser(user.first_name ,user.id)} تم حظره في {get_display_name(await event.get_chat())}\n"
            f"المحظور الى غاية {cattime}\n"
        )
        if BOTLOG:
            await event.client.send_message(
                BOTLOG_CHATID,
                "#حظر_مؤقت\n"
                f"**المعرف : **[{user.first_name}](tg://user?id={user.id})\n"
                f"**المحادثة : **{get_display_name(await event.get_chat())}(**{event.chat_id}**)\n"
                f"**محظور الى غاية :** **{cattime}**",
            )
