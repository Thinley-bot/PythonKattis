all_grades = []
for _ in range(5):
        all_grades.append(list(map(int,input().split())))
        
sum_grades = []
for grades in all_grades:
    total = sum(grades)
    sum_grades.append(total)

maximum_sum = max(sum_grades)
winner_index = sum_grades.index(maximum_sum)

print(winner_index+1, maximum_sum)

