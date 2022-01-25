import logging


async def main():
    logging.basicConfig(level=logging.INFO)

    import handlers
    from common import dp, bot
    from services import weather_api
    from database.query import conn
    try:
        await dp.start_polling()
    finally:
        conn.close()
        await weather_api.api_session.close()
        await bot.session.close()


if __name__ == '__main__':
    import asyncio
    try:
        asyncio.run(main())
    except (KeyboardInterrupt, SystemExit):
        logging.info("Bot stopped!")



#Test comment