def lengthOfLastWord(s):
    s = s.strip(' ')
    s = s.split(' ')
    return len(s[(len(s) - 1)])

s = "   fly me   to   the moon  "
print(lengthOfLastWord(s))