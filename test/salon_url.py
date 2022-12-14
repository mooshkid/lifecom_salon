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


# webdriver 
url = 'https://hair-chiba.or.jp/category/salon/'
options = Options()
options.add_argument('--headless')
driver = webdriver.Chrome(options=options)
driver.get(url)


# empty list 
url_list = []


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
    while is_found:
        try:
            next_page=driver.find_element(By.CSS_SELECTOR, '.next.page-numbers')
        except:
            find_products() # calls function with loop to extract products
            print("Did NOT find next page")
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


df = pd.DataFrame(url_list)
df.to_csv(timestamp + '.csv', index=False, header=False)

#print elapsed time
end = time.time()
elapsed = end - start
print('Task Completed in: ' + time.strftime('%H:%M:%S', time.gmtime(elapsed)) + '\n')
