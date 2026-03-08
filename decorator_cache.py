# This is my cache decorator
def cache_Result(func):
    cache = {}
    
    def wrapper(product_id):
        
        if product_id in cache:
            print("returned the cache result")
            return cache[product_id]
        
        result = func(product_id)
        cache[product_id] = result
        return result 
    
    return wrapper
    
# below is my function using the cache decoartor to storethe result in cache
@cache_Result
def calcaulte_price(product_id):
    print("Calcualting the price...")
    
    product_prices = {    # this data will come from the DB
        101: 4000,
        102: 3000,
        103: 6700
    }
    
    return product_prices.get(product_id,"Product not found")

# calling the functions
print(calcaulte_price(101)) #this will store the result into the cahache for 1st time
print(calcaulte_price(101)) # this will return the cahcahed results from here onwards
print(calcaulte_price(101))
print(calcaulte_price(101))
print(calcaulte_price(102))
print(calcaulte_price(103))
print(calcaulte_price(102))
