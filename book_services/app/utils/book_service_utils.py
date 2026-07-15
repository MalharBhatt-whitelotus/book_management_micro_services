def valid_sort_by(sort_by: str):
    valid_sort_by = ("id", "title", "author", "category", "price", "quantity", "book_type")
    if sort_by not in valid_sort_by:
        return False
    return True

def valid_order(order: str):
    valid_order = ("asc","desc")
    if order not in valid_order:
        return False
    return True

def valid_min_price(min_value: int):
    if min_value<= 0:
        return False
    return True
def valid_max_price(max_value: int):
    if max_value<= 0:
        return False
    return True
def valid_max_min_price(min_value: int, max_value: int):
    if (min_value<= 0 or max_value<=0) or (min_value>max_value):
        return False
    return True