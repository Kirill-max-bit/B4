def is_two_digit_sum_and_compare_to_a(two_digit_number, a):

    first_digit = two_digit_number // 10
    second_digit = two_digit_number % 10

    digit_sum = first_digit + second_digit

    is_two_digit_sum = 9 < digit_sum < 100

    greater_than_sum = a > digit_sum

    return is_two_digit_sum, greater_than_sum


two_digit_number = 45
a = 50
result = is_two_digit_sum_and_compare_to_a(two_digit_number, a)
print(result)
