# 2018-9-13
import cv2
import numpy as np
def center(points):
    """
    [[768 242]
     [784 384]
     [673 397]
     [657 255]]
    """
    # x1 = (points[0][0] + points[1][0]) / 2
    # x2 = (points[2][0] + points[3][0]) / 2
    # x = (x1 + x2) / 2
    x = (points[0][0] + points[1][0] + points[2][0] + points[3][0]) / 4
    y = (points[0][1] + points[1][1] + points[2][1] + points[3][1]) / 4
    return np.array([np.float32(x), np.float32(y)], np.float32)


class Pedestrain(object):
    def __init__(self, id, frame, track_window, algorithm="CAMShift", color=255):

        self.algorithm = algorithm
        self.id = id
        self.track_window = track_window
        self.color = color

        x, y, w, h = track_window
        self.roi = cv2.cvtColor(frame[y : y + h, x : x + w], cv2.COLOR_BGR2HSV)

        # 计算直方图,然后归一化
        # P145
        roi_hist = cv2.calcHist([self.roi], [0], None, [16], [0, 180])
        self.roi_hist = cv2.normalize(roi_hist, roi_hist, 0, 255, cv2.NORM_MINMAX)

        # 设置卡尔曼滤波器
        self.kalman = cv2.KalmanFilter(4, 2)
        self.kalman.measurementMatrix = np.array([[1,0,0,0],[0,1,0,0]], np.float32)
        self.kalman.transitionMatrix = np.array([[1,0,1,0],[0,1,0,1],[0,0,1,0],[0,0,0,1]],np.float32)
        self.kalman.processNoiseCov = np.array([[1,0,0,0],[0,1,0,0],[0,0,1,0],[0,0,0,1]],np.float32) * 0.03
        self.measurement = np.array((2,1), np.float32) 
        self.prediction = np.zeros((2,1), np.float32)

        # 迭代终止条件, 均值漂移迭代10次后或者中心移动至少1个像素时， 均值漂移就停止计算中心移动
        self.term_crit = ( cv2.TERM_CRITERIA_EPS | cv2.TERM_CRITERIA_COUNT, 10, 1 )

        self.center = None
        self.update(frame)


    def __del__(self):
        print("Pedestrain %d destropyed" % self.id)

    def update(self, frame):
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        back_project = cv2.calcBackProject([hsv], [0], self.roi_hist, [0, 180], 1)

        if self.algorithm == "CAMShift":
            # 使用camshit得到新的位置
            ret, self.track_window = cv2.CamShift(back_project, self.track_window, self.term_crit)
            # 矩形坐标
            pts = cv2.boxPoints(ret)
            pts = np.int0(pts)

            # 计算中心
            # print("矩形坐标: ", pts)
            self.center = center(pts)
            cv2.polylines(frame, [pts], True, 255, 1)

        if self.algorithm == "MEANShift":
            ret, self.track_window = cv2.meanShift(back_project, self.track_window, self.term_crit)
            x,y,w,h = self.track_window
            # 计算目标中心
            self.center = center([[x,y],[x+w, y],[x,y+h],[x+w, y+h]])  
            # cv2.rectangle(frame, (x,y), (x+w, y+h), (self.color, 255, 0), 1)   


        if self.algorithm not in ["MEANShift", "CAMShift"]:
            print("Error algorithm input.")
            return None


        # 卡尔曼滤波器预测
        self.kalman.correct(self.center)
        prediction = self.kalman.predict()
        cv2.circle(frame, (int(prediction[0]), int(prediction[1])), 4, (255, 0, 0), -1)

        cv2.putText(frame, "ID: %d -> %s" % (self.id, self.center), (11, (self.id + 1) * 25 + 1), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 1, cv2.LINE_AA)
        # cv2.putText(frame, "ID: %d -> %s" % (self.id, self.center), (11, (self.id + 1) * 25), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 1, cv2.LINE_AA)

def main(file_path, history):
    camera = cv2.VideoCapture(file_path)
    # KNN背景提取器
    bs = cv2.createBackgroundSubtractorKNN() # detectShadows=False

    # 另外两个背景提取器
    # MOG subtractor
    # bs = cv2.bgsegm.createBackgroundSubtractorMOG(history = history)
    # bs.setHistory(history)

    # GMG
    # bs = cv2.bgsegm.createBackgroundSubtractorGMG(initializationFrames = history)

    cv2.namedWindow("test")
    pedestrain = {}
    firstFrame = True
    frame_count = 0
    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    out = cv2.VideoWriter('output.avi',fourcc, 20.0, (640,480))

    while True:
        ret, frame = camera.read()
        if not ret:
            print("Failed to read video.")
            break

        # 计算前景掩码
        fgmask = bs.apply(frame)

        # 多次计算前景
        if frame_count < history:
            frame_count += 1
            continue

        # 阈值处理，腐蚀，膨胀并提取轮廓
        th = cv2.threshold(fgmask.copy(), 127, 255, cv2.THRESH_BINARY)[1]
        th = cv2.erode(th, cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (3, 3)), iterations=2)
        dilated = cv2.dilate(th, cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (8,3)), iterations = 2)
        image, contours, hier = cv2.findContours(dilated, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

        man_id = 0
        for c in contours:
            if cv2.contourArea(c) > 500:
                x, y, w, h = cv2.boundingRect(c)
                cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 1)
                if firstFrame:
                    colr = man_id * 10
                    pedestrain[man_id] = Pedestrain(man_id, frame, (x, y, w, h), algorithm="MEANShift", color=colr)
                man_id += 1
        for i,p in pedestrain.items():
            p.update(frame)

        firstFrame = False

        frame_count += 1

        cv2.imshow("test", frame)
        out.write(frame)

        if cv2.waitKey(1000 // 12) & 0xff == ord('q'):
            break
    print("Total frame: %d" % frame_countc )
    out.release()
    camera.release()

if __name__ == '__main__':
    main("video.avi", 2)




