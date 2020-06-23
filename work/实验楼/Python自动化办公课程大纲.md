# Python自动化办公课程大纲


## 实验1 Python自动化办公介绍和环境的安装
### 一、实验介绍
- 1.1 知识点
    - 为什么需要Python自动化办公？
    - Python操作Excel、Word、PDF分别用到哪些第三方库
    - 为什么选择这些第三方库？第三方库的安装和验证
    - 自动化办公的演示，并提供代码进行预习。
- 1.2 实验环境
- 课程使用的实验环境为 WebIDE 容器 1G版本。实验中会用到程序：Python
### 二、实验内容
- 2.1 Python自动化办公介绍
    - 为什么需要Python自动化办公？
    - Python操作Excel、Word、PPT、PDF分别用到哪些第三方库
- 2.2 第三方库的安装和验证
    - Excel：xlwings
    - Word：python-docx
    - PDF：PyPDF2和pdfplumber
    - 验证安装成功
    	- pip show XX库
- 2.3 自动化办公的演示
    - 自动化办公Excel演示
    - 自动化办公Word演示
    - 自动化办公PDF演示
    - 自动化办公文件夹演示

---
## 实验2 自动化办公之Excel：Python读写任意Excel中内容
### 一、实验介绍
- 1.1 知识点
    - Python读取Excel为什么选择xlwings？
    - 读取指定Excel的指定内容
    - 写入指定Excel指定内容
- 1.2 实验环境
    - 课程使用的实验环境为 WebIDE 容器 1G版本。实验中会用到程序：Python IDE
### 二、实验内容
- 2.1 xlwings的优势和安装
    - xlwings基础api的介绍
    - ![xlwings优势](https://mmbiz.qpic.cn/mmbiz/SAHDhZ6pPOicbIricia7UAXzbej2CZK0iaicGnBnYdEz9dgmMXTdTDMiaG3M5FoTeFicKGXrgaHPfrwicrwa53xTibVEic3Q/640?wx_fmt=other&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)
- 2.2 读取单个文件
    - 需要使用 glob 库
- 2.3 读取指定sheet
- 2.4 读取指定单元格
- 2.5 批量读取单元格内容
- 2.6 指定单元格赋值并保存
- 2.7 使用excel公式
- 2.8 增加指定sheet
- 2.9 创建新的Excel文件
- 2.10 合并多个Excel到一个Excel

---
## 实验3 自动化办公之Excel：统计小王一年的出勤率
### 一、实验介绍
- 1.1 知识点
    - 单表批量读取Excel内容
    - 计算Excel数据并写入Excel
    - 生成新Excel表格
- 1.2 实验环境
    - 课程使用的实验环境为 WebIDE 容器 1G版本。实验中会用到程序：Python IDE
### 二、实验内容
- 单个Excel文件，单个Sheet，内有每个月小王的签到数据
- 通过Python读取所有数据，并计算当年小王的出勤率，生成一个新的Excel表格
- 拓展：公司的所有员工

---
## 实验4 自动化办公之Excel：超市货物价格批量调整
### 一、实验介绍
- 1.1 知识点
    - 读取指定单元格
    - 指定单元格赋值并保存
    - 增加指定sheet
- 1.2 实验环境
    - 课程使用的实验环境为 WebIDE 容器 1G版本。实验中会用到程序：Python IDE
### 二、实验内容
- 单个Excel文件，单个Sheet，内有超市每个物品区的价格数据
- 通过Python读取所有数据，并通过超市政策，对每个物品进行不同比例的调价

---
## 实验5 自动化办公之Excel：哪些客户的保险该续保了？
### 一、实验介绍
- 1.1 知识点
    - 读取指定sheet
    - 批量读取单元格内容
    - Python定时刷新
- 1.2 实验环境
    - 课程使用的实验环境为 WebIDE 容器 1G版本。实验中会用到程序：Python IDE
### 二、实验内容
- 单个Excel文件，多个Sheet，内有保险客户的数据
- 通过Python读取所有数据，并通过匹配不同Sheet中的日期、金额、人员，核算出哪些人的保险到期了
- 生成新的Sheet，并可以根据需要设置定时刷新

---
## 实验6 自动化办公之Excel：7月车间所有生产线的产量汇总
### 一、实验介绍
- 1.1 知识点
    - 合并多个Excel到一个Excel
- 1.2 实验环境
    - 课程使用的实验环境为 WebIDE 容器 1G版本。实验中会用到程序：Python IDE
### 二、实验内容
- 多个Excel文件，单个Sheet，内有车间多条生产线的产量数据
- 通过Python读取所有数据，并根据不同生产线的名称，汇总计算7月的总产量
- 生成新的Excel，将数据写入其中


---
## 实验7 自动化办公之Word：读取word中的内容，并制作可视化词云
### 一、实验介绍
- 1.1 知识点
    - python-docx介绍，基础api介绍
    - 词云介绍和制作
- 1.2 实验环境
    - 课程使用的实验环境为 WebIDE 容器 1G版本。实验中会用到程序：Python IDE
### 二、实验内容
- 2.1 使用python-docx读取Word内容
- 2.2 利用读取的内容制作词云
    - ![词云效果](http://p2.ssl.cdn.btime.com/t01dc252bfc16898fd5.jpg)

---
## 实验8 自动化办公之PDF：批量加水印、批量加密解密
### 一、实验介绍
- 1.1 知识点
    - PyPDF2 和 pdfplumber 介绍，基础api应用
- 1.2 实验环境
    - 课程使用的实验环境为 WebIDE 容器 1G版本。实验中会用到程序：Python IDE
### 二、实验内容
- 2.1 提取pdf中的文字
- 2.2 合并拆分PDF
- 2.3 添加水印，加密解密

---
## 实验9 自动化办公之文件夹：批量重命名、删除、移动、创建
### 一、实验介绍
- 1.1 知识点
    - os、glob库介绍，基础api应用
- 1.2 实验环境
    - 课程使用的实验环境为 WebIDE 容器 1G版本。实验中会用到程序：Python IDE
### 二、实验内容
- 2.1 批量重命名文件夹
- 2.2 批量删除文件夹
- 2.3 批量移动文件夹
- 2.4 批量创建文件夹