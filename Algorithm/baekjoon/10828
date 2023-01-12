n = int(input())
arr = []
for i in range(n):
    command = input()
    if command[:4] == "push":
        arr.append(int(command.split()[1]))
    elif command == "pop":
        if len(arr) < 1:
            print(-1)
        else:
            arr.pop()
    elif command == "size":
        print(len(arr))
    elif command == "empty":
        if len(arr) < 1:
            print(1)
        else:
            print(0)
    elif command == "top":
        if len(arr) < 1:
            print(-1)
        else:
            print(arr[-1])