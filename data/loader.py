import os
import pandas as pd

_cache = None
_last_mod_time = None

def load_hsn_data(file_path="HSN_SAC.xlsx"):
    global _cache, _last_mod_time
    try:
        mod_time = os.path.getmtime(file_path)
        if _cache is None or mod_time != _last_mod_time:
            df = pd.read_excel(file_path, skiprows=1, header=None)
            df = df.iloc[:, :2]
            df.columns = ["HSNCode", "Description"]
            df["HSNCode"] = df["HSNCode"].apply(lambda x: str(x).strip().replace(".0", ""))
            _cache = dict(zip(df["HSNCode"], df["Description"]))
            _last_mod_time = mod_time
        return _cache
    except Exception as e:
        print("Error loading HSN master data:", e)
        return {}