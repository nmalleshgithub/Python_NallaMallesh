# Discount Decorator
def apply_discount_decorator(func):
    def wrapper(base_price):
        price = func(base_price)
        discount_price = price - (price * 0.10)   # 10% discount
        print("After 10% discount:", discount_price)
        return discount_price
    return wrapper


# Tax Decorator
def tax_decorator(func):
    def wrapper(base_price):
        price = func(base_price)
        final_price = price + (price * 0.18)   # 18% GST
        print("After 18% GST:", final_price)
        return final_price
    return wrapper


@tax_decorator
@apply_discount_decorator
def calculate_flight_price(base_price):
    print("Base Price:", base_price)
    return base_price


# Call the function
calculate_flight_price(2000)    
