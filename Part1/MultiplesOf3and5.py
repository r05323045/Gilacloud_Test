def multiple_calculate(num_limit):
    multiples_sum = 0
    for num in range(1, num_limit):
        if num % 3 == 0 or num % 5 == 0:
            multiples_sum += num
    return multiples_sum

if __name__ == '__main__':
    print(multiple_calculate(1000))