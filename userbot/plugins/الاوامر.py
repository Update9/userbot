import re

from telethon import Button, events
from telethon.events import CallbackQuery

from Jmthon.razan.resources.assistant import *
from Jmthon.razan.resources.mybot import *
from userbot import jmthon
from ..core import check_owner
from ..Config import Config

ROE = "** هـذه هي قائمة اوامـر سـورس جمثـون الخـاصه بـك**"

if Config.TG_BOT_USERNAME is not None and tgbot is not None:

    @tgbot.on(events.InlineQuery)
    async def inline_handler(event):
        builder = event.builder
        result = None
        query = event.text
        await bot.get_me()
        if query.startswith("اوامري") and event.query.user_id == bot.uid:
            buttons = [
                [
                    Button.inline("ملفات الادمن 👮", data="jmthon0"),
                    Button.inline("ملفات البوت 🤖", data="BOTCME"),
                ],
                [
                    Button.inline("ملفات المرح ⛄️ ", data="FUNCMD_1"),
                    Button.inline("ملفات الميديا 🎧", data="MEDEA1"),
                ],
                [
                    Button.inline("الادوات 🧰", data="TTXOS"),
                    Button.inline("المرفقات 🗂", data="TKRAZRT"),
                ],
                [
                    Button.inline("الاضافيات ➕ ", data="krrznd"),
                    Button.inline("اغلاق القائمة 🔒", data="jrzst"),
                ],
            ]
            result = builder.article(
                    title="JMTHON - USERBOT",
                    text=ROE,
                    buttons=buttons,
                    link_preview=False,
                )
            await event.answer([result] if result else None)


@bot.on(admin_cmd(outgoing=True, pattern="اوامري"))
async def repo(event):
    if event.fwd_from:
        return
    RR7PP = Config.TG_BOT_USERNAME
    if event.reply_to_msg_id:
        await event.get_reply_message()
    response = await bot.inline_query(RR7PP, "اوامري")
    await response[0].click(event.chat_id)
    await event.delete()
    
@jmthon.tgbot.on(CallbackQuery(data=re.compile(rb"ma2in")))
@check_owner
async def _(event):
    buttons = [
    [
    Button.inline("ملفات الادمن 👮", data="jmthon0"),
    Button.inline("ملفات البوت 🤖", data="BOTCME"),
    ],
    [
    Button.inline("ملفات المرح ⛄️ ", data="FUNCMD_1"),
    Button.inline("ملفات الميديا 🎧", data="MEDEA1"),
    ],
    [
    Button.inline("الادوات 🧰", data="TTXOS"),
    Button.inline("المرفقات 🗂", data="TKRAZRT"),
    ],
    [
    Button.inline("الاضافيات ➕ ", data="krrznd"),
    Button.inline("اغلاق القائمة 🔒", data="jrzst"),
    ],
   ]
    await event.edit("هذه هي قائمه اوامر سورس جمثون", buttons=buttons)




@jmthon.tgbot.on(CallbackQuery(data=re.compile(rb"TKRAZRT")))
@check_owner
async def _(event):
    buttons = [
    [
    Button.inline("اضافه ترحيب", data="tkrraz1"),
    Button.inline("حذف الترحيبات", data="tkrraz2"),
    ],
    [
    Button.inline("اضافه رد", data="tkrraz3"),
    Button.inline("حذف الردود", data="tkrraz4"),
    ],
    [
    Button.inline("ايقاف رد", data="tkrraz5"),
    Button.inline("الردود المضافه", data="tkrraz6"),
    ],
    [
    Button.inline("عرض الترحيبات", data="tkrraz7"), 
    Button.inline("تكرار وقتي", data="tkrraz8"),
    ],
    [
    Button.inline("تكرار عادي", data="tkrraz9"),
    Button.inline("تكرار الملصق", data="tkrraz0"),
    ],
    [
    Button.inline("التالي", data=""),
    Button.inline("القائمه الرئيسي", data="ma2in"),
    Button.inline("رجوع", data=""),
    ], 
   ]
    await event.edit("اختر احد الاوامر التاليه", buttons=buttons)



@jmthon.tgbot.on(CallbackQuery(data=re.compile(rb"tkrraz1")))
@check_owner
async def _(event):
    buttons = [[Button.inline("رجوع", data="TKRAZRT"),]]
    await event.edit("**الامر :**  `.ترحيب`\n\nالفئة : المرفقات\n\n✘ مقدمة : لاضافة ترحيب في المجموعه\n\n✘ الشرح : لاضافة ترحيب في المجموعه ويقوم بالترحيب تلقائيا فور دخول عضو جديد للمجموعة يكتب الامر في الدردشه التي تريد اضافه الترحيب بها\n\n✘ الاستخدام :\n`.ترحيب` <ترحيبك>", buttons=buttons)
    
@jmthon.tgbot.on(CallbackQuery(data=re.compile(rb"tkrraz2")))
@check_owner
async def _(event):
    buttons = [[Button.inline("رجوع", data="TKRAZRT"),]]
    await event.edit("**الامر :**  `.حذف الترحيبات`\n\nالفئة : المرفقات\n\n✘ مقدمة : لحذف جميع الترحيبات في المجموعه\n\n✘ الشرح : لحذف جميع الترحيبات من المجموعة وعدم الترحيب بالاعضاء الجدد\n\n✘ الاستخدام :\n`.حذف الترحيبات`", buttons=buttons)

@jmthon.tgbot.on(CallbackQuery(data=re.compile(rb"tkrraz3")))
@check_owner
async def _(event):
    buttons = [[Button.inline("رجوع", data="TKRAZRT"),]]
    await event.edit("**الامر :**  `.رد`\n**الفئة : الادوات**\n\n**✘ مقدمة : يقوم بإضافة الرد في المجموعة**\n\n**✘ الشرح : بالرد على نص وكتابه الامر مع كلمه لحفظ رد في المجموعه*\n\n**✘ الاستخدام :**\n  `.رد` <الرد> <بالرد على نص>", buttons=buttons, link_preview=False)

@jmthon.tgbot.on(CallbackQuery(data=re.compile(rb"tkrraz4")))
@check_owner
async def _(event):
    buttons = [[Button.inline("رجوع", data="TKRAZRT"),]]
    await event.edit("**الامر :**  `.حذف الردود`\n**الفئة : الادوات**\n\n**✘ مقدمة : حذف جميع الردود**\n\n**✘ الشرح : يقوم بحذف جميع الردود الذي قمت باضافته في الدردشة اكتب الامر في المجموعه وارسله **\n\n**✘ الاستخدام :**\n  `.حذف الردود`", buttons=buttons)

@jmthon.tgbot.on(CallbackQuery(data=re.compile(rb"tkrraz5")))
@check_owner
async def _(event):
    buttons = [[Button.inline("رجوع", data="TKRAZRT"),]]
    await event.edit("**الامر :**  `.ايقاف`\n**الفئة : الادوات **\n\n**✘ مقدمة : يقوم بإيقاف رد معين في المجموعة**\n\n**✘ الشرح : بكتابه الامر مع الرد وارساله في المجموعه لايقاف هذا الرد**\n\n\n**✘ الاستخدام :**\n  `.ايقاف` <الرد> ", buttons=buttons)

@jmthon.tgbot.on(CallbackQuery(data=re.compile(rb"tkrraz6")))
@check_owner
async def _(event):
    buttons = [[Button.inline("رجوع", data="TKRAZRT"),]]
    await event.edit("**الامر :**  `.الردود`\n**الفئة : الادوات**\n\n**✘ مقدمة : عرض جميع الردود المضافة في المجموعة**\n\n**✘ الشرح : فقط قم بارسال الردود في المجموعه لعرض الردود التي تم اضافتها**\n\n\n**✘ الاستخدام :**\n  `.الردود`", buttons=buttons)

@jmthon.tgbot.on(CallbackQuery(data=re.compile(rb"tkrraz7")))
@check_owner
async def _(event):
    buttons = [[Button.inline("رجوع", data="TKRAZRT"),]]
    await event.edit("*الامر :**   `.الترحيبات`\n\n**الفئة : المرفقات**\n\n**✘ مقدمة : لعرض قائمة الترحيبات**\n\n**✘ الشرح : لعرض قائمة الترحيبات المضافة في المجموعة ارسل الامر فقط **\n\n\n**✘ الاستخدام** :\n. `.الترحيبات`", buttons=buttons)


@jmthon.tgbot.on(CallbackQuery(data=re.compile(rb"tkrraz8")))
@check_owner
async def _(event):
    buttons = [[Button.inline("رجوع", data="TKRAZRT"),]]
    await event.edit("الامر : `.مكرر` \nالفئة : الادوات \n\n✘ مقدمة : لتفعيل بوت النشر في المجموعه \n\n✘ الشرح : يقوم بالتكرار لرساله معينه في المجموعه بوقت محدد تضعه انت  ،  اكتب الامر اولا بعدها عدد الرسائل ثم الوقت الفاصل بين كل عمليه تكرار الوقت بالثواني  وبعدها ترد على النص المراد تكراره\n\n- شرح  أكثر   [اضغط هنا](https://t.me/RRRDF/99)\n\n✘ الاستخدام :\n     `.مكرر` <عدد التكرار> <الوقت بالثواني> < بالرد على الرساله >\n\n✘ مثال  :\n       `.مكرر 5 2`  < والرد على رساله>", buttons=buttons)

@jmthon.tgbot.on(CallbackQuery(data=re.compile(rb"tkrraz9")))
@check_owner
async def _(event):
    buttons = [[Button.inline("رجوع", data="TKRAZRT"),]]
    await event.edit("الامر :  `.كرر`    \nالفئة : المرفقات \n\n✘ مقدمة : لتكرار اي شي بالرد عليه\n\n✘ الشرح : يستخدم بكتابه الامر مع عدد التكرار و الرد على صورة او نص او يشي لتكراره في المجموعه \n\n✘ الاستخدام : \n`.كرر` <عدد><بالرد>", buttons=buttons)



@jmthon.tgbot.on(CallbackQuery(data=re.compile(rb"tkrraz0")))
@check_owner
async def _(event):
    buttons = [[Button.inline("رجوع", data="TKRAZRT"),]]
    await event.edit("الامر :  `.تكرار الملصق`    \nالفئة : المرفقات \n\n✘ مقدمة : لتكرار حزمه الملصقات\n\n✘ الشرح : يستخدم الامر بالرد على حزمه الملصقات ليقوم بأرسال جميع الملصقات التي في الحزمه في الدردشه\n\n✘ الاستخدام : \n`.تكرار الملصق`", buttons=buttons)
    
    
    
    

@jmthon.tgbot.on(CallbackQuery(data=re.compile(rb"TTXOS")))
@check_owner
async def _(event):
    buttons = [
    [
    Button.inline("اسم وقتي", data="ttos1"),
    Button.inline("بايو وقتي", data="ttos2"),
    ],
    [
    Button.inline("الصورة الوقتية", data="ttos3"),
    Button.inline("موقع", data="ttos4"),
    ],
    [
    Button.inline("احصائيات كورونا", data="ttos5"),
    Button.inline("تحميل صور", data="ttos7"),
    ],
    [
    Button.inline("سكرين شوت", data="ttos6"),
    Button.inline("حفظ الصورة الذاتية", data="ttos8"),
    ],
    [
    Button.inline("انتحال", data="ttos9"),
    Button.inline("الغاء الانتحال", data="ttos0"),
    ],
    [
    Button.inline("التالي", data="SSXJ"),
    Button.inline("القائمه الرئيسي", data="ma2in"),
    Button.inline("رجوع", data=""),
    ], 
   ]
    await event.edit("اختر احد الاوامر التاليه", buttons=buttons)



@jmthon.tgbot.on(CallbackQuery(data=re.compile(rb"BOTCME")))
@check_owner
async def _(event):
    buttons = [
    [
    Button.inline("فحص", data="bbost1"),
    Button.inline("البنك", data="bbost2"),
    ],
    [
    Button.inline("بوتي", data="bbost3"),
    Button.inline("الانلاين تشغيل ", data="bbost4"),
    ],
    [
    Button.inline("الانلاين تعطيل", data="bbost5"),
    Button.inline("اعادة تشغيل", data="bbost7"),
    ],
    [
    Button.inline("أيقاف السورس", data="bbost6"),
    Button.inline("أيقاف مؤقت", data="bbost8"),
    ],
    [
    Button.inline("اشعارات السورس", data="bbost9"),
    ],
    [
    Button.inline("التالي", data=""),
    Button.inline("القائمه الرئيسي", data="ma2in"),
    Button.inline("رجوع", data=""),
    ], 
   ]
    await event.edit("اختر احد الاوامر التاليه", buttons=buttons)



@jmthon.tgbot.on(CallbackQuery(data=re.compile(rb"bbost1")))
@check_owner
async def _(event):
    buttons = [[Button.inline("رجوع", data="BOTCME"),]]
    await event.edit("**الامر :**  `.فحص` \n**الفئة : البوت**\n\n**✘ مقدمة :  للتأكد من فعالية السورس**\n\n**✘ الشرح : فقط ارسل الامر لرؤية اذا كان البوت يعمل بنجاح او لا**\n\n✘ الاستخدام :\n\n `.فحص`", buttons=buttons)
    
@jmthon.tgbot.on(CallbackQuery(data=re.compile(rb"bbost2")))
@check_owner
async def _(event):
    buttons = [[Button.inline("رجوع", data="BOTCME"),]]
    await event.edit("**الامر :**  `.بنك` \n**الفئة : البوت**\n\n**✘ مقدمة : لعرض سرعه البوت مع صورة**\n\n**✘ الشرح : يقوم بعرض سرعه البوت والتاكد من البوت يعمل بنجاح**\n\n✘ الاستخدام :\n\n `.بنك`", buttons=buttons)

@jmthon.tgbot.on(CallbackQuery(data=re.compile(rb"bbost3")))
@check_owner
async def _(event):
    buttons = [[Button.inline("رجوع", data="BOTCME"),]]
    await event.edit("**الامر :**  `.بوتي` \n**الفئة : البوت**\n\n**✘ مقدمة :  لعرض البوت الخاص بك**\n\n**✘ الشرح : فقط ارسل الامر وسيعرض لك البون الذي قمت بالتنصيب به كذلك في البوت بعض الاوامر ادخل وجربه**\n\n✘ الاستخدام :\n\n `.بوتي`", buttons=buttons)

@jmthon.tgbot.on(CallbackQuery(data=re.compile(rb"bbost4")))
@check_owner
async def _(event):
    buttons = [[Button.inline("رجوع", data="BOTCME"),]]
    await event.edit("الامر : `.الانلاين تشغيل`\n\n الفئة: البوت\n\n✘ مقدمة : لتفعيل وضع الانلاين\n\n✘ الشرح : لتفعيل وضع الانلاين للبوت ليمكنك استخدام الاوامر بدون مشاكل \n\n✘ الاستخدام :\n `.الانلاين تشغيل`", buttons=buttons)

@jmthon.tgbot.on(CallbackQuery(data=re.compile(rb"bbost5")))
@check_owner
async def _(event):
    buttons = [[Button.inline("رجوع", data="BOTCME"),]]
    await event.edit("الامر : `.الانلاين تعطيل`\n\n الفئة: البوت\n\n✘ مقدمة : لتعطيل وضع الانلاين\n\n✘ الشرح : لتعطيل وضع الانلاين للبوت الخاص بك\n\n✘ الاستخدام :\n `.الانلاين تعطيل`", buttons=buttons)

@jmthon.tgbot.on(CallbackQuery(data=re.compile(rb"bbost6")))
@check_owner
async def _(event):
    buttons = [[Button.inline("رجوع", data="BOTCME"),]]
    await event.edit("الامر : `.أيقاف السورس`\n\n الفئة : البوت\n\n✘ مقدمة : لتعطيل عمل السورس\n\n✘ الشرح : لتعطيل السورس لديك بحيث لا يمكنك استخدامه مره ثانيه الا بتفعيله من داخل هيروكو\n\n✘ الاستخدام :\n `.أيقاف السورس`", buttons=buttons)

@jmthon.tgbot.on(CallbackQuery(data=re.compile(rb"bbost8")))
@check_owner
async def _(event):
    buttons = [[Button.inline("رجوع", data="BOTCME"),]]
    await event.edit("الامر : `.أيقاف مؤقت`\n\n الفئة: البوت\n\n✘ مقدمة : سوف يتوقف السورس عن العمل في الوقت المذكور\n\n✘ الاستخدام :\n `.أيقاف مؤقت` <عدد الثواني>", buttons=buttons)


@jmthon.tgbot.on(CallbackQuery(data=re.compile(rb"bbost7")))
@check_owner
async def _(event):
    buttons = [[Button.inline("رجوع", data="BOTCME"),]]
    await event.edit("الامر : `.اعادة تشغيل`\n\n الفئة : البوت\n\n✘ مقدمة : لاعادة تشغيل السورس الخاص بك فقط اكتب الامر و سيتوقف عن العمل لبعض من الدقائق\n\n✘ الاستخدام :\n `.اعادة تشغيل`", buttons=buttons)

@jmthon.tgbot.on(CallbackQuery(data=re.compile(rb"bbost9")))
@check_owner
async def _(event):
    buttons = [[Button.inline("رجوع", data="BOTCME"),]]
    await event.edit("الامر : `.التحديثات تشغيل`\n`.التحديثات ايقاف`\n\n الفئة : البوت\n\n✘ مقدمة : لتحديث المحادثه بعد اعادة تشغيل السورس او تحديثه\n\n✘ الشرح : بعد تفعيل هذه الميزه سيقوم البوت تلقائيا بارسال امر بنك بعد اعادة تشغيله او تحديثه لتذكيرك انه رجع طبيعي\n\n✘ الاستخدام :\n `.التحديثات تشغيل`\n`.التحديثات ايقاف`", buttons=buttons)

@jmthon.tgbot.on(CallbackQuery(data=re.compile(rb"SSXJ")))
@check_owner
async def _(event):
    buttons = [
    [
    Button.inline("تشغيل الحماية", data="kkui1"),
    Button.inline("تعطيل الحماية", data="kkui2"),
    ],
    [
    Button.inline("السماح", data="kkui3"),
    Button.inline("الرفض", data="kkui4"),
    ],
    [
    Button.inline("قائمه الحمايه", data="kkui5"),
    Button.inline("إذاعة للكروبات", data="kkui7"),
    ],
    [
    Button.inline("اذاعه للخاص", data="kkui6"),
    Button.inline("سليب", data="kkui8"),
    ],
    [
    Button.inline("سليب ميديا", data="kkui9"),
    Button.inline("ايدي", data="kkui0"),
    ],
    [
    Button.inline("التالي", data=""),
    Button.inline("القائمه الرئيسي", data="ma2in"),
    Button.inline("رجوع", data="TTXOS"),
    ], 
   ]
    await event.edit("اختر احد الاوامر التاليه", buttons=buttons)


@jmthon.tgbot.on(CallbackQuery(data=re.compile(rb"kkui1")))
@check_owner
async def _(event):
    buttons = [[Button.inline("رجوع", data="SSXJ"),]]
    await event.edit("**الامر :**  `.الحماية تشغيل` \n**الفئة : الادوات**\n\n**✘ مقدمة :  لتفعيل حماية الخاص**\n\n**✘ الشرح : لتفعيل وضع الحمايه للخاص اي مستخدم سيقوم بارسال رساله لك سيتم تحذيره 7 مرات وبعدها حظره**\n\n✘ الاستخدام :\n\n `.الحماية تشغيل`", buttons=buttons)
    
@jmthon.tgbot.on(CallbackQuery(data=re.compile(rb"kkui2")))
@check_owner
async def _(event):
    buttons = [[Button.inline("رجوع", data="SSXJ"),]]
    await event.edit("**الامر :**  `.الحماية تعطيل` \n**الفئة : الادوات**\n\n**✘ مقدمة :  لتعطيل حماية الخاص**\n\n**✘ الشرح : لتعطيل حمايه الخاص والسماح بجميع المستخدمين بالدخول اليك**\n\n✘ الاستخدام :\n\n `.الحماية تعطيل`", buttons=buttons)

@jmthon.tgbot.on(CallbackQuery(data=re.compile(rb"kkui3")))
@check_owner
async def _(event):
    buttons = [[Button.inline("رجوع", data="SSXJ"),]]
    await event.edit("**الامر :**  `.سماح` \n**الفئة : الادوات**\n\n**✘ مقدمة :  للسماح بالشخص التكلم معك**\n\n**✘ الشرح : يستخدم هذا الامر عند تفعيل حمايه الخاص عندما تريد ان تسمح لشخص بالتكلم بدون تحذيرات**\n\n✘ الاستخدام :\n\n `.سماح` <بالرد>", buttons=buttons)

@jmthon.tgbot.on(CallbackQuery(data=re.compile(rb"kkui4")))
@check_owner
async def _(event):
    buttons = [[Button.inline("رجوع", data="SSXJ"),]]
    await event.edit("**الامر :**  `.رفض` \n**الفئة : الادوات**\n\n**✘ مقدمة :  لرفض الشخص للتكلم معك**\n\n**✘ الشرح : يستخدم هذا الامر عند تفعيل حمايه الخاص عندما تريد ان ترفض من مستخدم بالتكلم معك سيتم تحذيره**\n\n✘ الاستخدام :\n\n `.رفض` <بالرد>", buttons=buttons)

@jmthon.tgbot.on(CallbackQuery(data=re.compile(rb"kkui5")))
@check_owner
async def _(event):
    buttons = [[Button.inline("رجوع", data="SSXJ"),]]
    await event.edit("الامر : `.المسموح لهم`\n\n الفئة : الأدوات\n\n✘ مقدمة : لعرض الاشخاص الذي سمحت لهم بالتكلم معك\n\n✘ الشرح : يستخدم هذا الامر بعد تفعيل حمايه الخاص لعرض من الذي قمت بالسماح له او رفضه في الخاص \n\n✘ الاستخدام :\n `.المسموح لهم`", buttons=buttons)

@jmthon.tgbot.on(CallbackQuery(data=re.compile(rb"kkui6")))
@check_owner
async def _(event):
    buttons = [[Button.inline("رجوع", data="SSXJ"),]]
    await event.edit("الامر : `.للكروبات`\n\n الفئة : الأدوات\n\n✘ مقدمة : لعمل اذاعه في المجموعات\n\n✘ الشرح : لعمل اذاعه في الكروبات بالرد على نص او صورة او ايشي بالامر وسيرسله لجميع المجموعات \n\n✘ الاستخدام :\n `.للكروبات` < بالرد >", buttons=buttons)

@jmthon.tgbot.on(CallbackQuery(data=re.compile(rb"kkui7")))
@check_owner
async def _(event):
    buttons = [[Button.inline("رجوع", data="SSXJ"),]]
    await event.edit("الامر : `.للخاص`\n\n الفئة : الأدوات\n\n✘ مقدمة : لعمل اذاعه في الخاص\n\n✘ الشرح : لعمل اذاعه في الخاص بالرد على نص او صورة او اي شيء بالامر وسيرسله لجميع المحادثات في الخاص \n\n✘ الاستخدام :\n `.للخاص` < بالرد >", buttons=buttons)

@jmthon.tgbot.on(CallbackQuery(data=re.compile(rb"kkui8")))
@check_owner
async def _(event):
    buttons = [[Button.inline("رجوع", data="SSXJ"),]]
    await event.edit("الامر : `.سليب`\n\n الفئة : الأدوات\n\n✘ مقدمة : امر سليب لوضع حسابك اوفلاين\n\n✘ الشرح : عند تفعيل الامر هذا اي شخص سيرسلك سيقوم بقول له ان مالك الحساب ليس موجود الان \n\n✘ الاستخدام :\n `.سليب`  <سبب>(السبب اختياري) ", buttons=buttons)

@jmthon.tgbot.on(CallbackQuery(data=re.compile(rb"kkui9")))
@check_owner
async def _(event):
    buttons = [[Button.inline("رجوع", data="SSXJ"),]]
    await event.edit("الامر : `.سليب_ميديا`\n\n الفئة : الأدوات\n\n✘ مقدمة : امر سليب لوضع حسابك اوفلاين\n\n✘ الشرح : بالرد على صورة او متحركه و اي شخص سيرسلك سيقوم بقول له ان مالك الحساب ليس موجود الان مع ارسال له صورة او متحركه  \n\n✘ الاستخدام :\n `.سليب_ميديا`  <بالرد على متحركه او صورة>", buttons=buttons)

@jmthon.tgbot.on(CallbackQuery(data=re.compile(rb"kkui0")))
@check_owner
async def _(event):
    buttons = [[Button.inline("رجوع", data="SSXJ"),]]
    await event.edit("الامر : `.ايدي`\n\n الفئة : الأدوات\n\n✘ مقدمة : لعرض معلومات المستخدم \n\n✘ الشرح : بالرد على المستخدم او وضع معرفه مع الامر لعرض معلوماته من اسم ومعرف والخ..\n\n✘ الاستخدام :\n `.ايدي` <بالرد/ايدي/معرفه>", buttons=buttons)
    

@jmthon.tgbot.on(CallbackQuery(data=re.compile(rb"ttos1")))
@check_owner
async def _(event):
    buttons = [[Button.inline("رجوع", data="TTXOS"),]]
    await event.edit("**الامر :**  `.اسم وقتي` \n**الفئة : الادوات**\n\n**✘ مقدمة :  لتفعيل الاسم الوقتي**\n\n**✘ الشرح : يقوم بوضع وقت مع اسمك اكتب الامر بعدها قم بتعديل اسم العائله بأسمك**\n\n✘ الاستخدام :\n\n `.اسم وقتي`", buttons=buttons)
    
@jmthon.tgbot.on(CallbackQuery(data=re.compile(rb"ttos2")))
@check_owner
async def _(event):
    buttons = [[Button.inline("رجوع", data="TTXOS"),]]
    await event.edit("**الامر :**  `.بايو وقتي` \n**الفئة : الادوات**\n\n**✘ مقدمة :  لتفعيل البايو الوقتي**\n\n**✘ الشرح : يقوم بوضع وقت مع النبذه الخاصه بك شاهد خانه الفارات لمعرفه كيفيه تغيير البايو**\n\n✘ الاستخدام :\n\n `.بايو وقتي`", buttons=buttons)

@jmthon.tgbot.on(CallbackQuery(data=re.compile(rb"ttos3")))
@check_owner
async def _(event):
    buttons = [[Button.inline("رجوع", data="TTXOS"),]]
    await event.edit("**الامر :**  `.الصورة الوقتية` \n**الفئة : الادوات**\n\n**✘ مقدمة :  لوضع وقت على صورة حسابك**\n\n**✘ الشرح : يقوم بوضع وقت على صورة حسابك اكتب الامر فقط، شاهد خانه الفارات لمعرفه كيفيه تغيير الصورة الخاصه بك**\n\n✘ الاستخدام :\n\n `.الصورة الوقتية`", buttons=buttons)

@jmthon.tgbot.on(CallbackQuery(data=re.compile(rb"ttos4")))
@check_owner
async def _(event):
    buttons = [[Button.inline("رجوع", data="TTXOS"),]]
    await event.edit("الامر : .موقع\n\n الفئة : الأدوات\n\n✘ مقدمة : ارسال  الموقع المحدد\n\n✘ الشرح : يقوم بإرسال الموقع اي مدينه اكتب الامر مع اسم المدينه بالانكليزي \n\n✘ الاستخدام :\n .موقع < اسم الموقع كمثال Baghdad>", buttons=buttons)

@jmthon.tgbot.on(CallbackQuery(data=re.compile(rb"ttos5")))
@check_owner
async def _(event):
    buttons = [[Button.inline("رجوع", data="TTXOS"),]]
    await event.edit("الامر : .كورونا\n\n الفئة : الأدوات\n\n✘ مقدمة : لعرض احصائيات كورونا\n\n✘ الشرح : يقوم بإرسال احصائيات يوميه لكورونا اكتب اسم الدوله مع الامر بالانكليزي\n\n✘ الاستخدام :\n `.كورونا` < اسم دولة كمثال Iraq>", buttons=buttons)

@jmthon.tgbot.on(CallbackQuery(data=re.compile(rb"ttos6")))
@check_owner
async def _(event):
    buttons = [[Button.inline("رجوع", data="TTXOS"),]]
    await event.edit("الامر : .سكرين\n\n الفئة : الأدوات\n\n✘ مقدمة : يقوم بعمل سكرينشوت لموقع معين\n\n✘ الشرح : يقوم بعمل سكرينشوت لموقع معين اكتب الامر مع رابط الموقع \n\n✘ الاستخدام :\n .سكرين < رابط >", buttons=buttons)

@jmthon.tgbot.on(CallbackQuery(data=re.compile(rb"ttos7")))
@check_owner
async def _(event):
    buttons = [[Button.inline("رجوع", data="TTXOS"),]]
    await event.edit("الامر : .صور\n\n الفئة : الأدوات\n\n✘ مقدمة : يقوم بتحميل صور\n\n✘ الشرح : تحميل الصور من الكوكل اكتب الامر مع عدد الصور من 1-10 والعنوان \n\n✘ الاستخدام :\n .صور <عدد> <عنوان>", buttons=buttons)

@jmthon.tgbot.on(CallbackQuery(data=re.compile(rb"ttos8")))
@check_owner
async def _(event):
    buttons = [[Button.inline("رجوع", data="TTXOS"),]]
    await event.edit("الامر : .جلب الصورة او  `هممم`\n\n الفئة : الأدوات\n\n✘ مقدمة : يقوم بحفظ الصورة ذاتيه التدمير \n\n✘ الشرح : بالرد على صورة موقوته ذاتيه التدمير بالامر و سيقوم بحفظها وارسالها على الرسائل المحفوظه \n\n✘ الاستخدام :\n .جلب الصورة\n`هممم`   - بدون نقطه او اضافه ", buttons=buttons)

@jmthon.tgbot.on(CallbackQuery(data=re.compile(rb"ttos9")))
@check_owner
async def _(event):
    buttons = [[Button.inline("رجوع", data="TTXOS"),]]
    await event.edit("الامر : .انتحال\n\n الفئة : الأدوات\n\n✘ مقدمة : لنسخ حساب الشخص وانتحاله \n\n✘ الشرح : بالرد على المستخدم او وضع معرفه مع الامر لنسخ حسابه من اسم و صورة والخ...\n\n✘ الاستخدام :\n `.انتحال` < معرف / بالرد >", buttons=buttons)

@jmthon.tgbot.on(CallbackQuery(data=re.compile(rb"ttos0")))
@check_owner
async def _(event):
    buttons = [[Button.inline("رجوع", data="TTXOS"),]]
    await event.edit("الامر : .اعادة\n\n الفئة : الأدوات\n\n✘ مقدمة : لارجاع حسابك الى وضعه السابق \n\n✘ الشرح : اكتب الامر وارسله فقط لارجاع حسابك الى وضعه السابق الطبيعي\n\n✘ الاستخدام :\n `.اعادة`", buttons=buttons)
    
                                ###$$tools
@jmthon.tgbot.on(CallbackQuery(data=re.compile(rb"MEDEA1")))
@check_owner
async def _(event):
    buttons = [
    [
    Button.inline("تحميل صور", data="med1"),
    Button.inline("تحميل بينترست", data="med2"),
    ],
    [
    Button.inline("تحميل صوتي", data="med3"),
    Button.inline("تحميل فيديو", data="med4"),
    ],
    [
    Button.inline("بحث يوتيوب", data="med5"),
    Button.inline("تحميل انستا", data="med6"),
    ],
    [
    Button.inline("اغنية", data="med7"),
    Button.inline("اسم الاغنية", data="med8"),
    ],
    [
    Button.inline("تيكتوك", data="med9"),
    Button.inline("تحويل لدائري", data="med0"),
    ],
    [
    Button.inline("التالي", data="MEDE_2"),
    Button.inline("القائمه الرئيسي", data="ma2in"),
    Button.inline("رجوع", data="MEDE_2"),
    ], 
   ]
    await event.edit("اختر احد الاوامر التاليه", buttons=buttons)
    
@jmthon.tgbot.on(CallbackQuery(data=re.compile(rb"MEDE_2")))
@check_owner
async def _(event):
    buttons = [
    [
    Button.inline("تحويل ملصق", data="meos1"),
    Button.inline("تحويل صورة", data="meos2"),
    ],
    [
    Button.inline("تحويل mp3", data="meos3"),
    Button.inline("تحويل صوتية", data="meos4"),
    ],
    [
    Button.inline("قراءة", data="meos5"),
    Button.inline("كتابة لملف", data="meos6"),
    ],
    [
    Button.inline("كتابة بصوره", data="meos7"),
    Button.inline("تحويل لمتحركه", data="meos8"),
    ],
    [
    Button.inline("التالي", data="MEDEA1"),
    Button.inline("القائمه الرئيسي", data="ma2in"),
    Button.inline("رجوع", data="MEDEA1"),
    ], 
   ]
    await event.edit("اختر احد الاوامر التاليه", buttons=buttons)


@jmthon.tgbot.on(CallbackQuery(data=re.compile(rb"meos1")))
@check_owner
async def _(event):
    buttons = [[Button.inline("رجوع", data="MEDE_2"),]]
    await event.edit("**الامر :**  `.تحويل ملصق` \n**الفئة : ميديا**\n\n**✘ مقدمة :  لتحويل الصورة لملصق**\n\n**✘ الشرح : يقوم بتحويل الصورة الى ملصق بالرد على الصوره بالامر**\n\n✘ الاستخدام :\n\n `.تحويل ملصق` <بالرد على الصور>", buttons=buttons)

@jmthon.tgbot.on(CallbackQuery(data=re.compile(rb"meos2")))
@check_owner
async def _(event):
    buttons = [[Button.inline("رجوع", data="MEDE_2"),]]
    await event.edit("**الامر :**  `.تحويل صورة` \n**الفئة : ميديا**\n\n**✘ مقدمة :  لتحويل الملصق الى صورة**\n\n**✘ الشرح : يقوم بتحويل الملصق الى صورة بالرد على الملصق بالامر**\n\n✘ الاستخدام :\n\n `.تحويل صورة` <بالرد على الملصق>", buttons=buttons)

@jmthon.tgbot.on(CallbackQuery(data=re.compile(rb"meos3")))
@check_owner
async def _(event):
    buttons = [[Button.inline("رجوع", data="MEDE_2"),]]
    await event.edit("**الامر :**  `.تحويل mp3` \n**الفئة : ميديا**\n\n**✘ مقدمة :  لتحويل البصمه الصوتية الى مقطع صوتي**\n\n**✘ الشرح : يقوم بتحويل البصمه الصوتيه الى مقطع صوتي بالرد على البصمه بالامر**\n\n✘ الاستخدام :\n\n `.تحويل mp3` <بالرد على البصمه>", buttons=buttons)
    
@jmthon.tgbot.on(CallbackQuery(data=re.compile(rb"meos4")))
@check_owner
async def _(event):
    buttons = [[Button.inline("رجوع", data="MEDE_2"),]]
    await event.edit("**الامر :**  `.تحويل voice` \n**الفئة : ميديا**\n\n**✘ مقدمة :  لتحويل المقطع صوتي الى بصمه الصوتية**\n\n**✘ الشرح : يقوم بتحويل المقطع الصوتي الى بصمه صوتية بالرد على المقطع الصوتي بالامر**\n\n✘ الاستخدام :\n\n `.تحويل voice` <بالرد على المقطع الصوتي>", buttons=buttons)

@jmthon.tgbot.on(CallbackQuery(data=re.compile(rb"meos5")))
@check_owner
async def _(event):
    buttons = [[Button.inline("رجوع", data="MEDE_2"),]]
    await event.edit("**الامر :**  `.قراءة` \n**الفئة : ميديا**\n\n**✘ مقدمة :  لكتابه ما يوجد بالملف **\n\n**✘ الشرح : يقوم بأستخراج الكتابه الموجودة بالملف وارسالها اليك بالرد على الملف بالامر**\n\n✘ الاستخدام :\n\n `.قراءة` <بالرد على الملف>", buttons=buttons)

@jmthon.tgbot.on(CallbackQuery(data=re.compile(rb"meos6")))
@check_owner
async def _(event):
    buttons = [[Button.inline("رجوع", data="MEDE_2"),]]
    await event.edit("**الامر :**  `.لملف` \n**الفئة : ميديا**\n\n**✘ مقدمة :  تحويل الكتابه الى ملف **\n\n**✘ الشرح : يقوم بتحويل الكتابه الى ملف بالرد على الكتابه مع وضع اسم للملف**\n\n✘ الاستخدام :\n\n `.لملف` <عنوان> <بالرد على نص>", buttons=buttons)

@jmthon.tgbot.on(CallbackQuery(data=re.compile(rb"meos7")))
@check_owner
async def _(event):
    buttons = [[Button.inline("رجوع", data="MEDE_2"),]]
    await event.edit("**الامر :**  `.اكتب` \n**الفئة : ميديا**\n\n**✘ مقدمة :  تحويل الكتابه الى صورة **\n\n**✘ الشرح : يقوم بتحويل الكتابه الى صورة بالرد على الكتابه بالامر**\n\n✘ الاستخدام :\n\n `.اكتب` <بالرد على نص>", buttons=buttons)

@jmthon.tgbot.on(CallbackQuery(data=re.compile(rb"meos8")))
@check_owner
async def _(event):
    buttons = [[Button.inline("رجوع", data="MEDE_2"),]]
    await event.edit("قريبا", buttons=buttons)
                                                      
####-----
@jmthon.tgbot.on(CallbackQuery(data=re.compile(rb"med1")))
@check_owner
async def _(event):
    buttons = [[Button.inline("رجوع", data="MEDEA1"),]]
    await event.edit("**الامر : .صور\nالفئة : الميديا **\n\n**✘ مقدمة : للبحث عن الصورة وتحميلها**\n\n**✘ الشرح : لتحميل صورة من كوكل وارسالها لك اكتب الامر مع عدد الصور و عنوان للبحث**\n\n**✘ الاستخدام :**\n   `.صور` <عنوان> \n    `.صور ` <عدد الصور>  <عنوان>\n\n**✘ أمثلة :**\n   `.صور انمي`\n    `.صور  7 انمي`", buttons=buttons)

@jmthon.tgbot.on(CallbackQuery(data=re.compile(rb"med2")))
@check_owner
async def _(event):
    buttons = [[Button.inline("رجوع", data="MEDEA1"),]]
    await event.edit("**الامر : `.بينت`\nالفئة : الميديا **\n\n**✘ مقدمة : التحميل من بينترست**\n\n**✘ الشرح : لتحميل الصور و الفيديوهات من برنامج بينترست اكتب اسم الامر مع رابط الصورة او الفيديو**\n\n**✘ الاستخدام :**\n   `.بينت` <رابط> ", buttons=buttons)

@jmthon.tgbot.on(CallbackQuery(data=re.compile(rb"med3")))
@check_owner
async def _(event):
    buttons = [[Button.inline("رجوع", data="MEDEA1"),]]
    await event.edit("**الامر :**  `.تحميل ص` \n**الفئة : ميديا**\n\n**✘ مقدمة :  تحميل المقاطع الصوتية عبر اليوتيوب **\n\n**✘ الشرح : يقوم بتحميل مقطع صوتي من اليوتيوب للفيديو بكتابه رابط المقطع مع الامر او بالرد على الرابط **\n\n✘ الاستخدام :\n\n `.تحميل ص` <بالرد على رابط> \n `.تحميل ص` <كتابه الرابط > ", buttons=buttons)
    
@jmthon.tgbot.on(CallbackQuery(data=re.compile(rb"med4")))
@check_owner
async def _(event):
    buttons = [[Button.inline("رجوع", data="MEDEA1"),]]
    await event.edit("**الامر :**  `.تحميل ف` \n**الفئة : ميديا**\n\n**✘ مقدمة :  تحميل الفيديوهات من اليوتيوب **\n\n**✘ الشرح : يقوم بتحميل الفيديو من اليوتيوب بكتابه رابط المقطع مع الامر او بالرد على الرابط **\n\n✘ الاستخدام :\n\n `.تحميل ف` <بالرد على رابط> \n `.تحميل ف` <كتابه الرابط > ", buttons=buttons)

@jmthon.tgbot.on(CallbackQuery(data=re.compile(rb"med5")))
@check_owner
async def _(event):
    buttons = [[Button.inline("رجوع", data="MEDEA1"),]]
    await event.edit("**الامر :**  `.نتائج` \n**الفئة : ميديا**\n\n**✘ مقدمة :  للبحث عن روابط في اليوتيوب **\n\n**✘ الشرح : يقوم بجلب لك روابط ومعلومات من اليوتيوب عن شي معين اكتب الامر والشي التي تريد البحث عنه **\n\n✘ الاستخدام :\n\n `.نتائج` <عنوان للبحث عنه> ", buttons=buttons)
                                                           
@jmthon.tgbot.on(CallbackQuery(data=re.compile(rb"med6")))
@check_owner
async def _(event):
    buttons = [[Button.inline("رجوع", data="MEDEA1"),]]
    await event.edit("**الامر :** `.انستا`   \n**الفئة : الميديا **\n\n**✘ مقدمة : يقوم بتحميل فيديو او صورة من انستكرام**\n\n**✘ الشرح : تحميل صور و الفيديوهات من انستكرام بوضع رابط الفيديو او الصورة مع الامر **\n\n✘ الاستخدام :\n `.انستا` <الرابط> ", buttons=buttons)

@jmthon.tgbot.on(CallbackQuery(data=re.compile(rb"med7")))
@check_owner
async def _(event):
    buttons = [[Button.inline("رجوع", data="MEDEA1"),]]
    await event.edit("**الامر :** `.اغنية`   \n**الفئة : الميديا **\n\n**✘ مقدمة : يقوم بتحميل الاغنيه مباشرة عبر اسمها**\n\n**✘ الشرح : تحميل مقطع صوتي للاغنيه مباشرة فقط اكتب الامر مع اسم المقطع الصوتي**\n\n✘ الاستخدام :\n `.اغنية` <عنوان> ", buttons=buttons)

@jmthon.tgbot.on(CallbackQuery(data=re.compile(rb"med8")))
@check_owner
async def _(event):
    buttons = [[Button.inline("رجوع", data="MEDEA1"),]]
    await event.edit("**الامر :** `.اسم الاغنيه`   \n**الفئة : الميديا **\n\n**✘ مقدمة : يقوم بالتعرف على اسم المقطع الصوتي**\n\n**✘ الشرح : بالرد على اي مقطع صوتي بالامر لجلب اسم المقطع الصوتي و عنوانه و صوره له**\n\n✘ الاستخدام :\n `.اسم الاغنيه` <بالرد على الاغنيه> ", buttons=buttons)

@jmthon.tgbot.on(CallbackQuery(data=re.compile(rb"med9")))
@check_owner
async def _(event):
    buttons = [[Button.inline("رجوع", data="MEDEA1"),]]
    await event.edit("**الامر :**  `.تيكتوك` \n**الفئة : ميديا**\n\n**✘ مقدمة :  تحميل الفيديوهات من التيكتوك **\n\n**✘ الشرح : يقوم بتحميل الفيديوهات من التيكتوك بالرد على رابط الفيديو فقط**\n\n✘ الاستخدام :\n\n `.تيكتوك` <بالرد على رابط>", buttons=buttons)

      
@jmthon.tgbot.on(CallbackQuery(data=re.compile(rb"med0")))
@check_owner
async def _(event):
    buttons = [[Button.inline("رجوع", data="MEDEA1"),]]
    await event.edit("**الامر :**  `.تحويل لدائري` \n**الفئة : ميديا**\n\n**✘ مقدمة :  لتحويل الفيديو او الصورة او اي ميديا لفيديو دائري **\n\n**✘ الشرح : يقوم بتحويل الفيديو و الصورة و الاغنيه لفيديو ظائري بالرد عليه بالأمر**\n\n✘ الاستخدام :\n\n `.تحويل لدائري` <بالرد على ميديا>", buttons=buttons)
             
@jmthon.tgbot.on(CallbackQuery(data=re.compile(rb"FUNCMD_1")))
@check_owner
async def _(event):
    buttons = [
    [
    Button.inline("غبي", data="fun1"),
    Button.inline("القنابل", data="fun2"),
    ],
    [
    Button.inline("متت", data="fun3"),
    Button.inline("قتل", data="fun4"),
    ],
    [
    Button.inline("اتصل", data="fun5"),
    Button.inline("شنو", data="fun6"),
    ],
    [
    Button.inline("طوبة", data="fun7"),
    Button.inline("مربعات", data="fun8"),
    ],
    [
    Button.inline("حلويات", data="fun9"),
    Button.inline("افكر", data="fun0"),
    ],
    [
    Button.inline("التالي", data="FUNCM2D"),
    Button.inline("القائمه الرئيسي", data="ma2in"),
    Button.inline("رجوع", data="FU5GMSCM"),
    ], 
   ]
    await event.edit("اختر احد الاوامر التاليه", buttons=buttons)

@jmthon.tgbot.on(CallbackQuery(data=re.compile(rb"FUNCM2D")))
@check_owner
async def _(event):
    buttons = [
    [
    Button.inline("ضايج", data="fbs1"),
    Button.inline("ساعه", data="fbs2"),
    ],
    [
    Button.inline("مح", data="fbs3"),
    Button.inline("قلب", data="fbs4"),
    ],
    [
    Button.inline("جيم", data="fbs5"),
    Button.inline("الارض", data="fbs6"),
    ],
    [
    Button.inline("قمر", data="fbs7"),
    Button.inline("اقمار", data="fbs8"),
    ],
    [
    Button.inline("قمور", data="fbs9"),
    Button.inline("نجمه", data="fbs0"),
    ],
    [
    Button.inline("التالي", data="FUNC3CM"),
    Button.inline("القائمه الرئيسي", data="ma2in"),
    Button.inline("رجوع", data="FUNCMD_1"),
    ], 
   ]
    await event.edit("اختر احد الاوامر التاليه", buttons=buttons)

    
            
@jmthon.tgbot.on(CallbackQuery(data=re.compile(rb"FUNC3CM")))
@check_owner
async def _(event):
    buttons = [
    [
    Button.inline("مكعبات", data="frz1"),
    Button.inline("مطر", data="frz2"),
    ],
    [
    Button.inline("تفريع", data="frz3"),
    Button.inline("فليم", data="frz4"),
    ],
    [
    Button.inline("طائره", data="frz5"),
    Button.inline("شرطه", data="frz6"),
    ],
    [
    Button.inline("النضام الشمسي", data="frz7"),
    Button.inline("عين", data="frz8"),
    ],
    [
    Button.inline("افكر", data="frz9"),
    Button.inline("افعى", data="frz0"),
    ],
    [
    Button.inline("التالي", data="FUN4MSCM"),
    Button.inline("القائمه الرئيسي", data="ma2in"),
    Button.inline("رجوع", data="FUNCM2D"),
    ], 
   ]
    await event.edit("اختر احد الاوامر التاليه", buttons=buttons)
    

@jmthon.tgbot.on(CallbackQuery(data=re.compile(rb"FUN4MSCM")))
@check_owner
async def _(event):
    buttons = [
    [
    Button.inline("مايكرو", data="fky1"),
    Button.inline("فايروس", data="fky2"),
    ],
    [
    Button.inline("قطار", data="fky3"),
    Button.inline("نيكول", data="fky4"),
    ],
    [
    Button.inline("موسيقى", data="fky5"),
    Button.inline("رسم", data="fky6"),
    ],
    [
    Button.inline("قمر", data="fky7"),
    Button.inline("اقمار", data="fky8"),
    ],
    [
    Button.inline("قمور", data="fky9"),
    Button.inline("رجل", data="fky0"),
    ],
    [
    Button.inline("التالي", data="FU5GMSCM"),
    Button.inline("القائمه الرئيسي", data="ma2in"),
    Button.inline("رجوع", data="FUNC3CM"),
    ], 
   ]
    await event.edit("اختر احد الاوامر التاليه", buttons=buttons)
    
    
@jmthon.tgbot.on(CallbackQuery(data=re.compile(rb"FU5GMSCM")))
@check_owner
async def _(event):
    buttons = [
    [
    Button.inline("الرفع", data="Rto1"),
    Button.inline("النسب", data="Rto2"),
    ],
    [
    Button.inline("التالي", data="FUNCMD_1"),
    Button.inline("القائمه الرئيسي", data="ma2in"),
    Button.inline("رجوع", data="FUN4MSCM"),
    ], 
   ]
    await event.edit("اختر احد الاوامر التاليه", buttons=buttons)
    
@jmthon.tgbot.on(CallbackQuery(data=re.compile(rb"Rto1")))
@check_owner
async def _(event):
    buttons = [[Button.inline("رجوع", data="FU5GMSCM"),]]
    await event.edit("**الامر : اوامر الرفع\nالفئة : الترفيه **\n\n**✘ مقدمة : اوامر ترفيه قم بتجربته بنفسك**\n\n**✘ الشرح : اوامر الرفع تستخدم بالرد على الشخص **\n\n✘ الاستخدام :\n `.رفع بكلبي`\n`.رفع مطي`\n`.رفع زوجي`\n`.رفع مرتي`\n`.رفع جلب`\n`.رفع تاج`\n`.رفع قرد`\n`.رفع حيوان`\n`.رفع بزون`\n`.رفع زاحف`", buttons=buttons)

@jmthon.tgbot.on(CallbackQuery(data=re.compile(rb"Rto2")))
@check_owner
async def _(event):
    buttons = [[Button.inline("رجوع", data="FU5GMSCM"),]]
    await event.edit("**الامر : اوامر النسب\nالفئة : الترفيه **\n\n**✘ مقدمة : اوامر ترفيه قم بتجربته بنفسك**\n\n**✘ الشرح : اوامر النسب والراندوم تستخدم بالرد على الشخص **\n\n✘ الاستخدام :\n `.هينه`\n`.اوصف`\n`.كت`\n`.شغله`\n`.نسبة الرجولة`\n`.نسبة الانوثة`\n`.نسبة الحب`\n`.نسبة الغباء`", buttons=buttons)


@jmthon.tgbot.on(CallbackQuery(data=re.compile(rb"fky0")))
@check_owner
async def _(event):
    buttons = [[Button.inline("رجوع", data="FUN4MSCM"),]]
    await event.edit("**الامر :** `.رجل`\n**الفئة : الترفيه** \n\n**✘ مقدمة : امر ترفيه قم بتجربته بنفسك**\n\n**✘ الشرح : فقط انسخ الامر وارسله في اي دردشه** \n\n**✘ الاستخدام **:\n   `.رجل`", buttons=buttons)
    
@jmthon.tgbot.on(CallbackQuery(data=re.compile(rb"fky1")))
@check_owner
async def _(event):
    buttons = [[Button.inline("رجوع", data="FUN4MSCM"),]]
    await event.edit("**الامر :** `.مايكرو`\n**الفئة : الترفيه** \n\n**✘ مقدمة : امر ترفيه قم بتجربته بنفسك**\n\n**✘ الشرح : فقط انسخ الامر وارسله في اي دردشه** \n\n**✘ الاستخدام **:\n   `.مايكرو`", buttons=buttons)

@jmthon.tgbot.on(CallbackQuery(data=re.compile(rb"fky2")))
@check_owner
async def _(event):
    buttons = [[Button.inline("رجوع", data="FUN4MSCM"),]]
    await event.edit("**الامر :** `.فايروس`\n**الفئة : الترفيه** \n\n**✘ مقدمة : امر ترفيه قم بتجربته بنفسك**\n\n**✘ الشرح : فقط انسخ الامر وارسله في اي دردشه** \n\n**✘ الاستخدام **:\n   `.فايروس`", buttons=buttons)

@jmthon.tgbot.on(CallbackQuery(data=re.compile(rb"fky3")))
@check_owner
async def _(event):
    buttons = [[Button.inline("رجوع", data="FUN4MSCM"),]]
    await event.edit("**الامر :** `.قطار`\n**الفئة : الترفيه** \n\n**✘ مقدمة : امر ترفيه قم بتجربته بنفسك**\n\n**✘ الشرح : فقط انسخ الامر وارسله في اي دردشه** \n\n**✘ الاستخدام **:\n   `.قطار`", buttons=buttons)

@jmthon.tgbot.on(CallbackQuery(data=re.compile(rb"fky4")))
@check_owner
async def _(event):
    buttons = [[Button.inline("رجوع", data="FUN4MSCM"),]]
    await event.edit("**الامر :** `.نيكول`\n**الفئة : الترفيه** \n\n**✘ مقدمة : امر ترفيه قم بتجربته بنفسك**\n\n**✘ الشرح : فقط انسخ الامر وارسله في اي دردشه** \n\n**✘ الاستخدام **:\n   `.نيكول`", buttons=buttons)

@jmthon.tgbot.on(CallbackQuery(data=re.compile(rb"fky5")))
@check_owner
async def _(event):
    buttons = [[Button.inline("رجوع", data="FUN4MSCM"),]]
    await event.edit("**الامر :** `.موسيقى`\n**الفئة : الترفيه** \n\n**✘ مقدمة : امر ترفيه قم بتجربته بنفسك**\n\n**✘ الشرح : فقط انسخ الامر وارسله في اي دردشه** \n\n**✘ الاستخدام **:\n   `.موسيقى`", buttons=buttons)

@jmthon.tgbot.on(CallbackQuery(data=re.compile(rb"fky6")))
@check_owner
async def _(event):
    buttons = [[Button.inline("رجوع", data="FUN4MSCM"),]]
    await event.edit("**الامر :** `.رسم`\n**الفئة : الترفيه** \n\n**✘ مقدمة : امر ترفيه قم بتجربته بنفسك**\n\n**✘ الشرح : فقط انسخ الامر وارسله في اي دردشه** \n\n**✘ الاستخدام **:\n   `.رسم`", buttons=buttons)

@jmthon.tgbot.on(CallbackQuery(data=re.compile(rb"fky7")))
@check_owner
async def _(event):
    buttons = [[Button.inline("رجوع", data="FUN4MSCM"),]]
    await event.edit("**الامر :** `.مكعبات`\n**الفئة : الترفيه** \n\n**✘ مقدمة : امر ترفيه قم بتجربته بنفسك**\n\n**✘ الشرح : فقط انسخ الامر وارسله في اي دردشه** \n\n**✘ الاستخدام **:\n   `.مكعبات`", buttons=buttons)

@jmthon.tgbot.on(CallbackQuery(data=re.compile(rb"fky8")))
@check_owner
async def _(event):
    buttons = [[Button.inline("رجوع", data="FUN4MSCM"),]]
    await event.edit("**الامر :** `.مكعبات`\n**الفئة : الترفيه** \n\n**✘ مقدمة : امر ترفيه قم بتجربته بنفسك**\n\n**✘ الشرح : فقط انسخ الامر وارسله في اي دردشه** \n\n**✘ الاستخدام **:\n   `.مكعبات`", buttons=buttons)

@jmthon.tgbot.on(CallbackQuery(data=re.compile(rb"fky9")))
@check_owner
async def _(event):
    buttons = [[Button.inline("رجوع", data="FUN4MSCM"),]]
    await event.edit("**الامر :** `.مكعبات`\n**الفئة : الترفيه** \n\n**✘ مقدمة : امر ترفيه قم بتجربته بنفسك**\n\n**✘ الشرح : فقط انسخ الامر وارسله في اي دردشه** \n\n**✘ الاستخدام **:\n   `.مكعبات`", buttons=buttons)


@jmthon.tgbot.on(CallbackQuery(data=re.compile(rb"frz1")))
@check_owner
async def _(event):
    buttons = [[Button.inline("رجوع", data="FUNC3CM"),]]
    await event.edit("**الامر :** `.مكعبات`\n**الفئة : الترفيه** \n\n**✘ مقدمة : امر ترفيه قم بتجربته بنفسك**\n\n**✘ الشرح : فقط انسخ الامر وارسله في اي دردشه** \n\n**✘ الاستخدام **:\n   `.مكعبات`", buttons=buttons)

@jmthon.tgbot.on(CallbackQuery(data=re.compile(rb"frz2")))
@check_owner
async def _(event):
    buttons = [[Button.inline("رجوع", data="FUNC3CM"),]]
    await event.edit("**الامر :** `.مطر`\n**الفئة : الترفيه** \n\n**✘ مقدمة : امر ترفيه قم بتجربته بنفسك**\n\n**✘ الشرح : فقط انسخ الامر وارسله في اي دردشه** \n\n**✘ الاستخدام **:\n   `.مطر`", buttons=buttons)

@jmthon.tgbot.on(CallbackQuery(data=re.compile(rb"frz3")))
@check_owner
async def _(event):
    buttons = [[Button.inline("رجوع", data="FUNC3CM"),]]
    await event.edit("**الامر :** `.تفريغ`\n**الفئة : الترفيه** \n\n**✘ مقدمة : امر ترفيه قم بتجربته بنفسك**\n\n**✘ الشرح : اكتب الامر مع سمايلات قليله** \n\n**✘ الاستخدام **:\n   `.تفريغ <سمايل>`", buttons=buttons)

@jmthon.tgbot.on(CallbackQuery(data=re.compile(rb"frz4")))
@check_owner
async def _(event):
    buttons = [[Button.inline("رجوع", data="FUNC3CM"),]]
    await event.edit("**الامر :** `.فليم`\n**الفئة : الترفيه** \n\n**✘ مقدمة : امر ترفيه قم بتجربته بنفسك**\n\n**✘ الشرح : فقط انسخ الامر وارسله في اي دردشه** \n\n**✘ الاستخدام **:\n   `.فليم`", buttons=buttons)

@jmthon.tgbot.on(CallbackQuery(data=re.compile(rb"frz5")))
@check_owner
async def _(event):
    buttons = [[Button.inline("رجوع", data="FUNC3CM"),]]
    await event.edit("**الامر :** `.طائره`\n**الفئة : الترفيه** \n\n**✘ مقدمة : امر ترفيه قم بتجربته بنفسك**\n\n**✘ الشرح : فقط انسخ الامر وارسله في اي دردشه** \n\n**✘ الاستخدام **:\n   `.طائره`", buttons=buttons)

@jmthon.tgbot.on(CallbackQuery(data=re.compile(rb"frz6")))
@check_owner
async def _(event):
    buttons = [[Button.inline("رجوع", data="FUNC3CM"),]]
    await event.edit("**الامر :** `.شرطه`\n**الفئة : الترفيه** \n\n**✘ مقدمة : امر ترفيه قم بتجربته بنفسك**\n\n**✘ الشرح : فقط انسخ الامر وارسله في اي دردشه** \n\n**✘ الاستخدام **:\n   `.شرطه`", buttons=buttons)

@jmthon.tgbot.on(CallbackQuery(data=re.compile(rb"frz7")))
@check_owner
async def _(event):
    buttons = [[Button.inline("رجوع", data="FUNC3CM"),]]
    await event.edit("**الامر :** `.النضام الشمسي`\n**الفئة : الترفيه** \n\n**✘ مقدمة : امر ترفيه قم بتجربته بنفسك**\n\n**✘ الشرح : فقط انسخ الامر وارسله في اي دردشه** \n\n**✘ الاستخدام **:\n   `.النضام الشمسي`", buttons=buttons)

@jmthon.tgbot.on(CallbackQuery(data=re.compile(rb"frz8")))
@check_owner
async def _(event):
    buttons = [[Button.inline("رجوع", data="FUNC3CM"),]]
    await event.edit("**الامر :** `.عين`\n**الفئة : الترفيه** \n\n**✘ مقدمة : امر ترفيه قم بتجربته بنفسك**\n\n**✘ الشرح : فقط انسخ الامر وارسله في اي دردشه** \n\n**✘ الاستخدام **:\n   `.عين`", buttons=buttons)

@jmthon.tgbot.on(CallbackQuery(data=re.compile(rb"frz9")))
@check_owner
async def _(event):
    buttons = [[Button.inline("رجوع", data="FUNC3CM"),]]
    await event.edit("**الامر :** `.افكر`\n**الفئة : الترفيه** \n\n**✘ مقدمة : امر ترفيه قم بتجربته بنفسك**\n\n**✘ الشرح : فقط انسخ الامر وارسله في اي دردشه** \n\n**✘ الاستخدام **:\n   `.افكر`", buttons=buttons)

@jmthon.tgbot.on(CallbackQuery(data=re.compile(rb"frz0")))
@check_owner
async def _(event):
    buttons = [[Button.inline("رجوع", data="FUNC3CM"),]]
    await event.edit("**الامر :** `.افعى`\n**الفئة : الترفيه** \n\n**✘ مقدمة : امر ترفيه قم بتجربته بنفسك**\n\n**✘ الشرح : فقط انسخ الامر وارسله في اي دردشه** \n\n**✘ الاستخدام **:\n   `.افعى`", buttons=buttons)


@jmthon.tgbot.on(CallbackQuery(data=re.compile(rb"fbs1")))
@check_owner
async def _(event):
    buttons = [[Button.inline("رجوع", data="FUNCM2D"),]]
    await event.edit("**الامر :** `.ضايج`\n**الفئة : الترفيه** \n\n**✘ مقدمة : امر ترفيه قم بتجربته بنفسك**\n\n**✘ الشرح : فقط انسخ الامر وارسله في اي دردشه** \n\n**✘ الاستخدام **:\n   `.ضايج`", buttons=buttons)

@jmthon.tgbot.on(CallbackQuery(data=re.compile(rb"fbs2")))
@check_owner
async def _(event):
    buttons = [[Button.inline("رجوع", data="FUNCM2D"),]]
    await event.edit("**الامر :** `.ساعه`\n**الفئة : الترفيه** \n\n**✘ مقدمة : امر ترفيه قم بتجربته بنفسك**\n\n**✘ الشرح : فقط انسخ الامر وارسله في اي دردشه** \n\n**✘ الاستخدام **:\n   `.ساعه`", buttons=buttons)


@jmthon.tgbot.on(CallbackQuery(data=re.compile(rb"fbs3")))
@check_owner
async def _(event):
    buttons = [[Button.inline("رجوع", data="FUNCM2D"),]]
    await event.edit("**الامر :** `.مح`\n**الفئة : الترفيه** \n\n**✘ مقدمة : امر ترفيه قم بتجربته بنفسك**\n\n**✘ الشرح : فقط انسخ الامر وارسله في اي دردشه** \n\n**✘ الاستخدام **:\n   `.مح`", buttons=buttons)

@jmthon.tgbot.on(CallbackQuery(data=re.compile(rb"fbs4")))
@check_owner
async def _(event):
    buttons = [[Button.inline("رجوع", data="FUNCM2D"),]]
    await event.edit("**الامر :** `.قلب`\n**الفئة : الترفيه** \n\n**✘ مقدمة : امر ترفيه قم بتجربته بنفسك**\n\n**✘ الشرح : فقط انسخ الامر وارسله في اي دردشه** \n\n**✘ الاستخدام **:\n   `.قلب`", buttons=buttons)

@jmthon.tgbot.on(CallbackQuery(data=re.compile(rb"fbs5")))
@check_owner
async def _(event):
    buttons = [[Button.inline("رجوع", data="FUNCM2D"),]]
    await event.edit("**الامر :** `.جيم`\n**الفئة : الترفيه** \n\n**✘ مقدمة : امر ترفيه قم بتجربته بنفسك**\n\n**✘ الشرح : فقط انسخ الامر وارسله في اي دردشه** \n\n**✘ الاستخدام **:\n   `.جيم`", buttons=buttons)

@jmthon.tgbot.on(CallbackQuery(data=re.compile(rb"fbs6")))
@check_owner
async def _(event):
    buttons = [[Button.inline("رجوع", data="FUNCM2D"),]]
    await event.edit("**الامر :** `.الارض`\n**الفئة : الترفيه** \n\n**✘ مقدمة : امر ترفيه قم بتجربته بنفسك**\n\n**✘ الشرح : فقط انسخ الامر وارسله في اي دردشه** \n\n**✘ الاستخدام **:\n   `.الارض`", buttons=buttons)

@jmthon.tgbot.on(CallbackQuery(data=re.compile(rb"fbs7")))
@check_owner
async def _(event):
    buttons = [[Button.inline("رجوع", data="FUNCM2D"),]]
    await event.edit("**الامر :** `.قمر`\n**الفئة : الترفيه** \n\n**✘ مقدمة : امر ترفيه قم بتجربته بنفسك**\n\n**✘ الشرح : فقط انسخ الامر وارسله في اي دردشه** \n\n**✘ الاستخدام **:\n   `.قمر`", buttons=buttons)

@jmthon.tgbot.on(CallbackQuery(data=re.compile(rb"fbs8")))
@check_owner
async def _(event):
    buttons = [[Button.inline("رجوع", data="FUNCM2D"),]]
    await event.edit("**الامر :** `.اقمار`\n**الفئة : الترفيه** \n\n**✘ مقدمة : امر ترفيه قم بتجربته بنفسك**\n\n**✘ الشرح : فقط انسخ الامر وارسله في اي دردشه** \n\n**✘ الاستخدام **:\n   `.اقمار`", buttons=buttons)


@jmthon.tgbot.on(CallbackQuery(data=re.compile(rb"fbs9")))
@check_owner
async def _(event):
    buttons = [[Button.inline("رجوع", data="FUNCM2D"),]]
    await event.edit("**الامر :** `.قمور`\n**الفئة : الترفيه** \n\n**✘ مقدمة : امر ترفيه قم بتجربته بنفسك**\n\n**✘ الشرح : فقط انسخ الامر وارسله في اي دردشه** \n\n**✘ الاستخدام **:\n   `.قمور`", buttons=buttons)

@jmthon.tgbot.on(CallbackQuery(data=re.compile(rb"fbs0")))
@check_owner
async def _(event):
    buttons = [[Button.inline("رجوع", data="FUNCM2D"),]]
    await event.edit("**الامر :** `.نجمه`\n**الفئة : الترفيه** \n\n**✘ مقدمة : امر ترفيه قم بتجربته بنفسك**\n\n**✘ الشرح : فقط انسخ الامر وارسله في اي دردشه** \n\n**✘ الاستخدام **:\n   `.نجمه`", buttons=buttons)


@jmthon.tgbot.on(CallbackQuery(data=re.compile(rb"fun1")))
@check_owner
async def _(event):
    buttons = [[Button.inline("رجوع", data="FUNCMD_1"),]]
    await event.edit("**الامر :** `.غبي`\n**الفئة : الترفيه** \n\n**✘ مقدمة : امر ترفيه قم بتجربته بنفسك**\n\n**✘ الشرح : فقط انسخ الامر وارسله في اي دردشه** \n\n**✘ الاستخدام **:\n   `.غبي`", buttons=buttons)

@jmthon.tgbot.on(CallbackQuery(data=re.compile(rb"fun2")))
@check_owner
async def _(event):
    buttons = [[Button.inline("رجوع", data="FUNCMD_1"),]]
    await event.edit("**الامر :** `.القنابل`\n**الفئة : الترفيه** \n\n**✘ مقدمة : امر ترفيه قم بتجربته بنفسك**\n\n**✘ الشرح : فقط انسخ الامر وارسله في اي دردشه** \n\n**✘ الاستخدام **:\n   `.القنابل`", buttons=buttons)

@jmthon.tgbot.on(CallbackQuery(data=re.compile(rb"fun3")))
@check_owner
async def _(event):
    buttons = [[Button.inline("رجوع", data="FUNCMD_1"),]]
    await event.edit("**الامر :** `.متت`\n**الفئة : الترفيه** \n\n**✘ مقدمة : امر ترفيه قم بتجربته بنفسك**\n\n**✘ الشرح : فقط انسخ الامر وارسله في اي دردشه** \n\n**✘ الاستخدام **:\n   `.متت`", buttons=buttons)

@jmthon.tgbot.on(CallbackQuery(data=re.compile(rb"fun4")))
@check_owner
async def _(event):
    buttons = [[Button.inline("رجوع", data="FUNCMD_1"),]]
    await event.edit("**الامر :** `.قتل`\n**الفئة : الترفيه** \n\n**✘ مقدمة : امر ترفيه قم بتجربته بنفسك**\n\n**✘ الشرح : فقط انسخ الامر وارسله في اي دردشه** \n\n**✘ الاستخدام **:\n   `.قتل`", buttons=buttons)

@jmthon.tgbot.on(CallbackQuery(data=re.compile(rb"fun5")))
@check_owner
async def _(event):
    buttons = [[Button.inline("رجوع", data="FUNCMD_1"),]]
    await event.edit("**الامر :** `.اتصل`\n**الفئة : الترفيه** \n\n**✘ مقدمة : امر ترفيه قم بتجربته بنفسك**\n\n**✘ الشرح : فقط انسخ الامر وارسله في اي دردشه** \n\n**✘ الاستخدام **:\n   `.اتصل`", buttons=buttons)

@jmthon.tgbot.on(CallbackQuery(data=re.compile(rb"fun6")))
@check_owner
async def _(event):
    buttons = [[Button.inline("رجوع", data="FUNCMD_1"),]]
    await event.edit("**الامر :** `.شنو`\n**الفئة : الترفيه** \n\n**✘ مقدمة : امر ترفيه قم بتجربته بنفسك**\n\n**✘ الشرح : فقط انسخ الامر وارسله في اي دردشه** \n\n**✘ الاستخدام **:\n   `.شنو`", buttons=buttons)

@jmthon.tgbot.on(CallbackQuery(data=re.compile(rb"fun7")))
@check_owner
async def _(event):
    buttons = [[Button.inline("رجوع", data="FUNCMD_1"),]]
    await event.edit("**الامر :** `.طوبة`\n**الفئة : الترفيه** \n\n**✘ مقدمة : امر ترفيه قم بتجربته بنفسك**\n\n**✘ الشرح : فقط انسخ الامر وارسله في اي دردشه** \n\n**✘ الاستخدام **:\n   `.طوبة`", buttons=buttons)

@jmthon.tgbot.on(CallbackQuery(data=re.compile(rb"fun8")))
@check_owner
async def _(event):
    buttons = [[Button.inline("رجوع", data="FUNCMD_1"),]]
    await event.edit("**الامر :** `.مربعات`\n**الفئة : الترفيه** \n\n**✘ مقدمة : امر ترفيه قم بتجربته بنفسك**\n\n**✘ الشرح : فقط انسخ الامر وارسله في اي دردشه** \n\n**✘ الاستخدام **:\n   `.مربعات`", buttons=buttons)

@jmthon.tgbot.on(CallbackQuery(data=re.compile(rb"fun9")))
@check_owner
async def _(event):
    buttons = [[Button.inline("رجوع", data="FUNCMD_1"),]]
    await event.edit("**الامر :** `.حلويات`\n**الفئة : الترفيه** \n\n**✘ مقدمة : امر ترفيه قم بتجربته بنفسك**\n\n**✘ الشرح : فقط انسخ الامر وارسله في اي دردشه** \n\n**✘ الاستخدام **:\n   `.حلويات`", buttons=buttons)

                                                                                                                               
@jmthon.tgbot.on(CallbackQuery(data=re.compile(rb"fun0")))
@check_owner
async def _(event):
    buttons = [[Button.inline("رجوع", data="FUNCMD_1"),]]
    await event.edit("**الامر :** `.افكر`\n**الفئة : الترفيه** \n\n**✘ مقدمة : امر ترفيه قم بتجربته بنفسك**\n\n**✘ الشرح : فقط انسخ الامر وارسله في اي دردشه** \n\n**✘ الاستخدام **:\n   `.افكر`", buttons=buttons)

@jmthon.tgbot.on(CallbackQuery(data=re.compile(rb"jmthon0")))
@check_owner
async def _(event):
    buttons = [
    [
    Button.inline("رفع العام", data="r33a"),
    Button.inline("تنزيل العام", data="tn3a"),
    ],
    [
    Button.inline("الاحداث", data="ahd6"),
    Button.inline("التثبيت", data="thpet"),
    ],
    [
    Button.inline("رفع مشرف", data="rfmsh"),
    Button.inline("تنزيل مشرف", data="zjmsh"),
    ],
    [
    Button.inline("صورة المجموعه", data="srzo"),
    Button.inline("طرد", data="rdmua"),
    ],
    [
    Button.inline("الغاء كتم", data="rimrz"),
    Button.inline("الكتم", data="ktmrz"),
    ],
    [
    Button.inline("التالي", data="jmthon1"),
    Button.inline("القائمه الرئيسي", data="ma2in"),
    Button.inline("رجوع", data="jmthon2"),
    ], 
   ]
    await event.edit("اختر احد الاوامر التاليه", buttons=buttons)
    
@jmthon.tgbot.on(CallbackQuery(data=re.compile(rb"jmthon1")))
@check_owner
async def _(event):
    buttons = [
    [
    Button.inline("حظر", data="bancmd"),
    Button.inline("الغاء حظر", data="unbancmd"),
    ],
    [
    Button.inline("تحذير", data="warncmd"),
    Button.inline("حذف التحذير", data="delwarncmd"),
    ],
    [
    Button.inline("التحذيرات", data="warningcmd"),
    Button.inline("منع", data="blacklistw"),
    ],
    [
    Button.inline("الغاء منع", data="dblacklistw"),
    Button.inline("قائمه المنع", data="blacklidj"),
    ],
    [
    Button.inline("الصلاحيات", data="ssroz"),
    Button.inline("منع التكرار", data="mtlraj"),
    ],
    [
    Button.inline("التالي", data="jmthon2"),
    Button.inline("القائمه الرئيسي", data="ma2in"),
    Button.inline("رجوع", data="jmthon0"),
    ], 
   ]
    await event.edit("اختر احد الاوامر التاليه", buttons=buttons)
    
    
@jmthon.tgbot.on(CallbackQuery(data=re.compile(rb"jmthon2")))
@check_owner
async def _(event):
    buttons = [
    [
    Button.inline("حظر مؤقت", data="antez"),
    Button.inline("تقييد مؤقت", data="tmutez"),
    ],
    [
    Button.inline("التالي", data="jmthon0"),
    Button.inline("القائمه الرئيسي", data="ma2in"),
    Button.inline("رجوع", data="jmthon1"),
    ], 
   ]
    await event.edit("اختر احد الاوامر التاليه", buttons=buttons)
    
@jmthon.tgbot.on(CallbackQuery(data=re.compile(rb"antez")))
@check_owner
async def _(event):
    buttons = [[Button.inline("رجوع", data="jmthon1"),]]
    await event.edit("**الامر : .حظر_مؤقت**\n**الفئة : الادمن **\n\n**✘ مقدمة : لحظر المستخدم في المجموعة مؤقت**\n\n**✘ الشرح : لحظر المستخدم مؤقتا بكتابة الامر مع الوقت والاضافه والرد على المستخدم**\n\n**✘ الاستخدام** :\n   `.حظر_مؤقت `<وقت> <الاضافة> <بالرد/ايدي/معرف> \n\n**✘ مثال :**\n`.حظر_مؤقت 30m @RR9R7`.\n\n**✘الاضافات \n\ns ثواني\nm الدقائق\nh ساعات\nd أيام\nw أسابيع**", buttons=buttons)


@jmthon.tgbot.on(CallbackQuery(data=re.compile(rb"tmutez")))
@check_owner
async def _(event):
    buttons = [[Button.inline("رجوع", data="jmthon1"),]]
    await event.edit("**الامر : .كتم_مؤقت**\n**الفئة : الادمن **\n\n**✘ مقدمة : لكتم المستخدم في المجموعة مؤقت**\n\n**✘ الشرح : لتقييد المستخدم مؤقتا بكتابة الامر مع الوقت والاضافه والرد على المستخدم**\n\n**✘ الاستخدام** :\n   `.كتم_مؤقت `<وقت> <الاضافة> <بالرد/ايدي/معرف> \n\n**✘ مثال :**\n`.كتم_مؤقت 30 @RR9R7`.\n\n**✘✘الاضافات \n\ns ثواني\nm الدقائق\nh ساعات\nd أيام\nw أسابيع**", buttons=buttons)

@jmthon.tgbot.on(CallbackQuery(data=re.compile(rb"mtlraj")))
@check_owner
async def _(event):
    buttons = [[Button.inline("رجوع", data="jmthon1"),]]
    await event.edit("**الامر :**   `.ضع تكرار`\n**الفئة : الادمن**\n\n**✘ مقدمة : لمنع التكرار في المجموعه .**\n\n**✘ الشرح : بكتابه الامر مع لعدد لمنع التكرار في مجموعتك يمكنك الغاء هذه الميزه بوضعه عدد تكرار كبير**\n\n**✘ الاستخدام :**      \n\n`.وضع تكرار` <عدد>\n`وضع تكرار 999999`", buttons=buttons)
    
@jmthon.tgbot.on(CallbackQuery(data=re.compile(rb"bancmd")))
@check_owner
async def _(event):
    buttons = [[Button.inline("رجوع", data="jmthon1"),]]
    await event.edit("**الامر :**   `.حظر`\n**الفئة : الادمن**\n\n**✘ مقدمة : لحظر المستخدم من الدردشه**\n\n**✘ الشرح : بالرد على المستخدم او وضع معرفه مع الامر لحظره من المجموعه ومنعه من الدخول مره ثانيه تحتاج صلاحيات الحظر**\n\n**✘ الاستخدام :**      \n\n`.حظر` <بالرد/معرف/ايدي>", buttons=buttons)
#
@jmthon.tgbot.on(CallbackQuery(data=re.compile(rb"warncmd")))
@check_owner
async def _(event):
    buttons = [[Button.inline("رجوع", data="jmthon1"),]]
    await event.edit("**الامر :**   `.تحذير`\n**الفئة : الادمن**\n\n**✘ مقدمة : لتحذير المستخدم في المجموعه.**\n\n**✘ الشرح : بالرد على المستخدم مع الامر ويمكنك ذكر سبب التحذير**\n\n**✘ الاستخدام :**      \n\n`.تحذير` <بالرد>\n      `.تحذير` <بالرد> <السبب> ", buttons=buttons)


@jmthon.tgbot.on(CallbackQuery(data=re.compile(rb"delwarncmd")))
@check_owner
async def _(event):
    buttons = [[Button.inline("رجوع", data="jmthon1"),]]
    await event.edit("**الامر :**   `.حذف التحذير`\n**الفئة : الادمن**\n\n**✘ مقدمة : لحذف تحذيرات المستخدم من المجموعه.**\n\n**✘ الشرح : بالرد على المستخدم مع الامر لمسح جميع التحذيرات السابقه**\n\n**✘ الاستخدام :**      \n\n`.حذف التحذير` <بالرد>", buttons=buttons)

@jmthon.tgbot.on(CallbackQuery(data=re.compile(rb"blacklistw")))
@check_owner
async def _(event):
    buttons = [[Button.inline("رجوع", data="jmthon1"),]]
    await event.edit("**الامر : .منع**\n**الفئة : الادمن **\n\n**✘ مقدمة : لاضافه الكلمه الى القائمه السوداء**\n\n**✘ الشرح : الكلمات المعطاة سيتم حظرها في الدردشه وسيتم حذفها عند ارسالها من قبل شخص اخر يمكنك اضافه اكثر من كلمه بوضع الكلمه في السطر الثاني**\n\n**✘ الاستخدام** :\n   `.منع `<كلمه> \n\n**✘ مثال :**\n`.منع هلا`\n`.منع هلا\nليش`", buttons=buttons)


@jmthon.tgbot.on(CallbackQuery(data=re.compile(rb"dblacklistw")))
@check_owner
async def _(event):
    buttons = [[Button.inline("رجوع", data="jmthon1"),]]
    await event.edit("**الامر : .الغاء منع**\n**الفئة : الادمن **\n\n**✘ مقدمة : لحذف الكلمه من القائمه السوداء**\n\n**✘ الشرح : الكلمات المعطاة سيتم السماح بها الدردشه ولن يتم حذفها عند ارسالها من قبل شخص اخر يمكنك اضافه اكثر من كلمه بوضع الكلمه في السطر الثاني**\n\n**✘ الاستخدام** :\n   `.الغاء منع `<كلمه> \n\n**✘ مثال :**\n`.الغاء منع هلا`\n`.الغاء منع هلا\nليش`", buttons=buttons)
    
@jmthon.tgbot.on(CallbackQuery(data=re.compile(rb"blacklidj")))
@check_owner
async def _(event):
    buttons = [[Button.inline("رجوع", data="jmthon1"),]]
    await event.edit("**الامر : .قائمة المنع**\n**الفئة : الادمن **\n\n**✘ مقدمة : لعرض الكلمات التي تم منعها في الدردشه**\n\n**✘ الشرح : لعرض الكلمات التي قمت بمنعها في دردشه معينه**\n\n**✘ الاستخدام** :\n   `.قائمة المنع`", buttons=buttons)
    
@jmthon.tgbot.on(CallbackQuery(data=re.compile(rb"ssroz")))
@check_owner
async def _(event):
    buttons = [[Button.inline("رجوع", data="jmthon1"),]]
    await event.edit("**⌔∮ اوامر قائـمه الصلاحيات قفل/فتح:**\n\n- `الدردشة`\n- `الوسائط`\n- `الروابط`\n- `المتحركه`\n- `الالعاب` \n- `الانلاين`\n- `الكل`\n- `الاضافه`\n\n ◂  `.الصلاحيات` \n- لعرض صلاحيات الدردشه", buttons=buttons)
    
            
@jmthon.tgbot.on(CallbackQuery(data=re.compile(rb"warningcmd")))
@check_owner
async def _(event):
    buttons = [[Button.inline("رجوع", data="jmthon1"),]]
    await event.edit("**الامر :**   `.التحذيرات`\n**الفئة : الادمن**\n\n**✘ مقدمة : لعرض عدد تحذيرات المستخدم في المجموعه.**\n\n**✘ الشرح : بالرد على المستخدم مع الامر لعرض عدد التحذيرات الخاصه به **\n\n**✘ الاستخدام :**      \n\n`.التحذيرات`", buttons=buttons)

@jmthon.tgbot.on(CallbackQuery(data=re.compile(rb"unbancmd")))
@check_owner
async def _(event):
    buttons = [[Button.inline("رجوع", data="jmthon1"),]]
    await event.edit("**الامر :**   `.الغاء حظر`\n**الفئة : الادمن**\n\n**✘ مقدمة : لألغاء حظر المستخدم في الدردشه**\n\n**✘ الشرح : بالرد على المستخدم او وضع معرفه مع الامر لألغاء حظره في الدردشه والسماح له بالدخول مره ثانيه**\n\n**✘ الاستخدام :**      \n\n`.الغاء حظر` <بالرد/معرف/ايدي>", buttons=buttons)

##
@jmthon.tgbot.on(CallbackQuery(data=re.compile(rb"r33a")))
@check_owner
async def _(event):
    buttons = [[Button.inline("رجوع", data="jmthon0"),]]
    await event.edit("الامر :   `.ارفع`\n**الفئة : الادمن **\n\n**✘ مقدمة : لرفع شخص عام في جميع المجموعات**\n\n**✘ الشرح : بالرد على الشخص لرفعه مشرف في جميع المجموعات التي تكون فيها مشرف**\n\n**✘ الاستخدام :**\n         `.ارفع`", buttons=buttons)

@jmthon.tgbot.on(CallbackQuery(data=re.compile(rb"tn3a")))
@check_owner
async def _(event):
    butze = [[Button.inline("رجوع", data="jmthon0"),]]
    await event.edit("الامر :   `.نزل`\nالفئة : الادمن \n\n**✘ مقدمة : لتنزيل شخص عام من جميع المجموعات**\n\n**✘ الشرح : يمكنك تنزيل المشرف من جميع الكروبات الذي مرفوع بها بشرط أن يكون لديك صلاحية الادمن**\n\n✘ الاستخدام :\n         `.نزل`  < بالرد على الشخص> ", buttons=butze)


@jmthon.tgbot.on(CallbackQuery(data=re.compile(rb"ahd6")))
@check_owner
async def _(event):
    buttons = [[Button.inline("التالي", data="jmthon0"),]]
    await event.edit("**الامر** : `.الاحداث` \n**الفئة : الادمن **\n\n**✘ مقدمة : لمعرفه الرسائل المحذوفه في المجموعه **\n\n**✘ الشرح  :  اكتب الامر وارسله يجب ان تكون لديك صلاحيات المشرف لاستخدام هذا الامر**\n\n**✘ الاستخدام :**\n      `.الاحداث`  < الارسال في مجموعه>", buttons=buttons)
    
    
#**الامر :**   `.كتم`\n**الفئة : الادمن**\n\n**✘ مقدمة : لكتم المستخدم في الدردشه**\n\n**✘ الشرح : بالرد على المستخدم او وضع معرفه مع الامر لكتمه في الدردشه ومنعه من التكلم تحتاج صلاحيات الحذف**\n\n**✘ الاستخدام :**      \n\n`.كتم` <بالرد/معرف/ايدي>

@jmthon.tgbot.on(CallbackQuery(data=re.compile(rb"thpet")))
@check_owner
async def _(event):
    buttons = [[Button.inline("رجوع", data="jmthon0"),]]
    await event.edit("**الامر :**  `.تثبيت`   \n**الفئة : الادمن **\n\n**✘ مقدمة : لتثبيت الرسائل في المجموعه **\n\n**✘ الشرح : لتثبيت رساله معينه في الدردشه كذلك بمكنك ان تضعها بالاشعار او بدون **\n\n**✘ الاستخدام :**\n\n     `.تثبيت`  < بالرد على رساله> \n`.تثبيت بالاشعار`  < بالرد على رسالة>", buttons=buttons)

@jmthon.tgbot.on(CallbackQuery(data=re.compile(rb"rfmsh")))
@check_owner
async def _(event):
    buttons = [[Button.inline("رجوع", data="jmthon0"),]]
    await event.edit("**الامر** : `.رفع مشرف`\n**الفئة : الادمن **\n\n**✘ مقدمة : رفع اشراف في المجموعة**\n\n**✘ الشرح : يقوم برفع المستخدم مشرف في المجموعة مع صلاحيات المشرف**\n\n**✘ الاستخدام** :   `.رفع مشرف` < بالرد على الشخص الذي تريد رفعه>", buttons=buttons)


@jmthon.tgbot.on(CallbackQuery(data=re.compile(rb"zjmsh")))
@check_owner
async def _(event):
    buttons = [[Button.inline("رجوع", data="jmthon0"),]]
    await event.edit("**الامر** : `.تنزيل مشرف`\n**الفئة : الادمن **\n\n**✘ مقدمة : تنزيل المستخدم من الاشراف في المجموعة**\n\n**✘ الشرح : يقوم بتنزيل المستخدم من الاشراف في المجموعة**\n\n**✘ الاستخدام** :   `.تنزيل مشرف` < بالرد على الشخص الذي تريد رفعه>", buttons=buttons)


@jmthon.tgbot.on(CallbackQuery(data=re.compile(rb"srzo")))
@check_owner
async def _(event):
    buttons = [[Button.inline("رجوع", data="jmthon0"),]]
    await event.edit("**الامر : .الصورة**\n**الفئة : الادمن** \n\n**✘ مقدمة : لحذف او تغيير صورة المجموعه** \n\n**✘ الشرح : تقوم بتغيير صورة المجموعه بالرد على صوره بالامر او حذفها بكتابه الامر مع اسم الاضافه ويجب ان تكون لديك صلاحيات**\n\n✘ الاستخدام :  \n\n`.الصورة -وضع`  < بالرد على صورة> \n`.الصورة -حذف`", buttons=buttons)


@jmthon.tgbot.on(CallbackQuery(data=re.compile(rb"ktmrz")))
@check_owner
async def _(event):
    buttons = [[Button.inline("رجوع", data="jmthon0"),]]
    await event.edit("**الامر :**   `.كتم`\n**الفئة : الادمن**\n\n**✘ مقدمة : لكتم المستخدم في الدردشه**\n\n**✘ الشرح : بالرد على المستخدم او وضع معرفه مع الامر لكتمه في الدردشه ومنعه من التكلم تحتاج صلاحيات الحذف**\n\n**✘ الاستخدام :**      \n\n`.كتم` <بالرد/معرف/ايدي>", buttons=buttons)
       
@jmthon.tgbot.on(CallbackQuery(data=re.compile(rb"rimrz")))
@check_owner
async def _(event):
    buttons = [[Button.inline("رجوع", data="jmthon0"),]]
    await event.edit("**الامر :**   `.الغاء كتم`\n**الفئة : الادمن**\n\n**✘ مقدمة : لألغاء كتم المستخدم في الدردشه**\n\n**✘ الشرح : بالرد على المستخدم او وضع معرفه مع الامر لألغاء كتمه في الدردشه والسماح له بالتكلم**\n\n**✘ الاستخدام :**      \n\n`.الغاء كتم` <بالرد/معرف/ايدي>", buttons=buttons)

@jmthon.tgbot.on(CallbackQuery(data=re.compile(rb"rdmua")))
@check_owner
async def _(event):
    buttons = [[Button.inline("رجوع", data="jmthon0"),]]
    await event.edit("**الامر :**   `.طرد`\n**الفئة : الادمن**\n\n**✘ مقدمة : لطرد المستخدم من الدردشه**\n\n**✘ الشرح : بالرد على المستخدم او وضع معرفه مع الامر لطرده من الدردشه يمكنه الدخول مره ثانيه**\n\n**✘ الاستخدام :**      \n\n`.طرد` <بالرد/معرف/ايدي>", buttons=buttons)
