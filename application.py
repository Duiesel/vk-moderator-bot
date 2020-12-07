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


if __name__ == '__main__':
    port = int(os.environ.get('PORT', 80))
    app = web.Application()
    logging.basicConfig(level=logging.DEBUG)
    logging.debug('starting!')
    app.add_routes([web.get('/', hello)])
    web.run_app(app, port=port)
