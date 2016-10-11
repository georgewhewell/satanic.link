from aiohttp import web

url_map = {}

homepage = open('index.html', 'rb').read()
index = lambda x: web.Response(body=homepage, content_type='text/html')


async def submit(request):
    url_map[request.post.get('url')] = 'something'
    return 

async def handle(request):
    name = request.match_info.get('code')
    text = "ur a fuckface " + name
    return web.Response(body=homepage, content_type='text/html')


app = web.Application()
app.router.add_get('/', index)
app.router.add_post('/', submit)
app.router.add_get('/{code}', handle)

web.run_app(app)
