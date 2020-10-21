from telegram import InlineQueryResultArticle, InputTextMessageContent
from telegram.ext import Updater, InlineQueryHandler
from itertools import count
import os
import requests

TOKEN = os.getenv('OTSBOT_TOKEN')


def make_secret(secret):
    result = requests.post(
            'https://onetimesecret.com/api/v1/share',
            params={'secret': secret},
            auth=('nu3toban@gmail.com', 'ac7e2027b263cb32c96dd7bd02dacdce8a2272cb'),
    )
    return 'https://onetimesecret.com/secret/' + result.json()['secret_key']


def inline_handler(u, c):
    try:
        query = u.inline_query.query
        result = [InlineQueryResultArticle(id=0, title='Your secret', input_message_content=InputTextMessageContent(make_secret(query)))]
        u.inline_query.answer(result, is_personal=False)
    except Exception as ex:
        print(f'Cannot send: {ex}')


def main():
    updater = Updater(TOKEN, use_context=True)
    dp = updater.dispatcher

    dp.add_handler(InlineQueryHandler(inline_handler))

    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()
