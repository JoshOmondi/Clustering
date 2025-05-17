from src.data_loader import load_data
from src.preprocessing import preprocess
from src.clustering import find_optimal_k, run_kmeans
from src.visualization import plot_elbow, plot_clusters

# Load and preprocess data
df = load_data("data/Mall_Customers.csv")
data, df = preprocess(df)

# Find optimal clusters
sse = find_optimal_k(data)
plot_elbow(sse)

# Run clustering
labels, score = run_kmeans(data, n_clusters=5)
df['Cluster'] = labels

# Visualize results
plot_clusters(df)
print(f"Silhouette Score: {score:.2f}")