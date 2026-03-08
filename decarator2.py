def discount(func):
    def wrapper(price):
        price = func(price)
        price = price * 0.9
        print("After 10% discount:", price)
        return price
    return wrapper

def tax(func):
    def wrapper(price):
        price = func(price)
        price = price * 1.18
        print("After 18% GST:", price)
        return price
    return wrapper

@tax
@discount
def flight_price(price):
    print("Base Price:", price)
    return price

flight_price(5000)
