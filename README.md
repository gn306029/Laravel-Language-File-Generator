#### Laravel Language File Generator

According excel file generate laravel lang file

Excel setting just like example.xlsx，Then edit this part
```
# main.py
language_df = pd.read_excel("<excel_path>")
target_dir = "<output_dir_path>"
output_file_name = "<output_file_name>.php"
```

Then run "python main.py", the lang file will be generate to target dir