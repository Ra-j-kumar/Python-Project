# 📊 NIFTY 50 Web Scraper

This Python project scrapes the list of NIFTY 50 companies from [Wikipedia](https://en.wikipedia.org/wiki/NIFTY_50) using `BeautifulSoup`, and stores the data in a clean tabular format as a `.csv` file.

---

## 🔧 Features

- Scrapes real-time NIFTY 50 company data from Wikipedia.
- Extracts clean and structured data into a Pandas DataFrame.
- Saves data to a local CSV file with index starting from 1.
- Easy to modify for additional scraping features.

---

## 📁 Output

The output file is:
- `Nifty50.csv`: Contains the latest NIFTY 50 companies and related information from Wikipedia.

---

## 🛠 Requirements

Install the following libraries before running the script:

```bash
pip install requests
pip install beautifulsoup4
pip install pandas
