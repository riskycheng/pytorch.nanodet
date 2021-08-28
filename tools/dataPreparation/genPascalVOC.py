# convert the yolo format files into the Pascal mode like : /home/matthew/VOC2007/JPEGImages/000000162.jpg 403,22,458,60,0 400,245,552,389,0
import os
path = r'/home/jian/Documents/dataset/hand_detection/labels'
imagePath = r'/home/jian/Documents/dataset/hand_detection/images'
files = os.listdir(path)

dataset = []
for file in files:
    fullPath = os.path.join(path, file)
    fileName = file.replace('.txt', '')
    sampleFile = open(fullPath)
    fullImgPath = os.path.join(imagePath, file.replace('.txt', '.png'))
    data = fullImgPath
    # the data format of Pascal is left,top,right,bottom,class-id
    # /home/matthew/VOC2007/JPEGImages/000000162.jpg 403,22,458,60,0 400,245,552,389,0
    data += ' '
    for line in sampleFile:
        datas = line.split(' ')
        anchor_x = float(datas[1]) * 1920
        anchor_y = float(datas[2]) * 1080
        width = float(datas[3]) * 1920
        height = float(datas[4]) * 1080
        left = max(0, int(anchor_x - width / 2))
        top = max(0, int(anchor_y - height / 2))
        right = min(1920, int(anchor_x + width / 2))
        bottom = min(1080, int(anchor_y + height / 2))
        clsType = datas[0]
        # write to the tmp data
        data += str(left) + ','
        data += str(top) + ','
        data += str(right) + ','
        data += str(bottom) + ','
        data += clsType + ' '
    # write into the buffer
    dataset.append(data)
    dataset.append('\n')

# write out to final file
dstFile = open(r'/home/jian/Documents/dataset/hand_detection/vocLabels/totalLabels.txt', 'w+')
for data in dataset:
    dstFile.write(data)
dstFile.close()