"""
Created by @Jisan7509
modified by  @mrconfused
Userbot plugin for CatUserbot
translate for Arabic by @RR9R7
"""

from userbot import jmthon

from ..core.managers import edit_or_reply
from ..helpers import fonts as emojify

plugin_category = "fun"


@jmthon.ar_cmd(
    pattern="ايموجي(?:\s|$)([\s\S]*)",
    command=("ايموجي", plugin_category),
    info={
        "header": "يتم تحويل نصك الى ايموجيات كبيره مع بعض السمايلات.",
        "usage": "{tr}ايموجي <نص>",
        "examples": ["{tr}ايموجي كات"],
    },
)
async def itachi(event):
    "لتغيير النص على شكل ايموجي كبير."
    args = event.pattern_match.group(1)
    get = await event.get_reply_message()
    if not args and get:
        args = get.text
    if not args:
        await edit_or_reply(
            event, "**- يجب عليك وضع اسم مع "
        )
        return
    result = ""
    for a in args:
        a = a.lower()
        if a in emojify.kakashitext:
            char = emojify.kakashiemoji[emojify.kakashitext.index(a)]
            result += char
        else:
            result += a
    await edit_or_reply(event, result)


@jmthon.ar_cmd(
    pattern="سمايل(?:\s|$)([\s\S]*)",
    command=("سمايل", plugin_category),
    info={
        "header": "لتحويل النص على شكل سمايل كبير .",
        "usage": "{tr}سمايل <سمايل> <نص>",
        "examples": ["{tr}سمايل 😺 jmthon"],
    },
)
async def itachi(event):
    "للحوصل على رسم للنص على سكل سمايل."
    args = event.pattern_match.group(1)
    get = await event.get_reply_message()
    if not args and get:
        args = get.text
    if not args:
        return await edit_or_reply(
            event, "يجب عليك وضع اسم مع "
        )
    try:
        emoji, arg = args.split(" ", 1)
    except Exception:
        arg = args
        emoji = "😺"
    result = ""
    for a in arg:
        a = a.lower()
        if a in emojify.kakashitext:
            char = emojify.itachiemoji[emojify.kakashitext.index(a)].format(cj=emoji)
            result += char
        else:
            result += a
    await edit_or_reply(event, result)
