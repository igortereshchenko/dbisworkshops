from sqlalchemy.engine import create_engine

# для создания таблиц Вам неободимо прописать путь к своей базе данніх oracle
DATABASE_URI = 'postgres+psycopg2://postgres:msn1973msn@localhost:5432/bot'

engine = create_engine(DATABASE_URI)

