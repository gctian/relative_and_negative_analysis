# 项目说明




### 1. 环境部署

 - Ubuntu/CentOS环境
 - pip install jieba
 - pip install pandas
 - pip install numpy
 - pip insatll scipy
 - pip install -U scikit-learn

### 2. 相关性分析

    
执行根目录下negative_analysis.py文件，在根目录下python negative_analysis.py即可，然后等待加载模型，模型加载成功后给出输入一段文本的提示，
输入一段和国网有关的文本，模型会给出预测结果。0表示国网负面，1表示国网正面。输入quit退出程序。

### 3. 负面舆情识别

执行根目录下negative_analysis.py文件，在根目录下python negative_analysis.py即可，然后等待加载模型，模型加载成功后给出输入一段文本的提示，
输入一段和国网有关的文本，模型会给出预测结果。0表示国网负面，1表示国网正面。输入quit退出程序。

### 4. 预处理及训练
此版本是加载训练好的模型，直接对一句话进行预测。关于具体的预处理及训练过程，请见StateGrid项目下的text_classify文件夹。
