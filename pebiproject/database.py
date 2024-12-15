# import sqlite3 as database
#
# conn = database.connect('example.db')
# exe = conn.cursor()
#
# exe.execute("""CREATE TABLE IF NOT EXISTS products(ID INTEGER PRIMARY KEY,
# PRODUCT TEXT,
# TYPE TEXT,
# NAME TEXT,
# PRICE TEXT)""")
# product = 'HairTreatment'
# types = ["Hair dryer", "Straightener", "Curling iron", "Hair brush", "Hair serum"]
# brand = {
#         1: [["Philips", 1299], ["Gladking", 1350], ["Beauty Star", 1650], ["Remington", 2125],
#             ["Super professional", 2477]],
#         2: [["Philips", 4599], ["MAC", 2000], ["Remington", 3732], ["Titanium", 1778], ["JML Supra", 3120]],
#         3: [["Philips", 3955], ["Conair", 1579], ["Dreame", 4880], ["Babyliss", 1259], ["W Elite", 3999]],
#         4: [["Goody Smooth Blends", 1199], ["Morrocanoil", 1800], ["Denman", 1995], ["Jill Stuart", 2844],
#             ["AZH", 2304]],
#
#         5: [["Creamsilk", 219], ["L’Oreal paris", 909], ["Kerastase", 3231], ["Mise En Scene", 1856],
#             ["Argan oil", 1116]]}
# for prod in brand:
#     for val in brand[prod]:
#         exe.execute("INSERT INTO products(PRODUCT, TYPE, NAME, PRICE) VALUES(?, ?, ?, ?)",
#                         (product, types[prod - 1], val[0], val[1]))
#         conn.commit()
#
# exe.close()
# conn.close()
#

#
#
# product =['Clothes', 'Bags', 'Perfumes', 'ShoesorSandals', 'Jewelry', 'Cosmetics', 'HairTreatment']
# subcategories = {
#         1: ["T-shirts", "Jeans", "Jackets", "Suits", "Sweaters"],
#         2: ["Backpacks", "Handbags", "Totes", "Clutches", "Messenger bags"],
#         3: ["Eau de toilette", "Eau de parfum", "Cologne", "Body spray"],
#         4: ["Sneakers", "Loafers", "Boots", "Sandals", "Dress shoes"],
#         5: ["Necklaces", "Bracelets", "Earrings", "Rings", "Brooches"],
#         6: ["Foundation", "Lipstick", "Mascara", "Eye shadow", "Blush"],
#         7: ["Hair dryer", "Straightener", "Curling iron", "Hair brush", "Hair serum"]
#
# if subcategory_number == 1:
#     brands = {
#         1: [["Nike", 2195], ["Adidas", 1800], ["H&M", 399], ["Zara", 1900]],  # T-shirts
#         2: [["Levi's", 1729], ["Wrangler", 2000], ["Diesel", 11000], ["Guess", 3999]],  # Jeans
#         3: [["The North Face", 4000], ["Patagonia", 2380], ["Canada Goose", 6798], ["Columbia", 5490]],  # Jackets
#         4: [["Hugo Boss", 27000], ["Armani", 200000], ["Ralph Lauren", 83994], ["Gucci", 196000]],  # Suits
#         5: [["Tommy Hilfiger", 6500], ["Gap", 1500], ["Uniqlo", 1490], ["Calvin Klein", 5565]]  # Sweaters
#     }
# elif subcategory_number == 2:
#     brands = {
#         1: [["Osprey", 16990], ["Jansport", 800], ["Dueter", 6536], ["Adidas", 2490], ["Baggu", 4633]],
#         2: [["Hermes", 6699], ["Loui Vuitton", 82204], ["Prada", 11550],
#             ["Saint Laurent", 67086], ["Channel", 12950]],
#         3: [["Gucci", 60000], ["Channel", 11550], ["Prada", 11244], ["Adidas", 2000], ["Jansport", 2490]],
#         4: [["Dior", 2500], ["Cole Haan", 3990], ["Hollow rose diamond", 3690],
#             ["New pearl small", 1099], ["Pedro Studio", 9100]],
#         5: [["DVL Iusso", 1999], ["Converse", 2290], ["Crumpler", 3900], ["Puma", 1800], ["World traveller", 2190]]
#     }
# elif subcategory_number == 3:
#     brands = {
#         1: [["Dior", 1500], ["Oxygn", 413], ["Triumph", 299], ["Os man thus", 3900], ["Cool water", 5098]],
#         2: [["Estee lauder", 5029], ["Chanel", 5000], ["Void", 4500], ["Sigl", 4999], ["Dansesauvage", 3900]],
#         3: [["Dorin", 11000], ["Bench", 100], ["Calvin", 3395], ["Escape", 1250]],
#         4: [["Jo Malone", 1128], ["SPRIG", 1404], ["Shea", 850], ["LUSH Authentic", 2544], ["Paco Rabanne", 1583]]
#     }
# elif subcategory_number == 4:
#     brands = {
#         1: [["Nike gamma force", 4995], ["ordan1 retro low dior", 1322648], ["Vans knu", 2980], ["Arc brothers", 2559]],
#         2: [["Mario D boro", 2760], ["Dr. Martens", 1270], ["Bigstrut loafers", 3000], ["Alta penny loafers", 950],
#             ["Tassel martin", 399]],
#         3: [["Dr. Martens", 1800], ["Mardini", 1900], ["Chelsea", 1443], ["Marquins", 2990], ["Surgut vancat", 2698]],
#         4: [["Arizona", 1329], ["Skechers", 3795], ["Birkenstock", 2228], ["Sperry", 1195], ["Michaela velcro", 1499]],
#         5: [["Marquins", 2990], ["Mario D boro", 1990], ["Bibo", 2749], ["Christen", 1000]]}
# elif subcategory_number == 5:
#     brands = {
#         1: [["Amethyst heart", 1146], ["Daniel wellington", 4950], ["Saudi gold VCA", 5200],
#             ["PRYA Jewelry", 2648], ["Valentino", 20364]],
#         2: [["Daniel wellington", 10960], ["Tory Burch kira", 8392], ["Valentino", 23489], ["Louis Vuitton", 18000],
#             ["Unclou Bracelet", 277537]],
#         3: [["Ross-simons", 8871], ["CUOKA MIRACLE", 2116], ["Zel", 2450], ["Michael Kors", 7187],
#             ["Setéur Paris", 18832]],
#         4: [["Moonstone Lab", 26300], ["Messika", 167000], ["LIV 18k gold", 10500], ["Aramis", 44850],
#             ["Illios", 29394]],
#         5: [["EMEGCY", 1336], ["Mooclife", 2784], ["Dolce & gabbana", 19357], ["Chanel", 57778], ["Elite", 4978]]
#     }
# elif subcategory_number == 6:
#     brands = {
#         1: [["Tarte", 2399], ["Clinique", 3355], ["E.L.F", 1960], ["The Ordinary", 5206], ["Uoma", 3559]],
#         2: [["Carslan", 1002], ["Clinique", 1702], ["Sephora", 2087], ["Rituel De Fille", 1394],
#             ["Souffle Matte", 1450]],
#         3: [["Maybelline", 1390], ["Guerlain Noir", 1800], ["Pere Perez", 1616], ["Kaja", 1321],
#             ["Oreal", 2845]],
#         4: [["Maybelle", 1199], ["Urban Decay", 2249], ["NYX", 2328], ["MAC", 3400], ["The Zodiac", 1389]],
#         5: [["Clinique", 1620], ["Dior", 2369], ["Nars", 2500], ["Sasa", 1506], ["Suqqu", 1899]]}
# elif subcategory_number == 7:
#     brands = {
#         1: [["Philips", 1299], ["Gladking", 1350], ["Beauty Star", 1650], ["Remington", 2125],
#             ["Super professional", 2477]],
#         2: [["Philips", 4599], ["MAC", 2000], ["Remington", 3732], ["Titanium", 1778], ["JML Supra", 3120]],
#         3: [["Philips", 3955], ["Conair", 1579], ["Dreame", 4880], ["Babyliss", 1259], ["W Elite", 3999]],
#         4: [["Goody Smooth Blends", 1199], ["Morrocanoil", 1800], ["Denman", 1995], ["Jill Stuart", 2844],
#             ["AZH", 2304]],
#
#         5: [["Creamsilk", 219], ["L’Oreal paris", 909], ["Kerastase", 3231], ["Mise En Scene", 1856],
#             ["Argan oil", 1116]]}