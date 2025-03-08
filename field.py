def draw_field(field: list, crosses: list):
    carriage_return = 0
    for i in range(1,10):
        carriage_return += 1
        if i in field:
            print(i, end = ' ')
        elif i in crosses:
            print("x", end= ' ')
        else:
            print("o", end= ' ')
        if carriage_return == 3:
            print()
            carriage_return = 0