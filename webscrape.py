import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from urllib.request import urlopen
from bs4 import BeautifulSoup

# Generate a Beautiful Soup object from the url
url = "https://www.nfl.com/scores/2018/REG1"
html = urlopen(url)
soup = BeautifulSoup(html,'lxml')

print(soup)