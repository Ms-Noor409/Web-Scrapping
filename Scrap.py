from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd
import matplotlib.pyplot as plt

options = Options()
options.add_argument("--start-maximized")
driver = webdriver.Chrome(options=options)

urls = [
    "https://www.rozee.pk/job/jsearch/q/all/fpn/0",
    "https://www.rozee.pk/job/jsearch/q/all/fpn/20",
    "https://www.rozee.pk/job/jsearch/q/all/fpn/40",
    "https://www.rozee.pk/job/jsearch/q/all/fpn/60",
    "https://www.rozee.pk/job/jsearch/q/all/fpn/80",
    "https://www.rozee.pk/job/jsearch/q/all/fpn/100"
   
]

jobs_data = []

for url in urls:
    driver.get(url)


wait = WebDriverWait(driver, 20)
wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "h3.s-18")))


wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "div.job")))
jobs= driver.find_elements(By.CSS_SELECTOR, "div.job")
    

for job in jobs:
    if len(jobs_data) >= 100:
        break
    try:
        title = job.find_element(By.TAG_NAME, "h3").text
    except:
        title = "N/A"

    try:
        company = job.find_element(By.CSS_SELECTOR, "div.cname").text
    except:
        company = "N/A"

    try:
        location = job.find_element(By.CSS_SELECTOR, "div.loc bdi").text
    except:
        location = "Unknown"

    try:
        job_type = job.find_element(By.CSS_SELECTOR, "div.jtype bdi").text
    except:
        job_type = "N/A"

    try:
        posted_date = job.find_element(By.CSS_SELECTOR, 'span[data-original-title="Posted On"]').text
    except:
        posted_date = "N/A"

    jobs_data.append({
        "Job Title": title,
        "Company": company,
        "Location": location,
        "Job Type": job_type,
        "Posted Date": posted_date
    })

driver.quit()



# ----- CREATE DATAFRAME -----
df = pd.DataFrame(jobs_data)
df.drop_duplicates(inplace=True)
df.to_csv("jobs.csv", index=False)
print("jobs.csv created successfully")

# ----- DATA ANALYSIS -----
df = pd.read_csv("jobs.csv")
print(df.head())

total_jobs = len(df)
print("Total jobs:", total_jobs)

unique_companies = df["Company"].nunique()
print("Number of unique companies:", unique_companies)

top_titles = df["Job Title"].value_counts().head(10)
print("Most frequent job titles:")
print(top_titles)

top_cities = df["Location"].value_counts().head(5)
print("Top 5 cities with most jobs:")
print(top_cities)

top_companies = df["Company"].value_counts().head(5)
print("Top 5 companies hiring the most:")
print(top_companies)

job_type_counts = df["Job Type"].value_counts()
print(job_type_counts)

keywords = ['Manager', 'Engineer', 'Intern', 'Developer', 'Sales']
for kw in keywords:
    count = df['Job Title'].str.contains(kw, case=False).sum()
    print(f"Jobs results '{kw}': {count}")

# ---- Data VISUALIZATION ------
plt.figure(figsize=(10,5))
df["Location"].value_counts().head(5).plot(kind="bar", color="skyblue", title="Top 5 Cities by Job Listings")
plt.ylabel("Number of Jobs")
plt.show()

plt.figure(figsize=(10,5))
df["Company"].value_counts().head(5).plot(kind="bar", color="orange", title="Top 5 Companies Hiring the Most")
plt.ylabel("Number of Jobs")
plt.show()