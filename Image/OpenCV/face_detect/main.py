# 2018-9-7
import os
import sys
import cv2
import numpy as np

def readFace(file, sz=None):
    """
    file: tag标签 face/xx/13.pgm 0
    X：存储图像数组
    y: 存储标签
    """
    X,y = [], []
    f = open(file)
    data = f.readlines()
    for l in data:
        if not l: continue

        line = l.split(" ")
        img = cv2.imread(line[0], cv2.IMREAD_GRAYSCALE)

        X.append(np.asarray(img, dtype=np.uint8))
        y.append(line[1])

    return [X, y]



def faceDetect(train):

    # 读取标签姓名
    n = open("labels.txt")
    da = n.readlines()
    name = []
    for i in da:
        name.append(i[:-1])
    print(name)
    [X,y] = readFace(train)
    y = np.asarray(y, dtype=np.int32) # print的输出与原y一样

    # model = cv2.face.FisherFaceRecognizer_create()
    # model = cv2.face.createEigenFaceRecognizer()
    model = cv2.face.LBPHFaceRecognizer_create()
    model.train(np.asarray(X), y)

    camera = cv2.VideoCapture(0)
    face = cv2.CascadeClassifier("data/haarcascade_frontalface_default.xml")

    while True:
        ret, frame = camera.read()
        faces = face.detectMultiScale(frame, 1.3, 5)

        for x,y,w,h in faces:
            img = cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)
            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

            f = gray[x : x + w, y : y + h]
            try:
                f = cv2.resize(f, (200, 200), interpolation=cv2.INTER_LINEAR)
                res = model.predict(f)
                print("Lable:%s, Accuray:%.2f" % (res[0], res[1]))
                cv2.putText(frame, name[res[0]], (x, y - 20), cv2.FONT_HERSHEY_SIMPLEX, 1, 255, 2)

            except:
                continue
        cv2.imshow("face", frame)
        if cv2.waitKey(1000 // 12) & 0xff == ord("q"):
            break
    camera.release()
    cv2.destroyAllWindows() 


if __name__ == "__main__":
    faceDetect("train.txt")