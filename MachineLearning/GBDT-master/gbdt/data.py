# -*- coding:utf-8 -*-


class DataSet:
    """
    分类问题默认标签列名称为label，二元分类标签∈{-1, +1}
    回归问题也统一使用label
    """
    def __init__(self, filename):  # just for csv data format
        line_cnt = 0
        self.instances = dict()
        self.distinct_valueset = dict()  # just for real value type
        for line in open(filename):
            if line == "\n":
                continue
            fields = line[:-1].split(",")
            if line_cnt == 0:  # csv head
                self.field_names = tuple(fields)
            else:
                if len(fields) != len(self.field_names):
                    print("wrong fields:", line)
                    raise ValueError("fields number is wrong!")
                if line_cnt == 1:  # determine the value type
                    self.field_type = dict()
                    for i in range(0, len(self.field_names)):
                        valueSet = set()
                        try:
                            float(fields[i])
                            self.distinct_valueset[self.field_names[i]] = set()
                        except ValueError:
                            valueSet.add(fields[i])
                        self.field_type[self.field_names[i]] = valueSet
                self.instances[line_cnt] = self._construct_instance(fields)
            line_cnt += 1

    def _construct_instance(self, fields):
        """构建一个新的样本"""
        instance = dict()
        for i in range(0, len(fields)):
            field_name = self.field_names[i]
            real_type_mark = self.is_real_type_field(field_name)
            if real_type_mark:
                try:
                    instance[field_name] = float(fields[i])
                    self.distinct_valueset[field_name].add(float(fields[i]))
                except ValueError:
                    raise ValueError("the value is not float,conflict the value type at first detected")
            else:
                instance[field_name] = fields[i]
                self.field_type[field_name].add(fields[i])
        return instance

    def describe(self):
        info = "features:"+str(self.field_names)+"\n"
        info = info+"\n dataset size="+str(self.size())+"\n"
        for field in self.field_names:
            info = info+"description for field:"+field
            valueset = self.get_distinct_valueset(field)
            if self.is_real_type_field(field):
                info = info+" real value, distinct values number:"+str(len(valueset))
                info = info+" range is ["+str(min(valueset))+","+str(max(valueset))+"]\n"
            else:
                info = info+" enum type, distinct values number:"+str(len(valueset))
                info = info+" valueset="+str(valueset)+"\n"
            info = info+"#"*60+"\n"
        print(info)

    def get_instances_idset(self):
        """获取样本的id集合"""
        return set(self.instances.keys())

    def is_real_type_field(self, name):
        """判断特征类型是否是real type"""
        if name not in self.field_names:
             raise ValueError(" field name not in the dictionary of dataset")
        return len(self.field_type[name]) == 0

    def get_label_size(self, name="label"):
        if name not in self.field_names:
            raise ValueError(" there is no class label field!")
        # 因为训练样本的label列的值可能不仅仅是字符类型，也可能是数字类型
        # 如果是数字类型则field_type[name]为空
        return len(self.field_type[name]) or len(self.distinct_valueset[name])

    def get_label_valueset(self, name="label"):
        """返回具体分离label"""
        if name not in self.field_names:
            raise ValueError(" there is no class label field!")
        return self.field_type[name] if self.field_type[name] else self.distinct_valueset[name]

    def size(self):
        """返回样本个数"""
        return len(self.instances)

    def get_instance(self, Id):
        """根据ID获取样本"""
        if Id not in self.instances:
            raise ValueError("Id not in the instances dict of dataset")
        return self.instances[Id]

    def get_attributes(self):
        """返回所有features的名称"""
        field_names = [x for x in self.field_names if x != "label"]
        return tuple(field_names)

    def get_distinct_valueset(self, name):
        if name not in self.field_names:
            raise ValueError("the field name not in the dataset field dictionary")
        if self.is_real_type_field(name):
            return self.distinct_valueset[name]
        else:
            return self.field_type[name]


if __name__ == "__main__":
    from sys import argv
    data = DataSet(r'C:\Study\github\Lookoop\MachineLearning\GBDT-master\data\credit.data.csv')
    print("instances size=", len(data.instances))
    print("data.instances[1]")
    print(data.instances[1])

    print()
    print('data.describe()')
    print(data.describe())

    print()
    print('data.get_instances_idset()')
    print(data.get_instances_idset())


    print()
    print('data.get_label_valueset()')
    print(data.get_label_valueset())


    print()
    print('\n data.size()')
    print(data.size())
    print('\n data.get_instance(1)')
    print(data.get_instance(1))
    print('\n data.get_attributes()')
    print(data.get_attributes())
    print('\n data.get_distinct_valueset(\'A1\')')
    print(data.get_distinct_valueset('A1'))
"""
instances size= 653
data.instances[1]
{'A1': 'b', 'A2': 30.83, 'A3': 0.0, 'A4': 'u', 'A5': 'g', 'A6': 'w', 'A7': 'v', 'A8': 1.25, 'A9': 't', 'A10': 't', 'A11': 1.0, 'A12': 'f', 'A13': 'g', 'A14': 202.0, 'A15': 0.0, 'label': 1.0}

data.describe()
features:('A1', 'A2', 'A3', 'A4', 'A5', 'A6', 'A7', 'A8', 'A9', 'A10', 'A11', 'A12', 'A13', 'A14', 'A15', 'label')

 dataset size=653
description for field:A1 enum type, distinct values number:2 valueset={'b', 'a'}
############################################################
description for field:A2 real value, distinct values number:340 range is [13.75,76.75]
############################################################
description for field:A3 real value, distinct values number:213 range is [0.0,28.0]
############################################################
description for field:A4 enum type, distinct values number:3 valueset={'l', 'u', 'y'}
############################################################
description for field:A5 enum type, distinct values number:3 valueset={'gg', 'p', 'g'}
############################################################
description for field:A6 enum type, distinct values number:14 valueset={'r', 'i', 'ff', 'q', 'm', 'w', 'aa', 'x', 'k', 'cc', 'j', 'e', 'c', 'd'}
############################################################
description for field:A7 enum type, distinct values number:9 valueset={'ff', 'bb', 'v', 'h', 'dd', 'z', 'n', 'j', 'o'}
############################################################
description for field:A8 real value, distinct values number:131 range is [0.0,28.5]
############################################################
description for field:A9 enum type, distinct values number:2 valueset={'f', 't'}
############################################################
description for field:A10 enum type, distinct values number:2 valueset={'f', 't'}
############################################################
description for field:A11 real value, distinct values number:23 range is [0.0,67.0]
############################################################
description for field:A12 enum type, distinct values number:2 valueset={'t', 'f'}
############################################################
description for field:A13 enum type, distinct values number:3 valueset={'p', 's', 'g'}
############################################################
description for field:A14 real value, distinct values number:164 range is [0.0,2000.0]
############################################################
description for field:A15 real value, distinct values number:229 range is [0.0,100000.0]
############################################################
description for field:label real value, distinct values number:2 range is [-1.0,1.0]
############################################################

None

data.get_instances_idset()
{1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142, 143, 144, 145, 146, 147, 148, 149, 150, 151, 152, 153, 154, 155, 156, 157, 158, 159, 160, 161, 162, 163, 164, 165, 166, 167, 168, 169, 170, 171, 172, 173, 174, 175, 176, 177, 178, 179, 180, 181, 182, 183, 184, 185, 186, 187, 188, 189, 190, 191, 192, 193, 194, 195, 196, 197, 198, 199, 200, 201, 202, 203, 204, 205, 206, 207, 208, 209, 210, 211, 212, 213, 214, 215, 216, 217, 218, 219, 220, 221, 222, 223, 224, 225, 226, 227, 228, 229, 230, 231, 232, 233, 234, 235, 236, 237, 238, 239, 240, 241, 242, 243, 244, 245, 246, 247, 248, 249, 250, 251, 252, 253, 254, 255, 256, 257, 258, 259, 260, 261, 262, 263, 264, 265, 266, 267, 268, 269, 270, 271, 272, 273, 274, 275, 276, 277, 278, 279, 280, 281, 282, 283, 284, 285, 286, 287, 288, 289, 290, 291, 292, 293, 294, 295, 296, 297, 298, 299, 300, 301, 302, 303, 304, 305, 306, 307, 308, 309, 310, 311, 312, 313, 314, 315, 316, 317, 318, 319, 320, 321, 322, 323, 324, 325, 326, 327, 328, 329, 330, 331, 332, 333, 334, 335, 336, 337, 338, 339, 340, 341, 342, 343, 344, 345, 346, 347, 348, 349, 350, 351, 352, 353, 354, 355, 356, 357, 358, 359, 360, 361, 362, 363, 364, 365, 366, 367, 368, 369, 370, 371, 372, 373, 374, 375, 376, 377, 378, 379, 380, 381, 382, 383, 384, 385, 386, 387, 388, 389, 390, 391, 392, 393, 394, 395, 396, 397, 398, 399, 400, 401, 402, 403, 404, 405, 406, 407, 408, 409, 410, 411, 412, 413, 414, 415, 416, 417, 418, 419, 420, 421, 422, 423, 424, 425, 426, 427, 428, 429, 430, 431, 432, 433, 434, 435, 436, 437, 438, 439, 440, 441, 442, 443, 444, 445, 446, 447, 448, 449, 450, 451, 452, 453, 454, 455, 456, 457, 458, 459, 460, 461, 462, 463, 464, 465, 466, 467, 468, 469, 470, 471, 472, 473, 474, 475, 476, 477, 478, 479, 480, 481, 482, 483, 484, 485, 486, 487, 488, 489, 490, 491, 492, 493, 494, 495, 496, 497, 498, 499, 500, 501, 502, 503, 504, 505, 506, 507, 508, 509, 510, 511, 512, 513, 514, 515, 516, 517, 518, 519, 520, 521, 522, 523, 524, 525, 526, 527, 528, 529, 530, 531, 532, 533, 534, 535, 536, 537, 538, 539, 540, 541, 542, 543, 544, 545, 546, 547, 548, 549, 550, 551, 552, 553, 554, 555, 556, 557, 558, 559, 560, 561, 562, 563, 564, 565, 566, 567, 568, 569, 570, 571, 572, 573, 574, 575, 576, 577, 578, 579, 580, 581, 582, 583, 584, 585, 586, 587, 588, 589, 590, 591, 592, 593, 594, 595, 596, 597, 598, 599, 600, 601, 602, 603, 604, 605, 606, 607, 608, 609, 610, 611, 612, 613, 614, 615, 616, 617, 618, 619, 620, 621, 622, 623, 624, 625, 626, 627, 628, 629, 630, 631, 632, 633, 634, 635, 636, 637, 638, 639, 640, 641, 642, 643, 644, 645, 646, 647, 648, 649, 650, 651, 652, 653}

data.get_label_valueset()
{1.0, -1.0}


 data.size()
653

 data.get_instance(1)
{'A1': 'b', 'A2': 30.83, 'A3': 0.0, 'A4': 'u', 'A5': 'g', 'A6': 'w', 'A7': 'v', 'A8': 1.25, 'A9': 't', 'A10': 't', 'A11': 1.0, 'A12': 'f', 'A13': 'g', 'A14': 202.0, 'A15': 0.0, 'label': 1.0}

 data.get_attributes()
('A1', 'A2', 'A3', 'A4', 'A5', 'A6', 'A7', 'A8', 'A9', 'A10', 'A11', 'A12', 'A13', 'A14', 'A15')

 data.get_distinct_valueset('A1')
{'b', 'a'}
[Finished in 0.2s]
"""