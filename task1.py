#生成器逻辑
# confession='Jony J and xy'
# message=''
# for char in confession:
#     #ord根据ASCII表将字符转换成十进制数字
#     number=ord(char)
#     #hex将十进制数字转换成十六进制数字
#     message += hex(number)[2:]
# print(message)

#生成器破解
message='4a6f6e79204a20616e64207879'
confession=''
for i in range(0,len(message),2):
    hex_num=message[i:i+2]
    num=int('0x'+hex_num,base=16)
    confession += chr(num)
print(confession)