# Userbot module for purging unneeded messages(usually spam or ot).
import re
from asyncio import sleep

from telethon.errors import rpcbaseerrors
from telethon.tl.types import (
    InputMessagesFilterDocument,
    InputMessagesFilterEmpty,
    InputMessagesFilterGeo,
    InputMessagesFilterGif,
    InputMessagesFilterMusic,
    InputMessagesFilterPhotos,
    InputMessagesFilterRoundVideo,
    InputMessagesFilterUrl,
    InputMessagesFilterVideo,
    InputMessagesFilterVoice,
)

from userbot import jmthon

from ..core.managers import edit_delete, edit_or_reply
from ..helpers.utils import reply_id
from . import BOTLOG, BOTLOG_CHATID

plugin_category = "utils"


purgelist = {}

purgetype = {
    "a": InputMessagesFilterVoice,
    "f": InputMessagesFilterDocument,
    "g": InputMessagesFilterGif,
    "i": InputMessagesFilterPhotos,
    "l": InputMessagesFilterGeo,
    "m": InputMessagesFilterMusic,
    "r": InputMessagesFilterRoundVideo,
    "t": InputMessagesFilterEmpty,
    "u": InputMessagesFilterUrl,
    "v": InputMessagesFilterVideo,
    # "s": search
}


@jmthon.ar_cmd(
    pattern="مسح(\s*| \d+)$",
    command=("مسح", plugin_category))
async def delete_it(event):
    "To delete replied message."
    input_str = event.pattern_match.group(1).strip()
    msg_src = await event.get_reply_message()
    if msg_src:
        if input_str and input_str.isnumeric():
            await event.delete()
            await sleep(int(input_str))
            try:
                await msg_src.delete()
                if BOTLOG:
                    await event.client.send_message(
                        BOTLOG_CHATID, "#المسح \n**تم حذف الرسالة بنجاح ✓**"
                    )
            except rpcbaseerrors.BadRequestError:
                if BOTLOG:
                    await event.client.send_message(
                        BOTLOG_CHATID,
                        "**- يجب ان تكون مشرف لمسح الرسائل هنا**",
                    )
        elif input_str:
            if not input_str.startswith("فار"):
                await edit_or_reply(event, "- عذرا يجب الرد بشكل صحيح")
        else:
            try:
                await msg_src.delete()
                await event.delete()
                if BOTLOG:
                    await event.client.send_message(
                        BOTLOG_CHATID, "#المسح \n**تم حذف الرسالة بنجاح ✓**"
                    )
            except rpcbaseerrors.BadRequestError:
                await edit_or_reply(event, "**- عذرا لا استطيع حذف الرسائل**")
    elif not input_str:
        await event.delete()


@jmthon.ar_cmd(
    pattern="حذف من$",
    command=("حذف من", plugin_category))
async def purge_from(event):
    "To mark the message for purging"
    reply = await event.get_reply_message()
    if reply:
        reply_message = await reply_id(event)
        purgelist[event.chat_id] = reply_message
        await edit_delete(
            event,
            "- تم تحديد هذه الرساله للحذف الان قم بالرد على رساله ثانيه تحتها بأمر  `.حذف الى`  لحذف الرسائل التي بين الرسالتين التي تم تحديدهما",
        )
    else:
        await edit_delete(event, "**- يجب عليك الرد على الرسالة اولا**")


@jmthon.ar_cmd(
    pattern="حذف الى$",
    command=("حذف الى", plugin_category))
async def purge_to(event):
    "To mark the message for purging"
    chat = await event.get_input_chat()
    reply = await event.get_reply_message()
    try:
        from_message = purgelist[event.chat_id]
    except KeyError:
        return await edit_delete(
            event,
            "اولا عليك تحديد رسالة بأمر  `.حذف من` بعدها استخدم امر  `.حذف الى` لحذف الرسائل بين الكلمتين التي تم الرد عليهما",
        )
    if not reply or not from_message:
        return await edit_delete(
            event,
            "اولا عليك تحديد رسالة بأمر  `.حذف من` بعدها استخدم امر  `.حذف الى` لحذف الرسائل بين الكلمتين التي تم الرد عليهما",
        )
    try:
        to_message = await reply_id(event)
        msgs = []
        count = 0
        async for msg in event.client.iter_messages(
            event.chat_id, min_id=(from_message - 1), max_id=(to_message + 1)
        ):
            msgs.append(msg)
            count += 1
            msgs.append(event.reply_to_msg_id)
            if len(msgs) == 100:
                await event.client.delete_messages(chat, msgs)
                msgs = []
        if msgs:
            await event.client.delete_messages(chat, msgs)
        await edit_delete(
            event,
            "تم التنظيف  بنجاح \nتم حذف " + str(count) + " من الرسائل",
        )
        if BOTLOG:
            await event.client.send_message(
                BOTLOG_CHATID,
                "#التنظيف \n**حذف " + str(count) + " من الرسائل تم بنجاح**",
            )
    except Exception as e:
        await edit_delete(event, f"**خطأ**\n`{e}`")


@jmthon.ar_cmd(
    pattern="حذف رسائلي",
    command=("حذف رسائلي", plugin_category),
    info={
        "header": "To purge your latest messages.",
        "description": "Deletes x(count) amount of your latest messages.",
        "usage": "{tr}purgeme <count>",
        "examples": "{tr}purgeme 2",
    },
)
async def purgeme(event):
    "To purge your latest messages."
    message = event.text
    count = int(message[9:])
    i = 1
    async for message in event.client.iter_messages(event.chat_id, from_user="me"):
        if i > count + 1:
            break
        i += 1
        await message.delete()

    smsg = await event.client.send_message(
        event.chat_id,
        "**تم التنظيف بنجاح ✓ \n**تم حذف " + str(count) + " من الرسائل**",
    )
    if BOTLOG:
        await event.client.send_message(
            BOTLOG_CHATID,
            "#حذف_رسائلي \n**تم حذف " + str(count) + " من الرسائل بنجاح ✓**",
        )
    await sleep(5)
    await smsg.delete()


# TODO: only sticker messages.
@jmthon.ar_cmd(
    pattern="تنظيف(?:\s|$)([\s\S]*)",
    command=("تنظيف", plugin_category),
    info={
        "header": "To purge messages from the replied message.",
        "description": "•  Deletes the x(count) amount of messages from the replied message\
        \n•  If you don't use count then deletes all messages from the replied messages\
        \n•  If you haven't replied to any message and used count then deletes recent x messages.\
        \n•  If you haven't replied to any message or havent mentioned any flag or count then doesnt do anything\
        \n•  If flag is used then selects that type of messages else will select all types\
        \n•  You can use multiple flags like -gi 10 (It will delete 10 images and 10 gifs but not 10 messages of combination images and gifs.)\
        ",
        "flags": {
            "a": "To delete Voice messages.",
            "f": "To delete documents.",
            "g": "To delete gif's.",
            "i": "To delete images/photos.",
            "l": "To delete locations/gps.",
            "m": "To delete Audio files(music files).",
            "r": "To delete Round video messages.",
            "t": "To delete stickers and text messages.",
            "u": "To delete url/links.",
            "v": "To delete Video messages.",
            "s": "To search paticular message and delete",
        },
        "usage": [
            "{tr}purge <flag(optional)> <count(x)> <reply> - to delete x flagged messages after reply",
            "{tr}purge <flag> <count(x)> - to delete recent x messages",
        ],
        "examples": [
            "{tr}purge 10",
            "{tr}purge -f 10",
            "{tr}purge -gi 10",
        ],
    },
)
async def fastpurger(event):  # sourcery no-metrics
    "To purge messages from the replied message"
    chat = await event.get_input_chat()
    msgs = []
    count = 0
    input_str = event.pattern_match.group(1)
    ptype = re.findall(r"-\w+", input_str)
    try:
        p_type = ptype[0].replace("-", "")
        input_str = input_str.replace(ptype[0], "").strip()
    except IndexError:
        p_type = None
    error = ""
    result = ""
    await event.delete()
    reply = await event.get_reply_message()
    if reply:
        if input_str and input_str.isnumeric():
            if p_type is not None:
                for ty in p_type:
                    if ty in purgetype:
                        async for msg in event.client.iter_messages(
                            event.chat_id,
                            limit=int(input_str),
                            offset_id=reply.id - 1,
                            reverse=True,
                            filter=purgetype[ty],
                        ):
                            count += 1
                            msgs.append(msg)
                            if len(msgs) == 50:
                                await event.client.delete_messages(chat, msgs)
                                msgs = []
                        if msgs:
                            await event.client.delete_messages(chat, msgs)
                    elif ty == "s":
                        error += "\n• لا يمكنك استخدام اضافه الـ `البحث`  مع بقيه الاضافات" 
                    else:
                        error += f"\n• `{ty}` هذه الاضافه غير صحيحه"
            else:
                count += 1
                async for msg in event.client.iter_messages(
                    event.chat_id,
                    limit=(int(input_str) - 1),
                    offset_id=reply.id,
                    reverse=True,
                ):
                    msgs.append(msg)
                    count += 1
                    if len(msgs) == 50:
                        await event.client.delete_messages(chat, msgs)
                        msgs = []
                if msgs:
                    await event.client.delete_messages(chat, msgs)
        elif input_str and p_type is not None:
            if p_type == "s":
                try:
                    cont, inputstr = input_str.split(" ")
                except ValueError:
                    cont = "خطأ"
                    inputstr = input_str
                cont = cont.strip()
                inputstr = inputstr.strip()
                if cont.isnumeric():
                    async for msg in event.client.iter_messages(
                        event.chat_id,
                        limit=int(cont),
                        offset_id=reply.id - 1,
                        reverse=True,
                        search=inputstr,
                    ):
                        count += 1
                        msgs.append(msg)
                        if len(msgs) == 50:
                            await event.client.delete_messages(chat, msgs)
                            msgs = []
                else:
                    async for msg in event.client.iter_messages(
                        event.chat_id,
                        offset_id=reply.id - 1,
                        reverse=True,
                        search=input_str,
                    ):
                        count += 1
                        msgs.append(msg)
                        if len(msgs) == 50:
                            await event.client.delete_messages(chat, msgs)
                            msgs = []
                if msgs:
                    await event.client.delete_messages(chat, msgs)
            else:
                error += f"\n• `{ty}` هذه الاضافه غير صحيحه"
        elif input_str:
            error += f"\n• `.تنظيف {input_str}` هو استخدام غير صحيح شاهد قائمه الاوامر و استخدم بشكل صحيح"
        elif p_type is not None:
            for ty in p_type:
                if ty in purgetype:
                    async for msg in event.client.iter_messages(
                        event.chat_id,
                        min_id=event.reply_to_msg_id - 1,
                        filter=purgetype[ty],
                    ):
                        count += 1
                        msgs.append(msg)
                        if len(msgs) == 50:
                            await event.client.delete_messages(chat, msgs)
                            msgs = []
                    if msgs:
                        await event.client.delete_messages(chat, msgs)
                else:
                    error += f"\n• `{ty}` هذه الاضافه غير صحيحه"
        else:
            async for msg in event.client.iter_messages(
                chat, min_id=event.reply_to_msg_id - 1
            ):
                count += 1
                msgs.append(msg)
                if len(msgs) == 50:
                    await event.client.delete_messages(chat, msgs)
                    msgs = []
            if msgs:
                await event.client.delete_messages(chat, msgs)
    elif p_type is not None and input_str:
        if p_type != "s" and input_str.isnumeric():
            for ty in p_type:
                if ty in purgetype:
                    async for msg in event.client.iter_messages(
                        event.chat_id, limit=int(input_str), filter=purgetype[ty]
                    ):
                        count += 1
                        msgs.append(msg)
                        if len(msgs) == 50:
                            await event.client.delete_messages(chat, msgs)
                            msgs = []
                    if msgs:
                        await event.client.delete_messages(chat, msgs)
                elif ty == "s":
                    error += "\n• لا يمكنك استخدام اضافه الـ `البحث`  مع بقيه الاضافات" 

                else:
                    error += f"\n• `{ty}` هذه الاضافه غير صحيحه"
        elif p_type == "s":
            try:
                cont, inputstr = input_str.split(" ")
            except ValueError:
                cont = "خطأ"
                inputstr = input_str
            cont = cont.strip()
            inputstr = inputstr.strip()
            if cont.isnumeric():
                async for msg in event.client.iter_messages(
                    event.chat_id, limit=int(cont), search=inputstr
                ):
                    count += 1
                    msgs.append(msg)
                    if len(msgs) == 50:
                        await event.client.delete_messages(chat, msgs)
                        msgs = []
            else:
                async for msg in event.client.iter_messages(
                    event.chat_id, search=input_str
                ):
                    count += 1
                    msgs.append(msg)
                    if len(msgs) == 50:
                        await event.client.delete_messages(chat, msgs)
                        msgs = []
            if msgs:
                await event.client.delete_messages(chat, msgs)
        else:
            error += f"\n• `{ty}` هذه الاضافه غير صحيحه"
    elif p_type is not None:
        for ty in p_type:
            if ty in purgetype:
                async for msg in event.client.iter_messages(
                    event.chat_id, filter=purgetype[ty]
                ):
                    count += 1
                    msgs.append(msg)
                    if len(msgs) == 50:
                        await event.client.delete_messages(chat, msgs)
                        msgs = []
                if msgs:
                    await event.client.delete_messages(chat, msgs)
            elif ty == "s":
                error += "\n• لا يمكنك استخدام اضافه الـ `البحث`  مع بقيه الاضافات" 

            else:
                error += f"\n• `{ty}`هذه الاضافه غير صحيحه"
    elif input_str.isnumeric():
        async for msg in event.client.iter_messages(chat, limit=int(input_str) + 1):
            count += 1
            msgs.append(msg)
            if len(msgs) == 50:
                await event.client.delete_messages(chat, msgs)
                msgs = []
        if msgs:
            await event.client.delete_messages(chat, msgs)
    else:
        error += "\n•  لم يتم تحديد اضافه يرجى استخدام الامر بشكل صحيح"
    if msgs:
        await event.client.delete_messages(chat, msgs)
    if count > 0:
        result += "**تم التنظيف بنجاح** \n**تم مسح**" + str(count) + "  ** من الرسائل**"
    if error != "":
        result += f"\n\n**خطأ:**{error}"
    if result == "":
        result += "- لا توجد رسائل لتنظيفها "
    hi = await event.client.send_message(event.chat_id, result)
    if BOTLOG:
        await event.client.send_message(
            BOTLOG_CHATID,
            f"#PURGE \n{result}",
        )
    await sleep(5)
    await hi.delete()
