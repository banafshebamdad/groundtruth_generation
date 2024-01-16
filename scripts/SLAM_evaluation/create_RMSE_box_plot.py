#
# Banafshe Bamdad
# So Jan 7, 2024 
#

import matplotlib.pyplot as plt
import pandas as pd

# Load the data into a DataFrame
data = pd.DataFrame({
    'Algorithm': ['ORB-1200', 'ORB-1000', 'ORB-900', 'ORB-750', 'SELM'],
    'RMSE': [0.211321, 0.19864, 0.202964, 0.194138, 0.176025]
})

# Create a boxplot of the RMSE data
plt.boxplot(data['RMSE'], labels=data['Algorithm'])
plt.show()

