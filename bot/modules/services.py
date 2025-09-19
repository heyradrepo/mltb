from time import time

from ..helper.ext_utils.bot_utils import new_task
from ..helper.telegram_helper.button_build import ButtonMaker
from ..helper.telegram_helper.message_utils import send_message, edit_message, send_file
from ..helper.telegram_helper.filters import CustomFilters
from ..helper.telegram_helper.bot_commands import BotCommands


@new_task
async def start(_, message):
    buttons = ButtonMaker()
    buttons.url_button("📢 频道", "https://t.me/halodeni")
    buttons.url_button("👤 老板", "https://t.me/clyfly")
    reply_markup = buttons.build_menu(2)

    image_url = "https://i.pinimg.com/736x/34/f8/f1/34f8f1c59d502ea5f7b8cf22f4080434.jpg"

    if await CustomFilters.authorized(_, message):
        caption = (
            "🤖 <b>嗨，欢迎呀！</b>\n\n"
            "我能帮你：\n"
            "➡️ 下载/镜像：链接、文件、种子、Rclone 云\n"
            "➡️ 上传到：Google 云盘、Telegram、Rclone\n\n"
            f"点 <code>/{BotCommands.HelpCommand}</code> 看所有命令 👀"
        )
    else:
        caption = (
            "⚠️ <b>还没授权哦！</b>\n\n"
            "功能：镜像 链接/文件/种子/Rclone\n"
            "上传：Google 云盘、Telegram、Rclone\n\n"
            "👉 想用的话，自己部署一个吧～"
        )

    await message.reply_photo(
        photo=image_url,
        caption=caption,
        reply_markup=reply_markup
    )


@new_task
async def ping(_, message):
    start_time = int(round(time() * 1000))
    reply = await send_message(message, "🏓\nPinging...")
    end_time = int(round(time() * 1000))
    await edit_message(reply, f"🏓\nPong! <b>{end_time - start_time} ms</b>")


@new_task
async def log(_, message):
    await send_file(message, "log.txt")