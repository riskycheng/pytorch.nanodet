import os
import shutil

path = r'/media/udata/dataset/hand_detection/Annotations_xml'
trainImgDstPath = r'/media/udata/dataset/hand_detection/VOC_handDet/Train/images'
trainAnnotationDstPath = r'/media/udata/dataset/hand_detection/VOC_handDet/Train/Annotations'
valImgDstPath = r'/media/udata/dataset/hand_detection/VOC_handDet/Val/images'
valAnnotationDstPath = r'/media/udata/dataset/hand_detection/VOC_handDet/Val/Annotations'

files = os.listdir(path)
index = 0
for file in files:
    xmlFileName = file
    imgFileName = xmlFileName.replace('.xml', '.png')
    fullXMLSrcPath = os.path.join(path, file)
    fullImgSrcPath = fullXMLSrcPath.replace('Annotations_xml', 'images').replace('.xml', '.png')
    if index % 10 == 0:  # indicating the eval set
        shutil.move(fullXMLSrcPath, os.path.join(valAnnotationDstPath, xmlFileName))
        shutil.move(fullImgSrcPath, os.path.join(valImgDstPath, imgFileName))
    else:  # indicating the training set
        shutil.move(fullXMLSrcPath, os.path.join(trainAnnotationDstPath, xmlFileName))
        shutil.move(fullImgSrcPath, os.path.join(trainImgDstPath, imgFileName))
    print('done for %s' % file)
    index += 1
