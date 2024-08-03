<!-- C:\Users\razer\Desktop\walkerrh.github.io\SCROLLS_FOLDER\PROGRAMMING\machine_learning.md -->




[Home](/index.html)


Google Machine Learning Education

[](https://developers.google.com/machine-learning)




| Category                | Model Type                            | Description                                                                                       |
|-------------------------|---------------------------------------|---------------------------------------------------------------------------------------------------|
| Supervised Learning     | Linear Regression                     | Predicts continuous target variables.                                                             |
|                         | Logistic Regression                   | Binary classification tasks.                                                                      |
|                         | Decision Trees                        | Tree-like models for classification and regression.                                               |
|                         | Random Forests                        | Ensemble of decision trees for improved accuracy.                                                 |
|                         | Gradient Boosting Machines (GBM)      | Sequential models to reduce errors.                                                               |
|                         | Support Vector Machines (SVM)         | Finds the optimal hyperplane for classification.                                                  |
|                         | Feedforward Neural Networks           | Basic neural network for regression and classification.                                           |
|                         | Convolutional Neural Networks (CNN)   | Primarily for image data.                                                                         |
|                         | Recurrent Neural Networks (RNN)       | For sequential data like time series or text.                                                     |
| Unsupervised Learning   | K-Means                               | Divides data into K clusters.                                                                     |
|                         | Hierarchical Clustering               | Builds a tree of clusters.                                                                        |
|                         | DBSCAN                                | Density-based clustering method.                                                                  |
|                         | Principal Component Analysis (PCA)    | Reduces dimensionality while preserving variance.                                                 |
|                         | t-SNE                                 | Reduces dimensionality for visualization.                                                         |
|                         | Apriori Algorithm                     | Identifies frequent item sets and association rules.                                              |
|                         | FP-Growth                             | Efficient version of the Apriori algorithm.                                                       |
| Semi-Supervised Learning| Self-Training                         | Uses labeled data to label and retrain on unlabeled data.                                         |
|                         | Co-Training                           | Multiple learners iteratively label and train on unlabeled data.                                  |
| Reinforcement Learning  | Q-Learning                            | Value-based method for learning optimal actions.                                                  |
|                         | Deep Q-Networks (DQN)                 | Combines Q-learning with deep neural networks.                                                    |
|                         | Policy Gradient Methods               | Directly optimizes the policy by gradient ascent.                                                 |



### Labels

the thing we're predicting—the y variable in simple linear regression

## Features

an input variable—the x variable in simple linear regression

## labeled example 

includes both feature(s) and the label

## unlabeled example 

contains features but not the label

## Training

means creating or learning the model

empirical risk minimization

## Loss

a number indicating how bad the model's prediction was on a single example

### Squared loss (L_2 Loss)

* the square of the difference between the label and the prediction
* (observation - prediction(x))^2
* (y - y')^2

### Mean square error (MSE)

$$ MSE = \frac{1}{N}\sum_{(x,y)\in D}(y-\text{prediction}(x))^2 $$

* (x,y) 
    * x is the set of features
    * y is the example's label
* prediction(x) is a function of the weights and bias in combination with the set of features x
* D is the data set containing labeled examples, which are (x,y) pairs
* N is the number of examples in D

### Reducing Loss: An Iterative Approach

![](/assets/machine_learning_assets/GradientDescentDiagram.png")

### Reducing Loss: Gradient Descent

The gradient descent algorithm then calculates the gradient of the loss curve at the starting point. The gradient of the loss is equal to the derivative (slope) of the curve, and tells you which way is "warmer" or "colder." When there are multiple weights, the gradient is a vector of partial derivatives with respect to the weights. The gradient vector has both a direction and a magnitude.

![](/assets/machine_learning_assets/GradientDescentGradientStep.png)

### Reducing Loss: Learning Rate

Gradient descent algorithms multiply the gradient by a scalar known as the learning rate (also sometimes called step size) to determine the next point. There's a Goldilocks learning rate for every regression problem. The Goldilocks value is related to how flat the loss function is. If you know the gradient of the loss function is small then you can safely try a larger learning rate, which compensates for the small gradient and results in a larger step size.

![](/assets/machine_learning_assets/LearningRateJustRight.png)

### Batch

The set of examples you use to calculate the gradient in a single training iteration.

### Reducing Loss: Stochastic Gradient Descent

Tt uses only a single example (a batch size of 1) per iteration. Given enough iterations, SGD works but is very noisy. The term "stochastic" indicates that the one example comprising each batch is chosen at random.

### Mini-batch stochastic gradient descent (mini-batch SGD)

A compromise between full-batch iteration and SGD. A mini-batch is typically between 10 and 1,000 examples, chosen at random. Mini-batch SGD reduces the amount of noise in SGD but is still more efficient than full-batch.

## Inference 

means applying the trained model to unlabeled examples

## regression model 

predicts continuous values

## classification model 

predicts discrete values

## Linear Regression

y = mx + b

* y = trying to predict
* m = slope
* x = input feature
* b = y-intercept

y' = b + (w_1)(x_1)

* y' = label (desired output)
* b = bias (y-intercept)
* w_1 = weight (slope)
* x_1 = feature (input)

## Hyperparameters 

The knobs that programmers tweak in machine learning algorithms

## correlation matrix

```python
pandas_dataframe.describe()
pandas_dataframe.corr()
```

indicates how each attribute's raw values relate to the other attributes' raw values

* 1.0: perfect positive correlation; that is, when one attribute rises, the other attribute rises.
* -1.0: perfect negative correlation; that is, when one attribute rises, the other attribute falls.
* 0.0: no correlation; the two columns are not linearly related.

## Overfitting

An overfit model gets a low loss during training but does a poor job predicting new data.

## William of Ockham

a 14th century friar and philosopher, loved simplicity. He believed that scientists should prefer simpler formulas or theories over more complex ones.

## statistical learning theory

## computational learning theory

## empirical evaluation

## Splitting Data

* training set = around 80% of the data
* test set = the other 20% of the data

## Validation Set: Another Partition

This partitioning enabled you to train on one set of examples and then to test the model against a different set of examples. With two partitions, the workflow could look as follows:

![](/assets/machine_learning_assets/WorkflowWithTestSet.png)

You can greatly reduce your chances of overfitting by partitioning the data set into the three subsets shown in the following figure:

![](/assets/machine_learning_assets/PartitionThreeSets.png)

Use the validation set to evaluate results from the training set. Then, use the test set to double-check your evaluation after the model has "passed" the validation set.

![](/assets/machine_learning_assets/WorkflowWithValidationSet.png)

## Feature Engineering

transforming raw data into a feature vector

* feature vector = set of floating-point values comprising the examples in your data set

![](/assets/machine_learning_assets/RawDataToFeatureVector.png)

![](/assets/machine_learning_assets/FloatingPointFeatures.png)

## vocabulary 

defining a mapping from categorical features to the feature values (possible values)

## OOV (out-of-vocabulary) bucket

group all other category

## binary vector

each categorical feature in our model that represents values as follows:

* For values that apply to the example, set corresponding vector elements to 1
* Set all other elements to 0

## vector is equal to the number of elements in the vocabulary

![](/assets/machine_learning_assets/OneHotEncoding.png)

### one-hot encoding

when a single value is 1

### multi-hot encoding 

when multiple values are 1

## sparse representation

Storing only the position(s) of nonzero elements in a sparse feature

## Representation: Qualities of Good Features

* Avoid rarely used discrete feature values
    * Good feature values should appear more than 5 or so times in a data set
* Prefer clear and obvious meanings
* Don't mix "magic" values with actual data
    * features don't contain peculiar out-of-range discontinuities
* Account for upstream instability
    * The definition of a feature shouldn't change over time

## Scaling 

converting floating-point feature values from their natural range (for example, 100 to 900) into a standard range (for example, 0 to 1 or -1 to +1)

## Z score

relates the number of standard deviations away from the mean

$$ \text{scaledvalue} = \frac{(\text{value} - \text{mean})}{\text{stddev}} $$

## Log scaling

## Clipping feature values

all values that were greater than x now become x

## bin by quantile

## Scrubbing

## Feature Crosses: Encoding Nonlinearity 

## feature cross (comes from cross product)

a synthetic feature that encodes nonlinearity in the feature space by multiplying two or more input features together

* [A X B]: a feature cross formed by multiplying the values of two features.
* [A x B x C x D x E]: a feature cross formed by multiplying the values of five features.
* [A x A]: a feature cross formed by squaring a single feature.

# Feature Crosses: Crossing One-Hot Vectors


