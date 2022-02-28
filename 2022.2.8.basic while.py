i = 0
n = 100
sum = 0
while i <= n:
      sum = sum+i
      i = i+1
print("1-%d=%d"%(n,sum))
j=0
sum=0
for j in range(0, 101, 1):
    sum=sum+j
print("sum=%d"%sum)
count = 0
while count <5:
    print(count,"小于5")
    count+=1
else :
    print(count,"大于或者等于5")
'''
# while 和 break 区别
i =0
while i<10:
    i=i+1
    print("-"*10)
    if i==5:
        continue
    print(i)
