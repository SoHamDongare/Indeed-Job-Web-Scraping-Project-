import pymysql
import time
from bs4 import BeautifulSoup

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

def save_data(data):
    db=pymysql.connect(
        host="localhost",
        user="root",
        password="@Soham2004",
        database="jobsdata",
        charset="utf8mb4"
        )
    cur=db.cursor()
    query=""" 
        INSERT IGNORE INTO PeopleData(title,company,location,link)
        VALUES(%s,%s,%s,%s)
    """
    cur.executemany(query,data)
    db.commit()
    print("Data Inserted Successfully",cur.rowcount)
    db.close()

def scrape_jobs():
    url='https://in.indeed.com/jobs?q=python+developer&l='
    driver=webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get(url)
    time.sleep(3)
    soup=BeautifulSoup(driver.page_source,"html.parser")
    driver.quit()

    job_cards=soup.select("div.job_seen_beacon")
    scrape_data=[]




    for job in job_cards:
        title = job.select_one("h2.jobTitle span")
        title1 = title.text.strip() if title else "N/A"

        find_company = job.select_one("span.companyName")
        if not find_company:
            find_company = job.select_one("div[class*='company'] span")

        company = find_company.text.strip() if find_company else "NA"

        find_location = job.select_one("span.companyLocation")
        if not find_location:
            find_location = job.select_one("span.location")
        location = find_location.text.strip() if find_location else "NA"

        link_tag = job.select_one("h2.jobTitle a")
        link = "https://in.indeed.com"+link_tag["href"] if link_tag else "NA"

        scrape_data.append((title1, company, location, link))
    print("Scrapped", len(scrape_data))
    save_data(scrape_data)
    print("Scraped data & saved successfully")


if __name__ == '__main__':
    scrape_jobs()
