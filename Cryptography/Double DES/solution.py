import binascii
#nc mercury.picoctf.net 33425

#flag after nc 228f7939b7a283033e780bf2d5486a44b892cd101227216aff241cd6e31a561caccf6cbdd92c3711


flag_hex_string = '228f7939b7a283033e780bf2d5486a44b892cd101227216aff241cd6e31a561caccf6cbdd92c3711'

for i in range(len(flag_hex_string) -1):
    int_char = int('0x'+flag_hex_string[i:i+2],16)
    print(chr(int_char),end='')



res = binascii.unhexlify(flag_hex_string.rstrip()).decode()

print(res)

