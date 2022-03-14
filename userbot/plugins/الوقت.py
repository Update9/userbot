import os
from datetime import datetime as dt

from PIL import Image, ImageDraw, ImageFont
from pytz import country_names as c_n
from pytz import country_timezones as c_tz
from pytz import timezone as tz

from userbot import jmthon

from ..Config import Config
from ..core.managers import edit_or_reply
from . import reply_id

plugin_category = "utils"

# Userbot timezone


FONT_FILE_TO_USE = "/usr/share/fonts/truetype/dejavu/DejaVuSansMono.ttf"


async def get_tz(con):
    """Get time zone of the given country."""
    if "(Uk)" in con:
        con = con.replace("Uk", "UK")
    if "(Us)" in con:
        con = con.replace("Us", "US")
    if " Of " in con:
        con = con.replace(" Of ", " of ")
    if "(Western)" in con:
        con = con.replace("(Western)", "(western)")
    if "Minor Outlying Islands" in con:
        con = con.replace("Minor Outlying Islands", "minor outlying islands")
    if "Nl" in con:
        con = con.replace("Nl", "NL")
    for c_code in c_n:
        if con == c_n[c_code]:
            return c_tz[c_code]
    try:
        if c_n[con]:
            return c_tz[con]
    except KeyError:
        return


@jmthon.ar_cmd(
    pattern="وقت(?:\s|$)([\s\S]*)(?<![0-9])(?: |$)([0-9]+)?",
    command=("وقت", plugin_category),
    info={
        "header": "للحصول على الوقت الحالي لبلد معين",
        "note": "ملاحظه لمعرفه اسماء البلدان [اضغط هنا](https://telegra.ph/اسماء-الدول-02-25)",
        "usage": "{tr}وقت <اسم الدولة> <رقم المنطقة الزمنية>",
        "examples": "{tr}وقت Brazil 2",
    },
)
async def time_func(tdata):
    """للحصول على الوقت الحالي لبلد معين"""
    con = tdata.pattern_match.group(1).title()
    tz_num = tdata.pattern_match.group(2)
    t_form = "%I:%M"
    d_form = "%d/%m/%y - %A"
    c_name = ""
    if len(con) > 4:
        try:
            c_name = c_n[con]
        except KeyError:
            c_name = con
        timezones = await get_tz(con)
    elif Config.COUNTRY:
        c_name = Config.COUNTRY
        tz_num = Config.TZ_NUMBER
        timezones = await get_tz(Config.COUNTRY)
    else:
        return await edit_or_reply(
            tdata,
            f"⌯︙الـساعة الآن {dt.now().strftime(t_form)}\n⌯︙تـاريـخ اليوم {dt.now().strftime(d_form)}",
        )
    if not timezones:
        return await edit_or_reply(tdata, "⌯︙الـبلد غير صالح")
    if len(timezones) == 1:
        time_zone = timezones[0]
    elif len(timezones) > 1:
        if tz_num:
            tz_num = int(tz_num)
            time_zone = timezones[tz_num - 1]
        else:
            return_str = f"`{c_name} لها مناطق زمنية متعددة:`\n\n"

            for i, item in enumerate(timezones):
                return_str += f"`{i+1}. {item}`\n"

            return_str += "\n**اختر واحدة عن طريق كتابة الرقم "
            return_str += "مع الامر **\n"
            return_str += f"- مثال: .وقت {c_name} 2`"

            return await edit_or_reply(tdata, return_str)

    dtnow1 = dt.now(tz(time_zone)).strftime(t_form)
    dtnow2 = dt.now(tz(time_zone)).strftime(d_form)
    if c_name != Config.COUNTRY:
        await edit_or_reply(
            tdata,
            f"`إنه`  **{dtnow1}**` على `**{dtnow2}**  `في {c_name} ({time_zone} timezone).`",
        )
    if Config.COUNTRY:
        await edit_or_reply(
            tdata,
            f"`إنه`  **{dtnow1}**` على `**{dtnow2}**  `هنا، في {Config.COUNTRY}"
            f"({time_zone} timezone).`",
        )


# كـتابة  @RR7PP
@jmthon.ar_cmd(
    pattern="الوقت(?:\s|$)([\s\S]*)",
    command=("الوقت", plugin_category),
    info={
        "header": "يقوم بعرض الوقت الحالي الخاص بك.",
        "description": "يظهر الوقت الافتراضي الحالي الذي يمكنك تغييره عن طريق تغيير فار TZ في فارات هيروكو.",
        "usage": "{tr}الوقت",
    },
)
async def _(event):
    "يقوم بعرض الوقت الحالي"
    reply_msg_id = await reply_id(event)
    current_time = dt.now().strftime(
        f"⚡⚡⚡⚡⚡⚡⚡⚡⚡⚡⚡⚡⚡⚡⚡⚡⚡⚡\n⚡JMTHON⚡\n⚡⚡⚡⚡⚡⚡⚡⚡⚡⚡⚡⚡⚡⚡⚡⚡⚡⚡\n   {os.path.basename(Config.TZ)}\n  Time: %I:%M:%S \n  Date: %d.%m.%y \n⚡⚡⚡⚡⚡⚡⚡⚡⚡⚡⚡⚡⚡⚡⚡⚡⚡⚡⚡⚡"
    )
    input_str = event.pattern_match.group(1)
    if input_str:
        current_time = input_str
    if not os.path.isdir(Config.TEMP_DIR):
        os.makedirs(Config.TEMP_DIR)
    required_file_name = Config.TEMP_DIR + " " + str(dt.now()) + ".webp"
    img = Image.new("RGBA", (350, 220), color=(0, 0, 0, 115))
    fnt = ImageFont.truetype(FONT_FILE_TO_USE, 30)
    drawn_text = ImageDraw.Draw(img)
    drawn_text.text((10, 10), current_time, font=fnt, fill=(255, 255, 255))
    img.save(required_file_name)
    await event.client.send_file(
        event.chat_id,
        required_file_name,
        reply_to=reply_msg_id,
    )
    os.remove(required_file_name)
    await event.delete()
