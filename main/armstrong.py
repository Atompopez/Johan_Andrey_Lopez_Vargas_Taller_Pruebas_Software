def is_armstrong(num):
    if not isinstance(num, int):
        raise TypeError("Input must be integer")
    if num < 0:
        raise ValueError("Negative numbers not allowed")

    digits = str(num)
    power = len(digits)
    total = sum(int(d)**power for d in digits)
    return total == num

