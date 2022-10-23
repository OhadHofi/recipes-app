import pymysql

DEFAULT_HOST = "localhost"
DEFAULT_USER = "root"
DEFAULT_DB = "recipes_app"
DEFAULT_PWD = ""


class DB_Manager:
    def __init__(self, host=DEFAULT_HOST, user=DEFAULT_USER, pwd=DEFAULT_PWD, db=DEFAULT_DB):
        self.connection = pymysql.connect(
            host=host,
            user=user,
            password=pwd,
            db=db,
            charset="utf8",
            cursorclass=pymysql.cursors.DictCursor
        )

    def get_dairy_ingredients(self):
        with self.connection.cursor() as cursor:
            query = """ SELECT * from dairy_ingredients;"""
            cursor.execute(query)
            result = cursor.fetchall()
            return [res["dairy_ingredient"] for res in result]

    def get_gluten_ingredients(self):
        with self.connection.cursor() as cursor:
            query = """ SELECT * from gluten_ingredients;"""
            cursor.execute(query)
            result = cursor.fetchall()
            return [res["gluten_ingredient"] for res in result]


db_manager = DB_Manager()
