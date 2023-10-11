from bs4 import BeautifulSoup
import pandas as pd

# Parse the HTML content using BeautifulSoup
with open("table.html", "r", encoding="utf-8") as file:
    html_content = file.read()

# Parse the HTML content using BeautifulSoup
soup = BeautifulSoup(html_content, 'html.parser')

# Find the table element
table = soup.find('table')

# Initialize empty lists to store the table data
character_levels = []
encounter_difficulties = []

# Find all rows in the table body
rows = table.find('tbody').find_all('tr')

headers = [th.get_text() for th in table.find_all('th')]
headers[1] =  'Character Level'

# Iterate through the rows
data = []
for row in table.find_all('tr'):
    cells = row.find_all('td')
    row_data = [cell.get_text() for cell in cells]
    data.append(row_data)

# Create a Pandas DataFrame
df = pd.DataFrame(data[2:], columns = headers[1:])
df['Character Level'] = df['Character Level'].str[:-2]

# Display the DataFrame
df.to_csv('xpthreshhold.csv', index=False)
