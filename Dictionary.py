monthly_expense={
    'January':2200,
    'February':2000,
    'March':2600,
    'April':2130,
    'May':2190,
}

extra1=monthly_expense['January']-monthly_expense['February']
print(extra1)

expense_threemonths= monthly_expense['January']+monthly_expense['February']+monthly_expense['March']
print(expense_threemonths)

for i in monthly_expense:
    if monthly_expense[i]==2000:
        print("The month",monthly_expense[i])
    print("Don't have the value")
    
monthly_expense['June']=1980
print(monthly_expense)


refund=monthly_expense['April']-200
print(refund)