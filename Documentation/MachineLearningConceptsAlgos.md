# Machine Learning Concepts & Algorithms

### What is Machine Learning?

In a nutshell, ML uses various algorithms to find patterns from our data and then makes sense of it.  The hardware will essentially learn and make decisions based on this.  There are three main parameters of any ML algorithm:

1. Improve Performance P - this parameter tells the machine if it is up to expectations, such as precision or accuracy [1]
2. At executing a task T - the problem we are trying to solve with the machine [1], in our case proximity sensors with gesture recognition
3. Over time with experience E - this refers to the machine learning from the datasets extracted from the hardware.

Python is the most popular language for ML and data science[1]

### ML Methods

ML algorithms can be broken into several different high-level learning styles:</br></br>

1. **Supervised Learning** - These are the most common[1] and basically the machine goes through a training process in which we the developers supervise the process.  The initial input data is used to train the machine and it is corrected when it is wrong.  You continue this process until a required level of accuracy/precision is obtained [2].  Common types are **classification** and **regression**:
	1. **Classification** is predicting a class label based on input data, requires training datasets and lots of input/output for learning [3].  There are several types of classification tasks, one being binary which does not sound like something we could use within the context of this projet.  It essentially maps to one of two values, and expected and abnormal state.  What sounds more like something we could use is Multi-Class  classification, which is tasks that have more than 2 classes (an output category)[3].  Since we will have more than 2 gestures, and it is not as simple as normal/abnormal, this seems like the most similar to our problem at hand.  A popular model for multi-class classification according to Brownlee[3] is prediction with a Multinoulli probability distribution.  This will predict the probability that some data input belongs to a given class label.  In our context this could mean the probability that the data represents a specific gesture which we are trying to train the hardware to recognize.  Multi-Label classification is another type of classification task, but here in the context of our project it would mean a single gesture could be translated into multiple inputs, which I don't think we want.
	2. **Regression** is used to model the relationship between variables and predict outputs based on the given regression models.  These correspond to some standard statisical regression models such as linear regression (straight line) and polynomial regression (parabolic curve) to predict the dependent variable value based on the independent input variables [1].
		
2. **Unsupervised Learning** - These are different from the previous algorithm type in that obviously here there is no human-aided training or guidance that takes place [1].  This is more for scenarios where we don't have labelled input data to learn from and still want to find meaningful patterns.  I'm not sure this will apply to our project directly, since we'll be using known and labeled data with specific outputs/responses that we want to elicit.  Most common and useful unsupervised learning types are:
	1. **Clustering** - This algorithm type finds similarities and patterns among various data samples and "clusters" them into group based on these features [1].
	2. **Association** - This is more about learning new details and patterns about large data sets and is commonly used for analyzing customer shopping patterns [1].
	3. **Dimensionality Reduction** - This method seeks to reduce the number of variables for the data sample by finding a set of the most representative features [1].
	4. **Anomoly Detection** - This is used to identify abnormal, rare, or unexpected events from the data [1].
	
3. **Semi-Supervised Learning** - This is a combination of the previous 2 types of algorithms and contains both labeled and unlabeled data.  Some of the previous types of algorithms are also part of this section. [1]
	1. **Classification** - See above
	2. **Regression** - See above 
	
### ML Algorithms for the Project

Based on the above research it seems that the best option for our project is going to be supervised learning algorithm, and more specifically a multi-class classification algorithm.  This most correctly will apply to our project; we will have labeled data from which we will need to extract and analyze and "classify" this data into an appropriate output, i.e. categorize the type of gesture being presented to the hardware sensors.  Some popular algorithms that can be used for multi-class classification ML include[3]:

1. **K-Nearest Neighbors** - In simple terms, this algorithm works on the idea that similar data points are near each other, and can be grouped as such[4].  One big disadvantage of this algorithm is that it gets significantly less efficient the larger the data set.  

2. **Decision Trees** - Decision tree algorithms are essentially top to bottom binary trees, with decision nodes, edges and leaves (meaning no further decision is made).  This has some feasibility within the scope of our project, as we could potentially use this to confirm different conditions, leading to a final determination as to what gesture is being presented to the sensors.  There are many types of decision tree algorithms:[2]
	1. **Classification and Regression Tree (CART)** - This is your standard binary tree model that we all know from Data Structures class.   See above description for decision trees.
	2. **Iterative Dichotomiser 3 (ID3)** - This is a specific decision tree algorithm which seeks to create a shallow decision tree and is generally only used for nominal data only.  It uses this data to continuously split the data into 2 opposite sets.  That essentially rules this algorithm out as an option for our project.
	3. **C4.5 and C5.0** - These are both similar in concept to the ID3 algorithm with some minor improvements from each previous version
	4. **Chi-squared Automatic Interaction Detection (CHAID)** - This is a decision tree algorithm that uses the chi-square statistic which correlates to the similarity between 2 data points.  In order to use this one for the project we would need to categorize all of our continuous dependent variables (the sensor readings) into categories[6].
	5. **Decision Stump** - This is a decision tree with only one root node and all leaves then connected to this node.  This is not relevant to the project as we will have much more than a single input value.
	6. **M5** - This is a combination of a decision tree and also uses linear regression modeling at each node as well.  This works well with lots of attributes, and is specifically good for predicting values of numerical responses.[7]

3. **Naive Bayes** - The first piece to understanding the Naive Bayes algorithm is understanding the Bayes Theorem, which is defined by Wikipedia as a theorem in probability theory and statistics that "describes the probability of an event, based on prior knowledge of conditions that might be related to the event."  One key point is that it works best when each of the variables can be considered independent of one another.  In the context of our project it would work by predicting the probability of the data representing a specific gesture.  Each data point would be analyzed for the probability that it independently represents a specific gesture.  One common example of this algorithm's usage is spam email detection.[8]  There are three kinds of this algorithm that are mainly based on how the data is distributed:
	1. **Gaussian Naive Bayes** - When the data is continuous and distribution is Gaussian [8]
	2. **Multinomial Naive Bayes** - Data is multinomial distributed (common use is text classification[8]
	3. **Bernoulli Naive Bayes** - Data is multivariate Bernoulli distributed, meaning that each variable is a binary value with each having *p* and *1-p* probability of occurring (not for this project based on that).
	
4. **Random Forest** - This algorithm is a group of decision trees that work together for a prediction of the class of data (or in our project, the gesture being presented) [1]

5. **Gradient Boosting** - Works by iteratively learning from previous predictions with non-linear functions.  This algorithm will be best used when the number of independent variables in the data is not significant and when non-linear models are a more appropriate fit for the data points.  

6. **Logistic Regression** - This algorithm is more specific and useful for binary classification which will not apply to our project.  Abstract real world examples are spam/not spam, pass/fail, etc.  

7. **Support Vector Machine** - Some real world applications of this algorithm are face detection, image classification, text classification, and bioinformatics.  

### Other ML Algorithms

There are many ML algorithms, an overwhelming amount actually.  Here's a Wikipedia [link](https://en.wikipedia.org/wiki/Outline_of_machine_learning#Machine_learning_methods) with a nice list of many others for review.

### Summary

After much research I feel like we are just scratching the surface on Machine Learning and the different kinds of algorithms that can be used.  It seems that the best type of algorithm for this project is going to be a **Supervised, Multi-Class Classification algorithm**.  Some of the specific algorithms to take deep dives in are going to be **K-Nearest Neighbors, Random Forest/decision trees, Support Vector Machine, and Naive Bayes**.  We may want to implement multiple algorithms and find the one that is most accurate for our training and test data sets.

### References

[1] *Machine Learning with Python Tutorial*.  Accessed on: Oct. 13, 2020.  [Online].  Available:  https://www.tutorialspoint.com/machine_learning_with_python/index.htm

[2] J. Brownlee, "A Tour of Machine Learning Algorithms," *Machine Learning Mastery,* August 2020. Accessed on: Oct. 13, 2020. [Online]. Available: https://machinelearningmastery.com/a-tour-of-machine-learning-algorithms/

[3] J. Brownlee, "4 Types of Classification Tasks in Machine Learning," *Machine Learning Mastery,* August 2020. Accessed on: Oct. 13, 2020. [Online]. Available: https://machinelearningmastery.com/types-of-classification-in-machine-learning/

[4] O. Harrison, "Machine Learning Basics with the K-Nearest Neighbors Algorithm," *Towards Data Science,* September 2018. Accessed on: Oct. 14, 2020. [Online]. Available: https://towardsdatascience.com/machine-learning-basics-with-the-k-nearest-neighbors-algorithm-6a6e71d01761

[5] P. Gupta, "Decision Trees in Machine Learning," *Towards Data Science,* May 2017. Accessed on: Oct. 14, 2020. [Online]. Available: https://towardsdatascience.com/decision-trees-in-machine-learning-641b9c4e8052

[6] J. Ramzai, "Simple guide for Top 2 types of Decision Trees: CHAID & CART," *Towards Data Science,* June 2020. Accessed on: Oct. 14, 2020. [Online]. Available: https://towardsdatascience.com/clearly-explained-top-2-types-of-decision-trees-chaid-cart-8695e441e73e

[7] S. Shaier, "ML Algorithms: One SD - Decision Trees Algorithms," *Towards Data Science,* February 2019. Accessed on: Oct. 14, 2020. [Online]. Available: https://towardsdatascience.com/ml-algorithms-one-sd-%CF%83-decision-trees-algorithms-746e866ac3f

[8] R. Dwivedi, "What is Naive Bayes Algorithm in Machine Learning?," *Analytics Steps,* April 2020. Accessed on: Oct. 16, 2020. [Online]. Available: https://www.analyticssteps.com/blogs/what-naive-bayes-algorithm-machine-learning

[9] J. Brownlee, "Logistic Regression for Machine Learning," *Machine Learning Mastery,* August 2020. Accessed on: Oct. 16, 2020. [Online]. Available: https://machinelearningmastery.com/logistic-regression-for-machine-learning/

