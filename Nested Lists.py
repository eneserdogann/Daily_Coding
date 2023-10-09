if __name__ == '__main__':
    newDict = dict()
    seconds = list()
    for _ in range(int(input())):
        name = input()
        score = float(input())

        newDict[name] = score

    newSet = set(newDict.values())
    newSet = sorted(newSet, reverse=True)
    second = newSet[-2]

    for key, value in newDict.items():
        if value == second:
            seconds.append(key)

    seconds = sorted(seconds)

    for i in seconds:
        print(i)