from psycopg2 import connect


stmt = "SELECT ROUND(AVG(buyprice)::NUMERIC, 2) FROM products"
with connect(user='postgres', password='postgres', database='classicmodels') as cnx:
    with cnx.cursor() as cursor:
        cursor.execute(stmt)
        result = cursor.fetchall()


print(result)
