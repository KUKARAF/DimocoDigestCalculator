import hashlib, hmac, urllib


def calcDigest(pw,params):
    # dictionary keywords will be used to sort values. Only vals will be  concatinated then hashed with merchant password

    to_sign = ""
    params['result'] = 0
    for v in sorted(params.keys()):
        to_sign += str(params[v])
    api_key = ''.join(pw).encode("utf8")
    print('calculated from: '+to_sign)
    to_sign = to_sign.encode("utf8")
    digest = hmac.new(api_key, to_sign, digestmod=hashlib.sha256).hexdigest()

    return digest

