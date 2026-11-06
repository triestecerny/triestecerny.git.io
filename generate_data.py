import pandas as pd
import numpy as np

# Set random seed for reproducibility
np.random.seed(42)

# Generate 250 realistic observations for Etsy minimalist wall art
n_obs = 250

adjectives = ["Minimalist", "Abstract", "Boho", "Mid-Century Modern", "Geometric", "Line Art", "Neutral", "Aesthetic"]
subjects = ["Sunburst", "Botanical Leaf", "Mountain Landscape", "Arch Poster", "Custom Family Name", "Coastal Wave", "Line Face"]
formats = ["Digital Download", "Printable Wall Art", "PDF Print", "Instant Download", "Physical Print"]

titles = [f"{np.random.choice(adjectives)} {np.random.choice(subjects)} - {np.random.choice(formats)}" for _ in range(n_obs)]
prices = np.round(np.random.exponential(scale=8.0, size=n_obs) + 3.0, 2) # prices skewed towards affordable digital art
review_counts = np.random.poisson(lam=45, size=n_obs) * np.random.randint(1, 15, size=n_obs)
is_bestseller = np.random.choice([0, 1], size=n_obs, p=[0.85, 0.15])
is_digital = np.array([1 if 'digital' in t.lower() or 'printable' in t.lower() or 'download' in t.lower() else 0 for t in titles])

df = pd.DataFrame({
    "title": titles,
    "price": prices,
    "review_count": review_counts,
    "is_bestseller": is_bestseller,
    "is_digital": is_digital
})

df.to_csv("etsy_wall_art_data.csv", index=False)
print(f"Successfully generated {len(df)} observations in etsy_wall_art_data.csv!")
print(df.head())