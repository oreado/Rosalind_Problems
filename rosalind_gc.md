**增加list项**  
.append  
**取连续范围**  
range()，输出为生成器对象，要print内容需要list()或者遍历。  
**遍历组成的列表内容**
[x.replace('\n', '') for x in list] 
**计算特定字符数**  
str.count('x')
**保留指定位小数**
'%.6f' % f，或者 format(f, '.4f')

-----
**去除行尾符**
str.rstrip()
**寻找最大值的index**
seqgc.index(max_gc)

-----

**Python中0和空值为false**
**判断开头字母**
str.startwith('x')
**标准化字符串**
'%s\n%.6f%%' % (max_gc_name, max_gc_content * 100)
**逐行处理**
f = open('rosalind_gc.txt', 'r')
buf = f.readline().rstrip()
while buf:
……
f.close()
**以'>'分段**
str.split(‘>’)