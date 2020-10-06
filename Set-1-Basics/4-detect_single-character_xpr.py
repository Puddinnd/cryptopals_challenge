import sys
character = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.!\',?\n "

def onexor(c, string):
    tmp = ""
    for s in string:
        tmp += chr(c ^ ord(s))
    return tmp

def check (s):
    for i in s:
        if not i in character:
            return False
    return True

with open("./src/4.txt") as f:
    for line in f:
        line = line.strip("\n")
        if len(line) != 60:
            continue
        for i in range(1, 128):
                try:
                    tmp = onexor(i, bytes.fromhex(line).decode('utf-8'))
                    if check(tmp):
                        print(bytes.fromhex(tmp).decode('utf-8'))
                except:
                    continue