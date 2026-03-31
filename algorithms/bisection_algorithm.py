def square_root_bisection(number, tolerance=1e-7, maximum=100):
    if number < 0:
        raise ValueError("Square root of negative number is not defined in real numbers")

    if number == 0 or number == 1:
        print(f"The square root of {number} is {number}")
        return number

    low = 0
    high = max(1, number)

    for _ in range(maximum):
        mid = (low + high) / 2

        if high - low <= tolerance:
            print(f"The square root of {number} is approximately {mid}")
            return mid

        if mid * mid < number:
            low = mid
        else:
            high = mid

    print(f"Failed to converge within {maximum} iterations")
    return None