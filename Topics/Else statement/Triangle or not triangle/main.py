angles = [0, 0, 0]
i = 0
while i < 3:
    angles[i] = int(input())
    i += 1
if sum(angles) == 180:
    print("The triangle is valid!")
else:
    print("The triangle is not valid!")
