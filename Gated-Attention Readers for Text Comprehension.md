Gated-Attention Readers for Text Comprehension

研究短文本完形填空

a new attention mechanism .uses multiplicative interactions between the query embedding and intermediate states of a recurrent neural network reader

数据：CNN & Daily Mail news stories and Children's Book Test

compute an element-wise product between the query embedding and document representations at the intermediate layers of a  Bidirectional GRU

GRU的重置门和遗忘门,the element-wise product simply helps it focus on the query

Related Work:
  (d,q,a),d 是文档，q是问答问题,a是答案. 答案来自于固定词汇A(dataset中)。任务可以被描述为：document-query pair(d,q) ,

   LSTMs with Attention:

 use recurrent neural networks to read the document and query, but use a different attention mechanism and restrict candidate answers to the tokens appearing in the document

Memory Networks
   输入稳定中的每句话s encoded to memory m .



