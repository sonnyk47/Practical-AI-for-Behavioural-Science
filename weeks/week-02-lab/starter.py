"""
Week 2 — Starter Script: Visualising Lifestyle and Mental Health
================================================================

This is a starter template for the SCRIPT workflow (Part 2 of the lab).
The imports and data loading are done for you — your AI coding assistant
will help you write the visualisation code.

How to use this file:
    1. First, have your AI create a plan.md file (see README.md for details)
    2. Review and revise the plan until you're happy with it
    3. Have the AI edit THIS file (or create a new .py file) with the code
    4. Run from the terminal:
         conda activate psyc4411-env
         python starter.py

Your AI assistant can edit this file directly, create new files alongside it,
or do both — build up your project piece by piece.

Dataset: data/lifestyle_mental_health.csv
    3,000 participants, 44 variables including demographics, lifestyle factors,
    DASS-21 items (Depression, Anxiety, Stress subscales), and life satisfaction.
    There are ~2-3% missing values in the lifestyle columns.
"""

# === IMPORTS ===
# These are the same libraries used in the notebook.
# pandas: for loading and working with data tables
# numpy: for numerical operations (like calculating trend lines)
# matplotlib: for creating plots and figures
# seaborn: for making statistical plots look great with less code

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Set some defaults so our plots look nice
sns.set_theme(style="whitegrid", font_scale=1.1)

# === LOAD THE DATA ===
# This reads the CSV file into a pandas DataFrame called 'data'.
# A DataFrame is like a spreadsheet — rows are participants, columns are variables.

data = pd.read_csv("data/lifestyle_mental_health.csv")

print(f"Dataset loaded: {data.shape[0]} participants, {data.shape[1]} variables")
print(f"Columns: {', '.join(data.columns)}")
print()

# === YOUR VISUALISATION CODE GOES BELOW ===
# Have your AI assistant write the visualisation code based on your plan.

# Create a 2x2 figure
fig, axes = plt.subplots(2, 2, figsize=(12, 10))
fig.suptitle("Lifestyle Factors Associated with Depression", fontsize=16, fontweight="bold")

# Define the variables to plot (Variable Name, Axis, Title)
plot_vars = [
    ("Sleep_hrs_night", axes[0, 0], "Sleep Duration"),
    ("Exercise_hrs_week", axes[0, 1], "Weekly Exercise"),
    ("Social_Support_score", axes[1, 0], "Social Support"),
    ("SocialMedia_hrs_week", axes[1, 1], "Social Media Use")
]

# Loop through variables and create plots
for var, ax, title in plot_vars:
    # Drop missing values for the specific variables to avoid errors
    subset = data.dropna(subset=[var, "DASS_Depression"])
    
    # Create scatter plot with regression line
    sns.regplot(
        data=subset, 
        x=var, 
        y="DASS_Depression", 
        ax=ax,
        scatter_kws={"alpha": 0.3, "s": 15}, # Transparency helps with 3000 points
        line_kws={"color": "C1"} # Contrast color for the trend line
    )
    
    # Add mean lines
    mean_val = subset[var].mean()
    mean_dep = subset["DASS_Depression"].mean()
    ax.axvline(mean_val, color="red", linestyle="--", alpha=0.7)
    ax.axhline(mean_dep, color="red", linestyle="--", alpha=0.7)
    
    # Set titles and labels
    ax.set_title(title)
    ax.set_xlabel(var.replace("_", " "))
    ax.set_ylabel("DASS Depression Score")
    
    # Remove top and right borders for a cleaner look
    sns.despine(ax=ax)

# Adjust layout to prevent overlap
plt.tight_layout()

# === SAVE THE FIGURE ===
# Uncomment and modify these lines once your figure code is ready:

fig.savefig("lifestyle_depression.png", dpi=300, bbox_inches="tight")
print("Figure saved as 'lifestyle_depression.png'")
