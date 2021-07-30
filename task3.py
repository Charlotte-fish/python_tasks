from pathlib import Path
import struct
file_features={
    "b'\\xff\\xd8'":".jpg",
    "b'\\x89P'":".png",
    "b'BM'":".bmp",
    "b'%P'":".pdf",
    "b'PK'":".docx",
    "b'PK1'":".pptx",
    "b'MZ'":".exe"
}
# print(file_features["b'PK'"])
bm_list=list()
root = input('请输入你要遍历的目录: ')
files = Path(root).glob('**/*')
# print(files)

normal_dir =input('请输入正常文件存储的目录: ')
Path(normal_dir).mkdir(exist_ok=True)

malicious_dir =input('请输入异常文件存储的目录: ')
Path(malicious_dir).mkdir(exist_ok=True)
for file in files:
    # print(file)
    # print(Path(file))
    # print(type(Path(file)))
    # print(Path(file).suffix)
    if Path(file).is_file():
        # print(Path(normal_dir)/Path(file).name)
        with open(file,'rb') as f:
            features=f.read(2)
            bm = struct.unpack('<2s', features)
            # print(bm)
            # print(type(bm))
            # print(type(bm[0]))
            # test=str(bm[0])
            # print(test)
            # print(type(test))
        #     bm_list.append(str(bm[0]))
        # print(bm_list)
        if(str(bm[0])=="b'PK'"):
            if(file_features["b'PK'"]==Path(file).suffix or file_features["b'PK1'"]==Path(file).suffix):
                filename=Path(normal_dir)/Path(file).name
                # print(filename)
                Path(file).rename(filename)
            else:
                filename=Path(malicious_dir)/Path(file).name
                Path(file).rename(filename)
        else:
            if(file_features[str(bm[0])]==Path(file).suffix):
                filename=Path(normal_dir)/Path(file).name
                Path(file).rename(filename)
            else:
                filename=Path(malicious_dir)/Path(file).name
                Path(file).rename(filename) 

#注：使用rename时路径需在同一磁盘，否则会报错