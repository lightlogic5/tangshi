import jieba

txt = open('result1.txt', 'r',encoding='utf-8').read()
words = jieba.cut(txt,cut_all=True)
counts = {} 

for word in words:
    if  len(word) == 1:    # 单个词语不计算在内
        continue
    else:
        counts[word] = counts.get(word, 0) + 1

items = list(counts.items()) #将字典转为list
items.sort(key=lambda x:x[1],reverse=True) #根据单词出现次数降序排序
    #打印前15个
for i in range(15):
    word,counter = items[i]
    with open('finall.txt', 'a', encoding='utf-8') as f:
        f.write("{},{}".format(word,counter) + '\n')
        f.close()
