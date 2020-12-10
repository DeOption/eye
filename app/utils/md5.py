import hashlib


def md5(contend: bytes) -> str:
    """md5加密"""
    md5 = hashlib.md5()
    md5.update(contend)
    return md5.hexdigest()


if __name__ == '__main__':
    contend = b"password"
    result = md5(contend)
    print(result)