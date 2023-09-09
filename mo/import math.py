import math
from math import *
def calculate_gamma_0(alpha, beta_0):
    tangamma_0 = abs(math.tan(math.radians(alpha)) * math.sin(math.radians(180 - beta_0)))
    return tangamma_0

d_min = Dc - math.sqrt(5) * 1852 * abs(math.tan(math.radians(alpha)) * math.cos(math.atan(1 / 2)))
D0 = d_min
D1= D0 + math.sqrt(3)*D0*calculate_gamma_0(alpha, beta)
d_max = Dc + math.sqrt(5) * 1852 * abs(math.tan(math.radians(alpha)) * math.cos(math.atan(1 / 2)))


# 计算测线测线垂面方向坡度tangamma_0
def calculate_tangamma_0(alpha, beta_0):
    tangamma_0 = abs(math.tan(math.radians(alpha)) * math.sin(math.radians(180 - beta_0)))
    return tangamma_0

#深度D_i
def calculate_d_i(D1, d, gamma_0, i):
    D_i = D1 + (i - 1) * d * gamma_0
    return D_i

#覆盖范围W_i
def calculate_W_i(D_i, gamma_0):
    a_1 = gamma_0 * math.sin(math.radians(60)) * math.cos(gamma_0) * (
        1 / math.sin(gamma_0 + math.radians(30)) + 1 / math.sin(math.radians(30) - atan(gamma_0))
    )
    b_1 = D1 * math.sin(math.radians(60)) * math.cos(gamma_0) * (
        1 / math.sin(gamma_0 + math.radians(30)) + 1 / math.sin(math.radians(30) - atan(gamma_0))
    )
    W_i = (D_i * math.sin(math.radians(60)) * math.cos(gamma_0) * (
        1 / math.sin(gamma_0 + math.radians(30)) + 1 / math.sin(math.radians(30) - atan(gamma_0))
    ))
    return W_i


    

a_1 = calculate_tangamma_0(alpha, beta) * math.sin(math.radians(60)) * math.cos(calculate_tangamma_0(alpha, beta)) * (
        1 / math.sin(calculate_tangamma_0(alpha, beta) + math.radians(30)) + 1 / math.sin(math.radians(30) - calculate_tangamma_0(alpha, beta)))

b_1 = D1 * math.sin(math.radians(60)) * math.cos(calculate_tangamma_0(alpha, beta)) * (
        1 / math.sin(atan(calculate_tangamma_0(alpha, beta)) + math.radians(30)) + 1 / math.sin(math.radians(30) - atan(calculate_tangamma_0(alpha, beta))))
gamma_0 =  calculate_tangamma_0(alpha, beta)

def calculate_eta(d,gamma,s):
    a_1 = gamma * math.sin(math.radians(60)) * math.cos(atan(gamma_0)) * (
        1 / math.sin(atan(gamma) + math.radians(30)) + 1 / math.sin(math.radians(30) - atan(gamma_0)))
    eta = 1- (d*cos(atan(gamma)))/(2*(a_1*s+b_1)*sin(150-atan(gamma)))
    return eta


def calculate_length(beta, d_0):
    L = 0
    o = 0
    if 0<beta and beta<90:
        if math.tan(beta)>0.5:
            d_1 = d_0
            sum = d_1
            sumSN = math.sqrt(3)*D0/math.cos(beta)
            sumWE = math.sqrt(3)*D0/math.sin(beta)
            d_2 = d_1
            eta = calculate_eta(d_1,gamma_0,sum)
            sum += d_2
            i = 2
            while sumSN <= 2*1852:
                d_i = (2 * (b_1 * math.sin(radians(150) - gamma_0))) / (
                    cos(gamma_0) - sin(radians(150) - gamma_0) * 2 * (1 - eta) * a_1 * i)
                eta=calculate_eta(d_2,gamma_0,sum)
                if eta > 0.2 or eta <0.1:
                    return 0
                L += sumSN/math.sin(beta)
                sumSN += d_i/cos(beta)
                sumWE += d_i/sin(beta)
                d_2 = d_i
                sum += d_i
                i+=1

            while sumWE <= 4 * 1852:
                L+=(2*1852)/sin(beta)
                d_i = (2 * (b_1 * math.sin(radians(150) - gamma_0))) / (
                    cos(gamma_0) - sin(radians(150) - gamma_0) * 2 * (1 - eta) * a_1 * i)
                eta = calculate_eta(d_2, gamma_0, sum)
                if eta > 0.2 or eta < 0.1:
                    return 0
                sumSN += d_i / cos(beta)
                sumWE += d_i / sin(beta)
                d_2 = d_i
                sum += d_i
                i+=1
            sumSN = (sumWE-4*1852)*tan(beta)
            sumWE = (sumSN - 2 * 1852) * (1 / tan(beta))
            sumSN = 2 * 1852 - sumSN
            sumWE = 4 * 1852 - sumWE
            while sumSN > 0 and sumWE > 0:
                L += sumSN/sin(beta)
                d_i = (2 * (b_1 * math.sin(radians(150) - gamma_0))) / (
                    cos(gamma_0) - sin(radians(150) - gamma_0) * 2 * (1 - eta) * a_1 * i)
                eta = calculate_eta(d_2, gamma_0, sum)
                if eta > 0.2 or eta < 0.1:
                    return 0
                sumSN -= d_i/cos(beta)
                sumWE -= d_i / sin(beta)
                o = d_i/sin(beta)
                d_2 = d_i
                sum += d_i
                i+=1
            sumSN += o
            if sumSN>(sqrt(3)*d_max)/cos(beta):
                L += (sqrt(3)*d_max)/(cos(beta)*sin(beta))
        else:
            d_1 = d_0
            sum = d_1
            d_2 = d_1
            eta = calculate_eta(d_1, gamma_0, sum)
            sum += d_2
            i = 2
            sumSN = math.sqrt(3)*D0/math.cos(beta)
            sumWE = math.sqrt(3)*D0/math.sin(beta)
            while sumWE <= 4 * 1852:
                d_i = (2 * (b_1 * math.sin(radians(150) - gamma_0))) / (
                    cos(gamma_0) - sin(radians(150) - gamma_0) * 2 * (1 - eta) * a_1 * i)
                eta = calculate_eta(d_2, gamma_0, sum)
                if eta > 0.2 or eta < 0.1:
                    return 0
                L += sumSN/math.sin(beta)
                sumSN += d_i/cos(beta)
                sumWE += d_i/sin(beta)
                d_2 = d_i
                sum += d_i
                i+=1
            while sumSN <= 2 * 1852:
                L+=(4*1852)/cos(beta)
                d_i = (2 * (b_1 * math.sin(radians(150) - gamma_0))) / (
                    cos(gamma_0) - sin(radians(150) - gamma_0) * 2 * (1 - eta) * a_1 * i)
                eta = calculate_eta(d_2, gamma_0, sum)
                if eta > 0.2 or eta < 0.1:
                    return 0
                sumSN += d_i / cos(beta)
                sumWE += d_i / sin(beta)
                d_2 = d_i
                sum += d_i
                i+=1
            sumWE = (sumSN-2*1852)*(1/tan(beta))
            sumSN = (sumWE - 4 * 1852) * tan(beta)
            sumWE = 4*1852-sumWE
            sumSN = 2 * 1852 - sumSN
            while sumWE > 0 and sumSN > 0:
                L += sumWE/cos(beta)
                d_i = (2 * (b_1 * math.sin(radians(150) - gamma_0))) / (
                    cos(gamma_0) - sin(radians(150) - gamma_0) * 2 * (1 - eta) * a_1 * i)
                eta = calculate_eta(d_2, gamma_0, sum)
                if eta > 0.2 or eta < 0.1:
                    return 0
                sumWE -= d_i/sin(beta)
                sumSN -= d_i /cos(beta)
                o = d_i/sin(beta)
                d_2 = d_i
                sum += d_i
                i+=1
            sumWE += o
            if sumWE>(sqrt(3)*d_max)/cos(beta):
                L += (sqrt(3)*d_max)/(cos(beta)*sin(beta))