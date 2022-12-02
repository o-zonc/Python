hunmin = open("d:\Python\EngineeringInformationProcessing\lab\서문.txt", "r", encoding="utf-8")
EOF = ''
line = hunmin.readline()
while line != EOF:
    print(line)
    line = hunmin.readline()
hunmin.close()