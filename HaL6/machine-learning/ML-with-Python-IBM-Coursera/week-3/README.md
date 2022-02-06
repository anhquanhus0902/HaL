### Introduction to Classification

#### What is classification?

- A supervised learning approach

- Categorizing some unknown items into a discrete set of categories or "classes"

- The target attribute is a categorical variable

#### How does classification work?

Classification determines the class label for an unlabeled test case.

#### Classification algorithms in ML

- Decision Trees (ID3, C4.5, C5.0)

- Naive Bayes

- Linear Discriminant Analysis

- k-Nearest Neighbor

- Logistic Regression

- Neural Networks

- Support Vector Machines (SVM)

### K-Nearest Neighbours

#### What is KNN?

The KNN algorithm is a classification algorithm that takes a bunch of labeled points and uses them to learn how to label other points. <br />

- A method for classifyng cases based on their similarity to other cases

- Cases that are near each other are said to be "neighbors"

- Based on similar cases with same class labels are near each other

#### The KNN algorithm

1. Pick a value for K

2. Calculate the distance of unknown case from all cases

3. Select the K-observations in the trainning data that are "nearest" to the unknown data point.

4. Predict the response of the unknown data point using the most popular response value from the K-nearest neighbors.

#### Calculating the similarity/distance in a dimensional space

Euclidean distance: <br /> ![render.png](https://2.pik.vn/20226e030c0d-59c9-4237-88bb-8e8ab29bc8e6.png)

#### What is the best value of K for KNN?

The general solution is to reverse a part of your data for testing the accuracy of the model. <br />

Choose K equals one and then use the training part for modeling and calculate the accuracy of prediction using all samples in your test set. Repeat this process increasing the K and see which K is best for your model. <br />

#### Computing continuous targets using KNN

KNN can also be used for regression

### Evaluation Metrics in Classification

#### Classification accuracy

There are different model evaluation metrics but we just talk about three of them:

- Jaccard index
- F1-score
- Log Loss

#### Jaccard index

![render.png](https://2.pik.vn/2022ef8b1a22-c692-47cf-a93c-5be8e5f49043.png)

#### F1-score

TP = number of true positives <br />
FP = number of false positives <br />
FN = number of true negatives

- Precision = TP/(TP + FP)

- Recall = TP/(TP+FN)

- F1-score = 2 x (prc x rec)/(prc + rec)

#### Log loss

Performance of a classifier where the predicted output is a probability value between 0 and 1. <br />

![render.png](https://2.pik.vn/2022f4ee9dcc-5f38-4975-997e-0c77d4111ae7.png)


### Introduction to Decision Trees

#### What is a decision tree?

> The basic intuition behind a decision tree is to map out all possible decision paths in the form of a tree.

#### Build a decision tree with the trainning set

- Each internal node corresponds to a test

- Each branch corresponds to a result of the test

- Each leaf node assigns a classification

#### Decision tree learning algorithm

1. Choose an attribute from your dataset

2. Calculate the significance of attribute in splitting of data

3. Split data based on the value of the best attribute

4. Go to step 1

### Building Decision Trees

#### Which attribute is the best?

A node in the tree is considered pure if in 100 percent of the cases, the nodes fall into a specific category of the target field.

Impurity of nodes is calculated by entropy of data in the node.

> The tree with the higher Information Gain after splitting

#### Entropy

The entropy in the node depends on how much random data is in that node and is calculated for each node. <br />

The lower the Entropy, the less uniform the distribution, the purer the node. <br />

<p align="center">
  Entropy = - p(A)log(p(A)) - p(B)log(p(B)) <br />
  P is for the proportion or ratio of a category
</p>

#### What is Information Gain

Information gain is the information that can increase the level of certainly after splitting.

<p align="center">
  IG = (Entropy before split) - (weighted entropy after split)
</p>

### Intro to Logistic Regression

#### What is logistic regression?

Logistic regression is a classification algorithm for categorical variables. <br />

In logistic regression, independent variables should be continuous. If categorical, they should be dummy or indicator coded.

#### Logistic regression applications

- Predicting the probability of a person having a heart attack

- Predicting the mortality in injured patients

- Predicting a customer's propensity to purchase a product or halt a subscription

- Predicting the probability of failure of a given process or product

- Predicting the likelihood of a homeowner defaulting on a mortgage

#### When is logistic regression suitable?

- If your data is binary
  - 0/1, true/false, YES/NO

- If you need probabilistic results

- When you need a linear decision boundary

- If you need to understand the impact of a feature

### Logistic regression vs Linear regression

#### Sigmoid function in logistic regression

- Logistic Function
- The sigmoid functions output is always between 0 and 1

![render.png](https://2.pik.vn/2022ee223bb4-3896-464d-870d-aad40c88c684.png) <br />

#### The training process

1. Initialize theta

2. Calculate y_hat = sigmoid((theta transpose) * X)

3. Compare the output of y_hat with actual output, y, and record it as error

4. Calculate the error for all records
  - The total error is the cost of your model and is calculated by the models cost function.

5. Change the theta to reduce the cost

6. Go back to the step 2

### Logistic Regression Trainning

#### General cost function

![render.png](https://2.pik.vn/2022f51f605e-9a4a-46af-829c-8ac538b66eca.png) <br />

![render.png](https://2.pik.vn/2022dd055dd9-3b67-40a4-8249-5123cb828f7f.png) <br />

#### Logistic cost function

- If y = 1: Cost(y_hat, y) = -log(y_hat)
- If y = 0: Cost(y_hat, y) = -log(1 - y_hat)

![render.png](https://2.pik.vn/202270ccae5d-9d4e-4f35-a139-5fe2227b344d.png)

#### Minimizing the cost function of the model

- How to find the best parameters for our model?
  - Minimize cost function

- How to minimize the cost function?
  - Using Gradient Descent

- What is Gradient Descent?
  - A technique to use the derivative of a cost function to change the parameter values, in order to minimize the cost

#### Using gradient descent to minimize the cost

![render.png](https://2.pik.vn/202294355b0c-aef7-4303-9970-401af46c805d.png) <br />

![render.png](https://2.pik.vn/2022ec857bdb-c764-4acf-bc34-dc7535553b4c.png) <br />

![render.png](https://2.pik.vn/2022238e58c2-ce52-4808-90b0-a0771890ce45.png) <br />

#### Training algorithm 

1. Initialize the parameters randomly

2. Feed the cost function with trainning set, and calculate the error

3. Calculate the gradient of cost function

4. Update weights with new values.

5. Go to step 2 until cost is small enough

6. Predict

### Support Vector Machjne

#### What is SVM?

SVM is a supervised algorithm that classifies cases by finding a separator.

1. Mapping data to a high-dimensional feature space

2. Finding a separator

#### Data transformation

Mapping data into a higher-dimensional space is called, kernelling. <br />

The mathematical function used for the transformation is known as the kernel function, and can be of different types, such as linear, polynomial, Radial Basis Function,or RBF, and sigmoid.

#### Using SVM to find the hyperplane

#### Pros and cons of SVM

- Advantages:
  - Accurate is high-dimensional spaces
  - Memory efficient

- Disadvantages:
  - Prone to over-fitting
  - No probability estimation

#### SVM Applications

- Image recognition
- Text category assignment
- Detecting spam
- Sentiment analysis
- Gene Expression Classification
- Regression, outlier detection and clustering