# Rozee.pk Job Market Analysis (Web Scrapping)

## Overview

This project uses Selenium WebDriver to scrape job listings from Rozee.pk and perform exploratory data analysis (EDA) on the collected data. The scraped data is stored in a CSV file and analyzed using Pandas and Matplotlib.

## Features

* Automated web scraping using Selenium
* Collection of job title, company name, location, job type, and posted date
* Data cleaning and duplicate removal
* Export data to CSV format
* Job market analysis using Pandas
* Data visualization with Matplotlib

## Technologies Used

* Python
* Selenium
* Pandas
* Matplotlib

## Data Collected

The scraper extracts:

* Job Title
* Company Name
* Location
* Job Type
* Posted Date

## Installation

1. Clone the repository:

bash
git clone https://github.com/your-username/rozee-job-analysis.git


2. Install required libraries:

bash
pip install selenium pandas matplotlib


3. Download and install ChromeDriver compatible with your Chrome version.

4. Run the script:

bash
python job_scraper.py


## Analysis Performed

* Total number of jobs scraped
* Number of unique companies
* Most frequent job titles
* Top cities with the highest job listings
* Top hiring companies
* Job type distribution
* Keyword-based job title analysis

## Visualizations

The project generates:

* Top 5 Cities by Job Listings (Bar Chart)
* Top 5 Companies Hiring the Most (Bar Chart)

## Output Files

* jobs.csv → Contains scraped job listings

## Future Improvements

* Scrape additional pages automatically
* Salary analysis
* Skills extraction from job descriptions
* Interactive dashboards using Power BI
* Store data in SQL databases

## Author

Noor_ul_Huda

