# -*- coding: utf-8 -*-
"""
Created on Tue Jul 18 08:06:33 2023

@author: rfo7799
"""

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import time
import os
import pandas as pd
import glob

#driver = webdriver.Chrome()

def download_pga_data(url_site):
    
    driver = webdriver.Chrome()
    driver.get(url_site)
    time.sleep(3)
    
    download_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div[2]/div/div[1]/main/div/div[3]/div[4]/button[1]')))
    download_button.click()
    time.sleep(10)
    driver.quit()
    return


def downloaded_file_load_in():
    downloads_folder = r'C:\Users\rfo7799\Downloads'
    files = os.listdir(downloads_folder)
    files.sort(key=lambda x: os.path.getmtime(os.path.join(downloads_folder, x)), reverse=True)
    
    if files:
        most_recent_file = os.path.join(downloads_folder, files[0])
        if most_recent_file.lower().endswith('.csv'):
            df = pd.read_csv(most_recent_file)
    return df

        
url_list = ['https://www.pgatour.com/stats/detail/120','https://www.pgatour.com/stats/detail/156','https://www.pgatour.com/stats/detail/02675',
            'https://www.pgatour.com/stats/detail/101','https://www.pgatour.com/stats/detail/103','https://www.pgatour.com/stats/detail/02564']
stat_name_list = ['Scoring Average','Birdie Average','Strokes Gained',
                  'Driving Distance','GIR %', 'SG: Putting']
file_name_list = ['Scoring_Average','Birdie_Average','Strokes_Gained','Driving_Distance',
                  'GIR','Putting']

for x,y,z in zip(url_list,stat_name_list,file_name_list):
    download_pga_data(x)
    data = downloaded_file_load_in()
    print('Data for ' + y + ' has been downloaded')
    data['Stat Name'] = y
    data.to_csv(r'C:\Users\rfo7799\Desktop\Git\Fantasy Golf\\' + z + '.csv', index=False)
    
file_list = os.listdir(r'C:\Users\rfo7799\Desktop\Git\Fantasy Golf\\')
file_list


total = pd.DataFrame()

for file in file_list:
    df = pd.read_csv(file)
    total = total.append(df, ignore_index=True)
    total.to_csv(r'C:\Users\rfo7799\Desktop\Git\Fantasy Golf\total.csv')