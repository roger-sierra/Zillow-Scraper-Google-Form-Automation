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

3. **Set up environment variables:**

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
