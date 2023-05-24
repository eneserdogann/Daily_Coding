def plusOne(digits):
    digits = int(''.join(map(str, digits)))
    digits += 1
    digits = list(str(digits))
    digits = [int(element) for element in digits]
    return digits

digits = [1,2,3]
print(plusOne(digits))