from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.core.config import setting

# 第一步是创建一个SQLAlchemy“引擎”。
engine = create_engine(setting.SQLALCHEMY_DATABASE_URI)

# SessionLocal该类的每个实例将是一个数据库会话。该类本身还不是数据库会话。
# 但是，一旦我们创建了SessionLocal该类的实例，该实例将成为实际的数据库会话。
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)