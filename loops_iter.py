#Two important keyword are break and continue(move on next iteration)
nums=[1,2,3,4,5]

for num in nums:
    if num==3:
        print("Found")
        # break
        continue
    print(num)