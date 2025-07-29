# Import necessary libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Set plot style
sns.set(style="whitegrid")

# Load the dataset
file_path = "/mnt/data/German_FinTechCompanies.csv"  # Update this path if necessary
df = pd.read_csv(file_path)

# Prepare data for visualizations
legal_form_counts = df['Legal form'].value_counts().head(10)
top_cities = df['City'].value_counts().head(10)
founding_year_trend = df['Founding year'].dropna().astype(int).value_counts().sort_index()
segment_counts = df['Segment'].value_counts()
subsegment_counts = df['Subsegment'].value_counts().head(10)
bank_coop_counts = df['Bank Cooperation'].value_counts().rename({0: 'No', 1: 'Yes'})