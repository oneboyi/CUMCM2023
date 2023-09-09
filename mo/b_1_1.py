import pandas as pd
from math import *
import math


def coverage_width_and_overlap_rate():
    D0 = 70  # 初始点深度
    theta = radians(120)
    alpha = radians(1.5)
    dist = [-800, -600, -400, -200, 0, 200, 400, 600, 800]  # 测线距中心点处的距离

    width = []
    width_left = []
    width_right = []
    overlap_rate = []
    depth = []
    overlap_rate.append(-1)
    for index, dis in enumerate(dist):
        D = None
        if dis >= 0:
            D = D0 - dis * tan(alpha)  # 新的深度

        if dis < 0:
            dis = fabs(dis)
            D = D0 + dis * tan(alpha)  # 新的深度
        # 计算宽度
        # D左侧宽度
        w_l = D * sin(theta / 2) * (1 / sin(radians(30)-alpha))
        # D右侧宽度
        w_r = D * tan(theta / 2) * (1 / (cos(alpha) + sin(alpha) * tan(theta / 2)))
        W = w_l + w_r  # 宽度

        width_left.append(w_l)
        width_right.append(w_r)
        width.append(W)
        depth.append(D)

        if index > 0:
            # 计算覆盖率
            d = 200
            overlap = (width_right[index-1]+width_left[index])-(d/cos(alpha))
            rate=(overlap/width[index])*100
            overlap_rate.append(rate)

        # 结果存储到DataFrame
    df_result = pd.DataFrame({
        '测线距中心点处的距离/m': dist,
        '海水深度/m': depth,
        '覆盖宽度/m': width,
        '与前一条测线的重叠率/%': overlap_rate
    })

    #报存
    file_path = "result1_1.csv"
    df_result.to_csv(file_path, index=False, encoding='utf-8-sig')
    print(f"结果已保存到 {file_path}")




if __name__ == "__main__":
    coverage_width_and_overlap_rate()