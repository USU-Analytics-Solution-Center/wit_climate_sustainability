import requests
from bs4 import BeautifulSoup
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

number_of_projects = int(input('How many projects would you like to scrape? '))

driver = webdriver.Chrome()
driver.get("https://www.adaptation-fund.org/projects-programmes/")

# wait for data to fully load
wait = WebDriverWait(driver, 10)  # wait up to 10 seconds
wait.until(EC.presence_of_element_located((By.ID, 'af-projects-table')))
table_html = driver.find_element(By.ID, 'af-projects-table').get_attribute('outerHTML')
soup = BeautifulSoup(table_html, 'html.parser')

# we can close the driver now! 
#driver.close()

tbody = soup.find('tbody')  # find the table body

# find all rows
rows = tbody.find_all('tr')


data = []  # create an empty list to hold all the data
for row in rows:  # loop through each row
    cols = row.find_all('td')  # find all cells in that row
    # extract text from each cell and add to data list
    data.append({
        'Country': cols[0].text.strip(),
        'Project Name': cols[1].text.strip(),
        'Project Link': cols[1].find('a')['href'],
        'Implementing Entity': cols[2].text.strip(),
        'Approved Amount (USD)': float(cols[3].text.strip().replace(',', '')),
        'Amount Transferred (USD)': float(cols[4].text.strip().replace(',', '')),
        'Approval Date': cols[5].text.strip(),
        'Status': cols[6].text.strip(),
        'Grant Category': cols[7].text.strip(),
    })


# Now let's create a dataframe from the data
df = pd.DataFrame(data)
df.to_csv('adaptation_fund_project_list.csv', index=False)

# Great, now let's loop through all the projects and get the project description and component table
driver = webdriver.Chrome()
#project_titles = []
project_descs = []
project_info_dicts = []



for link in df['Project Link'][0:number_of_projects]:
    driver.get(link)
    # wait for data to fully load
    wait = WebDriverWait(driver, 10)  # wait up to 10 seconds
    wait.until(EC.presence_of_element_located((By.ID, 'main')))
    project_desc_html = driver.find_element(By.ID, 'main').get_attribute('outerHTML')
    soup = BeautifulSoup(project_desc_html, 'html.parser')
   
    # Extract project title
    title = soup.find(class_='entry-title').text.strip()
    #project_titles.append(title)

    # Extract project description
    paragraphs = [p.text.replace('\xa0', ' ').replace('\n', '')  for p in soup.find_all('p')]
    project_desc = ' '.join(paragraphs)
    project_descs.append(project_desc)



    # Extract project info
    project_info_all = soup.find_all(class_='project-info-box')
    project_info_list= [t.text.strip().replace('\t','') for t in project_info_all]  
    
    
    project_info_dict = {}
    # adding project titles to the project info dicts
    project_info_dict['Project Title'] = title

    for item in project_info_list:
        split_item = item.split(':\n\n', 1)  # split at the first occurrence of ':\n\n'
        key = split_item[0]
        value = split_item[1].replace('\n','') if len(split_item) > 1 else None  # handle cases where there is no value
        project_info_dict[key] = value

    project_info_dicts.append(project_info_dict)

    

# combining project desc and project info
for i, project_desc in enumerate(project_descs):
    try:
        # checking if project desc is not empty
        if project_desc != '':
            project_info_dicts[i]['Project Description'] = project_desc
        else:
            project_info_dicts[i]['Project Description'] = None
    except IndexError:
        print(f"No project info dict found for index: {i}")
        # You can continue with the next URL or perform some other action
        continue  # Skip the current URL and proceed with the next one

print(project_info_dicts)



# Now, you can create a DataFrame

import csv

def save_dicts_to_csv(data, filename):
    """
    Save a list of dictionaries to a CSV file with index.

    Parameters:
        data (list): A list of dictionaries.
        filename (str): The name of the file to save.
    """
    # Find all unique keys across dictionaries to ensure all data is written to CSV
    all_keys = set()
    for row in data:
        all_keys.update(row.keys())
    
    # Add 'Index' as the first key
    all_keys = ['Index'] + list(all_keys)

    # Open the file and write the data
    with open(filename, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=all_keys)
        writer.writeheader()

        
        # Add index to each dictionary and write to the CSV
        for i, row in enumerate(data):
            row_with_index = {'Index': i, **row}
            writer.writerow(row_with_index)

save_dicts_to_csv(project_info_dicts,'adaptation_fund_project_details.csv')


test = pd.read_csv('adaptation_fund_project_details.csv' , index_col='Index')

# reordering columns 
test.drop(['Locations:\nTo navigate, press the arrow keys.', 'Locations:'], inplace=True, axis=1)
