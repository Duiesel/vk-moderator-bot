import os

from aiohttp import web


async def hello(request):
    """Test request handler."""
    return web.Response(text="Hello, world")


if __name__ == '__main__':
    PORT = os.getenv('PORT')
    app = web.Application()
    app.add_routes([web.get('/', hello)])
    web.run_app(app, port=PORT)
