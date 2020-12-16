from pydantic import BaseSettings


class Setting(BaseSettings):
    # 路由
    API_V1_STR: str = "/app/v1"

    # 密钥，由MD5加密生成
    SECRET_KEY: str = 'heida'

    # 过期时间
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 1800

    # 数据库连接
    HOSTNAME: str = '59.110.53.228'
    PORT: str = '3306'
    DATABASE: str = 'db_test'
    USERNAME: str = 'root'
    PASSWORD: str = 'root'
    DB_URI: str = 'mysql+pymysql://{}:{}@{}:{}/{}?charset=utf8'.format(USERNAME, PASSWORD, HOSTNAME, PORT, DATABASE)
    SQLALCHEMY_DATABASE_URI: str = DB_URI
    # SQLALCHEMY_DATABASE_URI: str = 'mysql+pymysql://root:root@59.110.53.228:3306/db_test'


setting = Setting()
