"""
`Credits` @amnd33p
from ..helpers.utils import _format
Modified by @mrconfused
Translate  :  @GGGNE
"""

import io
import traceback
from datetime import datetime

import requests
from selenium import webdriver
from validators.url import url

from userbot import jmthon

from ..Config import Config
from ..core.managers import edit_or_reply
from . import reply_id

plugin_category = "utils"


@jmthon.ar_cmd(
    pattern="سكرين ([\s\S]*)",
    command=("سكرين", plugin_category),
    info={
        "header": "لالتقاط لقطة شاشة لموقع ويب.",
        "usage": "{tr}سكرين <رابط>",
        "examples": "{tr}سكرين https://github.com/sandy1709/j",
    },
)
async def _(event):
    "لالتقاط لقطة شاشة لموقع ويب."
    if Config.CHROME_BIN is None:
        return await edit_or_reply(
            event, "تحتاج إلى تثبيت جوجل كروم."
        )
    jmthonevent = await edit_or_reply(event, "**- تتم المعالجه...**")
    start = datetime.now()
    try:
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument("--ignore-certificate-errors")
        chrome_options.add_argument("--test-type")
        chrome_options.add_argument("--headless")
        # https://stackoverflow.com/a/53073789/4723940
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--disable-dev-shm-usage")
        chrome_options.binary_location = Config.CHROME_BIN
        await event.edit("**Starting Google Chrome BIN**")
        driver = webdriver.Chrome(chrome_options=chrome_options)
        input_str = event.pattern_match.group(1)
        inputstr = input_str
        jmthonurl = url(inputstr)
        if not jmthonurl:
            inputstr = "http://" + input_str
            jmthonurl = url(inputstr)
        if not jmthonurl:
            return await jmthonevent.edit("**- يرجى وضع رابط مع الامر **")
        driver.get(inputstr)
        await jmthonevent.edit("**حساب أبعاد الصفحة**")
        height = driver.execute_script(
            "return Math.max(document.body.scrollHeight, document.body.offsetHeight, document.documentElement.clientHeight, document.documentElement.scrollHeight, document.documentElement.offsetHeight);"
        )
        width = driver.execute_script(
            "return Math.max(document.body.scrollWidth, document.body.offsetWidth, document.documentElement.clientWidth, document.documentElement.scrollWidth, document.documentElement.offsetWidth);"
        )
        driver.set_window_size(width + 100, height + 100)
        # Add some pixels on top of the calculated dimensions
        # for good measure to make the scroll bars disappear
        im_png = driver.get_screenshot_as_png()
        # saves screenshot of entire page
        await jmthonevent.edit("**إيقاف Chrome Bin**")
        driver.close()
        message_id = await reply_id(event)
        end = datetime.now()
        ms = (end - start).seconds
        hmm = f"**الرابط : **{input_str} \n**الوقت :** **{ms} ثواني**"
        await jmthonevent.delete()
        with io.BytesIO(im_png) as out_file:
            out_file.name = input_str + ".PNG"
            await event.client.send_file(
                event.chat_id,
                out_file,
                caption=hmm,
                force_document=True,
                reply_to=message_id,
                allow_cache=False,
                silent=True,
            )
    except Exception:
        await jmthonevent.edit(f"**{traceback.format_exc()}**")


@jmthon.ar_cmd(
    pattern="سكرينشوت ([\s\S]*)",
    command=("سكرينشوت", plugin_category),
    info={
        "header": "To Take a screenshot of a website.",
        "description": "For functioning of this command you need to set SCREEN_SHOT_LAYER_ACCESS_KEY var",
        "usage": "{tr}scapture <link>",
        "examples": "{tr}سكرينشوت https://github.com/sandy1709/catuserbot",
    },
)
async def _(event):
    "To Take a screenshot of a website."
    start = datetime.now()
    message_id = await reply_id(event)
    if Config.SCREEN_SHOT_LAYER_ACCESS_KEY is None:
        return await edit_or_reply(
            event,
            "**تحتاج الى ايبي من هذا الموقع https://screenshotlayer.com/product \n SCREEN_SHOT_LAYER_ACCESS_KEY **",
        )
    jmthonevent = await edit_or_reply(event, "**- جـارِ المعالجه ...**")
    sample_url = "https://api.screenshotlayer.com/api/capture?access_key={}&url={}&fullpage={}&viewport={}&format={}&force={}"
    input_str = event.pattern_match.group(1)
    inputstr = input_str
    jmthonurl = url(inputstr)
    if not jmthonurl:
        inputstr = "http://" + input_str
        jmthonurl = url(inputstr)
    if not jmthonurl:
        return await jmthonevent.edit("**The given input is not supported url**")
    response_api = requests.get(
        sample_url.format(
            Config.SCREEN_SHOT_LAYER_ACCESS_KEY, inputstr, "1", "2560x1440", "PNG", "1"
        )
    )
    # https://stackoverflow.com/a/23718458/4723940
    contentType = response_api.headers["content-type"]
    end = datetime.now()
    ms = (end - start).seconds
    hmm = f"**url : **{input_str} \n**Time :** **{ms} seconds**"
    if "image" in contentType:
        with io.BytesIO(response_api.content) as screenshot_image:
            screenshot_image.name = "screencapture.png"
            try:
                await event.client.send_file(
                    event.chat_id,
                    screenshot_image,
                    caption=hmm,
                    force_document=True,
                    reply_to=message_id,
                )
                await jmthonevent.delete()
            except Exception as e:
                await jmthonevent.edit(str(e))
    else:
        await jmthonevent.edit(f"**{response_api.text}**")
