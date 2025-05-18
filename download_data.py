from kaggle.api.kaggle_api_extended import KaggleApi
from dotenv import load_dotenv
import os

load_dotenv()

# Debug print
print("Loaded Username:", os.getenv("KAGGLE_USERNAME"))
print("Loaded Key:", os.getenv("KAGGLE_KEY")[:4], "...")

os.environ["KAGGLE_USERNAME"] = os.getenv("KAGGLE_USERNAME")
os.environ["KAGGLE_KEY"] = os.getenv("KAGGLE_KEY")

api = KaggleApi()
api.authenticate()

dataset = "vjchoudhary7/customer-segmentation-tutorial"
print("Dataset URL: https://www.kaggle.com/datasets/vjchoudhary7/customer-segmentation-tutorial")
api.dataset_download_files(dataset, path="data", unzip=True)
print("✅ Dataset downloaded and extracted.")
