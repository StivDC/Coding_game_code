# Takes number as a string, returns sum of digits
# "123" => 6 because 1 + 2 + 3 = 6
def sum_of_digits(n):
    return sum(int(x)for x in n if x.isdigit())
