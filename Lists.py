if __name__ == '__main__':
    N = int(input())
    liste = list()
    newList = []
    for i in range(N):
        liste.append(input().split())

    for value in liste:
        if value[0] == 'insert':
            newList.insert(int(value[1]), int(value[2]))
        elif value[0] == 'print':
            print(newList)
        elif value[0] == 'remove':
            newList.remove(int(value[1]))
        elif value[0] == 'append':
            newList.append(int(value[1]))
        elif value[0] == 'sort':
            newList = sorted(newList)
        elif value[0] == 'pop':
            newList.pop()
        elif value[0] == 'reverse':
            newList = newList[::-1]