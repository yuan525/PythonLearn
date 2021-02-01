#TextProBarV1.py
'''import time
scale = 10
print("-------执行开始-------")
for i in range(scale+1):
    a = '*' * i
    b = '.' * (scale - i)
    c = (i/scale)*100
    #>:右对齐   3：宽度   .0f：浮点数精度（小数点后0位）
    print("{:>3.0f}%[{}->{}]".format(c,a,b))
    time.sleep(0.1)
print("-------执行结束-------")'''

#TextProBarV2.py
#单行动态刷新
'''import time 
for i in range(101):
	print("\r{:3}%".format(i),end='')
	time.sleep(0.1)'''

#TextProBarV3.py
import time 
scale = 50 
# //表示整数除，比如10//3=3
print("执行开始".center(scale//2,'-'))
start = time.perf_counter()
for i in range(scale+1):
	a = '*' * i
	b = '.' * (scale - i)
	c = (i/scale)*100
	dur = time.perf_counter() - start
	print("\r{:^3.0f}%[{}->{}]{:.2f}s".format(c,a,b,dur),end='')
	time.sleep(0.1)
print("执行结束".center(scale//2,'-'))