import pymysql


dairy_ingredients = ["Cream", "Cheese", "Milk", "Butter",
                     "Creme", "Ricotta", "Mozzarella", "Custard", "Cream Cheese"]
gluten_ingredients = ["Flour", "Bread", "spaghetti", "Biscuits", "Beer"]

connection = pymysql.connect(
    host="localhost",
    user="root",
    password="",
    db="recipes_app",
    charset="utf8",
    cursorclass=pymysql.cursors.DictCursor
)


def insert_ingredient(db_name, ingredient):

    with connection.cursor() as cursor:
        query = f"""INSERT INTO {db_name} VALUES("{ingredient}")"""
        cursor.execute(query)
        connection.commit()


def insert_to_db(db_name, ingredients):
    for ingredient in ingredients:
        insert_ingredient(db_name, ingredient)


insert_to_db("dairy_ingredients", dairy_ingredients)
insert_to_db("gluten_ingredients", gluten_ingredients)
