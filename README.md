# Zillow Rental Scraper and Google Form Auto-Filler

This Python project automates the process of scraping rental listings from a Zillow clone website and filling out a Google Form with the scraped data using Selenium.

## Features

- Scrapes rental listings from a Zillow clone website.
- Extracts addresses, prices, and links from the listings.
- Automatically fills a Google Form with the scraped data.

## Installation

### Prerequisites

- Python 3.x
- [Google Chrome](https://www.google.com/chrome/)
- [Selenium](https://selenium.dev/)
- [BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/)
- [python-dotenv](https://pypi.org/project/python-dotenv/)

### Setup

1. **Clone the repository:**

   ```bash
   git clone https://github.com/yourusername/zillow-rental-scraper.git
   cd zillow-rental-scraper

2. **Install the required Python packages:**

   ```bash
   pip install selenium beautifulsoup4 python-dotenv

3. **Create a Google Form with three short_answer questions. For example:

   - "What's the address of the property?"
   - "What's the price per month?"
   - "What's the link to the property?"

4. **Set up environment variables:**

   Create a .env file in the project root directory and add your Google Form URL:

   ```env
   GOOGLE_FORM_URL="your_google_form_url"

## Usage

1. **Run the script:**

   ```bash
   python main.py

  The script will:
  
  - Open Google Chrome.
  - Navigate to the Zillow clone website.
  - Scrape the rental data.
  - Automatically fill out the Google Form with the scraped data.
  - Close the broswer when finished.

2. **Download a Google spreadsheet with all data:**

   - Navigate to the Google form from the account which created it.
   - Click on the "Responses" tab.
   - Click on the "View in Sheets" button.

  ![image](https://github.com/roger-sierra/Zillow-Scraper-Google-Form-Automation/assets/51401112/f8f5d4f2-d486-46bd-a365-c8aeda58af2d)
  
  ![image](https://github.com/roger-sierra/Zillow-Scraper-Google-Form-Automation/assets/51401112/e6f9065a-9007-44c8-b7e0-44dcdee27717)
