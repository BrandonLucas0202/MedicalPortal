ENC = [95, 91, 68, 33, 67, 83, 73, 91, 48, 62, 35, 45, 53]

def main():
    dec = ''
    rotate = [12, 16, 29]
    count = 0
    for byt in ENC:
        dec += chr(byt ^ rotate[count])
        count = (count + 1) % 3

    print(dec)

if __name__ == '__main__':
    main()