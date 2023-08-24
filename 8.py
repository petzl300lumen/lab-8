import datetime

def order_time(order):
    def inner(q):
        result = order(q)
        print(f"[{datetime.datetime.now()}], Стоимость доставки:{result},")
        return result
    return inner

@order_time
def quality_sum(q):
    first = 10.95
    other = 2.95
    if q ==1:
        return first
    else:
        return first + other * q

    
q = int(input("Количество товаров:"))
quality_sum(q)
    