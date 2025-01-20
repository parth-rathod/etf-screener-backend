# ETF Screener

## Project Overview

This innovative application provides a comprehensive breakdown of ETF component tickers and their respective weights within Exchange-Traded Funds. By analyzing the underlying securities of popular ETFs, users gain valuable insights into:

- The composition of each ETF 
- Relative importance of individual stocks within the fund
- Potential concentration risks

## Table of Contents

1. [Setup](#setup)
2. [CSV Data Requirements](#csv-data-requirements)
3. [Usage](#usage)

## Setup

To set up the project, follow these steps:

1. Clone the repository:

    `git clone https://github.com/yourusername/etf-screener-backend.git`

2. Install dependencies: `poetry install`

## CSV Data Requirements

Before running the ETF screener, please ensure that the CSV files in the `data` folder meet the following requirements:

1. File Naming Convention:
   - Each CSV file should be named after the ETF ticker symbol (e.g., `DGRO.csv`, `SCHD.csv`, etc.)

2. File Structure:
   - The CSV files should have columns for 'Ticker', 'Name', and 'Weight(%)'
   - The 'Weight(%)' column should contain decimal values representing the percentage weight of each component in the ETF

3. Data Format:
   - Ensure that all numeric values (including weights) are properly formatted as decimals
   - Remove any commas from numeric values

4. Header Row:
   - The first row of each CSV file should contain the column headers: 'Ticker', 'Name', and 'Weight(%)'

5. Encoding:
   - Use UTF-8 encoding for all CSV files

By adhering to these requirements, the ETF screener will be able to correctly read and process the data from the CSV files in the `data` folder.

## Usage

To run the ETF screener:

1. Activate the virtual environment: `poetry shell`

2. Run the main script: `poetry run run_cli` 


