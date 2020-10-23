# Naive Bayes Algorithm

### Overview
Naive Bayes algorithms are used for classification and are based on Bayes' Theorem.  A pretty straightforward explanation of that theorem can be found [here](https://www.mathsisfun.com/data/bayes-theorem.html).  The algorithm depends on independence of every pair of variables.  A good example I saw on [1] is that a fruit could be considered an apple if it is round/spherical, red, and around 3 inches in diameter.  Each of those properties are independent of each other but they all contribute to the probabiliy that it is an apple.  In the context of our project we would take each variable from the sensor data and independently determine the probability of which gesture each represents.  

### Real World Applications
Some common applications of this algorithm are real time predictions, multi-class (which is our project), text classification and natural language processing.  

### Types of Naive Bayes Algorithms
As mentioned in a previous document, there are three main types of Naive Bayes algorithms:

1.  **Gaussian** - used for classification with data that has a normal (Gaussian) distribution.  This would be the one for our project I believe, assuming we went with this algorithm in the project.  If the data does not have a normal distribution you can use various methods (such as simple transformations) to convert the data to such.  We calculate the mean and standard deviation of the input data to use this against continuous value data.

2.  **Multinomial** - used for data with discrete values.  this would be used in a text classification scenario where we are counting the number of instances of words.  We are dealing with integers only here and it would not be valid for our project's sensor data.

3.  **Bernoulli** - This is not going to be applicable to our project either due to it's binary nature.

### Our Project
If we were to use the Naive Bayes Algorithm for our ML in the project, we'd definitely use the Gaussian approach.  Since the data the sensors provide will not be dependent on each other (only dependent on the gesture being used) this is a viable option for our project as well.


### References
[1] S. Ray, "6 Easy Steps to Learn Naive Bayes Algorithm with codes in Python and R" *Analytics Vidhya,* September 2017. Accessed on: Oct. 22, 2020. [Online]. Available: https://www.analyticsvidhya.com/blog/2017/09/naive-bayes-explained/

[2] B. Stecanella, "A practical explanation of a Naive Bayes classifier" *MonkeyLearn,* May 2017. Accessed on: Oct. 22, 2020. [Online]. Available: https://monkeylearn.com/blog/practical-explanation-naive-bayes-classifier/

