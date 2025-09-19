import pandas as pd
import re
import matplotlib.pyplot as plt

# Read the CSV with columns: movie_title, rating, rating count, year, time
df = pd.read_csv("imdb_top_250_movies.csv")

# Convert types
df["year"] = pd.to_numeric(df["year"], errors="coerce")
df["rating"] = pd.to_numeric(df["rating"], errors="coerce")

# rating count like "3.1M", "948K" → integer
def parse_count(x):
    if pd.isna(x):
        return pd.NA
    t = str(x).strip().upper().replace(",", "")
    m = re.match(r"([0-9]*\.?[0-9]+)\s*([KMB]?)", t)
    if not m:
        return pd.NA
    num, suf = float(m.group(1)), m.group(2)
    mult = {"": 1, "K": 1_000, "M": 1_000_000, "B": 1_000_000_000}[suf]
    return int(num * mult)

# time like "2h 22m" → total minutes
def parse_time(x):
    if pd.isna(x):
        return pd.NA
    t = str(x).lower()
    h = re.search(r"(\d+)h", t)
    m = re.search(r"(\d+)m", t)
    return (int(h.group(1)) if h else 0) * 60 + (int(m.group(1)) if m else 0)

df["rating count"] = df["rating count"].apply(parse_count)
df["runtime_min"] = df["time"].apply(parse_time)

print("✅ Dataset Loaded:", df.shape)
print(df.head())

# Quick plot: Rating vs Runtime (minutes)
plot_df = df.dropna(subset=["rating", "runtime_min"]) 
if not plot_df.empty:
    plt.figure(figsize=(6, 4))
    plt.scatter(plot_df["runtime_min"], plot_df["rating"], s=12, alpha=0.6)
    plt.xlabel("Runtime (minutes)")
    plt.ylabel("IMDb Rating")
    plt.title("Rating vs Runtime")
    plt.grid(True, alpha=0.2)
    plt.tight_layout()
    plt.show()

# Histograms: Ratings and Runtime
if df["rating"].notna().any():
    plt.figure(figsize=(6, 4))
    df["rating"].dropna().plot(kind="hist", bins=20, alpha=0.8)
    plt.xlabel("IMDb Rating")
    plt.ylabel("Count")
    plt.title("Distribution of Ratings")
    plt.grid(True, alpha=0.2)
    plt.tight_layout()
    plt.show()

if df["runtime_min"].notna().any():
    plt.figure(figsize=(6, 4))
    df["runtime_min"].dropna().plot(kind="hist", bins=20, alpha=0.8)
    plt.xlabel("Runtime (minutes)")
    plt.ylabel("Count")
    plt.title("Distribution of Runtime")
    plt.grid(True, alpha=0.2)
    plt.tight_layout()
    plt.show()
