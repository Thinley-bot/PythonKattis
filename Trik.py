moves = input()

ball_position = 1  # Start with the ball under the leftmost cup

for move in moves:
    if move == 'A':
        if ball_position == 1:
            ball_position = 2
        elif ball_position == 2:
            ball_position = 1
    elif move == 'B':
        if ball_position == 2:
            ball_position = 3
        elif ball_position == 3:
            ball_position = 2
    elif move == 'C':
        if ball_position == 1:
            ball_position = 3
        elif ball_position == 3:
            ball_position = 1

print(ball_position)