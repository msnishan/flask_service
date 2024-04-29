from functools import reduce

fruit_price = {'apple': 100, 'orange': 40, 'banana': 20}
print(fruit_price)
fruit_price['orange'] = 45
print(fruit_price)
del (fruit_price['banana'])
print(fruit_price)
fruit_price['banana'] = 25
print(fruit_price.keys())
print(fruit_price.values())
items = fruit_price.items()
for i in items:
    print(f"key : {i[0]} and val: {i[1]}")
new_dict = {key: val for (key, val) in fruit_price.items()}
print(new_dict)
new_price = {key: val * 2 for (key, val) in fruit_price.items()}
print(new_price)

# using lambda

new_price_vals = list(map(lambda x: x * 3, fruit_price.values()))
print(new_price_vals)
new_price_lambda = dict(zip(fruit_price.keys(), new_price_vals))
print(new_price_lambda)

# Dictionary Comprehension with condition
new_price_greater_than_75 = {key: val for (key, val) in new_price_lambda.items() if val > 75}
print(new_price_greater_than_75)
new_price_mapping = {key: ('high' if val > 75 else 'low') for (key, val) in new_price_lambda.items()}
print(new_price_mapping)

# array operations

fruits = ['apple', 'orange', 'mango', 'tomato']
fruits_filter = [x for x in fruits if x.startswith('a') or x.startswith('t')]
print(fruits_filter)
fruits_double = [x * 2 for x in fruits]
print(fruits_double)

fruits_double_lambda = list(map(lambda x: x * 2, fruits))
print(fruits_double_lambda)

fruits_double_lambda_set = set(map(lambda x: x * 2, fruits))
print(fruits_double_lambda_set)

all_fruits = reduce(lambda x, y: x + ' ' + y, fruits)
print(all_fruits)
