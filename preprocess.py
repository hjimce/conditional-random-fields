#coding=utf-8
#以句号为单元，进行分词操作
import  numpy as np
import  re
def create_dictionary(textroot):
    char_index={}
    with open(textroot,"rb") as f:
        text=f.read().split()
        text=''.join(text).decode('utf-8')
        words=re.split(u'。',text)
        count=0
        for word in words:
            for char in word:
                if char_index.has_key(char):
                    continue
                else:
                    char_index[char]=count
                    count+=1
    index_char={}
    for item,value in char_index.items():
        index_char[value]=item

    return char_index,index_char
def preprocess_wordsegment_text(input_textroot,output_textroot):
    tag_text=open(output_textroot,'wb')
    with open(textroot,"rb") as f:
        text=f.read().decode('utf-8')
        sentences=re.split(u'。',text)#每个句子进行处理
        for sentence in sentences:
            sentence_split=sentence.split()
            sentence_tag=[]
            for word in sentence_split:
                if len(word)==1:
                    sentence_tag.append('S')
                elif len(word)==2:
                    sentence_tag.append('BE')
                else:
                    wtemp='B'+'M'*(len(word)-2)+'E'
                    sentence_tag.append(wtemp)
            write_sentence=''.join(sentence_split)
            sentence_tag=''.join(sentence_tag)
            if len(write_sentence)>0:
                tag_text.writelines(write_sentence+'\n')
                tag_text.writelines(sentence_tag.decode('utf-8')+'\n')


            print len(write_sentence)
            print len(sentence_tag)
#总结上面所有的函数，输入训练数据路径，返回：
# 1、字典、索引映射
# 2、条件随机场特征矩阵f(x,y)
def all_in_one()：








preprocess_wordsegment_text('traindata/1.txt','tag_text.txt')


