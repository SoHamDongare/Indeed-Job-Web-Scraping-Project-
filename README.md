# Indeed Job Web Scraping Project (Python)

## Project Overview
This project is a Python-based web scraping application that extracts Python Developer job listings from the Indeed website and stores the scraped data into a MySQL database. The script uses Selenium for browser automation and BeautifulSoup for HTML parsing.

## Technologies Used
- Python
- Selenium
- BeautifulSoup
- MySQL
- PyMySQL
- webdriver-manager

## Features
- Scrapes Python Developer job listings from Indeed
- Extracts job title, company name, location, and job link
- Stores scraped data into a MySQL database
- Prevents duplicate data entries

## Project Structure
indeed-job-webscraping/
│
├── indeeed.py
└── README.md

## How It Works
- Opens Indeed job search page using Selenium
- Parses HTML content using BeautifulSoup
- Extracts job details from job cards
- Saves the data into MySQL database

## Database Details
- Database Name: jobsdata
- Table Name: PeopleData
- Columns: title, company, location, link

## How to Run the Project
1. Install required libraries:
   pip install selenium beautifulsoup4 pymysql webdriver-manager
2. Update MySQL credentials in the Python file
3. Run the script:
   python indeeed.py

## Author
Soham Dongare
B.Sc IT Undergraduate | Aspiring Python Developer
