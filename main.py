from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import pandas as pd
import os, time, datetime

# start timer 
start = time.time()

# change cwd to the script directory 
os.chdir(os.path.dirname(__file__))
path = os.getcwd()

