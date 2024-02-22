# Scrape data Pemilu 2024 (Presidential Election)
This Python code scrapes the vote count results for Indonesia's presidential and vice-presidential elections per province from https://pemilu2024.kpu.go.id/. The output will be stored in a CSV format.
<img width="1425" alt="Screenshot 2024-02-19 at 13 09 32" src="https://github.com/cencencendi/pemilu_2024/assets/85205431/71e262b8-521d-477c-bcb3-0b5d6ba765d8">

## What is in this repository?
* `requirements.txt`: This file stores all the libraries that must be installed in your Python to use the `scraping_and_clean_data_pilpres.py` code.
* `link_scraping.csv`: This file contains a list of all the pairs of provinces and their corresponding links on https://pemilu2024.kpu.go.id/.
* `scraping_and_clean_data_pilpres.ipynb`: This is the main script for scraping and cleaning data from all of the links provided.
* `data_pilpres_perprovince.csv`: A dataset of votes per province that has been cleaned and is ready to be used for analysis.

## How to use.
* Step 1.
  Clone the repository by copy and paste the provided code into your terminal or command prompt. Once done, you can just run the code to complete the process. And don't forget to make sure you have installed git on your PC.
  `https://github.com/cencencendi/pemilu_2024.git`
* Step 2.
  Make sure to download and install Python on your PC if you haven't already done so. You can find the download link [here](https://www.python.org/).
* Step 3.
  Run this code on your terminal or command prompt to install the requirement packages.
  
  `pip install -r requirements.txt`
* Step 4.
  To obtain the `data_pilpres_perprovince.csv` file, please run the `scraping_and_clean_data_pilpres.ipynb` script.

