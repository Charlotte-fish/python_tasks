
#编码
base='ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/'
inputStr=input('请输入一个字符串：')
outputStr=''
binary='' #存储输入字符串对应的拼接二进制串
for item in inputStr:
    asciiNum=ord(item) #字符转换成ascii码
    # print(asciiNum)
    binStr=bin(asciiNum) #acill码转换成二进制
    # print(binStr)
    binStr=binStr[2:]
    if len(binStr)<8:
        zeroCount=8-len(binStr) #二进制串少于八位补零个数
        for i in range(zeroCount):
            binStr = '0'+binStr #补零后的八位二进制串
        # print(binStr)
        binary += binStr #将每个字符的八位二进制串拼接起来
    else:
        binary += binStr
# print(binary)
for j in range(0,len(binary),6):
    index=int('0b'+binary[j:j+6],base=2) #取六位二进制串转十进制作为索引
    # print(index)
    outputStr += base[index:index+1] #索引查base编码
print(outputStr)

#解码
# base='ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/'
# baseList=list(base)
# # print(baseList)
# inputStr=input('请输入一个Base64编码：')
# outputStr=''
# binary=''
# for item in inputStr:
#     index=baseList.index(item)
#     # print(index)
#     binStr=bin(index)
#     # print(binStr)
#     binStr=binStr[2:]
#     if len(binStr)<6:
#         zeroCount=6-len(binStr) 
#         for i in range(zeroCount):
#             binStr = '0'+binStr
#         # print(binStr)
#         binary += binStr 
#     else:
#         binary += binStr
# # print(binary)
# for j in range(0,len(binary),8):
#     asciiNum=int('0b'+binary[j:j+8],base=2)
#     # print(asciiNum)
#     str=chr(asciiNum)
#     # print(str)
#     outputStr += str
# print(outputStr)