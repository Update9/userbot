import os
from PIL import Image, ImageDraw, ImageFont
from userbot import jmthon
from . import *
from ..core.managers import edit_delete as eod, edit_or_reply as eor


def text_set(text):
    lines = []
    if len(text) <= 55:
        lines.append(text)
    else:
        all_lines = text.split("\n")
        for line in all_lines:
            if len(line) <= 55:
                lines.append(line)
            else:
                k = int(len(line) / 55)
                for z in range(1, k + 2):
                    lines.append(line[((z - 1) * 55) : (z * 55)])
    return lines[:25]
    

@jmthon.on(admin_cmd(pattern="اكتب ?(.*)"))
async def writer(e):
    if e.reply_to:
        reply = await e.get_reply_message()
        text = reply.message
    elif e.pattern_match.group(1):
        text = e.text.split(maxsplit=1)[1]
    else:
        return await e.edit("- يجب عليك الرد على نص اولا")
    img = Image.open("Jmthon/mhd/template.jpg")
    draw = ImageDraw.Draw(img)
    font = ImageFont.truetype("Jmthon/mhd/arjmthon.ttf", 30)
    x, y = 150, 140
    lines = text_set(text)
    line_height = font.getsize("hg")[1]
    for line in lines:
        draw.text((x, y), line, fill=(1, 22, 55), font=font)
        y = y + line_height - 5
    file = "jmthon.jpg"
    img.save(file)
    await e.reply(file=file)
    os.remove(file)
    await e.delete()
