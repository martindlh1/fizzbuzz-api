def generate_fizzbuzz(fizz_nb, buzz_nb, start, end):
    result = []
    for i in range(start, end + 1):
        if i % fizz_nb == 0 and i % buzz_nb == 0:
            result.append("fizzbuzz")
        elif i % fizz_nb == 0:
            result.append("fizz")
        elif i % buzz_nb == 0:
            result.append("buzz")
        else:
            result.append(str(i))
    return result
