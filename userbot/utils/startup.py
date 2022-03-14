import glob
import os
import sys
from datetime import timedelta
from pathlib import Path

from telethon import Button, functions, types, utils

from userbot import BOTLOG, BOTLOG_CHATID, PM_LOGGER_GROUP_ID
from telethon.tl.functions.channels import JoinChannelRequest

from ..Config import Config
from ..core.logger import logging
from ..core.session import jmthon
from ..helpers.utils import install_pip
from ..sql_helper.global_collection import (
    del_keyword_collectionlist,
    get_item_collectionlist,
)
from ..sql_helper.globals import addgvar, gvarstatus
from .pluginmanager import load_module
from .tools import create_supergroup

LOGS = logging.getLogger("jmthon")
cmdhr = Config.COMMAND_HAND_LER


async def setup_bot():
    """
    To set up bot for userbot
    """
    try:
        await jmthon.connect()
        config = await jmthon(functions.help.GetConfigRequest())
        for option in config.dc_options:
            if option.ip_address == jmthon.session.server_address:
                if jmthon.session.dc_id != option.id:
                    LOGS.warning(
                        f"معرف DC ثابت في الجلسة من {jmthon.session.dc_id}"
                        f" الى {option.id}"
                    )
                jmthon.session.set_dc(option.id, option.ip_address, option.port)
                jmthon.session.save()
                break
        bot_details = await jmthon.tgbot.get_me()
        Config.TG_BOT_USERNAME = f"@{bot_details.username}"
        # await jmthon.start(bot_token=Config.TG_BOT_USERNAME)
        jmthon.me = await jmthon.get_me()
        jmthon.uid = jmthon.tgbot.uid = utils.get_peer_id(jmthon.me)
        if Config.OWNER_ID == 0:
            Config.OWNER_ID = utils.get_peer_id(jmthon.me)
    except Exception as e:
        LOGS.error(f"STRING_SESSION - {e}")
        sys.exit()


async def startupmessage():
    """
    Start up message in telegram logger group
    """
    try:
        if BOTLOG:
            Config.JMTHONLOGO = await jmthon.tgbot.send_file(
                BOTLOG_CHATID,
                "https://telegra.ph/file/e9cd63140ffaba419db6b.jpg",
                caption="**- اهلا بك تم تشغيل سورس جمثون بنجاح و بدون اي مشاكل\n لعرض اوامر السورس ارسل `.الاوامر`**",
                buttons=[(Button.url("مجموعة المساعده", "https://t.me/jmthon_support"),)],
            )
    except Exception as e:
        LOGS.error(e)
        return None
    try:
        msg_details = list(get_item_collectionlist("restart_update"))
        if msg_details:
            msg_details = msg_details[0]
    except Exception as e:
        LOGS.error(e)
        return None
    try:
        if msg_details:
            await jmthon.check_testcases()
            message = await jmthon.get_messages(msg_details[0], ids=msg_details[1])
            text = message.text + "\n\n**الان البوت يعمل بشكل طبيعي.**"
            await jmthon.edit_message(msg_details[0], msg_details[1], text)
            if gvarstatus("restartupdate") is not None:
                await jmthon.send_message(
                    msg_details[0],
                    f"{cmdhr}فحص",
                    reply_to=msg_details[1],
                    schedule=timedelta(seconds=10),
                )
            del_keyword_collectionlist("restart_update")
    except Exception as e:
        LOGS.error(e)
        return None


async def add_bot_to_logger_group(chat_id):
    """
    To add bot to logger groups
    """
    bot_details = await jmthon.tgbot.get_me()
    try:
        await jmthon(
            functions.messages.AddChatUserRequest(
                chat_id=chat_id,
                user_id=bot_details.username,
                fwd_limit=1000000,
            )
        )
    except BaseException:
        try:
            await jmthon(
                functions.channels.InviteToChannelRequest(
                    channel=chat_id,
                    users=[bot_details.username],
                )
            )
        except Exception as e:
            LOGS.error(str(e))


async def load_plugins(folder):
    """
    To load plugins from the mentioned folder
    """
    path = f"userbot/{folder}/*.py"
    files = glob.glob(path)
    files.sort()
    for name in files:
        with open(name) as f:
            path1 = Path(f.name)
            shortname = path1.stem
            try:
                if shortname.replace(".py", "") not in Config.NO_LOAD:
                    flag = True
                    check = 0
                    while flag:
                        try:
                            load_module(
                                shortname.replace(".py", ""),
                                plugin_path=f"userbot/{folder}",
                            )
                            break
                        except ModuleNotFoundError as e:
                            install_pip(e.name)
                            check += 1
                            if check > 5:
                                break
                else:
                    os.remove(Path(f"userbot/{folder}/{shortname}.py"))
            except Exception as e:
                os.remove(Path(f"userbot/{folder}/{shortname}.py"))
                LOGS.info(f"غير قادر على تحميل {shortname} بسبب الخطأ {e}")

async def autojo():
    try:
        await jmthon(JoinChannelRequest("@JMTHON"))
        if gvar("AUTOEO") is False:
            return
        else:
            try:
                await jmthon(JoinChannelRequest("@JMTHON"))
            except BaseException:
                pass
            try:
                await jmthon(JoinChannelRequest("@jmthon"))
            except BaseException:
                pass
    except BaseException:
        pass


async def autozs():
    try:
        await jmthon(JoinChannelRequest("@RRRMB"))
        if gvar("AUTOZS") is False:
            return
        else:
            try:
                await jmthon(JoinChannelRequest("@RRRMB"))
            except BaseException:
                pass
            try:
                await jmthon(JoinChannelRequest("@RRRMB"))
            except BaseException:
                pass
    except BaseException:
        pass
        
async def verifyLoggerGroup():
    """
    Will verify the both loggers group
    """
    flag = False
    if BOTLOG:
        try:
            entity = await jmthon.get_entity(BOTLOG_CHATID)
            if not isinstance(entity, types.User) and not entity.creator:
                if entity.default_banned_rights.send_messages:
                    LOGS.info(
                        "- الصلاحيات غير كافيه لأرسال الرسالئل في مجموعه فار ااـ PRIVATE_GROUP_BOT_API_ID."
                    )
                if entity.default_banned_rights.invite_users:
                    LOGS.info(
                        "لا تمتلك صلاحيات اضافه اعضاء في مجموعة فار الـ PRIVATE_GROUP_BOT_API_ID."
                    )
        except ValueError:
            LOGS.error(
                "PRIVATE_GROUP_BOT_API_ID لم يتم العثور عليه . يجب التاكد من ان الفار صحيح."
            )
        except TypeError:
            LOGS.error(
                "PRIVATE_GROUP_BOT_API_ID قيمه هذا الفار غير مدعومه. تأكد من انه صحيح."
            )
        except Exception as e:
            LOGS.error(
                "حدث خطأ عند محاولة التحقق من فار PRIVATE_GROUP_BOT_API_ID.\n"
                + str(e)
            )
    else:
        descript = "لا تحذف هذه المجموعة ولا تغير شيء بها (اذا قمت بعمل شيء جميع الملاحظات الترحيبيه التي اضفتها ستحذف.)"
        photobt = await jmthon.upload_file(file="Jmthon/razan/resources/start/Jmthonp.jpg")
        _, groupid = await create_supergroup(
            "كروب بوت جمثون", jmthon, Config.TG_BOT_USERNAME, descript, photobt 
        )
        addgvar("PRIVATE_GROUP_BOT_API_ID", groupid)
        print(
            "المجموعه الخاصه لفار الـ PRIVATE_GROUP_BOT_API_ID تم حفظه بنجاح و اضافه الفار اليه."
        )
        flag = True
    if PM_LOGGER_GROUP_ID != -100:
        try:
            entity = await jmthon.get_entity(PM_LOGGER_GROUP_ID)
            if not isinstance(entity, types.User) and not entity.creator:
                if entity.default_banned_rights.send_messages:
                    LOGS.info(
                        " الصلاحيات غير كافيه لأرسال الرسالئل في مجموعه فار ااـ PM_LOGGER_GROUP_ID."
                    )
                if entity.default_banned_rights.invite_users:
                    LOGS.info(
                        "لا تمتلك صلاحيات اضافه اعضاء في مجموعة فار الـ  PM_LOGGER_GROUP_ID."
                    )
        except ValueError:
            LOGS.error("PM_LOGGER_GROUP_ID يم تم العثور على قيمه هذا الفار . تاكد من أنه صحيح .")
        except TypeError:
            LOGS.error("PM_LOGGER_GROUP_ID قيمه هذا الفار خطا. تاكد من أنه صحيح.")
        except Exception as e:
            LOGS.error(
                "حدث خطأ اثناء التعرف على فار PM_LOGGER_GROUP_ID.\n"
                + str(e)
            )
    else:
        descript = "⌯︙ وظيفه الكروب يحفظ رسائل الخاص اذا ما تريد الامر احذف الكروب نهائي \n  - @JMTHON"
        photobt = await jmthon.upload_file(file="Jmthon/razan/resources/start/Jmthonp.jpg")
        _, groupid = await create_supergroup(
            "مجموعة التخزين", jmthon, Config.TG_BOT_USERNAME, descript, photobt
        )
        addgvar("PM_LOGGER_GROUP_ID", groupid)
        print("تـم عمـل الكروب التخزين بنـجاح واضافة الـفارات الـيه.")
        flag = True
    if flag:
        executable = sys.executable.replace(" ", "\\ ")
        args = [executable, "-m", "userbot"]
        os.execle(executable, *args, os.environ)
        sys.exit(0)
