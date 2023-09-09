''' B问题1'''
# 1. 导入需要的库
python 
import numpy as np
import math
import pandas as pd
#2. 定义参数
python
alpha = 1.5 / 180 * math.pi  # 坡度
theta = 120 / 180 * math.pi # 声束角
L = 35 # 相邻测线间距
H = 70 # 海域中心水深
#3. 定义计算覆盖宽度的函数
python
def calculate_width(x, alpha, theta):
    y = x * math.tan(theta)
    d = x / math.cos(alpha)
    return d
#4. 定义计算重叠率的函数
python  
def calculate_overlap(d, L):
    r = (d - L) / d 
    return r
#5. 计算表1中的指标值
python
x_list = [0, 30, 50]
width_list = [calculate_width(x, alpha, theta) for x in x_list]
overlap_list = [calculate_overlap(d, L) for d in width_list]
#6. 将结果存为DataFrame
python
df = pd.DataFrame({'x': x_list, 
                   '覆盖宽度': width_list,
                   '重叠率': overlap_list})
#7. 输出结果到Excel
python
df.to_excel('result1.xlsx', index=False)



#2

1. 导入必要的库
python
import numpy as np 
import pandas as pd
2. 定义参数
python 
beta = 30 / 180 * np.pi
theta = 120 / 180 * np.pi
H = 120
3. 定义计算覆盖宽度的函数
python
def calculate_width(x, beta, theta):
  width = (x * np.sec(beta)) / np.cos(beta + theta)
  return width
4. 计算表2中的覆盖宽度
python
x_list = [0, 50, 100]
width_list = [calculate_width(x, beta, theta) for x in x_list] 
5. 将结果存为DataFrame
python
df = pd.DataFrame({'x坐标': x_list, '覆盖宽度': width_list})
6. 输出结果到Excel
python
df.to_excel('result2.xlsx', index=False)


#3

1. 导入库
python
import numpy as np
import math
2. 定义海域参数
python 
length = 2 # 海里
width = 4 
depth = 110 # 中心深度
alpha = 1.5 / 180 * math.pi # 坡度
theta = 120 / 180 * math.pi # 声束角
3. 定义计算函数
python
def calculate_overlap(l):
  d = l / math.cos(alpha) # 覆盖宽度
  overlap = 0.1 * d # 最小重叠宽度
  return overlap

def calculate_length(n):
  l = width / n # 单条线长度
  total_len = n * (l - n*calculate_overlap(l)) # 总长度
  return total_len
4. 求解
python
for n in range(1, int(width/0.1)):
  if 0.1 < calculate_overlap(width/n)/width < 0.2: 
    print(calculate_length(n))
    break 