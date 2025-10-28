word1 = "Hello Word"
word2 = "Today is sunny Day"
print(word1 + word2,)
print(word1, word2,sep=',',end='。')
print(word1*5)
print('H' in word1)
print('H' in word2)
print('H' not in word1)
print('H' not in word2)

print(word1[0:3])
print(word2[0:])
print(word1[-1:-5:-1])
print(word1[-1:-8:-2])
print(word2.find('s',0,5))
print(word2.find('s',0,8))
#输出的是s在word2中的下标位置

str = 'Hello Python'
print(str.split('o',1))
print(str.lower())
print(str.capitalize())
print(str.upper())
print(str)
