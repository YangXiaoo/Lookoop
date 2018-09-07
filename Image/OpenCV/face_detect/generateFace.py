# 2018-9-7
# 生成人脸识别数据
import os
import cv2
from generateCSV import generateCSV
def generateFace(name, end=200):
    face = cv2.CascadeClassifier("data/haarcascade_frontalface_default.xml")
    eye = cv2.CascadeClassifier("data/haarcascade_eye.xml")

    camera = cv2.VideoCapture(0)
    count = 0 # 图片计数
    dirs = "C:\\Study\\github\\Lookoop\\Image\\OpenCV\\face_detect\\face\\" + str(name) +'\\'
    while True:
        ret, frame = camera.read()
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = face.detectMultiScale(gray, 1.3, 5)

        for x,y,w,h in faces:
            img = cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)

            f = cv2.resize(gray[y : y + h, x : x + w], (200, 200)) # 将人脸resize

            # 保存
            if not os.path.isdir(dirs):
                os.makedirs(dirs)
            cv2.imwrite("%s%s.pgm" % (dirs, str(count)), f)
            count += 1
            print("%s%s.pgm" % (dirs, str(count)))

        cv2.imshow("face", frame)

        if cv2.waitKey(1000 // 12) & 0xff == ord("q") or count == end:
            break

    camera.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    generateFace("tes", 50)
    dirs = "C:\\Study\\github\\Lookoop\\Image\\OpenCV\\face_detect\\face"
    generateCSV(dirs)