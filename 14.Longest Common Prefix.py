strs = ["flower", "flow", "flight"]

def long1(strs):
    temp = ""
    for i in range(len(strs[0])):
        for j in strs:
            if i == len(j) or j[i] != strs[0][i]:
                return temp
        temp += strs[0][i]

    return temp

result = long1(strs)
print(result)

def optimal(strs):
    temp2 = ""
    strs = sorted(strs)
    first = strs[0]
    last = strs[-1]
    for i in range(min(len(first), len(last))):
        if (first[i] != last[i]):
            return temp2
        temp2 += first[i]
    return temp2

optimal = optimal(strs)
print(optimal)