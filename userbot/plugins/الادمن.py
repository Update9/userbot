from asyncio import sleep

from telethon.errors import (
    BadRequestError,
    ImageProcessFailedError,
    PhotoCropSizeSmallError,
)
from telethon.errors.rpcerrorlist import UserAdminInvalidError, UserIdInvalidError
from telethon.tl.functions.channels import (
    EditAdminRequest,
    EditBannedRequest,
    EditPhotoRequest,
)
from telethon.tl.functions.users import GetFullUserRequest
from telethon.tl.types import (
    ChatAdminRights,
    ChatBannedRights,
    InputChatPhotoEmpty,
    MessageMediaPhoto,
)
from telethon.utils import get_display_name

from userbot import jmthon

from ..core.logger import logging
from ..core.managers import edit_delete, edit_or_reply
from ..helpers import media_type
from ..helpers.utils import _format, get_user_from_event
from ..sql_helper.mute_sql import is_muted, mute, unmute
from . import BOTLOG, BOTLOG_CHATID

# =================== STRINGS ============
PP_TOO_SMOL = "**- الصورة صغيرة جدا**"
PP_ERROR = "**فشل اثناء معالجة الصورة**"
NO_ADMIN = "**- عذرا انا لست مشرف هنا**"
NO_PERM = "**- ليست لدي صلاحيات كافيه في هذه الدردشة**"
CHAT_PP_CHANGED = "**- تم تغيير صورة الدردشة**"
INVALID_MEDIA = "**- ابعاد الصورة غير صالحة**"

BANNED_RIGHTS = ChatBannedRights(
    until_date=None,
    view_messages=True,
    send_messages=True,
    send_media=True,
    send_stickers=True,
    send_gifs=True,
    send_games=True,
    send_inline=True,
    embed_links=True,
)

UNBAN_RIGHTS = ChatBannedRights(
    until_date=None,
    send_messages=None,
    send_media=None,
    send_stickers=None,
    send_gifs=None,
    send_games=None,
    send_inline=None,
    embed_links=None,
)

LOGS = logging.getLogger(__name__)
MUTE_RIGHTS = ChatBannedRights(until_date=None, send_messages=True)
UNMUTE_RIGHTS = ChatBannedRights(until_date=None, send_messages=False)

plugin_category = "admin"
# ================================================


@jmthon.ar_cmd(
    pattern="الصورة( -وضع| -حذف)$",
    command=("gpic", plugin_category),
    info={
        "header": "For changing group display pic or deleting display pic",
        "description": "Reply to Image for changing display picture",
        "flags": {
            "-s": "To set group pic",
            "-d": "To delete group pic",
        },
        "usage": [
            "{tr}gpic -s <reply to image>",
            "{tr}gpic -d",
        ],
    },
    groups_only=True,
    require_admin=True,
)
async def set_group_photo(event):  # sourcery no-metrics
    "For changing Group dp"
    flag = (event.pattern_match.group(1)).strip()
    if flag == "-وضع":
        replymsg = await event.get_reply_message()
        photo = None
        if replymsg and replymsg.media:
            if isinstance(replymsg.media, MessageMediaPhoto):
                photo = await event.client.download_media(message=replymsg.photo)
            elif "image" in replymsg.media.document.mime_type.split("/"):
                photo = await event.client.download_file(replymsg.media.document)
            else:
                return await edit_delete(event, INVALID_MEDIA)
        if photo:
            try:
                await event.client(
                    EditPhotoRequest(
                        event.chat_id, await event.client.upload_file(photo)
                    )
                )
                await edit_delete(event, CHAT_PP_CHANGED)
            except PhotoCropSizeSmallError:
                return await edit_delete(event, PP_TOO_SMOL)
            except ImageProcessFailedError:
                return await edit_delete(event, PP_ERROR)
            except Exception as e:
                return await edit_delete(event, f"**خطأ : **`{str(e)}`")
            process = "- تم تحديثها"
    else:
        try:
            await event.client(EditPhotoRequest(event.chat_id, InputChatPhotoEmpty()))
        except Exception as e:
            return await edit_delete(event, f"**خطأ : **`{e}`")
        process = "- تم حذفها "
        await edit_delete(event, "***- تم حذف صورة الكروب بنجاح***")
    if BOTLOG:
        await event.client.send_message(
            BOTLOG_CHATID,
            "#صورة_الكروب\n"
            f"- صورة الكروب تم {process} بنجاح "
            f"الدردشة : {get_display_name(await event.get_chat())}(`{event.chat_id}`)",
        )


@jmthon.ar_cmd(
    pattern="رفع مشرف(?:\s|$)([\s\S]*)",
    command=("رفع مشرف", plugin_category),
    info={
        "header": "To give admin rights for a person",
        "description": "Provides admin rights to the person in the chat\
            \nNote : You need proper rights for this",
        "usage": [
            "{tr}promote <userid/username/reply>",
            "{tr}promote <userid/username/reply> <custom title>",
        ],
    },
    groups_only=True,
    require_admin=True,
)
async def promote(event):
    "To promote a person in chat"
    new_rights = ChatAdminRights(
        add_admins=False,
        invite_users=True,
        change_info=False,
        ban_users=True,
        delete_messages=True,
        pin_messages=True,
    )
    user, rank = await get_user_from_event(event)
    if not rank:
        rank = "ادمن"
    if not user:
        return
    rozevent = await edit_or_reply(event, "**- يتم الرفع **")
    try:
        await event.client(EditAdminRequest(event.chat_id, user.id, new_rights, rank))
    except BadRequestError:
        return await rozevent.edit(NO_PERM)
    await rozevent.edit("**- تم الرفع بنجاح**")
    if BOTLOG:
        await event.client.send_message(
            BOTLOG_CHATID,
            f"#رفع_مشرف \
            \nالمستخدم: [{user.first_name}](tg://user?id={user.id})\
            \nالدردشة: {get_display_name(await event.get_chat())} (**{event.chat_id}**)",
        )


@jmthon.ar_cmd(
    pattern="تنزيل مشرف(?:\s|$)([\s\S]*)",
    command=("demote", plugin_category),
    info={
        "header": "To remove a person from admin list",
        "description": "Removes all admin rights for that peron in that chat\
            \nNote : You need proper rights for this and also u must be owner or admin who promoted that guy",
        "usage": [
            "{tr}demote <userid/username/reply>",
            "{tr}demote <userid/username/reply> <custom title>",
        ],
    },
    groups_only=True,
    require_admin=True,
)
async def demote(event):
    "- تنزيل رتبة شخص في المجموعة"
    user, _ = await get_user_from_event(event)
    if not user:
        return
    rozevent = await edit_or_reply(event, "**- جاري تنزيل الشخص**")
    newrights = ChatAdminRights(
        add_admins=None,
        invite_users=None,
        change_info=None,
        ban_users=None,
        delete_messages=None,
        pin_messages=None,
    )
    rank = "ادمن"
    try:
        await event.client(EditAdminRequest(event.chat_id, user.id, newrights, rank))
    except BadRequestError:
        return await rozevent.edit(NO_PERM)
    await rozevent.edit("**- تم تنزيل المشرف بنجاح**")
    if BOTLOG:
        await event.client.send_message(
            BOTLOG_CHATID,
            f"#تنزيل_مشرف\
            \nالمستخدم: [{user.first_name}](tg://user?id={user.id})\
            \nالدردشه: {get_display_name(await event.get_chat())}(**{event.chat_id}**)",
        )


@jmthon.ar_cmd(
    pattern="حظر(?:\s|$)([\s\S]*)",
    command=("ban", plugin_category),
    info={
        "header": "Will ban the guy in the group where you used this command.",
        "description": "Permanently will remove him from this group and he can't join back\
            \nNote : You need proper rights for this.",
        "usage": [
            "{tr}ban <userid/username/reply>",
            "{tr}ban <userid/username/reply> <reason>",
        ],
    },
    groups_only=True,
    require_admin=True,
)
async def _ban_person(event):
    "- لحظر شخص في المجموعة"
    user, reason = await get_user_from_event(event)
    if not user:
        return
    if user.id == event.client.uid:
        return await edit_delete(event, "**- لا تستطيع حظر نفسك**")
    rozevent = await edit_or_reply(event, "**- تم حظرة بنجاح**")
    try:
        await event.client(EditBannedRequest(event.chat_id, user.id, BANNED_RIGHTS))
    except BadRequestError:
        return await rozevent.edit(NO_PERM)
    try:
        reply = await event.get_reply_message()
        if reply:
            await reply.delete()
    except BadRequestError:
        return await rozevent.edit(
            "**- ليست لدي صلاحيات كافيه لكنه ما زال محظور**"
        )
    if reason:
        await rozevent.edit(
            f"{_format.mentionuser(user.first_name ,user.id)}** تم حظره !!**\n**السبب : ****{reason}**"
        )
    else:
        await rozevent.edit(
            f"{_format.mentionuser(user.first_name ,user.id)} **تم حظره !!**"
        )
    if BOTLOG:
        if reason:
            await event.client.send_message(
                BOTLOG_CHATID,
                f"#حظر\
                \nالمستخدم: [{user.first_name}](tg://user?id={user.id})\
                \nالدردشة: {get_display_name(await event.get_chat())}(**{event.chat_id}**)\
                \nالسبب : {reason}",
            )
        else:
            await event.client.send_message(
                BOTLOG_CHATID,
                f"#حظر\
                \nUSER: [{user.first_name}](tg://user?id={user.id})\
                \nالدردشة: {get_display_name(await event.get_chat())}(**{event.chat_id}**)",
            )


@jmthon.ar_cmd(
    pattern="الغاء حظر(?:\s|$)([\s\S]*)",
    command=("unban", plugin_category),
    info={
        "header": "Will unban the guy in the group where you used this command.",
        "description": "Removes the user account from the banned list of the group\
            \nNote : You need proper rights for this.",
        "usage": [
            "{tr}unban <userid/username/reply>",
            "{tr}unban <userid/username/reply> <reason>",
        ],
    },
    groups_only=True,
    require_admin=True,
)
async def nothanos(event):
    "- لالغاء حظر شخص"
    user, _ = await get_user_from_event(event)
    if not user:
        return
    rozevent = await edit_or_reply(event, "**- جاري الغاء حظر المستخدم**")
    try:
        await event.client(EditBannedRequest(event.chat_id, user.id, UNBAN_RIGHTS))
        await rozevent.edit(
            f"{_format.mentionuser(user.first_name ,user.id)} **- تم الغاء حظر المستخدم**"
        )
        if BOTLOG:
            await event.client.send_message(
                BOTLOG_CHATID,
                "#الغاء_الحظر\n"
                f"المستخدم: [{user.first_name}](tg://user?id={user.id})\n"
                f"الدردشة: {get_display_name(await event.get_chat())}(**{event.chat_id}**)",
            )
    except UserIdInvalidError:
        await rozevent.edit("**- عذرا حدث خطا اثناء الغاء الحظر**")
    except Exception as e:
        await rozevent.edit(f"**خطأ :**\n**{e}**")


@jmthon.ar_cmd(incoming=True)
async def watcher(event):
    if is_muted(event.sender_id, event.chat_id):
        try:
            await event.delete()
        except Exception as e:
            LOGS.info(str(e))


@jmthon.ar_cmd(
    pattern="كتم(?:\s|$)([\s\S]*)",
    command=("كتم", plugin_category),
    info={
        "header": "To stop sending messages from that user",
        "description": "If is is not admin then changes his permission in group,\
            if he is admin or if you try in personal chat then his messages will be deleted\
            \nNote : You need proper rights for this.",
        "usage": [
            "{tr}mute <userid/username/reply>",
            "{tr}mute <userid/username/reply> <reason>",
        ],
    },  # sourcery no-metrics
)
async def startmute(event):
    "- لكتم شخص في الدردشة"
    if event.is_private:
        await event.edit("**- ربما ستحدث بعض المشاكل والاخطاء**")
        await sleep(2)
        await event.get_reply_message()
        replied_user = await event.client(GetFullUserRequest(event.chat_id))
        if is_muted(event.chat_id, event.chat_id):
            return await event.edit(
                "**- الشخص مكتوم بالاصل**"
            )
        if event.chat_id == jmthon.uid:
            return await edit_delete(event, "**- عذرا لا يمكنك كتم نفسك**")
        try:
            mute(event.chat_id, event.chat_id)
        except Exception as e:
            await event.edit(f"**خطأ **\n**{e}**")
        else:
            await event.edit("**- تم كتم الشخص بنجاح\n**｀-´)⊃━☆ﾟ.*･｡ﾟ ****")
        if BOTLOG:
            await event.client.send_message(
                BOTLOG_CHATID,
                "#الكتم\n"
                f"**المستخدم :** [{replied_user.user.first_name}](tg://user?id={event.chat_id})\n",
            )
    else:
        chat = await event.get_chat()
        admin = chat.admin_rights
        creator = chat.creator
        if not admin and not creator:
            return await edit_or_reply(
                event, "**- عذرا انا لست مشرف هنا**  "
            )
        user, reason = await get_user_from_event(event)
        if not user:
            return
        if user.id == jmthon.uid:
            return await edit_or_reply(event, "**- اسف لايمكنك كتم نفسك**")
        if is_muted(user.id, event.chat_id):
            return await edit_or_reply(
                event, "**- هذا الشخص مكتوم بالاصل**"
            )
        result = await event.client.get_permissions(event.chat_id, user.id)
        try:
            if result.participant.banned_rights.send_messages:
                return await edit_or_reply(
                    event,
                     "**- هذا الشخص مكتوم بالاصل**", 
                )
        except AttributeError:
            pass
        except Exception as e:
            return await edit_or_reply(event, f"**خطأ : ****{e}**")
        try:
            await event.client(EditBannedRequest(event.chat_id, user.id, MUTE_RIGHTS))
        except UserAdminInvalidError:
            if "admin_rights" in vars(chat) and vars(chat)["admin_rights"] is not None:
                if chat.admin_rights.delete_messages is not True:
                    return await edit_or_reply(
                        event,
                        "**- لايمكنك كتم المستخدم بدون صلاحيات حذف الرسائل**",
                    )
            elif "creator" not in vars(chat):
                return await edit_or_reply(
                    event, "**- انا لست مشرف هنا** ಥ﹏ಥ  "
                )
            mute(user.id, event.chat_id)
        except Exception as e:
            return await edit_or_reply(event, f"**خطأ : ****{e}**")
        if reason:
            await edit_or_reply(
                event,
                f"المستخدم {_format.mentionuser(user.first_name ,user.id)}\n**تم كتمه بنجاح\nالدردشة {get_display_name(await event.get_chat())}**\n"
                f"**السبب:**{reason}",
            )
        else:
            await edit_or_reply(
                event,
                f"المستخدم {_format.mentionuser(user.first_name ,user.id)}\n**تم كتمه بنجاح\nالدردشة {get_display_name(await event.get_chat())}**\n"
            )
        if BOTLOG:
            await event.client.send_message(
                BOTLOG_CHATID,
                "#كتم\n"
                f"**المستخدم :** [{user.first_name}](tg://user?id={user.id})\n"
                f"**الدردشه :** {get_display_name(await event.get_chat())}(**{event.chat_id}**)",
            )


@jmthon.ar_cmd(
    pattern="الغاء كتم(?:\s|$)([\s\S]*)",
    command=("unmute", plugin_category),
    info={
        "header": "To allow user to send messages again",
        "description": "Will change user permissions ingroup to send messages again.\
        \nNote : You need proper rights for this.",
        "usage": [
            "{tr}unmute <userid/username/reply>",
            "{tr}unmute <userid/username/reply> <reason>",
        ],
    },
)
async def endmute(event):
    "- الالغاء كتم شخص في الدردشة "
    if event.is_private:
        await event.edit("**- ربما ستحدث بعض المشاكل والاخطاء**")
        await sleep(1)
        replied_user = await event.client(GetFullUserRequest(event.chat_id))
        if not is_muted(event.chat_id, event.chat_id):
            return await event.edit(
                "**- ههذا المستخدم غير مكتوم**"
            )
        try:
            unmute(event.chat_id, event.chat_id)
        except Exception as e:
            await event.edit(f"**خطأ **\n**{e}**")
        else:
            await event.edit(
                "**- تم الغاء كتم المستخدم بنجاح**"
            )
        if BOTLOG:
            await event.client.send_message(
                BOTLOG_CHATID,
                "#الغاء_كتم\n"
                f"**المستخدم** [{replied_user.user.first_name}](tg://user?id={event.chat_id})\n",
            )
    else:
        user, _ = await get_user_from_event(event)
        if not user:
            return
        try:
            if is_muted(user.id, event.chat_id):
                unmute(user.id, event.chat_id)
            else:
                result = await event.client.get_permissions(event.chat_id, user.id)
                if result.participant.banned_rights.send_messages:
                    await event.client(
                        EditBannedRequest(event.chat_id, user.id, UNBAN_RIGHTS)
                    )
        except AttributeError:
            return await edit_or_reply(
                event,
                "**- تم الغاء الكتم لهذا المستخدم بنجاح ✓**",
            )
        except Exception as e:
            return await edit_or_reply(event, f"**خطا : ****{e}**")
        await edit_or_reply(
            event,
            f"المستخدم {_format.mentionuser(user.first_name ,user.id)}\n**تم الغاء كتمه ✓ \nالدردشة {get_display_name(await event.get_chat())}**",
        )
        if BOTLOG:
            await event.client.send_message(
                BOTLOG_CHATID,
                "#الغاء_كتم\n"
                f"**المستخدم :** [{user.first_name}](tg://user?id={user.id})\n"
                f"**الدردشه :** {get_display_name(await event.get_chat())}(**{event.chat_id}**)",
            )


@jmthon.ar_cmd(
    pattern="طرد(?:\s|$)([\s\S]*)",
    command=("kick", plugin_category),
    info={
        "header": "To kick a person from the group",
        "description": "Will kick the user from the group so he can join back.\
        \nNote : You need proper rights for this.",
        "usage": [
            "{tr}kick <userid/username/reply>",
            "{tr}kick <userid/username/reply> <reason>",
        ],
    },
    groups_only=True,
    require_admin=True,
)
async def endmute(event):
    "- لطرد الشخص من الدردشه"
    user, reason = await get_user_from_event(event)
    if not user:
        return
    rozevent = await edit_or_reply(event, "**- جاري طرد المستخدم انتظر**")
    try:
        await event.client.kick_participant(event.chat_id, user.id)
    except Exception as e:
        return await rozevent.edit(NO_PERM + f"\n{e}")
    if reason:
        await rozevent.edit(
            f"**- تم بنجاح طرد ** [{user.first_name}](tg://user?id={user.id})**!**\nالسبب: {reason}"
        )
    else:
        await rozevent.edit(f"**- تم بنجاح طرد** [{user.first_name}](tg://user?id={user.id})**!**")
    if BOTLOG:
        await event.client.send_message(
            BOTLOG_CHATID,
            "#طرد\n"
            f"المستخدم: [{user.first_name}](tg://user?id={user.id})\n"
            f"الدردشه: {get_display_name(await event.get_chat())}(**{event.chat_id}**)\n",
        )


@jmthon.ar_cmd(
    pattern="تثبيت( بالاشعار|$)",
    command=("pin", plugin_category),
    info={
        "header": "For pining messages in chat",
        "description": "reply to a message to pin it in that in chat\
        \nNote : You need proper rights for this if you want to use in group.",
        "options": {"loud": "To notify everyone without this.it will pin silently"},
        "usage": [
            "{tr}pin <reply>",
            "{tr}pin loud <reply>",
        ],
    },
)
async def pin(event):
    "- لتثبيت الرسالة في المجموعة "
    to_pin = event.reply_to_msg_id
    if not to_pin:
        return await edit_delete(event, "**- ييجب الرد على الرسالة لتثبيتها**", 5)
    options = event.pattern_match.group(1)
    is_silent = bool(options)
    try:
        await event.client.pin_message(event.chat_id, to_pin, notify=is_silent)
    except BadRequestError:
        return await edit_delete(event, NO_PERM, 5)
    except Exception as e:
        return await edit_delete(event, f"**{e}**", 5)
    await edit_delete(event, "**- تم تثبيت الرساله بنجاح**", 3)
    if BOTLOG and not event.is_private:
        await event.client.send_message(
            BOTLOG_CHATID,
            f"#تثبيت\
                \n**تم بنجاح تثبيت الرسالة في الدردشه**\
                \nالدردشة: {get_display_name(await event.get_chat())}(**{event.chat_id}**)\
                \nالاشعار: {is_silent}",
        )


@jmthon.ar_cmd(
    pattern="الغاء تثبيت( الكل|$)",
    command=("unpin", plugin_category),
    info={
        "header": "For unpining messages in chat",
        "description": "reply to a message to unpin it in that in chat\
        \nNote : You need proper rights for this if you want to use in group.",
        "options": {"all": "To unpin all messages in the chat"},
        "usage": [
            "{tr}unpin <reply>",
            "{tr}unpin all",
        ],
    },
)
async def pin(event):
    "- لالغاء تثبيت الرساله في المجموعة"
    to_unpin = event.reply_to_msg_id
    options = (event.pattern_match.group(1)).strip()
    if not to_unpin and options != "الكل":
        return await edit_delete(
            event,
            "**- يجب الرد على رسالة لإلغاء تثبيتها **",
            5,
        )
    try:
        if to_unpin and not options:
            await event.client.unpin_message(event.chat_id, to_unpin)
        elif options == "الكل":
            await event.client.unpin_message(event.chat_id)
        else:
            return await edit_delete(
                event, "**- يجب الرد على رسالة لإلغاء تثبيتها **", 5
            )
    except BadRequestError:
        return await edit_delete(event, NO_PERM, 5)
    except Exception as e:
        return await edit_delete(event, f"**{e}**", 5)
    await edit_delete(event, "**- تم بنجاح الغاء التثبيت**", 3)
    if BOTLOG and not event.is_private:
        await event.client.send_message(
            BOTLOG_CHATID,
            f"#الغاء_تثبيت\
                \n**تم بنجاح الغاء تثبيت الرسالة**\
                \nالدردشه: {get_display_name(await event.get_chat())}(**{event.chat_id}**)",
        )


@jmthon.ar_cmd(
    pattern="الاحداث( -u)?(?: |$)(\d*)?",
    command=("الاحداث", plugin_category),
    info={
        "header": "To get recent deleted messages in group",
        "description": "To check recent deleted messages in group, by default will show 5. you can get 1 to 15 messages.",
        "flags": {
            "u": "use this flag to upload media to chat else will just show as media."
        },
        "usage": [
            "{tr}undlt <count>",
            "{tr}undlt -u <count>",
        ],
        "examples": [
            "{tr}undlt 7",
            "{tr}undlt -u 7 (this will reply all 7 messages to this message",
        ],
    },
    groups_only=True,
    require_admin=True,
)
async def _iundlt(event):  # sourcery no-metrics
    "- للتحقق من الرسائل المحذوفة الأخيرة في المجموعة‌‌"
    rozevent = await edit_or_reply(event, "**- يتم البحث عن الأحداث**")
    flag = event.pattern_match.group(1)
    if event.pattern_match.group(2) != "":
        lim = int(event.pattern_match.group(2))
        if lim > 15:
            lim = int(15)
        if lim <= 0:
            lim = int(1)
    else:
        lim = int(5)
    adminlog = await event.client.get_admin_log(
        event.chat_id, limit=lim, edit=False, delete=True
    )
    deleted_msg = f"**الرسائل المحذوفة {lim} الأخيرة في هذه المجموعة هي‌‌:**"
    if not flag:
        for msg in adminlog:
            ruser = (
                await event.client(GetFullUserRequest(msg.old.from_id.user_id))
            ).user
            _media_type = media_type(msg.old)
            if _media_type is None:
                deleted_msg += f"\n• **{msg.old.message}** **ارسلت بواسطه** {_format.mentionuser(ruser.first_name ,ruser.id)}"
            else:
                deleted_msg += f"\n• **{_media_type}** **ارسلت بواسطه** {_format.mentionuser(ruser.first_name ,ruser.id)}"
        await edit_or_reply(rozevent, deleted_msg)
    else:
        main_msg = await edit_or_reply(rozevent, deleted_msg)
        for msg in adminlog:
            ruser = (
                await event.client(GetFullUserRequest(msg.old.from_id.user_id))
            ).user
            _media_type = media_type(msg.old)
            if _media_type is None:
                await main_msg.reply(
                    f"{msg.old.message}\n**ارسلت بواسطه** {_format.mentionuser(ruser.first_name ,ruser.id)}"
                )
            else:
                await main_msg.reply(
                    f"{msg.old.message}\n**ارسلت بواسطه** {_format.mentionuser(ruser.first_name ,ruser.id)}",
                    file=msg.old.media,
                )
