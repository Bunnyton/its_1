values1 = [ 109,  112,  115,  117,  117,  112,  111,  112,  112,  110,  110,  109,  108,  108,  107,  107]
values2 = [ 12,  11,  10, 8, 7, 7, 6, 6,  13,  16,  17,  17,  15,  17,  18,  17]

d = "01001000010001010100110001010000"

code_4b3t = [{
            "0000": [ 0, -1,  1],
            "0001": [-1,  1,  0],
            "0010": [-1,  0,  1],
            "0011": [ 1, -1,  1],
            "0100": [ 0,  1,  1],
            "0101": [ 0,  1,  0],
            "0110": [ 0,  0,  1],
            "0111": [-1,  1,  1],
            "1000": [ 0,  1, -1],
            "1001": [ 1, -1,  0],
            "1010": [ 1,  0, -1],
            "1011": [ 1,  0,  0],
            "1100": [ 1,  0,  1],
            "1101": [ 1,  1,  0],
            "1110": [ 1,  1, -1],
            "1111": [ 1,  1,  1]
                                    },
         {
             "0000": [ 0, -1,  1],
             "0001": [-1,  1,  0],
             "0010": [-1,  0,  1],
             "0011": [-1,  1, -1],
             "0100": [ 0, -1, -1],
             "0101": [ 0, -1,  0],
             "0110": [ 0,  0, -1],
             "0111": [ 1, -1, -1],
             "1000": [ 0,  1, -1],
             "1001": [ 1, -1,  0],
             "1010": [ 1,  0, -1],
             "1011": [-1,  0,  0],
             "1100": [-1,  0, -1],
             "1101": [-1, -1,  0],
             "1110": [-1, -1,  1],
             "1111": [-1, -1, -1]
         }]

code_fomot = [{
            "0000": [-1, +1, +1],
            "0001": [-1, +1,  0],
            "0010": [+1, -1,  0],
            "0011": [+1,  0,  0],
            "0100": [-1,  0, +1],
            "0101": [+1, +1, +1],
            "0110": [+1,  0, +1],
            "0111": [+1,  0, -1],
            "1000": [ 0, +1, +1],
            "1001": [ 0, +1,  0],
            "1010": [+1, -1, +1],
            "1011": [+1, +1,  0],
            "1100": [ 0,  0, +1],
            "1101": [ 0, +1, -1],
            "1110": [ 0, -1, +1],
            "1111": [+1, +1, -1]
    }, {
            "0000": [-1,  0,  0],
            "0001": [-1, +1,  0],
            "0010": [+1,  -1, 0],
            "0011": [+1, -1, -1],
            "0100": [-1,  0, +1],
            "0101": [-1, +1, -1],
            "0110": [+1,  0, +1],
            "0111": [+1,  0, -1],
            "1000": [ 0, +1, +1],
            "1001": [ 0, -1,  0],
            "1010": [+1, -1, +1],
            "1011": [+1, +1,  0],
            "1100": [-1, -1, +1],
            "1101": [ 0, +1, -1],
            "1110": [ 0, -1, +1],
            "1111": [ 0,  0, -1]
    }, {
            "0000": [-1, +1, +1],
            "0001": [-1, +1,  0],
            "0010": [+1, -1,  0],
            "0011": [+1,  0,  0],
            "0100": [-1,  0, +1],
            "0101": [-1, +1, -1],
            "0110": [-1,  0, -1],
            "0111": [+1,  0, -1],
            "1000": [-1, -1,  0],
            "1001": [ 0, +1,  0],
            "1010": [+1, -1, +1],
            "1011": [ 0, -1, -1],
            "1100": [ 0,  0, +1],
            "1101": [ 0, +1, -1],
            "1110": [ 0, -1, +1],
            "1111": [+1, +1, -1]
    }, {
            "0000": [-1,  0,  0],
            "0001": [-1, +1,  0],
            "0010": [+1, -1,  0],
            "0011": [+1, -1, -1],
            "0100": [-1,  0, +1],
            "0101": [-1, +1, -1],
            "0110": [-1,  0, -1],
            "0111": [+1,  0, -1],
            "1000": [-1, -1,  0],
            "1001": [ 0, -1,  0],
            "1010": [-1, -1, +1],
            "1011": [ 0, -1, -1],
            "1100": [-1, -1, +1],
            "1101": [ 0, +1, -1],
            "1110": [ 0, -1, +1],
            "1111": [ 0,  0, -1]
    }
                                    ]

def to_byte_sequence(val):
    bytes = list()
    for _ in range(8):
        bytes.append(str(val % 2))
        val //= 2
    return "".join(bytes)[::-1]


def to_byte_arr(values):
    byte_arr = list()
    for val in values:
        byte_arr.append(to_byte_sequence(val))
    return byte_arr


def print_byte(byte):
    for bit in byte:
        if bit == '1':
            print('#', end='')
        else:
            print('_', end='')


def print_byte_sequence(byteseq):
    for byte in byteseq:
        print_byte(byte)
    print(end="|")


def print_bytes_arr(bytes_arr, count_in_str=4):
    count = 0
    for bs in bytes_arr:
        print_byte_sequence(bs)

        count += 1
        if count % count_in_str == 0:
            print()


def multiplex(byte_arr1, byte_arr2, d="00000000000000000000000000000000"):
    d_count = 0
    b_count = 0

    mult_byte_arr = list()
    for _ in range(len(byte_arr1)):
        mult_byte_arr.append(byte_arr1[b_count])
        mult_byte_arr.append(d[d_count])

        mult_byte_arr.append(byte_arr2[b_count])
        mult_byte_arr.append(d[d_count + 1])

        b_count += 1
        d_count += 2
    return mult_byte_arr


def to_4b3t(byte_arr):
    byte_str = "".join(byte_arr)

    res_arr_keys = list()
    res_arr_values = list()
    summ = 0
    for i in range(len(byte_str)//4):
        res_arr_keys.append(byte_str[i * 4: (i + 1) * 4])

        if summ <= 0:
            res_arr_values.append(code_4b3t[0]
                                  [res_arr_keys[-1]])
        else:
            res_arr_values.append(code_4b3t[1]
                                  [res_arr_keys[-1]])
        summ += sum(res_arr_values[-1])

    return res_arr_keys, res_arr_values


def to_fomot(byte_arr):
    byte_str = "".join(byte_arr)

    res_arr_keys = list()
    res_arr_values = list()
    summ = 0
    for i in range(len(byte_str)//4):
        res_arr_keys.append(byte_str[i * 4: (i + 1) * 4])

        res_arr_values.append(code_fomot[summ + 1]
                                  [res_arr_keys[-1]])

        summ += sum(res_arr_values[-1])

    return res_arr_keys, res_arr_values


def print_triple(arr, arr_str, count_in_str=9):
    for i in range(len(arr_str)//count_in_str):
        for j in range(count_in_str):
            print("".join([arr[count_in_str * i + j], "  "]), end="")
        print()

        for j in range(count_in_str):
            for k in range(3):
                if arr_str[i * count_in_str + j][k] == 1:
                    print("#", end=" ")
                else:
                    print(" ", end=" ")
            print("\b", end="|")
        print()

        for _ in range(count_in_str):
            for k in range(3):
                print("-", end=" ")
            print("\b", end="|")
        print()

        for j in range(count_in_str):
            for k in range(3):
                if arr_str[i * count_in_str + j][k] == -1:
                    print("#", end=" ")
                else:
                    print(" ", end=" ")
            print("\b", end="|")
        print("\n")




bytes_arr1 = to_byte_arr(values1)
bytes_arr2 = to_byte_arr(values2)

print("task1:")
print_bytes_arr(bytes_arr1)

print("\ntask2:")
mult_arr = multiplex(bytes_arr1, bytes_arr2, d)
print_bytes_arr(mult_arr, 8)

print("\ntask3 (4b3t):")
code_4b3t_arr, code_4b3t_arr_str = to_4b3t(mult_arr)
print_triple(code_4b3t_arr, code_4b3t_arr_str)

print("\ntask4 (fomot):")
code_fomot_arr, code_fomot_arr_str = to_fomot(mult_arr)
print_triple(code_fomot_arr, code_fomot_arr_str)
