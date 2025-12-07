# Reflection

## What Copilot Generated

I used Copilot to help write the `load_data()` and `clean_column_names()` functions. When I typed the function name and a comment, Copilot suggested using `pd.read_csv()` to load the file and `.str.lower()` to make column names lowercase.

## What I Modified

I added `.str.replace(' ', '_')` to the column cleaning function because Copilot only suggested lowercase. I also changed `handle_missing_values()` to use `subset=['price', 'quantity']` instead of dropping all missing values.

## What I Learned

I learned that data cleaning needs multiple steps and that Copilot helps with syntax but I still need to decide what makes sense. For example, I had to tell it that negative prices are errors.