from aiohttp import web

from os.path import join, dirname


url_map = {}

index_filename = join(dirname(__file__), 'index.html')
homepage = open(index_filename, 'rb').read()


async def index(request):
    return web.Response(body=homepage, content_type='text/html')


async def submit(request):
    url_map[request.post.get('url')] = 'something'
    return 'something'


async def redirect(request):
    name = request.match_info.get('code')
    text = "ur a fuckface " + name
    return web.Response(body=homepage, content_type='text/html')


app = web.Application()

# get index
app.router.add_get('/', index)

# shortened url
app.router.add_get('/{code}', redirect)

# submit new url
app.router.add_post('/', submit)


if __name__ == '__main__':
    web.run_app(app)
