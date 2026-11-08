from extractor import fetch_raw_data
from cleaner import clean_sales_data
from loader import save_data

data = clean_sales_data(fetch_raw_data())
save_data(data)
