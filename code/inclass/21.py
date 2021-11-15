from os import EX_PROTOCOL


def readlines(fname):
    try:
        with open(fname, 'r') as fpt:
            return fpt.readlines()
    except:
        return []
































def convert(data):
    for i in range(len(data)):
        try:
            data[i] = float(data[i])
        except ValueError:
            continue

def csv_lst(fname):
    l = readlines(fname)
    if len(l) == 0:
        raise Exception('Missing file')
    output = []
    for i in l[1:]:
        data = i.split(',')
        convert(data)
        output.append(data)
    return output

dd = csv_lst('titanic.csv')

sur = 0
for x in dd:
    sur += x[0]
print(sur)
