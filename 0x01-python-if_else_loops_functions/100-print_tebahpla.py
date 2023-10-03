j = 0
for i in range(122, 96, -1):
    if j % 2 == 0:
        print("{}".format(chr(i)), end="")
        j += 1
        continue
    else:
        print("{}".format(chr(i).upper()), end="")
        j += 1
