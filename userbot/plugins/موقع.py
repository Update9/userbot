#    Credts @Mrconfused    translate for Arabic by @RR9R7
from geopy.geocoders import Nominatim
from telethon.tl import types

from userbot import jmthon

from ..core.managers import edit_or_reply
from ..helpers import reply_id

plugin_category = "extra"


@jmthon.ar_cmd(
    pattern="موقع ([\s\S]*)",
    command=("موقع", plugin_category),
    info={
        "header": "لإرسال خريطة الموقع المحدد",
        "usage": "{tr}موقع <مكان>",
        "examples": "{tr}موقع Baghdad",
    },
)
async def gps(event):
    "خريطة الموقع المحدد."
    reply_to_id = await reply_id(event)
    input_str = event.pattern_match.group(1)
    catevent = await edit_or_reply(event, "يتم العثور على الموقع المطلوب")
    geolocator = Nominatim(user_agent="catuserbot")
    geoloc = geolocator.geocode(input_str)
    if geoloc:
        lon = geoloc.longitude
        lat = geoloc.latitude
        await event.client.send_file(
            event.chat_id,
            file=types.InputMediaGeoPoint(types.InputGeoPoint(lat, lon)),
            caption=f"**الموقع : **{input_str}",
            reply_to=reply_to_id,
        )
        await catevent.delete()
    else:
        await catevent.edit("لم أجد الموقع")
