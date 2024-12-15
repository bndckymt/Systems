# import sqlite3
#
# conn = sqlite3.connect('MSMdatabase.db')
# cursor = conn.cursor()
# seasonings_products = ('Magic sarap', 'Aji nomoto', 'Knor cubes', 'Sinigang mix', 'Oyster sauce',
#                                'Soy sauce', 'Vinegar')
# seasonings_price = [4.00, 3.00, 5.00, 10.00, 5.00, 10.00, 10.00,]
# type = "seasonings"
# count = 0
# for item in seasonings_products:
#     product_type = type
#     product_name = item
#     product_price = seasonings_price[count]
#     count += 1
#
#     cursor.execute("INSERT INTO product(product_type, product_name, product_price) VALUES(?, ?, ?)",
#      (product_type, product_name, product_price))
#     conn.commit()
#
# conn.close()
