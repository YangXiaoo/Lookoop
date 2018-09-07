# 2018-9-7
# 生成CSV(comma-separated value)
import os
def generateCSV(dirpath):
    file = []
    direction = []
    count = 0
    if os.path.isfile("train.txt"):
        os.system("DEL train.txt ")
        print("ok")
    labels = []
    for root, dirs, files in os.walk(dirpath, topdown=False):
        for name in files:
            path = os.path.join(root, name)
            preffix = "/".join(path.split("\\")[-3:])
            file.append(preffix)
            n = preffix.split("/")[1]
            if n not in labels:
                labels.append(n)

        if len(file) != 0:
            with open("train.txt", "a") as f:
                for i in file:
                    f.write(i + " " + str(count) + '\n')
                f.close()
        file = []
        count += 1
    print(labels)
    with open("labels.txt","w") as l:
        for i in labels:
            i += '\n'
            l.write(i)
        l.close()

if __name__ == "__main__":
    dirs = "C:\\Study\\github\\Lookoop\\Image\\OpenCV\\face_detect\\face"
    generateCSV(dirs)