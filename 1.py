a = 'Сейчас на Земле появился новый вид роботов. Раньше их называли „железной оравой “, но это не очень точное определение'
c, d = a.split('.')
print(c + '.')

b = 'Палиндром'
print(b[::-1])

b = 'Норма'
print(b[::-1])

st1 = input()
first = st1[0:len(st1) // 2]
second = st1[len(st1) // 2 :]
print(second + first)

num = input()
print(num[::2] , num[1::2])

part = input()
print(part[-2:0:-1])