#!/usr/bin/env python3
"""نقطة تشغيل البوت الرئيسية"""
import sys
import os
import asyncio
from aiohttp import web

# Add project root to path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from bot.main import main


async def health_check(request):
    return web.Response(text="OK")


async def start_health_server():
    app = web.Application()
    app.router.add_get("/", health_check)
    app.router.add_get("/health", health_check)
    runner = web.AppRunner(app)
    await runner.setup()
    port = int(os.getenv("PORT", 10000))
    site = web.TCPSite(runner, "0.0.0.0", port)
    await site.start()
    print(f"Health check server running on port {port}")


async def run_all():
    await start_health_server()
    await main()


if __name__ == "__main__":
    print("""
╔══════════════════════════════════════════╗
║     بوت تحميل الوسائط العربي            ║
║     Arabic Media Downloader Bot          ║
║     Powered by aiogram 3.x + yt-dlp     ║
╚══════════════════════════════════════════╝
    """)
    asyncio.run(run_all())
