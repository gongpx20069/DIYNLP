DIY中文NLP算法包
====================
    这是一个DIY的中文NLP算法包，具体算法分析请参见https://blog.csdn.net/greepex/article/details/80493045
    其中有关于短文本相似度以及情感极性分析的算法。
短文本相似度算法(distance.py)
---------
    基于分词后单词：
    edit_similar(str1,str2)：编辑距离相似度，输入为分词后的两个句子的列表，返回值为两者相似度。
    cos_sim(str1, str2):余弦相似度，输入为分词后的两个句子的列表，返回值为两者相似度。
    基于字符：
    difflib.SequenceMatcher(None,str1,str2).ratio()：difflib为python自带的库，str1和str2无需分词。
    综合相似度：
    compare(str1, str2)：输入是两个字符串（中文句子），无需分词，返回值为两者相似度。

文本情感极性分析(SA.py)
---------
    getscore(str0)：输入是中文句子，无需分词，返回值为情感极性的值。
