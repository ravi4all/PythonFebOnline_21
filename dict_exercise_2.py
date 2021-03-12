products = [
    {"p_name":"Apple Iphone 11","brand":"Apple","Category":"Mobile","price":98000},
    {"p_name":"Redmi Note 6","brand":"Xiaomi","Category":"Mobile","price":15000},
    {"p_name":"Sports Shoes","brand":"Puma","Category":"Shoes","price":3400},
    {"p_name":"JBL Headphones bluetooth","brand":"JBL","Category":"Headphones","price":1200},
    {"p_name":"Leather Jacket","brand":"Zara","Category":"Clothes","price":4500},
    {"p_name":"Puma Shoes","brand":"Puma","Category":"Shoes","price":2070},
    {"p_name":"Adidas Sports Shoes","brand":"Adidas","Category":"Shoes","price":1900},
    {"p_name":"Macbook Pro","brand":"Apple","Category":"Laptop","price":128000},
    {"p_name":"Lenovo thinkpad","brand":"Lenovo","Category":"Laptop","price":78000},
    {"p_name":"Asus Zenbook","brand":"Asus","Category":"Laptop","price":88000},
    ]

to_search = input("Enter your search : ")
to_search = to_search.lower()
'''
1. User can enter either product name or brand or category
2. Store search results in a list
3. Ask user if he/she wants to filter data based on price
  a. low to high
  b. high to low
'''

results = []

for i in range(len(products)):
    condition_1 = to_search in products[i]['p_name'].lower()
    condition_2 = to_search in products[i]['brand'].lower()
    condition_3 = to_search in products[i]['Category'].lower()
    if condition_1 or condition_2 or condition_3:
        print("Name :",products[i]['p_name'])
        print("Brand :",products[i]['brand'])
        print("Price :",products[i]['price'])
        print("*" * 50)
        results.append(products[i])

to_filter = input("Filter Products : Yes | No ? ")

def return_price(x):
    return x['price']

if to_filter.lower() == 'yes':
    print("""
    1. High to Low
    2. Low to High
""")

    ch = input("Enter your choice : ")
    if ch == "1":
        sorted(results, key=return_price, reverse=True)
    else:
        sorted(results, key=return_price)

    for i in range(len(results)):
        print("Name :",results[i]['p_name'])
        print("Brand :",results[i]['brand'])
        print("Price :",results[i]['price'])
        print("*" * 50)







