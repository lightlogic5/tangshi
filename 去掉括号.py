import re

txt = open('result.txt', 'r',encoding='utf-8').read()
# txt = 'sfafdsfs，，，dfsdfsd(括号中的内容g)sdad<尖括号中的内容>ada.。。。sd'
pattern = re.compile('\(.*?\)|\<.*?\>|\u3002|\uff0c|\uff1f|"|\n|\\n')
tangshi = re.sub(pattern,'',txt).replace(r"\r\n", "").strip()
with open('result1.txt', 'a', encoding='utf-8') as f:
    f.write(tangshi)
    f.close()