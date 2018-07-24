import os
 
if __name__ == "__main__":

    dirs = ["train", "test"]
    data_dir = "C:/software/caffe/caffe-master/data/mydat/"

    for d in dirs:
        d_dir = data_dir + d
        dir_pre = d + "\\"
        file = d_dir + "/" + d + ".txt"
        d_file = open(file, "w")
        files = os.listdir(d_dir)
        index = 0
        for f in files:
            d_file.write("{0}{1} {2}\n".format(dir_pre, f, int(f[0])-3))
            index += 1
            if index % 100 == 0:
                print("{0} processed".format(index))
        d_file.close()
    print("Successful")
