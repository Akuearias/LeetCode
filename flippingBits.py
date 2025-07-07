def flippingBits(n):
    bin_str = bin(n)[2:].zfill(32)
    new_bin = ""
    for i in range(32):
        if bin_str[i] == '0':
            new_bin += '1'
        else:
            new_bin += '0'
    return int(new_bin, 2)
