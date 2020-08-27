def sum_of_power_result(n):
    """The function raises 2 to the power of the input
    and sum the digits of the result."""
    return sum([int(item) for item in str(2**n)])

print(sum_of_power_result(1000))
