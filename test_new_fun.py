from bill import shop_history
def test_shop_list():
    shop_list =  [["Trousers", 99.0], ["Suit", 300.0], ["Soks", 10.0], ["cigarets", 11.0], ["cognak", 40.0], ["whiski", 25.0]]
    assert shop_history(shop_list) == shop_list
test_shop_list()