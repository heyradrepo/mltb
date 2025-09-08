from time import time

from ..helper.ext_utils.bot_utils import new_task
from ..helper.telegram_helper.button_build import ButtonMaker
from ..helper.telegram_helper.message_utils import send_message, edit_message, send_file
from ..helper.telegram_helper.filters import CustomFilters
from ..helper.telegram_helper.bot_commands import BotCommands


@new_task
async def start(_, message):
    buttons = ButtonMaker()
    buttons.url_button("Channel", "https://t.me/halodeni")
    buttons.url_button("Owner", "https://t.me/clyfly")
    reply_markup = buttons.build_menu(2)

    if await CustomFilters.authorized(_, message):
        start_string = (
            "🤖 <b>Welcome!</b>\n\n"
            "This bot can mirror from:\n"
            "• Links | Telegram files\n"
            "• Torrents | NZB\n"
            "• Rclone-supported clouds\n\n"
            "➡️ Upload to:\n"
            "• Google Drive\n"
            "• Telegram Cloud\n"
            "• Any Rclone-supported cloud\n\n"
            f"Type <code>/{BotCommands.HelpCommand}</code> to see all available commands."
        )
        await send_message(message, start_string, reply_markup)
    else:
        not_auth = (
            "⚠️ <b>Unauthorized!</b>\n\n"
            "This bot supports mirroring from:\n"
            "• Links | Telegram files\n"
            "• Torrents | NZB\n"
            "• Rclone-supported clouds\n\n"
            "➡️ Upload to Google Drive, Telegram Cloud, or Rclone clouds.\n\n"
            "👉 Deploy your own bot to use these features!"
        )
        await send_message(message, not_auth, reply_markup)


@new_task
async def ping(_, message):
    start_time = int(round(time() * 1000))
    reply = await send_message(message, "🏓 Pinging...")
    end_time = int(round(time() * 1000))
    await edit_message(reply, f"🏓 Pong! <b>{end_time - start_time} ms</b>")


@new_task
async def log(_, message):
    await send_file(message, "log.txt")