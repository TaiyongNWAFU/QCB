# This are scripts for deal with QCB project.
author: caominghao	date: 2024.6.13
****
## 1.文件说明
```shell
## (1)snp_calling
将下机的fastq文件一步转为vcf和gvcf
## (2)pop_struc
基于vcf文件中遗传变异信息，构建品种系统发育树、主成分分析、血统组成
## (3)pop_divers
基于vcf文件中遗传变异信息，评估各群体之间的遗传分化程度（FST）、核苷酸多样性（PI）、连锁不平衡衰减（LD decay）
## (4)pop_select
急于vcf文件中的遗传变异信息，使用窗口扫描的方式筛选两群体间受选择的区域（FST、PI、XPCLR、GWAS）


## script
代码中所有的软件、脚本都可以在此文件夹内找到
```

## 2.示例文件 
```shell
## 输入文件
/examlple/data.csv
## 结果文件
/example/p_values_with_genes.csv
```
## 3.选择信号（HKA test）
```shell
## (1)测试数据在 ./example/data.csv
## (2)注意修改脚本：hka_v2.py 中，line12中数据的路径和名字
## (3)使用python3 hka_v2.py，进行HKA test。
```
