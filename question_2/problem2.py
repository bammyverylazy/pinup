fs = {}      # root
path = []    # current directory

while True:
    cmd = input().split()

    # cwd
    if cmd[0] == "cwd":
        if path == []:
            print("/")
        else:
            print("/" + "/".join(path))

    # ls
    elif cmd[0] == "ls":
        cur = fs
        for p in path:
            cur = cur[p]
        print(" ".join(sorted(cur.keys())))

    # mkdir
    elif cmd[0] == "mkdir":
        name = cmd[1]
        cur = fs
        for p in path:
            cur = cur[p]
        if name in cur:
            print(name, "already exists")
        else:
            cur[name] = {}

    # touch
    elif cmd[0] == "touch":
        name = cmd[1]
        cur = fs
        for p in path:
            cur = cur[p]
        if name in cur:
            print(name, "already exists")
        else:
            cur[name] = "file"

    # cd
    elif cmd[0] == "cd":
        name = cmd[1]

        if name == "/":
            path = []

        elif name == "..":
            if path == []:
                print("currently at root")
            else:
                path.pop()

        else:
            cur = fs
            for p in path:
                cur = cur[p]

            if name not in cur:
                print(name, "not found")
            elif cur[name] == "file":
                print(name, "is not a directory")
            else:
                path.append(name)

    # exit
    elif cmd[0] == "exit":
        break
