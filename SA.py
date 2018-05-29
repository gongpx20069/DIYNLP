import jieba
import json
import os
SAdic={}
with open(os.path.join(os.getcwd(),"DIYNLP/model/SA.model"),"r") as f:
    SAdic=json.loads(f.read())
def getscore(str0):
    score = 0
    for i in jieba.lcut(str0):
        if i in SAdic.keys():
            score+=SAdic[i]
    return score
