####################
# Lambdas
####################

sum_two_values = lambda first_value, second_value: first_value + second_value
print(sum_two_values(2, 4))

multiply_values = lambda first_value, second_value: first_value * second_value - 3
print(multiply_values(2, 4))


def sum_three_values(value):
    return lambda first_value, second_value: first_value + second_value + value

print(sum_three_values(3)(3,4))


def sum_three_values(value):
    sum_two_values = lambda first_value, second_value: first_value + second_value
    return (value + sum_two_values(4,5))

print(sum_three_values(4))  






