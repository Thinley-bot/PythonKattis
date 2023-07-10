width = int(input())
pieces = int(input())
area = 0

for _ in range(pieces):
    piece_width, piece_length = map(int, input().split())
    area += piece_width * piece_length

print(area // width)
