divisor = int(input())
boundary = int(input())
largest_multiple = boundary
while True:

    if largest_multiple % divisor == 0 and boundary >= largest_multiple > 0:
        print(largest_multiple)
        break
    else:
        largest_multiple -= 1



