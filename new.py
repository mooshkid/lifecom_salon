from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import pandas as pd
import os, time, datetime


# start timer 
start = time.time()
# timestamp
timestamp = datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')

# change cwd to the script directory 
os.chdir(os.path.dirname(__file__))
path = os.getcwd()


# output file name 
output_csv = timestamp + '.csv'


# empty list 
url_list = []
# create a empty dataframe with columns definied 
df_storeinfo = pd.DataFrame(columns=['店名', '住所', 'TEL', '営業時間', '定休日', 'HP', 'Email'])


### START MAIN.PY STUFF HERE ###
# webdriver 
url = 'https://hair-chiba.or.jp/category/salon/'
options = Options()
options.add_argument('--headless')
driver = webdriver.Chrome(options=options)
driver.get(url)


# Defining the function
# loop to find the stores 
def find_products():

    # find list element 
    store_list = driver.find_element(By.ID, 'index_blog_list')
    
    for i in store_list.find_elements(By.XPATH, 'li'):
        title = i.find_element(By.CLASS_NAME, 'title')
        href = title.get_attribute('href')
        print(href)

        url_list.append(href)


# Defining the function 
# next page stuff
def next_page():

    # counter
    counter = 1
    print("Starting Page: {}...".format(counter))

    is_found = True
    # for i in range(1):
    while is_found:
        try:
            next_page=driver.find_element(By.CSS_SELECTOR, '.next.page-numbers')
        except:
            find_products() # calls function with loop to extract products
            # print("Did NOT find next page")
            time.sleep(5)
            driver.close()

            # terminate the while loop
            is_found = False
        else:
            find_products()

            counter += 1

            next_page.click() 
            print('\n')
            print("Starting Page: {}...".format(counter))
            time.sleep(5)

# Call the function 
next_page()

print('\n')
print('Created URL List')



### START STORES.PY STUFF HERE ###
print('Beginning data extraction...')

# reset counter 
counter = 0

# loop through the urls
for i in url_list:

    counter += 1
    print('Starting url(' + str(int(counter)) + '): ' + i)

    # webdriver 
    url = i
    options = Options()
    options.add_argument('--headless')
    driver = webdriver.Chrome(options=options)
    driver.get(url)

    # find the table
    table = driver.find_element(By.XPATH, '//*[@id="article"]/div[1]/table')
    rows = table.find_elements(By.XPATH, 'tbody/tr')

    # empty list to store the td2 stuff
    test_list = [] #placed inside the loop here to reset the list for every new page
    for row in rows:
        td2 = row.find_element(By.XPATH, 'td[2]').text
        test_list.append(td2)
    
    # append list to dataframe 
    df_storeinfo.loc[len(df_storeinfo)] = test_list


# save df to csv file
df_storeinfo.to_csv(output_csv)

#print elapsed time
end = time.time()
elapsed = end - start
print('Task Completed in: ' + time.strftime('%H:%M:%S', time.gmtime(elapsed)) + '\n')
print(output_csv)