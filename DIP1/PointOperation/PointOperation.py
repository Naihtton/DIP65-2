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

def main():
    with open('DIP1/PointOperation/SEM256_256.pgm', 'rb') as stream_in, open('DIP1/PointOperation/SEM256_256_improved.pgm', 'wb') as stream_out:
        next(stream_in)
        row = int(next(stream_in))
        col = int(next(stream_in))
        max_val = int(next(stream_in))

        image = [[0] * col for _ in range(row)]
        HA = [0] * (max_val + 1)
        PA = [0] * (max_val + 1)
        DA = [0] * (max_val + 1)
        DP = [0] * (max_val + 1)
        DB = [0] * (max_val + 1)

        for i in range(row):
            for j in range(col):
                p = int.from_bytes(stream_in.read(1), byteorder='big')
                image[i][j] = p
                DA[p] += 1

        for i in range(max_val + 1):
            HA[i] = DA[i] / (row * col)
            if i == 0:
                PA[i] = HA[i]
            else:
                PA[i] = PA[i - 1] + HA[i]
            DP[i] = max_val * PA[i]
            DB[i] = round(DP[i])

        for i in range(max_val + 1):
            print(f"{i} {DA[i]} {HA[i]} {PA[i]} {DP[i]} {DB[i]}")

        stream_out.write("P5\n".encode())
        stream_out.write(f"{col} {row}\n".encode())
        stream_out.write(f"{max_val}\n".encode())
        for i in range(row):
            for j in range(col):
                p = image[i][j]
                image[i][j] = DB[p]
                stream_out.write(bytes([image[i][j]]))

if __name__ == '__main__':
    main()
