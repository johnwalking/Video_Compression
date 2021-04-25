
import numpy as np
import cv2
import os 
import io


class Node(object):
    def __init__(self,name=None,value=None):
        self._name=name
        self._value=value
        self._left=None
        self._right=None

class HuffmanTree():

    #根据Huffman树的思想：以节点为基础，反向建立Huffman树
    def __init__(self,char_weights):
        print(char_weights)
        self.Leav=[ Node(part[0],part[1]) for part in char_weights ]  #根据输入的字符及其频数生成节点
        while len(self.Leav) != 1:    

            self.Leav.sort(key=lambda node:node._value,reverse=True)
            c = Node(value=(self.Leav[-1]._value + self.Leav[-2]._value))
            c._left=self.Leav.pop(-1)
            c._right=self.Leav.pop(-1)
            self.Leav.append(c)
            
        self.root=self.Leav[0]
        self.Buffer=list(range(100)) 
        self.dic = dict()
    def pre(self,tree,length):
        node=tree
        if (not node):
            return
        elif node._name:
            print (str(node._name) + '    encoding:',end=''),
            ans = ""
            for i in range(length):
                print (self.Buffer[i],end='')
                ans += str(self.Buffer[i])
            self.dic[node._name] = ans
            print ('\n')
            return
        self.Buffer[length]=0
        self.pre(node._left,length+1)
        self.Buffer[length]=1
        self.pre(node._right,length+1)
     #生成哈夫曼编码   
    def get_code(self):
        self.pre(self.root,0)
    def return_value(self,value):
        return self.dic[value]

image1 = cv2.imread('foreman_qcif_0_rgb.bmp')
image2 = cv2.imread('foreman_qcif_1_rgb.bmp')
image3 = cv2.imread('foreman_qcif_2_rgb.bmp')

yuv1 = cv2.cvtColor(image1, cv2.COLOR_RGB2YUV_I420)
yuv2 = cv2.cvtColor(image2, cv2.COLOR_RGB2YUV_I420)
yuv3 = cv2.cvtColor(image3, cv2.COLOR_RGB2YUV_I420)

image11 = cv2.cvtColor(yuv3, cv2.COLOR_YUV2RGB_I420)

# calculate number
a = np.count_nonzero(image11<51)
b = np.count_nonzero(image11<102) - a
c = np.count_nonzero(image11<153) - a - b
d = np.count_nonzero(image11<204) - a - b - c
e = np.count_nonzero(image11<255) - a - b - c - d

image11 =  np.where(image11 > 51, image11, 1111)
image11 =  np.where(image11 > 102, image11, 2222)
image11 =  np.where(image11 > 153, image11, 3333)
image11 =  np.where(image11 > 204, image11, 4444)
image11 =  np.where(image11 > 255, image11, 5555)
# print(image11)

#build huffman 
input_dic = list()
input_dic.append([1111,a])
input_dic.append([2222,b])
input_dic.append([3333,c])
input_dic.append([4444,d])
input_dic.append([5555,e])

tree=HuffmanTree(input_dic)
tree.get_code()

image11[image11 == 1111] = tree.return_value(1111)
image11[image11 == 2222] = tree.return_value(2222)
image11[image11 == 3333] = tree.return_value(3333)
image11[image11 == 4444] = tree.return_value(4444)
image11[image11 == 5555] = tree.return_value(5555)

print(image11)
s = "image1 : a= " + str(a) + " b = " + str(b) + " c = " + str(c) + " d = " + str(d) + " e = " + str(e)
print(s)


cv2.imwrite("hw1_3_3.jpg",image11)


cv2.imshow('Input1', image1)
cv2.imshow('Input2', image2)
cv2.imshow('Input3', image3)
cv2.imshow('Result1', yuv1)
cv2.imshow('Result2', yuv2)
cv2.imshow('Result3', yuv3)



cv2.waitKey(1000)
