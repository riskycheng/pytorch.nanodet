import os
train_percentage = 0.9
val_percentage = 0.1
rootPath = r'/home/jian/Documents/dataset/hand_detection/vocLabels'

totalFile = open(os.path.join(rootPath, 'totalLabels.txt'))
trainFile = open(os.path.join(rootPath, 'trainLabels.txt'), 'w+')
evalFile = open(os.path.join(rootPath, 'evalLabels.txt'), 'w+')

index = 0
for line in totalFile:
    if index % 10 == 0:
        evalFile.write(line)
    else:
        trainFile.write(line)
    index += 1
evalFile.close()
trainFile.close()

