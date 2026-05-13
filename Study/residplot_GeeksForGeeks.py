import seaborn as sns
import matplotlib.pyplot as plt

titanic = sns.load_dataset('titanic')

sns.residplot(y='survived',
              x='age',
              data=titanic)

plt.show()