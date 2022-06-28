from user import User
import jwt
from sanic import Blueprint, text
from db_controller import check_if_user_exists

login = Blueprint("login", url_prefix="/login")


@login.post("/")
async def do_login(request):

    if len(request.json.keys()) == 0:
        return text("Error Veio Nulo", 400)
    if "nome" not in request.json.keys():
        return text("Error Faltou o nome", 400)
    if "pass" not in request.json.keys():
        return text("Error Faltou a senha", 400)

    user = User(0, request.json["nome"], request.json["pass"])

    if not check_if_user_exists(user):
        return text("Error Usuario Não Cadastrado", 400)

    token = jwt.encode({}, request.app.config.SECRET)
    return text(token)
