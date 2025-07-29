# Import necessary libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Set plot style
sns.set(style="whitegrid")

# Load the dataset
file_path = "/mnt/data/German_FinTechCompanies.csv"  # Update this path if necessary
df = pd.read_csv(file_path)