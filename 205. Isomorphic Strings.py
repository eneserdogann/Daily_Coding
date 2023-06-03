s = "egg"
t = "add"

def isIsomorphic(s, t):
    if len(set(s)) != len(set(t)):
        return False
    hash_map = {}
    for char in range(len(t)):
        if t[char] not in hash_map:
            hash_map[t[char]] = s[char]
        elif hash_map[t[char]] != s[char]:
            return False
    return True

print(isIsomorphic(s,t))