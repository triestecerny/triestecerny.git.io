import pandas as pd
import matplotlib.pyplot as plt

# Load your generated dataset
df = pd.read_csv("etsy_wall_art_data.csv")

# 1. Print summary statistics for your numeric features
print("--- SUMMARY STATISTICS ---")
print(df.describe())

# 2. Counts for categorical features (Digital vs Physical / Bestsellers)
print("\n--- DIGITAL VS PHYSICAL COUNTS ---")
print(df['is_digital'].value_counts())

# 3. Create and save a summary graphic (Price vs Review Counts)
plt.figure(figsize=(8, 5))
plt.scatter(df['price'], df['review_count'], alpha=0.6, color='purple')
plt.title("Etsy Minimalist Wall Art: Price vs. Review Counts")
plt.xlabel("Price ($)")
plt.ylabel("Review Count")
plt.grid(True, linestyle='--', alpha=0.5)

# Save the figure to include in your Quarto blog post
plt.savefig("price_vs_reviews.png", dpi=300, bbox_inches='tight')
print("\nSaved summary plot as price_vs_reviews.png!")