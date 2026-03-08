def apply_discount(func):

    def wrapper(base_price):
        price = func(base_price)
        print("Applying flight discount")
        discount_price = price - (price * 0.10)
        print("Price after discount:", discount_price)
        return discount_price

    return wrapper


def apply_tax(func):

    def wrapper(base_price):
        price = func(base_price)
        print("Adding GST tax")
        final_price = price + (price * 0.18)
        print("Final price after tax:", final_price)
        return final_price

    return wrapper


@apply_tax
@apply_discount
def calculate_flight_price(base_price):
    print("Base Ticket Price:", base_price)
    return base_price

# function call
calculate_flight_price(10000)
