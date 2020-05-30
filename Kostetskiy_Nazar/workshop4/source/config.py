import os

basedir = os.path.abspath(os.path.dirname(__file__))

SECRET_KEY = 'mega-secret'
DEBUG = True

''' Note: для того щоб під'єднати іншу базу даних необхідно:
                                                            1)змінити url
                                                            2)встановити необхідну бібліотеку(psycopg2, cx_Oracle, тощо)
    Для міграції баз даних та необхідно запустити програму та виконати:
                                                                    flask db init(якщо папки migrations немає)
                                                                    flask db migrate
                                                                    flask db upgrade
    При проблемах з міграціями варто 1) спробувати видалити папку migrations та виконати минулі команди знову.
                                     2) видалити табличку alembic_version в БД та спробувати виконати минулі команди знову
                                     
    Зараз під'єднана база postgresql на heroku, проте SQLAlchemy може працювати з будь-якою БД.
'''

MIGRATIONS_PATH = os.path.join(basedir, 'migrations')
DB_URL_PATH = 'postgres://lnzfuimjtjoqdj:fb515f9cf21f270e9fa671305c933e14354442cd6f4b68cff88330f781b08041@ec2-46-137-156-205.eu-west-1.compute.amazonaws.com:5432/dfb30v0l9ttssj'
