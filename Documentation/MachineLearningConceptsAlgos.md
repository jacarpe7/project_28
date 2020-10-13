# Machine Learning Concepts & Algorithms

### What is Machine Learning?

In a nutshell, ML uses various algorithms to find patterns from our data and then makes sense of it.  The hardware will essentially learn and make decisions based on this.  There are three main parameters of any ML algorithm:

1. Improve Performance P - this parameter tells the machine if it is up to expectations, such as precision or accuracy [1]
2. At executing a task T - the problem we are trying to solve with the machine [1], in our case proximity sensors with gesture recognition
3. Over time with experience E - this refers to the machine learning from the datasets extracted from the hardware.

Python is the most popular language for ML and data science[1]

### ML Methods

ML algorithms can be broken into several different high-level styles:</br></br>

1. **Supervised Learning** - These are the most common[1] and basically the machine goes through a training process in which we the developers supervise the process.  The initial input data is used to train the machine and it is corrected when it is wrong.  You continue this process until a required level of accuracy/precision is obtained [2].  Common types are **classification** and **regression**:
	1. **Classification** is predicting a class label based on input data, requires training datasets and lots of input/output for learning [3].  There are several types of classification tasks, one being binary which does not sound like something we could use within the context of this projet.  It essentially maps to one of two values, and expected and abnormal state.  What sounds more like something we could use is Multi-Class  classification, which is tasks that have more than 2 classes (an output category)[3].  Since we will have more than 2 gestures, and it is not as simple as normal/abnormal, this seems like the most similar to our problem at hand.  A popular model for multi-class classification according to Brownlee[3] is prediction with a Multinoulli probability distribution.  This will predict the probability that some data input belongs to a given class label.  In our context this could mean the probability that the data represents a specific gesture which we are trying to train the hardware to recognize.  Multi-Label classification is another type of classification task, but here in the context of our project it would mean a single gesture could be translated into multiple inputs, which I don't think we want.
	2. **Regression** is used to model the relationship between variables and predict outputs based on the given regression models.  These correspond to some standard statisical regression models such as linear regression (straight line) and polynomial regression (parabolic curve) to predict the dependent variable value based on the independent input variables [1].
		
2. **Unsupervised Learning** - These are different from the previous algorithm type in that obviously here there is no human-aided training or guidance that takes place [1].  This is more for scenarios where we don't have labelled input data to learn from and still want to find meaningful patterns.  I'm not sure this will apply to our project directly, since we'll be using known and labeled data with specific outputs/responses that we want to elicit.  Most common and useful unsupervised learning types are:
	1. **Clustering** - This algorithm type finds similarities and patterns among various data samples and "clusters" them into group based on these features [1].
	2. **Association** - This is more about learning new details and patterns about large data sets and is commonly used for analyzing customer shopping patterns [1].
	3. **Dimensionality Reduction** - This method seeks to reduce the number of variablwes for the data sample by finding a set of the most representative features [1].
	4. **Anomoly Detection** - This is used to identify abnormal, rare, or unexpected events from the data [1].

### References

[1] ***Machine Learning with Python Tutorial***.  Accessed on: Oct. 13, 2020.  [Online].  Available:  https://www.tutorialspoint.com/machine_learning_with_python/index.htm

[2] J. Brownlee, "A Tour of Machine Learning Algorithms," ***Machine Learning Mastery,*** August 2020. Accessed on: Oct. 13, 2020. [Online]. Available: https://machinelearningmastery.com/a-tour-of-machine-learning-algorithms/

[3] J. Brownlee, "4 Types of Classification Tasks in Machine Learning," ***Machine Learning Mastery,*** August 2020. Accessed on: Oct. 13, 2020. [Online]. Available: https://machinelearningmastery.com/types-of-classification-in-machine-learning/
