
## 2023年全国大学生数学建模竞赛时间安排  

### 重要时间点
    9.10，22：00前——完成选题，提交md5码
    9.10，20：00后只能再上传一次
    9.11，20：00前——完成论文与支撑材料的上传，必须与md5码相匹配,因此必须备份
    
## 文件结构说明
### 文件（夹）描述
    'cumcmthesis.cls'是模板文件，'documentclass'中调用
    'example.pdf'是模板例子的生成文件，可供参考
    'example.tex'是模板的初始tex文件，可供参考
    'example'后续需要修改为论文标题
    'figures'文件夹存放需要用到的图片
    'original template'文件夹存放模板的原始文件
### Tex模板'cumcmthesis.cls'说明
    模板中有已定义环境如定理、推论等
    文献引用使用'bibitem'形式
    表格使用三线表，'tabular'形式
    代码使用'tcode'形式
## 问题一分析
   先计算中间三个，再计算第一个，最后计算最后一个，已知的数据是当地经纬度与定日镜和吸收塔的参数，从而可以推算出入射光线的方向向量，从而计算出每个定日镜的余弦效率。

   阴影损失分为三个部分，反射遮挡、直射遮挡、塔遮挡





<!-- cumcmthesis 是为全国大学生数学建模竞赛编写的 `LaTeX` 模板, 旨在让大家专注于
论文的内容写作, 而不用花费过多精力在格式的定制和调整上. 本手册是相应的参考, 其
中提供了一些环境和命令可以让模板的使用更为方便. 同时需要注意, 使用者需要有一
定的 `LaTeX` 的使用经验, 至少要会使用 `ctex` 宏包的一些功能, 比如调节字距或修改字体
大小等等. 例子文件参看 [example.pdf](https://github.com/latexstudio/CUMCMThesis/blob/master/example.pdf).

另外, 本模板制作了视频使用教程, 参看[这里](https://item.taobao.com/item.htm?spm=a1z10.1-c.w4004-3473795048.2.ZlPoPL&id=43823508044). 

<img src="https://github.com/latexstudio/CUMCMThesis/blob/master/figures/gongzhonghao2.png" alt="" width="350px">




2019年建模模板的免费视频教程：

第一部分：
[https://www.bilibili.com/video/av64191560](https://www.bilibili.com/video/av64191560)

第二部分：
[https://www.bilibili.com/video/av64221508](https://www.bilibili.com/video/av64221508)


![](https://github.com/latexstudio/CUMCMThesis/blob/master/example-1.png)

![](https://github.com/latexstudio/CUMCMThesis/blob/master/example-3.png)

![](https://github.com/latexstudio/CUMCMThesis/blob/master/example-4.png)

## 更新记录
2021 年 7 月：
1， 更新 uline 与 hspace 的兼容问题。

2020 年 8 月：

1，适配官网新格式的封面和编号页。格式在[这里](http://www.mcm.edu.cn/html_cn/node/2ecdb523ea364d8fff6928ada7ebd923.html)

2，调整了部分的内容和说明。

2019年9月更新：

1，适配官网格式：[http://mcm.edu.cn/html_cn/node/8e7b0262daa56b8953d1b6ccaada9ed4.html](http://mcm.edu.cn/html_cn/node/8e7b0262daa56b8953d1b6ccaada9ed4.html)。

2，增加了更新说明，格式的说明，视频依然可以使用！

2019年8月更新：

1，更新说明文件和样例。

2，增加了免费视频教程和基础知识介绍。

2018年9月14日更新：

1，修改前面的承诺书内容。

2，修改附录链接问题，目录格式。

2017年8月14日更新说明：

1. 请大家使用较新的 `LaTeX` 发行版本进行编译，下载地址：http://www.latexstudio.net/page/texsoftware 首页焦点图。不要使用 `CTeX` 套装。

2. 遇到问题可以到91940767群进行交流或478023327群交流

2017年7月28日更新:

1. 适配2016年的格式要求，调整了承诺和编号页的内容。

2. 修改了附录的代码输入样式。


如果需要去掉封面并把论文标题保留在摘要上面，在加载类的使用如下语句：
```
    \documentclass[withoutpreface,bwprint]{cumcmthesis}
```
如果需要封面页，则是与原来一致：
```
    \documentclass[bwprint]{cumcmthesis}
``` -->
