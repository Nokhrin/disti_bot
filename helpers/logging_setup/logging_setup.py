import logging

logging.basicConfig(
        format='%(asctime)s :: %(levelname)s :: %(lineno)d :: %(message)s',
        filename='logs/disti_bot.log',
        filemode='a',
        encoding='utf-8',
        level=logging.DEBUG,
        )
