import os
from lxml.etree import Element, SubElement, tostring
import pprint
from xml.dom.minidom import parseString

path = r'/media/udata/dataset/hand_detection/Annotations'
files = os.listdir(path)


class HandEntity:
    left = 0
    right = 0
    top = 0
    bottom = 0

    def __init__(self, left, top, right, bottom):
        self.left = left
        self.top = top
        self.right = right
        self.bottom = bottom


def wrapXML(imageName, imagePath, dstXMLFile, handEntities):
    node_root = Element('annotation')
    node_folder = SubElement(node_root, 'folder')
    node_folder.text = 'AR_Hand'
    node_filename = SubElement(node_root, 'filename')
    node_filename.text = imageName

    node_size = SubElement(node_root, 'size')
    node_width = SubElement(node_size, 'width')
    node_width.text = '1920'

    node_height = SubElement(node_size, 'height')
    node_height.text = '1080'

    node_depth = SubElement(node_size, 'depth')
    node_depth.text = '3'

    for hand in handEntities:
        node_object = SubElement(node_root, 'object')
        node_name = SubElement(node_object, 'name')

        # rename it to others
        node_name.text = 'hand'

        node_difficult = SubElement(node_object, 'difficult')
        node_difficult.text = '0'
        node_bndbox = SubElement(node_object, 'bndbox')
        node_xmin = SubElement(node_bndbox, 'xmin')
        node_xmin.text = str(hand.left)
        node_ymin = SubElement(node_bndbox, 'ymin')
        node_ymin.text = str(hand.top)
        node_xmax = SubElement(node_bndbox, 'xmax')
        node_xmax.text = str(hand.right)
        node_ymax = SubElement(node_bndbox, 'ymax')
        node_ymax.text = str(hand.bottom)

    xml = tostring(node_root, pretty_print=True)
    dom = parseString(xml)
    dataStr = dom.toprettyxml()
    dstFile = open(dstXMLFile, 'w+')
    dstFile.write(dataStr)
    dstFile.close()


for file in files:
    fullPath = os.path.join(path, file)
    fileName = file.replace('.txt', '.png')
    fullImagePath = fullPath.replace('Annotations', 'images').replace('.txt', '.png')
    dstFullPath = fullPath.replace('.txt', '.xml').replace('Annotations', 'Annotations_xml')
    dataFile = open(fullPath)
    hands = []
    for line in dataFile:
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
        hand = HandEntity(left, top, right, bottom)
        hands.append(hand)

    # write into xml file
    wrapXML(fileName, fullImagePath, dstFullPath, hands)