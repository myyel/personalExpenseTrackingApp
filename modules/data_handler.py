import pandas as pd
import random
from datetime import datetime, timedelta
import os


def generate_sample_data(filepath):
    categories = ["Food", "Transport", "Rent", "Entertainment", "Bill", "Health", "Clothes"]
    data = []

    today = datetime.today()

    for _ in range(100):
        date = today - timedelta(days=random.randint(0, 90))
        category = random.choice(categories)
        amount = round(random.uniform(50, 1000), 2)
        data.append([date.strftime("%Y-%m-%d"), category, amount])

    df = pd.DataFrame(data, columns=["Date", "Category", "Amount"])
    os.makedirs(os.path.dirname(filepath), exist_ok=True)
    df.to_csv(filepath, index=False)


def load_data(filepath):
    return pd.read_csv(filepath, parse_dates=["Date"])
