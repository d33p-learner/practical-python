# bounce.py
#
# Exercise 1.5
total_bounce = 10
height = 100
for bounce in range(total_bounce):
    height = height * 3 / 5
    height = round(height, 4)
    print(bounce+1, end = ' ')
    print(height)