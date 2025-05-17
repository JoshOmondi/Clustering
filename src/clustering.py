from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score

def find_optimal_k(data, max_k=10):
    sse = []
    for k in range(1, max_k + 1):
        km = KMeans(n_clusters=k, random_state=42)
        km.fit(data)
        sse.append(km.inertia_)
    return sse

def run_kmeans(data, n_clusters=5):
    kmeans = KMeans(n_clusters=n_clusters, random_state=42)
    labels = kmeans.fit_predict(data)
    score = silhouette_score(data, labels)
    return labels, score