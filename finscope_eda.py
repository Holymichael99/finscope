# Import necessary libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Set plot style
sns.set(style="whitegrid")

# Load the dataset
file_path = "German_FinTechCompanies.csv"  # Update this path if necessary
df = pd.read_csv(file_path)

# Prepare data for visualizations
legal_form_counts = df['Legal form'].value_counts().head(10)
top_cities = df['City'].value_counts().head(10)
founding_year_trend = df['Founding year'].dropna().astype(int).value_counts().sort_index()
segment_counts = df['Segment'].value_counts()
subsegment_counts = df['Subsegment'].value_counts().head(10)
bank_coop_counts = df['Bank Cooperation'].value_counts().rename({0: 'No', 1: 'Yes'})

# Create plots
fig, axes = plt.subplots(3, 2, figsize=(16, 18))
fig.suptitle("German FinTech Companies Analysis", fontsize=18)

# Top 10 Legal Forms
sns.barplot(x=legal_form_counts.values, y=legal_form_counts.index, ax=axes[0, 0], palette="Blues_d")
axes[0, 0].set_title("Top 10 Legal Forms")

# Top 10 Cities
sns.barplot(x=top_cities.values, y=top_cities.index, ax=axes[0, 1], palette="Greens_d")
axes[0, 1].set_title("Top 10 Cities")

# Founding Year Trend
sns.lineplot(x=founding_year_trend.index, y=founding_year_trend.values, marker="o", ax=axes[1, 0])
axes[1, 0].set_title("Founding Year Trend")
axes[1, 0].set_xlabel("Year")
axes[1, 0].set_ylabel("Number of Companies")

# Segment Distribution
sns.barplot(x=segment_counts.values, y=segment_counts.index, ax=axes[1, 1], palette="Oranges_d")
axes[1, 1].set_title("Segment Distribution")


# Top 10 Subsegments
sns.barplot(x=subsegment_counts.values, y=subsegment_counts.index, ax=axes[2, 0], palette="Purples_d")
axes[2, 0].set_title("Top 10 Subsegments")

# Bank Cooperation Status
sns.barplot(x=bank_coop_counts.index, y=bank_coop_counts.values, ax=axes[2, 1], palette="Reds_d")
axes[2, 1].set_title("Bank Cooperation Status")
axes[2, 1].set_ylabel("Number of Companies")

# Layout adjustment
plt.tight_layout(rect=[0, 0, 1, 0.97])
plt.show()