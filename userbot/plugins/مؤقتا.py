from asyncio import sleep

from userbot import jmthon

plugin_category = "utils"


@jmthon.ar_cmd(
    pattern="مؤقتا (\d*) ([\s\S]*)",
    command=("مؤقتا", plugin_category),
    info={
        "header": "To schedule a message after given time(in seconds).",
        "usage": "{tr}schd <time_in_seconds>  <message to send>",
        "examples": "{tr}schd 120 hello",
    },
)
async def _(event):
    "To schedule a message after given time"
    jmthon = ("".join(event.text.split(maxsplit=1)[1:])).split(" ", 1)
    message = jmthon[1]
    ttl = int(jmthon[0])
    await event.delete()
    await sleep(ttl)
    await event.respond(message)
