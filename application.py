import logging
import os

from aiohttp import web
from aiohttp.web import middleware


@middleware
async def secret_validate(request, handler):

    resp = await handler(request)
    resp.text = resp.text + ' wink'
    return resp


async def hello(request):
    """Test request handler."""
    logging.info('hello world incoming request!')
    logging.debug('DEBUG on hello world incoming request!')
    return web.Response(text="Hello, world")


async def callbackapi_handler(request):
    """Callback API request handler"""
    data = await request.json()
    # here data['group_id'] can be checked
    if data['type'] == 'confirmation':
        # TODO: remove hard code
        return web.Response(text='ee49c27d')
    # new message
    elif data['type'] == 'message_new':
        logging.info(data['object'])

    return web.Response(text='OK')


if __name__ == '__main__':
    port = int(os.environ.get('PORT', 80))
    app = web.Application()
    logging.basicConfig(level=logging.DEBUG)
    logging.debug('starting!')
    app.add_routes([
        web.get('/', hello),
        web.post('/callback/send_notification', callbackapi_handler)
        ])
    web.run_app(app, port=port)
