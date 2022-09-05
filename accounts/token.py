import jwt as jwt


def get_token(request):
    token = request.COOKIE.get('jwt')
    return token


def get_payload(request):
    token = request.COOKIES.get('jwt')
    payload = jwt.decode(token, 'secretJWTkey', algorithms=['HS256'])
    return payload


def check_token(request):
    token = get_token(request)
    if not token:
        return False
    try:
        payload = get_payload(request)
    except jwt.ExpiredSignatureError:
        return False

    return True
