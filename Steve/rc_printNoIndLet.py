input_string = input()
letters = sorted(set(input_string))
for l in letters:
    print(input_string.count(l)*l)
