import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
df = pd.read_csv("etsy_wall_art_data.csv")

# Set plotting style
sns.set_theme(style="whitegrid")

# 1. Price vs Review Count Scatter Plot colored by Digital vs Physical
plt.figure(figsize=(9, 6))
sns.scatterplot(
    data=df, 
    x='price', 
    y='review_count', 
    hue='is_digital', 
    palette='viridis', 
    alpha=0.7, 
    s=70
)
plt.title("Etsy Minimalist Wall Art: Price vs. Review Volume by Format", fontsize=12, fontweight='bold')
plt.xlabel("Price ($)", fontsize=10)
plt.ylabel("Review Count", fontsize=10)
plt.legend(title="Is Digital? (1=Yes, 0=No)", loc='upper right')
plt.savefig("price_vs_reviews_colored.png", dpi=300, bbox_inches='tight')
plt.close()

# 2. Boxplot comparing Prices of Digital vs Physical items
plt.figure(figsize=(8, 5))
sns.boxplot(data=df, x='is_digital', y='price', palette='Set2')
plt.title("Price Distribution: Digital Downloads vs. Physical Prints", fontsize=12, fontweight='bold')
plt.xlabel("Format (0 = Physical Print, 1 = Digital Download)", fontsize=10)
plt.ylabel("Price ($)", fontsize=10)
plt.savefig("price_distribution_box.png", dpi=300, bbox_inches='tight')
plt.close()

print("Generated and saved both extra EDA plots successfully!")