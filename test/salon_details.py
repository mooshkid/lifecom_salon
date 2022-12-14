from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import pandas as pd
import os, time, datetime


# start timer 
start = time.time()
# timestamp
timestamp = datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
# counter 
counter = 0 


# change cwd to the script directory 
os.chdir(os.path.dirname(__file__))
path = os.getcwd()


# output file name 
output_csv = timestamp + '.csv'


# create a empty dataframe with columns definied 
df_storeinfo = pd.DataFrame(columns=['店名', '住所', 'TEL', '営業時間', '定休日', 'HP', 'Email'])




fakelist = ['https://hair-chiba.or.jp/salon/11510/', 'https://hair-chiba.or.jp/salon/1102346/','https://hair-chiba.or.jp/salon/10101/', 'https://hair-chiba.or.jp/salon/1106056/']
counter_max = len(fakelist)

# loop through the urls
for i in fakelist:

    counter += 1
    print('Starting(' + str(int(counter)) + '/' + str(int(counter_max)) + '): ' + i)

    # webdriver 
    options = Options()
    options.add_argument('--headless')
    driver = webdriver.Chrome(options=options)
    driver.get(i)

    # find the table
    table = driver.find_element(By.XPATH, '//*[@id="article"]/div[1]/table')
    rows = table.find_elements(By.XPATH, 'tbody/tr')

    # empty list to store the td2 stuff
    details_list = [] #placed inside the loop here to reset the list for every new page
    for row in rows:
        td2 = row.find_element(By.XPATH, 'td[2]').text
        details_list.append(td2)
    
    # append list to dataframe 
    df_storeinfo.loc[len(df_storeinfo)] = details_list
    driver.close()


# save df to csv file
df_storeinfo.to_csv(output_csv)

#print elapsed time
end = time.time()
elapsed = end - start
print('Task Completed in: ' + time.strftime('%H:%M:%S', time.gmtime(elapsed)) + '\n')