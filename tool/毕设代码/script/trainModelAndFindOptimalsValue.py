# coding:utf-8
# 2030-2-9

import sys
sys.path.append("../")

from trainModel import *
from GAMain import mainModelOptimus,singleModelOptimus
from quadRegresstion import *

logger.info("{}-v2-{}".format('@'*25, '@'*25))


# train()
# trainBySingleModel()
# testModelPdtRMAE()
# testModelPdtMAE()
# testSingleModelRMAE()
# testSingleModelMAE()
# crossValidateRMAE()
# crossValidateMAE()

mainModelOptimus()
singleModelOptimus()