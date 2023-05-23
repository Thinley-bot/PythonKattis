import re

shopping_list = '"Doughnuts, 4; doughnuts holes, 0.08; glue, 3.4; pencils, 2"'
items = [x.strip() for x in shopping_list.split(';')]

def clean(items):
    cleaned = []
    for item in items:
        price_match = re.search(r'\d+(\.\d+)?', item)
        if price_match:
            price = float(price_match.group())
            if price.is_integer():
                price = int(price)
            cleaned.append(price)
    return cleaned


cleaned_prices = clean(items)

total_cost = sum(cleaned_prices)

print("The total cost is ${:.2f}".format(total_cost))