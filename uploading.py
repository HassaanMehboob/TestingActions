import supabase
import pandas as pd
from supabase import create_client, Client

SUPABASE_KEY  = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJyb2xlIjoiYW5vbiIsImlhdCI6MTYzNTUwMDYyNiwiZXhwIjoxOTUxMDc2NjI2fQ.u9cmb06zlXwlKG-R9dNxWrqEozXKzDQGJQDq3d8s1V4"
SUPABASE_URL  = "https://azhzbzxkhefsuehwifxo.supabase.co"

key : str = SUPABASE_KEY
url : str = SUPABASE_URL
supabase: Client = create_client(url, key)

df3 = pd.read_csv("lists.csv")
print(df3)
for i in range(5):
    print("uploading",i)
    a = df3['Original_SKU'][i]
    b = df3['sku_file_price'][i]
    c = df3['Stock Qty'][i]
    data = supabase.table("Inventory").insert({"SKU":str(a),"Price":b,"Quantity":c}).execute()  
    print(data)    