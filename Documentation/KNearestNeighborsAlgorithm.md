# K Nearest Neighbors Algorithm
 
### Overview
The K Nearest Neighbors algorithm (KNN) is a supervised learning ML algorithm typically used in classification and regression.  It uses the distance from other points in the data set to determine how to classify the given data.  There are 3 different types of distance formulas to use (see Figure 1) but the most common is Euclidian distance; the idea is that similar data points will be closer together in Euclidian space.  The selection of the k value to use (which equals the number of elements in your training data set) needs to be chosen after inspecting the data.  Typically the higher the value the more sensitive the classification algorithm will be [2].  

![distance_functions](https://i.ibb.co/VLM54NP/distance-functions.jpg)</br>
*Figure 1 - distance functions [1]* </br></br>

Euclidian is usually best if the data is all the same type (as ours is), while Hamming method of distance calculation is better when they are represent different classes of data (such as age, height, weight, etc) [3].

The viability of KNN within the context of our project is dependent on the number of dimensions that the proximity sensors will use.  We do not have sample data yet (since we don't have proximity sensors yet), but calculating the distance between data points in higher and higher dimensions gets increasingly complex and "spacious".  Basically we could have 2 points which represent the same gesture but are very far apart.  This is known as the "curse of dimensionality" [3].  In the context of our project this may not be a viable solution for more than 3 dimensions.  So if we have a single variable for each of 3 sensors, this could work.  Any more than that and we may need to look at other algorithms as our first option.

### Real World Example

One example of this being used in the real world is when Netflix or Amazon try to recommend different movies to watch or products you might be interested in.  They will use KNN on your data, i.e. the movies you've watched and products you have purchased on their website, and with data from all customers with similar watches and purchases they fill classify you into a customer profile and know what to recommend to you.  

### Steps to using KNN

1. The algorithm is really dependent on good training data.  It works lazily against that data so it should be updated, pruned, and all bad entries removed when possible.  Once a new data point is received it will check against the K neighbors based on distance (see above).
2. The value to use for K needs to be "found" by trial and error.  According to Brownlee it is best to try many different K values to find the one that works best for your given data set.
3. The K nearest neighbors are then polled for which class they each belong to.
4. The class which represents to most nearest neighbors will then be used to classify the new data point.

A good example of this being used in Python can be found [here](https://machinelearningmastery.com/tutorial-to-implement-k-nearest-neighbors-in-python-from-scratch/)

### References

[1] S. Sayad, "An introduction to Data Science: K Nearest Neighbors - Classification," Accessed on: Oct. 19, 2020. [Online]. Available: https://www.saedsayad.com/k_nearest_neighbors.htm

[2] *1.6. Nearest Neighbors*.  Accessed on: Oct. 19, 2020.  [Online].  Available:  https://scikit-learn.org/stable/modules/neighbors.html

[3] J. Brownlee, "K-Nearest Neighbors in Machine Learning," *Machine Learning Mastery,* August 2020. Accessed on: Oct. 19, 2020. [Online]. Available: https://machinelearningmastery.com/k-nearest-neighbors-for-machine-learning/
