from asyncio import gather
from re import search as research
from time import time

from aiofiles.os import path as aiopath
from psutil import (
    boot_time,
    cpu_count,
    cpu_percent,
    disk_usage,
    net_io_counters,
    swap_memory,
    virtual_memory,
)

from bot import bot_start_time
from bot.helper.ext_utils.bot_utils import cmd_exec, new_task
from bot.helper.ext_utils.status_utils import (
    get_readable_file_size,
    get_readable_time,
)
from bot.helper.telegram_helper.message_utils import send_message

commands = {
    "aria2": ("xria --version", r"aria2 version ([\d.]+)"),
    "qBittorrent": ("xnox --version", r"qBittorrent v([\d.]+)"),
    "SABnzbd+": ("xnzb --version", r"xnzb-([\d.]+)"),
    "python": ("python3 --version", r"Python ([\d.]+)"),
    "rclone": ("xone --version", r"rclone v([\d.]+)"),
    "yt-dlp": ("yt-dlp --version", r"([\d.]+)"),
    "ffmpeg": ("xtra -version", r"ffmpeg version (n[\d.]+)"),
    "7z": ("7z i", r"7-Zip ([\d.]+)"),
}


@new_task
async def bot_stats(_, message):
    total, used, free, disk = disk_usage("/")
    swap = swap_memory()
    memory = virtual_memory()

    stats = (
        f"<b>🔹 Commit:</b> {commands['commit']}\n\n"
        f"<blockquote>⏱ Uptime\n"
        f" • Bot: <code>{get_readable_time(time() - bot_start_time)}</code>\n"
        f" • OS : <code>{get_readable_time(time() - boot_time())}</code></blockquote>\n\n"
        f"<blockquote>💾 Disk\n"
        f" • Total: <code>{get_readable_file_size(total)}</code>\n"
        f" • Used : <code>{get_readable_file_size(used)}</code> | Free: <code>{get_readable_file_size(free)}</code>\n"
        f" • Usage: <code>{disk}%</code></blockquote>\n\n"
        f"<blockquote>📡 Network\n"
        f" • Up  : <code>{get_readable_file_size(net_io_counters().bytes_sent)}</code>\n"
        f" • Down: <code>{get_readable_file_size(net_io_counters().bytes_recv)}</code></blockquote>\n\n"
        f"<blockquote>🖥 Resources\n"
        f" • CPU  : <code>{cpu_percent(interval=0.5)}%</code> ({cpu_count(logical=False)}/{cpu_count()} cores)\n"
        f" • RAM  : <code>{memory.percent}%</code>\n"
        f" • Swap : <code>{swap.percent}%</code> of <code>{get_readable_file_size(swap.total)}</code>\n"
        f" • Mem  : <code>{get_readable_file_size(memory.used)}</code> / <code>{get_readable_file_size(memory.total)}</code></blockquote>\n\n"
        f"<blockquote>📦 Packages\n"
        f" • Python     : <code>{commands['python']}</code>\n"
        f" • aria2      : <code>{commands['aria2']}</code>\n"
        f" • qBittorrent: <code>{commands['qBittorrent']}</code>\n"
        f" • SABnzbd+   : <code>{commands['SABnzbd+']}</code>\n"
        f" • rclone     : <code>{commands['rclone']}</code>\n"
        f" • yt-dlp     : <code>{commands['yt-dlp']}</code>\n"
        f" • ffmpeg     : <code>{commands['ffmpeg']}</code>\n"
        f" • 7z         : <code>{commands['7z']}</code></blockquote>"
    )

    await send_message(message, stats)


async def get_version_async(command, regex):
    try:
        out, err, code = await cmd_exec(command.split())
        if code != 0:
            return f"Error: {err}"
        match = research(regex, out)
        return match.group(1) if match else "Version not found"
    except Exception as e:
        return f"Exception: {e!s}"


@new_task
async def get_packages_version():
    tasks = [get_version_async(cmd, regex) for cmd, regex in commands.values()]
    versions = await gather(*tasks)
    commands.update(dict(zip(commands.keys(), versions)))

    if await aiopath.exists(".git"):
        last_commit = await cmd_exec(
            "git log -1 --date=short --pretty=format:'%cd <b>From</b> %cr'", True
        )
        last_commit = last_commit[0]
    else:
        last_commit = "No UPSTREAM_REPO"

    commands["commit"] = last_commit