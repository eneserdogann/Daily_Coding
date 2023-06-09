letters = ["c","f","j"]
target = "k"

def nextGreatestLetter(letters, target):
    min = max(letters)
    for i in letters:
        if ord(i) > ord(target):
            if ord(min) > ord(i):
                min = i
    if ord(max(letters)) == ord(target) or ord(min) < ord(target):
        min = letters[0]

    return min

print(nextGreatestLetter(letters, target))

