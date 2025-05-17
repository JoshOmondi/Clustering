import matplotlib.pyplot as plt
import seaborn as sns

def plot_elbow(sse):
    plt.plot(range(1, len(sse) + 1), sse, marker='o')
    plt.title('Elbow Method')
    plt.xlabel('Number of Clusters')
    plt.ylabel('SSE')
    plt.show()

def plot_clusters(df):
    sns.scatterplot(x='Annual Income (k$)', y='Spending Score (1-100)', hue='Cluster', data=df, palette='Set2')
    plt.title("Customer Segments")
    plt.show()