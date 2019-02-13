def add(lower_bound, upper_bound):
    a = 0
    for i in range(upper_bound-lower_bound + 1):
        a += i + 1
    return a
print(add(int(input('Enter Lower bound: ')), int(input('Enter upper bound: '))))