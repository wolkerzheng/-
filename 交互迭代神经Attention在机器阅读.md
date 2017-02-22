交互迭代关注机制的神经对于 机器阅读


a novel neural attention architecture to tackle machine comprehension tasks

deploy an iterative alternating attention mechanism that allows a fine-grained exploration of both the query and the document


绪论：
 机器阅读理解越来越接近实际，主要归功于两个方面：
  1.深度学习技术的出现
  2. 基于完形填空查询的机器阅读形式基准点，可以在模型概念和实验分析中快速的集成循环



完形填空式的查询（Cloze-style queries）

a novel neural attention-based inference mode

1.read the document and the query using a recurrent neural network(递归神经网络)
2.deploy an iterative inference process to uncover the inferential links that exist between the missing quety word ,the query,and the document
 involves a novel alternating attention mechanism
  1)attends to some parts of the query
  2)find their corresponding matches by attending to the document 
  3)the result of this alternating search is fed back into the iterative inference process to seed the next search step

paper contrubution:
	present a novel iterative, alternating attention mechanism that, unlike existing models
	 does not compress the query to a single representation, but instead alternates it attention between the query and the document to obtain a fine-grained query representation within a fixed computation time 


CBT ,CNN : two dataset ,cloze-style questions
(Q; D; A; a), 

Alternating Iterative Attention
first : the encoding phase,compute a set of vector representation,acting as a memory of the 
	content of the input document and query
second：the inference phase aims to untangle the complex semantic relationships  linking the 	
	document and the query in order to  provide sufficiently strong evidence for the answer prediction to be successful
	use an iterative process ,at each iteration ,alternates attentive memory accesses to the query and the document.
finally, the prediction phase uses the information gathered from the repeated attentions through 
    the query and the document to maximize the probability of the correct answer
Bidirectional Encoding
 a sequence of words ,a document or a query drawn from a vocabulary.each word is represented by a continuous word embedding matrix. the sequense  is processed by RNN encoder with GRN

Iterative Alternating Attention
    to uncover a possible inference chain that starts at the query and the document and leads to the answer .The inference is modelled by an additional recurrent GRU network。
    
 



iterative alternating attention
to uncover a possible inference chain that starts at the query and the document 

Training details
 stochastic gradient descent(随机梯度下降)
 学习率：0.001
 the batch size to 32 and decay the learning rate by 0.8 

related works 
neural attention models have been applied recently to machine learning and npl 
手写识别，图像分类,机器翻译，问答系统，caption generation。 attention models keep a memory of states that can be accessed at will by learned attention police
模型和之前相关，以前应用在question answering ，attention mechanism来预测最后的概率，
创新点:embedding the query into a single vector representation ,
the repeated tight integration between query attention and document attention,
(这篇文章的方法，很多都是叨叨问答或者其他应用)，作者将各个的有点吸收，结合起来就成了自己的新模型，加了gru，迭代循环
 conclution:

applied in a straightforward way to other tasks such as information retrieval