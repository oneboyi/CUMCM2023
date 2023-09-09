import numpy as np

# 定义参数
width = 4 * 1852  # 海域宽度，单位为米
D_center = 110  # 海域中心的深度，单位为米
theta = np.radians(120)  # 换能器开角，单位为弧度
alpha = np.radians(1.5)  # 坡度，单位为弧度

# 根据给定的重叠率计算最小和最大的测线间距
d_min = 2 * D_center * np.tan(theta / 2) * (1 - 0.2)
d_max = 2 * D_center * np.tan(theta / 2) * (1 - 0.1)

# 遗传算法参数
population_size = 100
num_generations = 500
elite_size = 10
mutation_rate = 0.1

def fitness_continuous_coverage(chromosome):
    total_length = 0
    last_line = 0
    for line in chromosome:
        coverage_width = 2 * (D_center + (line - width/2) * np.tan(alpha)) * np.tan(theta/2)
        overlap = coverage_width - (line - last_line)
        if overlap < d_min or overlap > d_max:
            return 0  # 无效的解
        total_length += line - last_line
        last_line = line

    # 如果最后一个测线没有覆盖到东端，适应度为0
    if last_line + coverage_width < width:
        return 0

    return total_length

def crossover(parent1, parent2):
    idx = np.random.randint(1, len(parent1)-1)
    child1 = np.concatenate((parent1[:idx], parent2[idx:]))
    child2 = np.concatenate((parent2[:idx], parent1[idx:]))
    return child1, child2

def adaptive_mutation(chromosome, fitness_value):
    if np.random.rand() < mutation_rate:
        idx = np.random.randint(0, len(chromosome))
        delta = np.random.uniform(-mutation_rate, mutation_rate) * (d_max - d_min)
        chromosome[idx] += delta

def initialize_population():
    initial_population = []
    for _ in range(population_size):
        angle = np.random.randint(1000, 89000)
        d = np.random.randint(45000,63000)
        one = (angle/1000,d/1000)
        initial_population.append(one)
    return np.array(initial_population)

def enhanced_genetic_algorithm_continuous_coverage():
    population = initialize_population()
    for generation in range(num_generations):
        fitness_values = [fitness_continuous_coverage(chromo) for chromo in population]
        elite_indices = np.argsort(fitness_values)[-elite_size:]
        new_population = [population[i] for i in elite_indices]
        while len(new_population) < population_size:
            parents = np.argsort(fitness_values)[-2:]
            child1, child2 = crossover(population[parents[0]], population[parents[1]])
            new_population.extend([child1, child2])
            for chromo in new_population[-2:]:
                adaptive_mutation(chromo, fitness_continuous_coverage(chromo))
        population = np.array(new_population)
    return population[np.argmax([fitness_continuous_coverage(chromo) for chromo in population])]

best_solution_continuous_coverage = enhanced_genetic_algorithm_continuous_coverage()
best_solution_continuous_coverage
