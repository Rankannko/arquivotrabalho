from sanic import Sanic, text

from auth import protected
from login import login

app = Sanic("AuthApp")
app.config.SECRET = "EU_NAO_GOSTO_PUTS_QUE_ESTAVA_DISTRAID@"
app.blueprint(login)


@app.get("/explicito")
async def esse_eh_aberto(request):
    return text("Esse cara é todo aberto!")


@app.get("/secret")
@protected
async def secret(request):
    return text("To go fast, you must be fast.")
