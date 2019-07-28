# About Deep learning  
## Train trick  
## Model architecture  
### 空洞卷积  
[Multi-scale context aggregation with dilated convolutions](https://arxiv.org/pdf/1511.07122.pdf)  
[Blog: https://blog.csdn.net/suixinsuiyuan33/article/details/79451069](https://blog.csdn.net/suixinsuiyuan33/article/details/79451069)

首先是诞生背景，在图像分割领域，图像输入到CNN（典型的网络比如FCN[3]）中，
FCN先像传统的CNN那样对图像做卷积再pooling，降低图像尺寸的同时增大感受野，
但是由于图像分割预测是pixel-wise的输出，所以要将pooling后较小的图像尺寸
upsampling到原始的图像尺寸进行预测（upsampling一般采用deconv反卷积操作，
deconv可参见知乎答案如何理解深度学习中的deconvolution networks？），之
前的pooling操作使得每个pixel预测都能看到较大感受野信息。因此图像分割FCN中
有两个关键，一个是pooling减小图像尺寸增大感受野，另一个是upsampling扩大图
像尺寸。在先减小再增大尺寸的过程中，肯定有一些信息损失掉了，那么能不能设计一种
新的操作，不通过pooling也能有较大的感受野看到更多的信息呢？答案就是dilated conv。

dilated的好处是不做pooling损失信息的情况下，加大了感受野，让每个卷积输出都包
含较大范围的信息。在图像需要全局信息或者语音文本需要较长的sequence信息依赖的问题中，
都能很好的应用dilated conv，比如图像分割[3]、语音合成WaveNet[2]、机器翻译ByteNet[1]中
。简单贴下ByteNet和WaveNet用到的dilated conv结构，可以更形象的了解dilated conv本身。

## Loss function  
### L1,L2,L0区别，为什么可以防止过拟合  
[https://www.jianshu.com/p/475d2c3197d2](https://www.jianshu.com/p/475d2c3197d2)
- 1）实现参数的稀疏有什么好处吗？一个好处是可以简化模型，避免过拟合。因为一个模型中真正重要的参数可能并不多
，如果考虑所有的参数起作用，那么可以对训练数据可以预测的很好，但是对测试数据就只能呵呵了。
另一个好处是参数变少可以使整个模型获得更好的可解释性。

- 2）参数值越小代表模型越简单吗？是的。
为什么参数越小，说明模型越简单呢，这是因为越复杂的模型，越是会尝试对所有的样本进行拟合，
甚至包括一些异常样本点，这就容易造成在较小的区间里预测值产生较大的波动，这种较大的波动也
反映了在这个区间里的导数很大，而只有较大的参数值才能产生较大的导数。因此复杂的模型，其参数值会比较大。

## ML  
### K-means  
### SVM 

