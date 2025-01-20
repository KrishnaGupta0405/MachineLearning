__Welcome to My Machine Learning Journey!__

Hey there! I'm Krishna Gupta, i had spent my last six months in learning the art of Machine Learning and yeah it's still going on. 
In this repo i will be giving my Recipe's of diffrent Machine Learning Algorithms, some project starting from the basic one's followed by advanced.. , 
and crisp short notes to for better understanding of the codes ╰(*°▽°*)╯

Here you can find Short Notes fo each topic
Level 1- Data Preprocessing
Level 2- Regression Model
Level 3- Classification Model
Level 4- Clustering Model
Level 5- Association Rule Learning
Level 6- Reinforcement Learning


Popular function's meaning->
    •>Fit - telling the algorithm to learn about how diffrent featues contribute in an output thier behavious and so on, just like telling the baby about learning how to create lego tower using multiple blocks like.
    •>Transform - now, actually creating those new output when a set of features we supplied to the algorithm, just like finally building those lego tower.
    •>Overfitting - it is the situation where we spend too much time on learning upon traing dataset, that when you were given the actual data you are too confused about what to predict and hot to...
        for example- yoo spent too much time on drawing of cat from 1 image, that when you were given diffrent one, you can't draw or your drawing was not even close...
    •>Underfitting - vice-versa of overfitting, situation where you have'nt leant too much, maybe due to in-sufficieny of data or in total not enough training maybe due to wrong featues supplied to the algorithm


__Level 1- Data Preprocessing__

X-> Independent variable or features,  of data used to make the predection
    for example-1> In predicting the value of the houses, X can contain the dimension od the house, number of bedrooms, distance from the city, etc features.
                2> In classifying model, like animal image classification, y can be the weight, height color of the animal

Y-> Dependent variable or Target,      it is the output of model predection
    for example-1> In predecting value of the house price it could be the final price of the house
                2> or in classification model it can be the category like DOG,CAT,BIRD, etc...

The overall goal of the ML Algo is to set a relationship between the X(Independent features or input) and Y (Dependent features or output) ^_~
    it can be stated as Y=F(X)+e ; where e it the random noise or error


So lets start, by understaning various data Preprocessing tool to make you data look clean and tidy (┬┬﹏┬┬), code for these tools are given in Level-1 file...

•> Simple Imputer - if you dataset has some missing or empty columns, this tool can fill it up by taking the average of the whole column making the missing 
                    value look more real & natural.
•> Feature Scaling - apply to convert much vaarying values into smaller ranges, two types are-
                1> Nomalization [0,1], mostly used in KNN, neural networks,
                2> Standardization [-3,+3] mostly used in Linear regression, Support vector machine (SVM)
•>One-Hot Encoding - To convert the categorical values into numerical forms,
                    used when there is no relationship between the columns of output like CAT,DOG,etc..
•>Label Encoding - this is also used to convert the categorical values into numeric value but,
                    it is used when there is relationship in-between the columns of the output, 
                    like customer satisfation the level could be the low, medium, high as low is smaller than medium, and similarly for medium and high,
                    or it could be YES/NO, because there it relationship like in the form of 0/1.

                    