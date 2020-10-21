# Decision Tree Algorithms

### Overview
The general idea of Decision Trees in machine learning is the basic binary tree structure that we are already familiar with.  A big part of using this is determining exactly which attributes and what values of those attributes will be used to split the data at each decision node.  Generally speaking, a decision tree works by finding the best attribute in the data set to split the records.  They we recursively select attributes to break the data into smaller and smaller subsets.  One way of selecting the attribute to split the data on is a statistical concept known as **Information Gain**.  A picture description is provided below in Figure 1. 

![information-gain](https://i.ibb.co/NtWhC3b/information-gain.jpg) </br>
*Figure 1 - Information Gain, image captured from [1]* </br></br>

The higher the information gain the better we have split the data and moved towards a classification for the data.  Within the scope of our project this could be used to select various partitions of data ranges that various sensors could return and it would essentially create an if/then series of statements that would categorize the gesture presented to the sensors based on each value of the different variables. I found a very detailed description of classification and regression trees [here](http://pages.stat.wisc.edu/~loh/treeprogs/guide/wires11.pdf).  It provides psuedo code for several differen types of tree algorithms.

### Splitting the Data at Decision Nodes
There are many ways to split the data, I'll review 2 main ones:  The Gini Split and Information Gain (previously mentioned).

1. Gini Split is better for larger partitions and is utilizes the sum of the square of probabilities of the various classes (gestures) for that value.  Here's the formula, screenshot from [3] below in Figure 2:

![gini_formula](https://i.ibb.co/R3X4HZW/gini-formula.jpg")</br>
*Figure 2 - the Gini Formula* </br></br>

And here's some psuedo code that describes the steps of the Gini calculation (also taken directly from [3]):

    > for each branch in split:
        > Calculate percent branch represents (Used for weighting)
        > for each class in branch:
            > Calculate probability of class in the given branch.
            > Square the class probability.
        > Sum the squared class probabilities.
        > Subtract the sum from 1. (This is the Ginin Index for branch)
    > Weight each branch based on the baseline probability.
    > Sum the weighted gini index for each split.
	
You want a split at each decision node that has a low Gini index value.  A typical decision tree type that uses Gini is the **CART decision tree algorithm**.

2. I've already discussed what Information Gain is, now let's use it to split the data.  This is better for less data that has more unique values.  Here's the formula, screenshot from [3] below in Figure 3:

![entropy_formula](https://i.ibb.co/1JjKbsh/entropy-formula.jpg)</br>
*Figure 3 - Entropy formula used in Information Gain* </br></br>

And here's some psuedo code that describes the steps of the Gini calculation (also taken directly from [3]):

    > for each branch in split:
        > Calculate percent branch represents (Used for weighting)
        > for each class in branch:
            > Calculate probability of class in the given branch.
            > Multiply probability times log(Probability,base=2)
            > Multiply that product by -1
        > Sum the calculated probabilities.
    > Weight each branch based on the baseline probability.
    > Sum the weighted entropy for each split.

### References

[1] D. Poojari, "Machine Learning Basics: Decistion Tree From Scratch" *Towards Data Science,* August 2019. Accessed on: Oct. 21, 2020. [Online]. Available: https://towardsdatascience.com/machine-learning-basics-descision-tree-from-scratch-part-i-4251bfa1b45c

[2] "Data Mining + Marketing in Plain English" *Learn by Marketing,* Accessed on: Oct. 21, 2020. [Online]. Available: http://www.learnbymarketing.com/481/decision-tree-flavors-gini-info-gain/#:~:text=Summary%3A%20The%20Gini%20Index%20is,of%20each%20class%20from%20one.&text=Information%20Gain%20multiplies%20the%20probability,partitions%20with%20many%20distinct%20values.
