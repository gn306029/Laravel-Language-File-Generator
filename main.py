import pandas as pd
import os

language_df = pd.read_excel("./language.xlsx")
target_dir = "C:\\xampp\\htdocs\\pier-manager\\resources\\lang"
output_file_name = "custom.php"

result = {}

for key in language_df.keys():
    # 檢查是否有建立語言的資料夾
    if key in ('key', 'group'): continue

    new_path = os.path.join(target_dir, key)

    if not os.path.exists(new_path):
        os.makedirs(new_path)
    
    # 初始化 result, 為每個語言設一個 key
    result[key] = ""

for index, row in language_df.iterrows():
    for key in result.keys():
        msg = str(row[key]).replace("\"", "\\\"")
        if msg == "nan": msg = ""
        result[key] += f"\"{row['key']}\" => \"{msg}\", "

for key, value in result.items():
    file_path = os.path.join(target_dir, key, output_file_name)

    f = open(file_path, 'w+', encoding="utf8")
    f.write(f"<?php return [ {value} ];")
    f.close()