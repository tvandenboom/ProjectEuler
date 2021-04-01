def ones(n):
    if n == 0:
        return ''
    if n == 1:
        return 'one'
    if n == 2:
        return 'two'
    if n == 3:
        return 'three'
    if n == 4:
        return 'four'
    if n == 5:
        return 'five'
    if n == 6:
        return 'six'
    if n == 7:
        return 'seven'
    if n == 8:
        return 'eight'
    if n == 9:
        return 'nine'
    else:
        return 'invalid integer'

def tens(n):
    if n == 2:
        return 'twenty'
    if n == 3:
        return 'thirty'
    if n == 4:
        return 'forty'
    if n == 5:
        return 'fifty'
    if n == 6:
        return 'sixty'
    if n == 7:
        return 'seventy'
    if n == 8:
        return 'eighty'
    if n == 9:
        return 'ninety'
    else:
        return 'invalid integer'

sum_one_to_nine = 36

sum_ten_to_nineteen = 70

sum_twenty_to_ninetynine = 0


for i in range(2,10):
    for j in range(0,10):
        i_word = tens(i) + ones(j)
        print(i_word)
        sum_twenty_to_ninetynine += len(i_word)

sum_one_to_ninetynine = sum_one_to_nine + sum_ten_to_nineteen + sum_twenty_to_ninetynine

print(sum_one_to_ninetynine)
