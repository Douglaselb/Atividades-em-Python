from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns

sns.displot(random.binomial(n= 5, p= 0.3, size= 100), hist= True, kde= False)
plt.show()
