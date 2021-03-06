from book_db_access import *
from user_db_access import *
from order_db_access import *
from sqlalchemy import *


DATABASEURI = "postgresql://yc3171:6567@w4111vm.eastus.cloudapp.azure.com/w4111"
engine = create_engine(DATABASEURI)
conn = None
try:
    conn = engine.connect()
except:
    print "uh oh, problem connecting to database"
    import traceback; traceback.print_exc()
    conn = None

bda = BookDBAccess(conn)
# print bda.get_reading_list(9, 'read')
# print bda.get_wishlist(9)
# print bda.get_books_from_wishlist(2)
# print bda.get_book_tags(16)
# print bda.get_books_by_tag_id(1)
# print bda.get_books_in_shoppingcart(1)
# print bda.get_genres()
# print bda.get_genre(1)
# print bda.search('da')
print bda.get_newest_book(8)
print bda.get_best_sellers(8)

uda = UserDBAccess(conn)
# print uda.get_followers(1)
# print uda.get_followings(1)

oda = OrderDBAccess(conn)
# print oda.insert_book_to_shoppingcart(6, 1, 3)
# print oda.insert_book_to_shoppingcart(9, 1, 5)
# print oda.insert_book_to_shoppingcart(8, 1, 2)
# print oda.remove_book_from_shoppingcart(6, 1)
#print oda.get_order(30)

# create an order
# books = [
#     {'bid': 17, 'quantity': 2},
#     {'bid': 18, 'quantity': 1},
#     {'bid': 8, 'quantity': 3}
# ]
# oda.create_order(7, 'Oslo somewhere', '48867735', 'Yue', 'Cen', books)

# get an order
# print oda.get_order(30)