**读入文件**  
with open('filename', 'r') as f:  

**字符串替换**  
str.replace('old', 'new')  

**字符串翻转**  
str[::-1]，或者 ''.join(reversed(str)) （reversed翻转list）

**集合取对称差集（相当于并集减交集）** 
set(A)^set(B) （前后顺序无所谓）

**根据列表顶替字符**  
str.translate( str.maketrans( intab, outtab ) )  

intab -- 字符串中要替代的字符组成的字符串。
outtab -- 相应的映射字符的字符串  