n = int(input())

person=0
for i in range(0,n):
    inp=input()
    quality_of_life,no_years=inp.split()
    a = float(quality_of_life)
    b = float(no_years)
    person+=a*b
    print()
print(person)
    