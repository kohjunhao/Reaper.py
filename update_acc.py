

def update_acc(emoji=None,details=False):

    data = []
    read_handle = open('accuracy.txt')
    for line in read_handle:
        data.append(line.strip())
    read_handle.close()
    check = int(data[0])
    cross = int(data[1])

    if emoji == "\u2705":
        check += 1
    elif emoji == "\u274E":
        cross +=1

    total = round(check*100/(check+cross),1)

    write_handle = open('accuracy.txt','w')
    write_handle.write(str(check)+'\n')
    write_handle.write(str(cross)+'\n')
    write_handle.write(str(total))
    write_handle.close()
    if details:
        return str(check)+'/'+str(cross)
    return total