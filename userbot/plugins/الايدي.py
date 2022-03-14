from telethon.utils import pack_bot_file_id

from userbot import jmthon
from userbot.core.logger import logging

from ..core.managers import edit_delete, edit_or_reply

plugin_category = "utils"

LOGS = logging.getLogger(__name__)

#translate for Arabic by @RR9R7
@jmthon.ar_cmd(
    pattern="الايدي(?:\s|$)([\s\S]*)",
    command=("الايدي", plugin_category))
async def _(event):
    "للحصول على ايدي المجموعة أو المستخدم"
    input_str = event.pattern_match.group(2)
    if input_str:
        try:
            p = await event.client.get_entity(input_str)
        except Exception as e:
            return await edit_delete(event, f"`{e}`", 5)
        try:
            if p.first_name:
                return await edit_or_reply(
                    event, f"الايدي الخاص بـ `{input_str}` هو `{p.id}`"
                )
        except Exception:
            try:
                if p.title:
                    return await edit_or_reply(
                        event, f"الايدي الخاص بالقناه او الدردشه `{p.title}` هو `{p.id}`"
                    )
            except Exception as e:
                LOGS.info(str(e))
        await edit_or_reply(event, "يجب أن تضع معرف المستخدم أو ترد على المستخدم")
    elif event.reply_to_msg_id:
        r_msg = await event.get_reply_message()
        if r_msg.media:
            bot_api_file_id = pack_bot_file_id(r_msg.media)
            await edit_or_reply(
                event,
                f"**معرف الدردشة الحالي : **`{event.chat_id}`\n**من ايدي المستخدم: **`{r_msg.sender_id}`\n**ايدي ملف الميديا: **`{bot_api_file_id}`",
            )

        else:
            await edit_or_reply(
                event,
                f"**ايدي الدردشه الحاليه : **`{event.chat_id}`\n**من ايدي المستخدم: **`{r_msg.sender_id}`",
            )

    else:
        await edit_or_reply(event, f"**ايدي الدردشه الحاليه : : **`{event.chat_id}`")
