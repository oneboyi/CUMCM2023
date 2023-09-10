import numpy as np
import math
from math import *

# 定义参数
width = 4 * 1852  # 海域宽度，单位为米
Dc= 110  # 海域中心的深度，单位为米
theta = np.radians(120)  # 换能器开角，单位为弧度
alpha = np.radians(1.5)  # 坡度，单位为弧度



# 遗传算法参数
population_size = 100
num_generations = 500
elite_size = 10
mutation_rate = 0.1

import math
from math import *


def calculate_gamma_0(alpha, beta_0):
    tangamma_0 = abs(math.tan(math.radians(alpha)) * math.sin(math.radians(180 - beta_0)))
    return tangamma_0

def d_min(Dc):
    d_min = Dc - math.sqrt(5) * 1852 * abs(math.tan(math.radians(alpha)) * math.cos(math.atan(1 / 2)))
    return d_min

def D1(beta,Dc):
    D0 = d_min(Dc)
    D1 = D0 + math.sqrt(3) * D0 * calculate_gamma_0(alpha, beta)
    return D1

def d_max(Dc):
    d_max = Dc + math.sqrt(5) * 1852 * abs(math.tan(math.radians(alpha)) * math.cos(math.atan(1 / 2)))
    return d_max

# 计算测线测线垂面方向坡度tangamma_0
def calculate_tangamma_0(alpha, beta_0):
    tangamma_0 = abs(math.tan(math.radians(alpha)) * math.sin(math.radians(180 - beta_0)))
    return tangamma_0

def gamma0(beta):
    gamma_0 = calculate_tangamma_0(alpha, beta)
    return gamma_0
# 深度D_i
def calculate_d_i(D1, d, gamma_0, i):
    D_i = D1 + (i - 1) * d * gamma_0
    return D_i


# 覆盖范围W_i
def calculate_W_i(D_i, gamma_0, beta):
    a_1 = gamma_0 * math.sin(math.radians(60)) * math.cos(gamma_0) * (
            1 / math.sin(gamma_0 + math.radians(30)) + 1 / math.sin(math.radians(30) - atan(gamma_0))
    )
    b_1 = D1(beta,Dc) * math.sin(math.radians(60)) * math.cos(gamma_0) * (
            1 / math.sin(gamma_0 + math.radians(30)) + 1 / math.sin(math.radians(30) - atan(gamma_0))
    )
    W_i = (D_i * math.sin(math.radians(60)) * math.cos(gamma_0) * (
            1 / math.sin(gamma_0 + math.radians(30)) + 1 / math.sin(math.radians(30) - atan(gamma_0))
    ))
    return W_i

def a1(beta):
    a_1 = calculate_tangamma_0(alpha, beta) * math.sin(math.radians(60)) * math.cos(calculate_tangamma_0(alpha, beta)) * (
           1 / math.sin(calculate_tangamma_0(alpha, beta) + math.radians(30)) + 1 / math.sin(
        math.radians(30) - calculate_tangamma_0(alpha, beta)))
    return a_1
def b1(beta, Dc):
    b_1 = D1(beta,Dc) * math.sin(math.radians(60)) * math.cos(calculate_tangamma_0(alpha, beta)) * (
            1 / math.sin(atan(calculate_tangamma_0(alpha, beta)) + math.radians(30)) + 1 / math.sin(
        math.radians(30) - atan(calculate_tangamma_0(alpha, beta))))
    return b_1




def calculate_eta(d, gamma, s,beta):
    b_1=b1(beta,Dc)
    a_1 = gamma * math.sin(math.radians(60)) * math.cos(atan(gamma0(beta))) * (
            1 / math.sin(atan(gamma) + math.radians(30)) + 1 / math.sin(math.radians(30) - atan(gamma0(beta))))
    eta = 1 - (d * cos(atan(gamma))) / (2 * (a_1 * s + b_1) * sin(150 - atan(gamma)))
    return eta


def calculate_length(beta, d_0, Dc):
    L = 0
    o = 0
    a_1 = a1(beta)
    b_1 = b1(beta,Dc)
    D0 = d_min(Dc)
    if 0 < beta and beta < 90:
        if math.tan(beta) > 0.5:
            d_1 = d_0
            sum = d_1
            sumSN = math.sqrt(3) * D0 / math.cos(beta)
            sumWE = math.sqrt(3) * D0 / math.sin(beta)
            d_2 = d_1
            eta = calculate_eta(d_1, gamma0(beta), sum, beta)
            sum += d_2
            i = 2
            while sumSN <= 2 * 1852:
                d_i = (2 * (b_1 * math.sin(radians(150) - gamma0(beta)))) / (
                        cos(gamma0(beta)) - sin(radians(150) - gamma0(beta)) * 2 * (1 - eta) * a_1 * i)
                eta = calculate_eta(d_2, gamma0(beta), sum, beta)
                # if eta > 0.2 or eta < 0.1:
                #     return 0
                L += sumSN / math.sin(beta)
                sumSN += d_i / cos(beta)
                sumWE += d_i / sin(beta)
                d_2 = d_i
                sum += d_i
                i += 1

            while sumWE <= 4 * 1852:
                L += (2 * 1852) / sin(beta)
                d_i = (2 * (b_1 * math.sin(radians(150) - gamma0(beta)))) / (
                        cos(gamma0(beta)) - sin(radians(150) - gamma0(beta)) * 2 * (1 - eta) * a_1 * i)
                eta = calculate_eta(d_2, gamma0(beta), sum, beta)
                # if eta > 0.2 or eta < 0.1:
                #     return 0
                sumSN += d_i / cos(beta)
                sumWE += d_i / sin(beta)
                d_2 = d_i
                sum += d_i
                i += 1
            sumSN = (sumWE - 4 * 1852) * tan(beta)
            sumWE = (sumSN - 2 * 1852) * (1 / tan(beta))
            sumSN = 2 * 1852 - sumSN
            sumWE = 4 * 1852 - sumWE
            while sumSN > 0 and sumWE > 0:
                L += sumSN / sin(beta)
                d_i = (2 * (b_1 * math.sin(radians(150) - gamma0(beta)))) / (
                        cos(gamma0(beta)) - sin(radians(150) - gamma0(beta)) * 2 * (1 - eta) * a_1 * i)
                eta = calculate_eta(d_2, gamma0(beta), sum, beta)
                # if eta > 0.2 or eta < 0.1:
                #     return 0
                sumSN -= d_i / cos(beta)
                sumWE -= d_i / sin(beta)
                o = d_i / sin(beta)
                d_2 = d_i
                sum += d_i
                i += 1
            sumSN += o
            if sumSN > (sqrt(3) * d_max(Dc)) / cos(beta):
                L += (sqrt(3) * d_max(Dc)) / (cos(beta) * sin(beta))
        else:
            d_1 = d_0
            sum = d_1
            d_2 = d_1
            eta = calculate_eta(d_1, gamma0(beta), sum, beta)
            sum += d_2
            i = 2
            sumSN = math.sqrt(3) * D0 / math.cos(beta)
            sumWE = math.sqrt(3) * D0 / math.sin(beta)
            while sumWE <= 4 * 1852:
                d_i = (2 * (b_1 * math.sin(radians(150) - gamma0(beta)))) / (
                        cos(gamma0(beta)) - sin(radians(150) - gamma0(beta)) * 2 * (1 - eta) * a_1 * i)
                eta = calculate_eta(d_2, gamma0(beta), sum, beta)
                # if eta > 0.2 or eta < 0.1:
                #     return 0
                L += sumSN / math.sin(beta)
                sumSN += d_i / cos(beta)
                sumWE += d_i / sin(beta)
                d_2 = d_i
                sum += d_i
                i += 1
            while sumSN <= 2 * 1852:
                L += (4 * 1852) / cos(beta)
                d_i = (2 * (b_1 * math.sin(radians(150) - gamma0(beta)))) / (
                        cos(gamma0(beta)) - sin(radians(150) - gamma0(beta)) * 2 * (1 - eta) * a_1 * i)
                eta = calculate_eta(d_2, gamma0(beta), sum, beta)
                # if eta > 0.2 or eta < 0.1:
                #     return 0
                sumSN += d_i / cos(beta)
                sumWE += d_i / sin(beta)
                d_2 = d_i
                sum += d_i
                i += 1
            sumWE = (sumSN - 2 * 1852) * (1 / tan(beta))
            sumSN = (sumWE - 4 * 1852) * tan(beta)
            sumWE = 4 * 1852 - sumWE
            sumSN = 2 * 1852 - sumSN
            while sumWE > 0 and sumSN > 0:
                L += sumWE / cos(beta)
                d_i = (2 * (b_1 * math.sin(radians(150) - gamma0(beta)))) / (
                        cos(gamma0(beta)) - sin(radians(150) - gamma0(beta)) * 2 * (1 - eta) * a_1 * i)
                eta = calculate_eta(d_2, gamma0(beta), sum, beta)
                # if eta > 0.2 or eta < 0.1:
                #     return 0
                sumWE -= d_i / sin(beta)
                sumSN -= d_i / cos(beta)
                o = d_i / sin(beta)
                d_2 = d_i
                sum += d_i
                i += 1
            sumWE += o
            if sumWE > (sqrt(3) * d_max(Dc)) / cos(beta):
                L += (sqrt(3) * d_max(Dc)) / (cos(beta) * sin(beta))
    return L

def fitness_continuous_coverage(chromosome,index):
    beta=chromosome[0]
    d_0=chromosome[1]
    len=calculate_length(beta, d_0, Dc)
    value=[]
    value.append(len)
    value.append(index)
    return value


def crossover(parent1, parent2):
    # print(len(parent1))
    idx = np.random.randint(1, len(parent1)-1)
    child1 = np.concatenate((parent1[:idx], parent2[idx:]))
    child2 = np.concatenate((parent2[:idx], parent1[idx:]))
    return child1, child2

def adaptive_mutation(chromosome, fitness_value):
    # if np.random.rand() < mutation_rate:
    #     idx = np.random.randint(0, len(chromosome))
    #     delta = np.random.uniform(-mutation_rate, mutation_rate) * (d_max - d_min)
    #     chromosome[idx] += delta
    return 0

def initialize_population():
    initial_population = []
    for _ in range(population_size):
        line=[]
        for _ in range(22):
            angle = np.random.randint(1000, 89000)
            d = np.random.randint(45000, 63000)
            one = []
            one.append(radians(angle / 1000))
            one.append(d / 1000)
            line.append(one)
        initial_population.append(line)
    return np.array(initial_population)

def enhanced_genetic_algorithm_continuous_coverage():
    population = initialize_population()
    print(population.shape)
    for generation in range(num_generations):
        fitness_values = [fitness_continuous_coverage(chromo,index) for index,chromo in enumerate(population)]
        length = len(fitness_values)
        for i in range(length):
            for j in range(i):
                if fitness_values[i][0] < fitness_values[j][0]:
                    fitness_values[i],fitness_values[j] = fitness_values[j],fitness_values[i]
        elite_indices = fitness_values[-elite_size:]
        new_population = []
        for i in elite_indices:

            new_population.append(population[i[1]])
        while len(new_population) < population_size:
            length1 = len(fitness_values)
            for i in range(length1):
                for j in range(i):
                    if fitness_values[i][0] < fitness_values[j][0]:
                        fitness_values[i], fitness_values[j] = fitness_values[j], fitness_values[i]
            parents = fitness_values[-2:]
            parents0=parents[0][1]
            parents1=parents[1][1]
            # print(fitness_values[-2:],fitness_values[-2:][1])
            # print(parents0,parents1)
            child1, child2 = crossover(population[parents0], population[parents1])
            new_population.extend([child1, child2])
            for chromo in new_population[-2:]:
                adaptive_mutation(chromo, fitness_continuous_coverage(chromo))
        population = np.array(new_population)
    return population[np.argmax([fitness_continuous_coverage(chromo) for chromo in population])]

best_solution_continuous_coverage = enhanced_genetic_algorithm_continuous_coverage()
print(best_solution_continuous_coverage)