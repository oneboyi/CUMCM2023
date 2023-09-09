import math

# 定义已知参数
alpha = 1.5  # 角度值，例如30度
beta = 30   # 角度值，例如45
Dc = 110  # 海域中心距离，例如10000米
d =  44    # 测线间距，例如500米

# 计算Gamma
def calculate_gamma(beta, alpha):
    Gamma = math.sin(math.radians(60)) * (
        1 / math.sin(math.radians(30 - abs(math.degrees(math.atan(abs(math.tan(math.radians(alpha)) * math.sin(math.radians(180 - beta)))))))) +
        1 / math.sin(math.radians(30 + abs(math.degrees(math.atan(abs(math.tan(math.radians(alpha)) * math.sin(math.radians(180 - beta))))))))
    )
    return Gamma

# 计算D_min
def calculate_d_min(Dc, alpha):
    d_min = Dc - math.sqrt(5) * 1852 * abs(math.tan(math.radians(alpha)) * math.cos(math.atan(1 / 2)))
    return d_min

# 计算D_max
def calculate_d_max(Dc, alpha):
    d_max = Dc + math.sqrt(5) * 1852 * abs(math.tan(math.radians(alpha)) * math.cos(math.atan(1 / 2)))
    return d_max

# 计算tangamma_0
def calculate_gamma_0(alpha, beta_0):
    tangamma_0 = abs(math.tan(math.radians(alpha)) * math.sin(math.radians(180 - beta_0)))
    return tangamma_0

# 计算D_i
def calculate_d_i(D1, d, gamma_0, i):
    D_i = D1 + (i - 1) * d * gamma_0
    return D_i

# 计算W_i
def calculate_W_i(D_i, gamma_0):
    a_1 = gamma_0 * math.sin(math.radians(60)) * math.cos(gamma_0) * (
        1 / math.sin(math.radians(gamma_0 + 30)) + 1 / math.sin(math.radians(30 - gamma_0))
    )
    b_1 = D1 * math.sin(math.radians(60)) * math.cos(gamma_0) * (
        1 / math.sin(math.radians(gamma_0 + 30)) + 1 / math.sin(math.radians(30 - gamma_0))
    )
    W_i = (D_i * math.sin(math.radians(60)) * math.cos(gamma_0) * (
        1 / math.sin(math.radians(gamma_0 + 30)) + 1 / math.sin(math.radians(30 - gamma_0))
    ))
    return W_i

# 计算eta_i
def calculate_eta_i(alpha, beta_0, d, i):
    gamma_0 = calculate_gamma_0(alpha, beta_0)
    a_1 = gamma_0 * math.sin(math.radians(60)) * math.cos(math.atan(gamma_0)) * (
        1 / math.sin(math.atan(gamma_0) + math.radians(30)) + 1 / math.sin(math.radians(30) - math.atan(gamma_0))
    )
    b_1 = D1 * math.sin(math.radians(60)) * math.cos(math.atan(gamma_0)) * (
        1 / math.sin(math.atan(gamma_0 )+ math.radians(30)) + 1 / math.sin(math.radians(30) - math.atan(gamma_0))
    )
    eta_i = 1 - (d * math.cos(math.atan(gamma_0))) / (2 * (a_1 * (i - 1) * d + b_1) * math.sin(math.radians(150) - math.atan(gamma_0)))
    return eta_i

# 计算其他参数和长度
# 计算长度 L
def calculate_length_L(D0, beta, n_I, d, alpha):
    delta_l_I = d * (abs(math.tan(math.radians(beta))) + abs(1 / math.tan(math.radians(beta))))
    L_I = (2 * math.sqrt(3) * D0 + (n_I - 1) * d) * n_I / abs(math.sin(2 * math.radians(beta)))
    print("L_I=",L_I)
    d_II = 4 * 1852 - (math.sqrt(3) * D0 / abs(math.cos(math.radians(beta)))) - (
                n_I * (d / abs(math.cos(math.radians(beta)))))
    print("d_II=",d_II)
    n_II = math.floor(d_II / (d / abs(math.cos(math.radians(beta)))) + 1)
    print("n_II=",n_II)
    L_II = n_II * (2 * 1852 / abs(math.cos(math.radians(beta))))

    d_III = abs(1 / math.tan(math.radians(beta))) * (n_II * (d / abs(math.cos(math.radians(beta)))) - d_II)

    n_III = math.floor((2 * 1852 - d_III) / (d / abs(math.sin(math.radians(beta)))) + 1)
    print("n_III=",n_III)

    delta_l_III = -d * (abs(math.tan(math.radians(beta))) + abs(1 / math.tan(math.radians(beta))))

    l_n_I_n_II_1 = (2 * 1852 - d_III) / abs(math.cos(math.radians(beta)))

    L_III = n_III * l_n_I_n_II_1 + (n_III * (n_III - 1) / 2) * delta_l_III

    if (2 * 1852 - d_III - (n_III - 1) * (d / abs(math.sin(math.radians(beta))))) < (
            math.sqrt(3) * D0 / abs(math.sin(math.radians(beta)))):
        L_III = L_III
    else:
        L_III = L_III + (math.sqrt(3) * calculate_d_max(Dc, alpha)) / (
                    abs(math.sin(math.radians(beta))) * abs(math.cos(math.radians(beta))))

    L = L_I + L_II + L_III
    return L


# 示例使用

D1 = calculate_d_min(Dc, alpha)
n_I = math.floor((2 * 1852 - D1) / (d / abs(math.sin(math.radians(beta)))) + 1)
print("n_I=",n_I)
L = calculate_length_L(D1, beta, n_I, d, alpha)
print("Length L:", L)
# ... 可以根据需要继续实现其他方程

# 示例使用
beta_0 = 60  # 例如，初始角度为60度

W1 = calculate_W_i(D1, calculate_gamma_0(alpha, beta_0))
print("Gamma:", calculate_gamma(beta_0, alpha))
print("D_min:", D1)
print("D_max:", calculate_d_max(Dc, alpha))
print("tangamma_0:", calculate_gamma_0(alpha, beta_0))
print("D_i for i=2:", calculate_d_i(D1, d, calculate_gamma_0(alpha, beta_0), 2))
print("W_i for i=2:", calculate_W_i(calculate_d_i(D1, d, calculate_gamma_0(alpha, beta_0), 2), calculate_gamma_0(alpha, beta_0)))
print("eta_i for i=2:", calculate_eta_i(alpha, beta_0, d, 2))