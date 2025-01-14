#Note->
    #we are using data Ads_CTR_Optimisation.csv, which contains 10000 rows and 10 ads
    # each row represent single user, which when exposed to set of 10 ads,
    # each col. contains yes=1, no=0 i.e. if they clicked or not

    #Now we as programmer wants to find the bext optimal ad, which when exposed to end user has high CTR(click through rate), the problem is simliar to multi-armed bandit problem
    
    #UCB will intially take n (i.e. n=total no. of ads) number of rounds to give exploration reward to each of the available ad, so as to give a chance to each ad to be used, even if they low or no number of slecetion
    #this is done to to ensure exploration, and after the UCB begins exploitation, by intially running each of the ad and storing the best performed ad of each round, i.e. for the each user
    # and for the each best seleted ad, it will be rewards with some reward ehcne increasing its UCB value
    # after 500-1000 round in most optimal cases, the optimal ad will be exploitated again-n-again representing it as the most optimal solution
    
    #UCB algo works by reqrding the best performed ad of each round, so as increase their UCB value, whcih helps the algo to find the most optimal solution

#importing the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

#importing the dataset
dataset = pd.read_csv('Ads_CTR_Optimisation.csv')

#implementing UCB
import math
N=10000          #total no. of users
d=10             #total no. of ads shown
ads_selected = []   #best ad seleted in each round, contains the best ad selected in each round, the last elemment would be the winner i.e. the bested of all
number_of_selection = [0]*d      #containes the no. of time each ad was seleted
sums_of_reward = [0]*10      #total reward earned by each ad everytime time they were selcted
total_reward = 0    #cummalative reward earned as whole by all the ads
for n in range(0, N):
    ad = 0
    max_upper_bound = 0
    for i in range(0,d):
        if(number_of_selection[i]>0):
            average_reward = sums_of_reward[i]/number_of_selection[i]
            delta_i = math.sqrt(3/2 * math.log(n + 1) / number_of_selection[i])
            upper_bound = average_reward + delta_i
        else:
            upper_bound = 1e400 #10^400 which is very huge number
        if (upper_bound > max_upper_bound):
            max_upper_bound = upper_bound
            ad = i
    ads_selected.append(ad)
    number_of_selection[ad] +=1
    sums_of_reward[ad] += dataset.values[n, ad]    
    total_reward += dataset.values[n, ad]

#printing the ads_selected, i.e. the best ad seleted in all the diff. rounds
print(ads_selected)     #it will be in the form [0,0,2,5,9,9,5,5,5,4,3,...]

#visualing the results
plt.hist(ads_selected)
plt.title('Histogram of the ad selected')
plt.xlabel('ads')
plt.ylabel('Number of time the ad was selected')
plt.show()