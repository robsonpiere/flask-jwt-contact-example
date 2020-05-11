from functools import wraps
from flask_restful import request
import jwt
from flask import current_app
from app.models import User
from http import client

def jwt_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = None

        if "authorization" in request.headers:
            token = request.headers["authorization"]

        if not token:
            return {"error": "sem permissão"}, client.UNAUTHORIZED
        
        if not "Bearer" in token:
            return {"error": "Token inválido"}, client.UNAUTHORIZED 

        try:
            token_pure = token.replace("Bearer ", "")
            decoded = jwt.decode(token_pure, current_app.config["SECRET_KEY"])
            current_user = User.query.get(decoded["id"])
        except:
            return {"error": "Token inválido"}, client.FORBIDDEN

        return f(current_user = current_user, *args, **kwargs)
        
    return decorated
