import io

def main():
    with open("SanFranPeak_red.pgm", "rb") as stream_in1, \
         open("SanFranPeak_green.pgm", "rb") as stream_in2, \
         open("SanFranPeak_blue.pgm", "rb") as stream_in3, \
         open("2grb.pgm", "wb") as stream_out1, \
         open("rb.pgm", "wb") as stream_out2, \
         open("rgb_3.pgm", "wb") as stream_out3:

            next_line(stream_in1)
            col = int(next_line(stream_in1))
            row = int(next_line(stream_in1))
            next_line(stream_in1)

            for _ in range(4):
                next_line(stream_in2)
                next_line(stream_in3)

            imageR = [[0 for _ in range(col)] for _ in range(row)]
            imageG = [[0 for _ in range(col)] for _ in range(row)]
            imageB = [[0 for _ in range(col)] for _ in range(row)]
            image1 = [[0 for _ in range(col)] for _ in range(row)]
            image2 = [[0 for _ in range(col)] for _ in range(row)]
            image3 = [[0 for _ in range(col)] for _ in range(row)]

            for i in range(row):
                for j in range(col):
                    p1 = stream_in1.read(1)[0]
                    imageR[i][j] = p1
                    p2 = stream_in2.read(1)[0]
                    imageG[i][j] = p2
                    p3 = stream_in3.read(1)[0]
                    imageB[i][j] = p3

                    equl1 = 2 * p2 - p1 - p3
                    equl1 = min(max(equl1, 0), 255)
                    image1[i][j] = equl1

                    equl2 = p1 - p3
                    equl2 = min(max(equl2, 0), 255)
                    image2[i][j] = equl2

                    equl3 = (p1 + p2 + p3) // 3
                    equl3 = min(max(equl3, 0), 255)
                    image3[i][j] = equl3

            write(image1, stream_out1)
            write(image2, stream_out2)
            write(image3, stream_out3)


def next_line(stream):
    line_bytes = bytearray()
    while True:
        b = stream.read(1)[0]
        if b == ord('#'):
            while b not in (ord('\n'), ord('\r'), -1):
                b = stream.read(1)[0]
        elif not isspace(b):
            line_bytes.append(b)
        elif line_bytes:
            break
    return line_bytes.decode('ascii')


def write(image, stream):
    stream.write(b'P5\n')
    stream.write(str(image[0].__len__()).encode('ascii'))
    stream.write(b' ')
    stream.write(str(image.__len__()).encode('ascii'))
    stream.write(b'\n255\n')

    for row in image:
        stream.write(bytes(row))

    stream.close()


def isspace(b):
    return chr(b).isspace()


if __name__ == '__main__':
    main()
