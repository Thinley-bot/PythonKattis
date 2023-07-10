H, M = map(int, input().split())

if 0 <= H <= 23 and 0 <= M <= 59:
    total_minutes = H * 60 + M  # Convert hours to minutes and add the current minutes
    adjusted_minutes = total_minutes - 45

    if adjusted_minutes < 0:
        adjusted_minutes += 24 * 60  # Add 24 hours in minutes if the result is negative
        print(adjusted_minutes)

    adjusted_hours = adjusted_minutes // 60
    adjusted_minutes %= 60

    print(adjusted_hours, adjusted_minutes)