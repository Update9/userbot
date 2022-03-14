# Heroku manager for your catuserbot

# CC- @refundisillegal\nSyntax:-\n.get var NAME\n.del var NAME\n.set var NAME

# Copyright (C) 2020 Adek Maulana.
# All rights reserved.

import asyncio
import math
import os

import heroku3
import requests
import urllib3

from userbot import jmthon

from ..Config import Config
from ..core.managers import edit_delete, edit_or_reply

plugin_category = "tools"

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
# =================

Heroku = heroku3.from_key(Config.HEROKU_API_KEY)
heroku_api = "https://api.heroku.com"
HEROKU_APP_NAME = Config.HEROKU_APP_NAME
HEROKU_API_KEY = Config.HEROKU_API_KEY


@jmthon.ar_cmd(
    pattern="(اضف|جلب|حذف) فار ([\s\S]*)",
    command=("فار", plugin_category),
    info={
        "header": "لتعديل فارات هيروكو.",
        "flags": {
            "اضف": "لوضع فار جديد في هيروكو او لتحديث فار قديم",
            "جلب": "لاظهار قيمه و معلومات الفار .",
            "حذف": "لحذف بيانات الفار و ارجاعه الى قيمته الاصلية",
        },
        "usage": [
            "{tr}اضف فار <اسم الفار> <قيمة الفار>",
            "{tr}جلب فار <اسم الفار>",
            "{tr}حذف فار <اسم الفار>",
        ],
        "examples": [
            "{tr}جلب فار ALIVE_NAME",
        ],
    },
)
async def variable(var):  # sourcery no-metrics
    """
   لتعديل اعدادات الفارات، وضع فار جديد او حذف فار او جلب معلومات الفار..... 
    """
    if (Config.HEROKU_API_KEY is None) or (Config.HEROKU_APP_NAME is None):
        return await edit_delete(
            var,
            "عزيزي المستخدم يجب ان تعين معلومات الفارات التالية لاستخدام اوامر الفارات\n `HEROKU_API_KEY`\n `HEROKU_APP_NAME`.",
        )
    app = Heroku.app(Config.HEROKU_APP_NAME)
    exe = var.pattern_match.group(1)
    heroku_var = app.config()
    if exe == "جلب":
        jmthon = await edit_or_reply(var, "- يتم جلب معلومات هذا الفار")
        await asyncio.sleep(1.0)
        try:
            variable = var.pattern_match.group(2).split()[0]
            if variable in heroku_var:
                return await jmthon.edit(
                    "**معلومات الفار**:" f"\n\n`{variable}` = `{heroku_var[variable]}`\n"
                )
            await jmthon.edit(
                "**معلومات الفار**:" f"\n\n__Error:\n-> __`{variable}`__ لم يتم العثور عليه__"
            )
        except IndexError:
            configs = prettyjson(heroku_var.to_dict(), indent=2)
            with open("configs.json", "w") as fp:
                fp.write(configs)
            with open("configs.json", "r") as fp:
                result = fp.read()
                await edit_or_reply(
                    jmthon,
                    "`[HEROKU]` معلومات الفار:\n\n"
                    "================================"
                    f"\n```{result}```\n"
                    "================================",
                )
            os.remove("configs.json")
    elif exe == "اضف":
        variable = "".join(var.text.split(maxsplit=2)[2:])
        jmthon = await edit_or_reply(var, "- يتم وضع المعلومات لهذا الفار")
        if not variable:
            return await jmthon.edit("`.اضف فار <اسم الفار> <القيمة>`")
        value = "".join(variable.split(maxsplit=1)[1:])
        variable = "".join(variable.split(maxsplit=1)[0])
        if not value:
            return await jmthon.edit("`.اضف فار <اسم الفار> <القيمة>`")
        await asyncio.sleep(1.5)
        if variable in heroku_var:
            await jmthon.edit(f"`{variable}` **تم بنجاح تغييره الى  ->  **`{value}`")
        else:
            await jmthon.edit(
                f"`{variable}`**  تم بنجاح اضافته مع القيمة   ->  **`{value}`"
            )
        heroku_var[variable] = value
    elif exe == "حذف":
        jmthon = await edit_or_reply(var, "**- يتم جلب المعلومات لحذف هذا الفار")
        try:
            variable = var.pattern_match.group(2).split()[0]
        except IndexError:
            return await jmthon.edit("**- يجب كتابة اسم الفار الذي تريده حذفه**")
        await asyncio.sleep(1.5)
        if variable not in heroku_var:
            return await jmthon.edit(f"`{variable}`**  لم يتم العثور عليه**")

        await jmthon.edit(f"- الفار `{variable}` \n **تم حذفه بنجاح ✓**")
        del heroku_var[variable]


@jmthon.ar_cmd(
    pattern="استخدامي$",
    command=("استخدامي", plugin_category),
    info={
        "header": "للتحقق من استخدام الدينو للبوت وكذلك لمعرفة الوقت المتبقي لانتهاء تنصيبك.",
        "usage": "{tr}استخدامي",
    },
)
async def dyno_usage(dyno):
    """
    لعرض معلومات استخدامك للبوت الخاص بك
    """
    if (HEROKU_APP_NAME is None) or (HEROKU_API_KEY is None):
        return await edit_delete(
            dyno,
            "عزيزي المستخدم يجب ان تعين معلومات الفارات التالية لاستخدام اوامر الفارات\n `HEROKU_API_KEY`\n `HEROKU_APP_NAME`.",
        )
    dyno = await edit_or_reply(dyno, "**- يتم جلب المعلومات انتظر قليلا**")
    useragent = (
        "Mozilla/5.0 (Linux; Android 10; SM-G975F) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/80.0.3987.149 Mobile Safari/537.36"
    )
    user_id = Heroku.account().id
    headers = {
        "User-Agent": useragent,
        "Authorization": f"Bearer {Config.HEROKU_API_KEY}",
        "Accept": "application/vnd.heroku+json; version=3.account-quotas",
    }
    path = "/accounts/" + user_id + "/actions/get-quota"
    r = requests.get(heroku_api + path, headers=headers)
    if r.status_code != 200:
        return await dyno.edit(
            "**خطا: يوجد شي غير صحيح حدث**\n\n" f">.`{r.reason}`\n"
        )
    result = r.json()
    quota = result["account_quota"]
    quota_used = result["quota_used"]

    # - Used -
    remaining_quota = quota - quota_used
    percentage = math.floor(remaining_quota / quota * 100)
    minutes_remaining = remaining_quota / 60
    hours = math.floor(minutes_remaining / 60)
    minutes = math.floor(minutes_remaining % 60)
    # - Current -
    App = result["apps"]
    try:
        App[0]["quota_used"]
    except IndexError:
        AppQuotaUsed = 0
        AppPercentage = 0
    else:
        AppQuotaUsed = App[0]["quota_used"] / 60
        AppPercentage = math.floor(App[0]["quota_used"] * 100 / quota)
    AppHours = math.floor(AppQuotaUsed / 60)
    AppMinutes = math.floor(AppQuotaUsed % 60)
    await asyncio.sleep(1.5)
    return await dyno.edit(
        "**استخدام الدينو**:\n\n"
        f" -> `استخدام الدينو لتطبيق`  **{Config.HEROKU_APP_NAME}**:\n"
        f"     •  `{AppHours}`**ساعات**  `{AppMinutes}`**دقائق**  "
        f"**|**  [`{AppPercentage}`**%**]"
        "\n\n"
        " -> الساعات المتبقية لهذا الشهر :\n"
        f"     •  `{hours}`**ساعات**  `{minutes}`**دقائق**  "
        f"**|**  [`{percentage}`**%**]"
    )


@jmthon.ar_cmd(
    pattern="لوك$",
    command=("لوك", plugin_category),
    info={
        "header": "للحصول على أحدث 100 سطر من لوك التطبيق على هيروكو.",
        "usage": "{tr}لوك",
    },
)
async def _(dyno):
    "للحصول على أحدث 100 سطر من لوك التطبيق على هيروكو."
    if (HEROKU_APP_NAME is None) or (HEROKU_API_KEY is None):
        return await edit_delete(
            dyno,
            "عزيزي المستخدم يجب ان تعين معلومات الفارات التالية لاستخدام اوامر الفارات\n `HEROKU_API_KEY`\n `HEROKU_APP_NAME`.",
        )
    try:
        Heroku = heroku3.from_key(HEROKU_API_KEY)
        app = Heroku.app(HEROKU_APP_NAME)
    except BaseException:
        return await dyno.reply(
            " يجب التذكر من ان قيمه الفارات التاليه ان تكون بشكل صحيح \nHEROKU_APP_NAME\n HEROKU_API_KEY"
        )
    data = app.get_log()
    await edit_or_reply(
        dyno, data, deflink=True, linktext="**اخر 100 سطر في لوك هيروكو: **"
    )


def prettyjson(obj, indent=2, maxlinelength=80):
    """Renders JSON content with indentation and line splits/concatenations to fit maxlinelength.
    Only dicts, lists and basic types are supported"""
    items, _ = getsubitems(
        obj,
        itemkey="",
        islast=True,
        maxlinelength=maxlinelength - indent,
        indent=indent,
    )
    return indentitems(items, indent, level=0)
