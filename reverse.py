def reverse_chat():
    precontent = []
    content = []

    def read(lines=1):
        string = ''
        for i in range(lines):
            string += f.readline().decode()
        return string

    with open('chat.md', 'rb') as f:
        while True:
            line = read()
            precontent.append(line)
            if '<!-- more -->' in line:
                break
        precontent.append(read())
        content_temp = [i.decode() for i in f.readlines()]
        for i in range(len(content_temp) - 1, -1, -1):
            if content_temp[i] == '\r\n' or content_temp[i] == '\n':
                content_temp.pop()
            else:
                content_temp.append('\r\n')
                break
        i = 0
        while i < len(content_temp):
            if '##' in content_temp[i]:
                month = content_temp[i]
                i += 1
                day = []
                while i < len(content_temp) and '##' not in content_temp[i]:
                    day.append(content_temp[i])
                    i += 1
                content.append([month, day])

    with open('chat.md', 'wb') as f:
        for i in precontent:
            f.write(bytes(i.encode()))
        content.reverse()
        for i in content:
            f.write(bytes(i[0].encode()))
            i[1].reverse()
            for j in i[1]:
                f.write(bytes(j.encode()))
