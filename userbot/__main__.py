# @Jmthon - < https://t.me/Jmthon >
# Copyright (C) 2021 - JMTHON-AR
# All rights reserved.
#
# This file is a part of < https://github.com/JMTHON-AR/JMTHON >
# Please read the GNU Affero General Public License in;
# < https://github.com/JMTHON-AR/JM-THON/blob/master/LICENSE
# ===============================================================
import sys

import userbot
from userbot import BOTLOG_CHATID, PM_LOGGER_GROUP_ID

from .Config import Config
from .core.logger import logging
from .core.session import jmthon
from .utils import (
    add_bot_to_logger_group,
    saves,
    load_plugins,
    mybot,
    setup_bot,
    startupmessage,
    verifyLoggerGroup,
)

LOGS = logging.getLogger("arabic")

print(userbot.__copyright__)
print("جميع الحقوق مرخصة بموجب شروط " + userbot.__license__)

cmdhr = Config.COMMAND_HAND_LER

try:
    LOGS.info("يتم اعداد البوت")
    jmthon.loop.run_until_complete(setup_bot())
    LOGS.info("تم تحميل بيانات البوت المساعد")
except Exception as e:
    LOGS.error(f"{e}")
    sys.exit()


async def startup_process():
    await verifyLoggerGroup()
    await load_plugins("plugins")
    await load_plugins("assistant")
    await mybot()
    print("➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖")
    print("تم الان بنجاح اكتمال تنصيب بوت جمثون !!!")
    print(
        f"مبروك الان اذهب في التلجرام و ارسل {cmdhr}الاوامر لرؤية اذا كان البوت شغال\
        \n اذا احتجت مساعده اذهب الى مجموعه https://t.me/jmthon_support"
    )
    print("➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖")
    await verifyLoggerGroup()
    await add_bot_to_logger_group(BOTLOG_CHATID)
    if PM_LOGGER_GROUP_ID != -100:
        await add_bot_to_logger_group(PM_LOGGER_GROUP_ID)
    await startupmessage()
    return


jmthon.loop.run_until_complete(startup_process())
jmthon.loop.create_task(saves())

if len(sys.argv) not in (1, 3, 4):
    jmthon.disconnect()
else:
    try:
        jmthon.run_until_disconnected()
    except ConnectionError:
        pass
