# **dfcleanerx**

**dfcleaner** is a simple Python library to clean Pandas DataFrames quickly.

**Features**
- Remove duplicates
- Convert column names to snake_case
- Fill missing values

**Installation**

pip install dfcleaner

**Example**

```
import pandas as pd
from dfcleaner import clean_dataframe

df = pd.read_csv("data.csv")

df = clean_dataframe(df, fill_missing="mean")
```

**License**<br>
MIT License
