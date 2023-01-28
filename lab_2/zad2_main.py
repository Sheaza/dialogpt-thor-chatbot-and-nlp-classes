first_dot = [a**2 for a in range(51)]
print(first_dot)
second_dot = [a**3 for a in range(20, 31)]
print(second_dot)
third_dot = [(3*x-2) for x in range(-5, 6)]
print(third_dot)
fourth_dot = [(x, y) for x, y in zip(range(10, 21), range(5, 11))]
print(fourth_dot)
fifth_dot = [(x ,y) for x, y in zip(range(4, 8), ['jablko', 'gruszka', 'komputer'])]
print(fifth_dot)
