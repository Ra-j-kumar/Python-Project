from bs4 import BeautifulSoup
import pandas as pd
import requests

# Wikipedia URL containing the NIFTY 50 companies
url = 'https://en.wikipedia.org/wiki/NIFTY_50'
# Sending a GET request to the URL
response = requests.get(url)
# Parsing the HTML content using BeautifulSoup
soup = BeautifulSoup(response.text, 'html') 
# Finding all tables on the page here the second table contains the NIFTY 50 data
nifty_table  = soup.find_all('table')[1]
# Extracting the header titles of the table
header_cells = nifty_table.find_all('th')
column_names  = [title.text.strip() for title in header_cells]

# Creating an empty DataFrame with column names from the table headers
df = pd.DataFrame(columns=column_names )
# Extracting all rows from the table (including the header row)
table_rows = nifty_table.find_all('tr')
# Iterating through each row (skipping the header row)
for row in table_rows[1:]:
    # Extracting all cells in the current row
    data_cells = row.find_all('td')
    indivisual_row_data = [data.text.strip() for data in data_cells]
    # Appending the row to the DataFrame
    row_index  = len(df)
    df.loc[row_index] = indivisual_row_data
    
# Resetting index to start from 1 instead of 0
df.index = range(1,len(df)+1)

print(df)

# Save the DataFrame to a CSV file 
df.to_csv(r'Nifty50.csv')