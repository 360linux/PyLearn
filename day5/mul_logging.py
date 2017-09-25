#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 17-9-17 下午2:21
# @Author  : Liping
# @Site    : 
# @File    : mul_logging.py
# @Software: PyCharm

import  logging
from multiprocessing import Pool
logger=logging.getLogger(__name__)
logformat=logging.Formatter('%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s')
logging.basicConfig(level=logging.INFO,format=logformat)
fh=logging.FileHandler(filename="my.log",encoding="utf-8")
fh.setFormatter(logformat)
fh.setLevel(logging.INFO)
# frh=logger.handlers.RotatingFileHandler(filename="filerotate.log",maxBytes=1000000, backupCount=3, encoding="utf-8")
# frh.setlevel(logging.WARN)
sh=logging.StreamHandler()
logger.addHandler(fh)
logger.addHandler(sh)
# logger.addHandler(frh)

def logfun(i):
    logger.info("this is info log %d" %i)
    logger.warn("this is warn log %d" %i)
    logger.debug("this is debug log %d" %i)
    logger.error("this is error log %d" %i)
    logger.error("this is error log %d" %i)


p=Pool()
for i in xrange(50):
    p.apply_async(logfun,args=(i,))

p.close()
p.join()
