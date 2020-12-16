from sqlalchemy.ext.declarative import declarative_base

# 使用declarative_base()返回类的函数, 从该类继承以创建每个数据库模型或类（ORM模型）
Base = declarative_base()
