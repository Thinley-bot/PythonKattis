day = int(input("Enter number of days: "))
product = int(input("Enter number of products: "))

revenue_matrix = []
for i in range(day):
    revenue_row = []
    for j in range(product):
        revenue = int(input(f"Enter revenue for day {i+1} and product {j+1}: "))
        revenue_row.append(revenue)
    revenue_matrix.append(revenue_row)

for i in range(day):
    greatest_revenue = max(revenue_matrix[i])
    print(f"The greatest revenue for day {i+1} is {greatest_revenue}")
        
        
        
    

    
        
        
        
        
