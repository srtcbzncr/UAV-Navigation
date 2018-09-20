import cv2
import numpy
from matplotlib import pyplot as plt

map1 = cv2.imread('harita.png')
image = cv2.imread('6.png')

averageB = numpy.ndarray(shape = (11,29))
averageG = numpy.ndarray(shape = (11,29))
averageR = numpy.ndarray(shape = (11,29))

def AnalyseMap(img):
    totalB = 0
    totalG = 0
    totalR = 0
    x = 0
    y = 0
    for a in range(1,320):
        for i in range(0,45):
            for j in range(0,45):
                totalB = totalB + img[(x*45)+i][(y*45)+j][0]
                totalG = totalG + img[(x*45)+i][(y*45)+j][1]
                totalR = totalR + img[(x*45)+i][(y*45)+j][2]
        averageB[x][y] = totalB / (45 * 45)
        averageG[x][y] = totalG / (45 * 45)
        averageR[x][y] = totalR / (45 * 45)
        totalB = 0
        totalG = 0
        totalR = 0
        y = y + 1
        if a % 29 == 0:
            y = 0
            x = x+1

def AnalyseImage(img):
    x = 0
    y = 0
    totB = 0
    totG = 0
    totR = 0
    avB = 0
    avG = 0
    avR = 0
    while(True):
        for i in range(x,45+x):
            for j in range(y,45+y):
                totB = totB + img[i][j][0]
                totG = totG + img[i][j][1]
                totR = totR + img[i][j][2]
        avB = totB / (45 * 45)
        avG = totG / (45 * 45)
        avR = totR / (45 * 45)
        for a in range(0,11):
            for b in range(0,29):
                if avB == averageB[a][b] and avG == averageG[a][b] and avR == averageR[a][b]:
                    return [(a*45)+45, (b*45)+45]
        y = y + 1
        if y % 44 == 0:
            x = x + 1
            y = 0  
        totB = 0
        totG = 0
        totR = 0
        avB = 0
        avG = 0
        avR = 0

def DrawCircle(xCoordinate, yCoordinate, img):
    circle_img = cv2.circle(img,(yCoordinate,xCoordinate), 30, (0,0,255), -1)
    cv2.imshow("Lokasyon bulundu.", circle_img)
        
AnalyseMap(map1)
coordinates = AnalyseImage(image)
DrawCircle(coordinates[0], coordinates[1], map1)
