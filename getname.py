def get_name(line):
    line = line.split(':')
    return line[4]

with open("data/passwd.txt", 'r') as f:
    line = ' '
    while line:
        line = f.readline()
        if line:
            name = get_name(line)
            print(name)