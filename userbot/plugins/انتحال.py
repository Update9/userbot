import html

from telethon.tl import functions
from telethon.tl.functions.users import GetFullUserRequest

from ..Config import Config
from . import (
    ALIVE_NAME,
    AUTONAME,
    BOTLOG,
    BOTLOG_CHATID,
    DEFAULT_BIO,
    jmthon,
    edit_delete,
    get_user_from_event,
)

plugin_category = "utils"
DEFAULTUSER = str(AUTONAME) if AUTONAME else str(ALIVE_NAME)
DEFAULTUSERBIO = (
    str(DEFAULT_BIO)
    if DEFAULT_BIO
    else "it's just a bad day"
)


@jmthon.ar_cmd(
    pattern="انتحال(?:\s|$)([\s\S]*)",
    command=("انتحال", plugin_category),
    info={
        "header": "لأنتحال حساب المستخدم الذي وضعت معرفه أو المستخدم الذي تم الرد عليه",
        "usage": "{tr}انتحال <معرف/ايدي/بالرد عليه>",
    },
)
async def _(event):
    "لأنتحال حساب المستخدم الذي وضعت معرفه أو المستخدم الذي تم الرد عليه"
    replied_user, error_i_a = await get_user_from_event(event)
    if replied_user is None:
        return
    user_id = replied_user.id
    profile_pic = await event.client.download_profile_photo(user_id, Config.TEMP_DIR)
    first_name = html.escape(replied_user.first_name)
    if first_name is not None:
        first_name = first_name.replace("\u2060", "")
    last_name = replied_user.last_name
    if last_name is not None:
        last_name = html.escape(last_name)
        last_name = last_name.replace("\u2060", "")
    if last_name is None:
        last_name = "⁪⁬⁮⁮⁮⁮ ‌‌‌‌"
    replied_user = await event.client(GetFullUserRequest(replied_user.id))
    user_bio = replied_user.about
    if user_bio is not None:
        user_bio = replied_user.about
    await event.client(functions.account.UpdateProfileRequest(first_name=first_name))
    await event.client(functions.account.UpdateProfileRequest(last_name=last_name))
    await event.client(functions.account.UpdateProfileRequest(about=user_bio))
    try:
        pfile = await event.client.upload_file(profile_pic)
    except Exception as e:
        return await edit_delete(event, f"**فشل الانتحال هناك خطأ :**\n__{e}__")
    await event.client(functions.photos.UploadProfilePhotoRequest(pfile))
    await edit_delete(event, "**تم انتحال الحساب بنجاح**")
    if BOTLOG:
        await event.client.send_message(
            BOTLOG_CHATID,
            f"#الانتحال\nتم انتحال المستخدم  [{first_name}](tg://user?id={user_id }) بنجاح",
        )


@jmthon.ar_cmd(
    pattern="اعادة$",
    command=("اعادة", plugin_category),
    info={
        "header": "لارجاع حسابك إلى اسمه الأصلي ، و البايو ، و الصورة الشخصيه",
        "note": "للتشغيل الصحيح لهذا الأمر ، تحتاج إلى تعيين فار DEFAULT_BIO مع البايو الخاص بك.",
        "usage": "{tr}اعادة",
    },
)
async def _(event):
    "لأرجاع حسابك الى وضعه الطبيعي"
    name = f"{DEFAULTUSER}"
    blank = ""
    bio = f"{DEFAULTUSERBIO}"
    await event.client(
        functions.photos.DeletePhotosRequest(
            await event.client.get_profile_photos("me", limit=1)
        )
    )
    await event.client(functions.account.UpdateProfileRequest(about=bio))
    await event.client(functions.account.UpdateProfileRequest(first_name=name))
    await event.client(functions.account.UpdateProfileRequest(last_name=blank))
    await edit_delete(event, "تم اعادة حسابك بنجاح")
    if BOTLOG:
        await event.client.send_message(
            BOTLOG_CHATID,
            "#الاعادة \nتم بنجاح اعاد حسابك الى وضعه الاصلي",
        )
