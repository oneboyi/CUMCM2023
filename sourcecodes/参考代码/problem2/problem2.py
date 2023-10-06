import math

# 导入海里和β的值
d_c_values = [0, 0.3, 0.6, 0.9, 1.2, 1.5, 1.8, 2.1]
beta_values = [0, 45, 90, 135, 180, 225, 270, 315]

# 定义函数来计算W
def calculate_W(d_c, beta):
    alpha = math.radians(60)  # 将角度转换为弧度
    gamma = abs(math.tan(alpha) * math.cos(math.radians(180 - beta)))
    gamma_prime = abs(math.tan(alpha) * math.sin(math.radians(180 - beta)))

    if beta >= math.radians(90) and beta <= math.radians(270):
        D = 120 - 1852 * d_c * gamma
    else:
        D = 120 + 1852 * d_c * gamma

    l_i1 = D / math.sin(math.radians(30 - gamma_prime))
    l_i2 = D / math.sin(math.radians(30 + gamma_prime))

    W = (l_i1 + l_i2) / math.sin(math.radians(60))
    return W

# 计算每个组合下的W值
results = []
for d_c in d_c_values:
    for beta in beta_values:
        W = calculate_W(d_c, math.radians(beta))
        results.append((d_c, beta, W))

# 打印结果
for d_c, beta, W in results:
    print(f"d_c = {d_c}, beta = {math.degrees(beta)} degrees, W = {W}")
