import math

def next(stream):
    bytes = []
    while True:
        b = stream.read(1)
        if b != b'':
            c = b.decode('utf-8')
            if c == '#':
                while True:
                    d = stream.read(1)
                    if d == b'' or d == b'\n' or d == b'\r':
                        break
            elif not c.isspace():
                bytes.append(b)
            elif len(bytes) > 0:
                break
        else:
            break
    return b''.join(bytes).decode('utf-8')

def pqmoment(p, q, image):
    m = 0
    row, col = len(image), len(image[0])
    for x in range(row):
        for y in range(col):
            if image[x][y] > 0:
                m += math.pow(x, p) * math.pow(y, q) * 1
            else:
                m += 0
    return m

def pqHu(p, q, image):
    u = 0
    row, col = len(image), len(image[0])
    m10 = pqmoment(1, 0, image)
    m00 = pqmoment(0, 0, image)
    m01 = pqmoment(0, 1, image)
    for x in range(row):
        for y in range(col):
            if image[x][y] > 0:
                u += math.pow((x - (m10 / m00)), p) * math.pow((y - (m01 / m00)), q)
            else:
                u += 0
    return u

def pqN(p, q, image):
    n = 0
    row, col = len(image), len(image[0])
    n = pqHu(p, q, image) / math.pow(pqHu(0, 0, image), ((p + q / 2) + 1))
    return n

if __name__ == '__main__':
    with open('DIP1/HistrogramAndObjectMoment/scaled_shapes.pgm', 'rb') as stream_in:
        next(stream_in)
        row = int(next(stream_in))
        col = int(next(stream_in))
        max_val = int(next(stream_in))

        image = [[0] * col for _ in range(row)]
        D = [0] * (max_val + 1)
        q = []

        for i in range(row):
            for j in range(col):
                p = int.from_bytes(stream_in.read(1), byteorder='big')
                image[i][j] = p
                D[p] += 1


        for i in range(max_val):
            if D[i] > 1000:
                if not q:
                    print('Gray level of Object in the image (1) = ' + str(i))
                else:
                    print('Gray level of Object in the image (' + str(len(q)+1) + ') = ' + str(i))
                q.append(i)

        q = sorted(q, key=lambda x: x == 0, reverse=True)
        print('# of all Object =', len(q))
        for removedele in q:
            m = [[0] * col for _ in range(row)]
            for i in range(row):
                for j in range(col):
                    if image[i][j] == removedele:
                        m[i][j] = 1
            theata = pqN(2, 0, m) + pqN(0, 2, m)
            print('moment of an object Gray level (' + str(removedele) + ') = ' + str(theata))




