a = 0
for a in range(100):
    a = a + 1
    if a % 10 == 7:  #如果a除以10余数为7时
        continue
    if a // 10 == 7: #如果a除以10商的整数为7时
        continue
    if a % 7 == 0: #如果a除以7的余数为0时
        continue
    print(a)

