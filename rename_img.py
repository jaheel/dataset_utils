import os

path_name = r'E:\\dataset\\mahjong\\VOC_mahjong\\JPEGImages\\'
count = os.listdir(path_name)

for index in range(0, len(count)):
    jpg_begin = 0 
    
    k = str(index + jpg_begin)
    other_url = k.zfill(6) # 总共6位,除了数字部分,其余部分用0填充
    
    os.rename(os.path.join(path_name, count[index]), os.path.join(path_name, (other_url + '.jpg')))

    jpg_begin += 1

print("rename successed")