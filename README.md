# Programming for Data Analytics (PFDA)

This repository showcases my work for the "Programming for Data Analytics" module. The focus of this module is on developing programming skills for handling, visualizing, and analyzing data, as well as designing algorithms for data-intensive applications.

## Learning Outcomes

Throughout this module, I have gained proficiency in:

- **Data Structures**: Using appropriate data structures and techniques for efficiently handling large-scale data.
- **Numerical Libraries**: Leveraging standard numerical and scientific libraries, including NumPy and Pandas, to perform complex data manipulation and analysis.
- **Data Visualization**: Programmatically creating plots and visual outputs using libraries such as Matplotlib and Seaborn.
- **Regular Expressions**: Using regular expressions for data cleaning and text manipulation.
- **Algorithm Design**: Developing and implementing algorithms to solve numerical and data-related problems.
- **Machine Learning**: Working with basic machine learning models using scikit-learn for predictive analytics.
- **Database Interaction**: Interfacing with databases, specifically working with SQLite for storing and querying data.

## Repository Structure

This repository is organized into three main directories to reflect the different types of work completed during the course:

- **`assignments/`**: Contains practical assignments focusing on data manipulation, visualization, and algorithmic solutions.
- **`project/`**: Includes the final project, which demonstrates the culmination of the skills learned, with a focus on solving a real-world data problem.
- **`my-work/`**: Personal experiments and additional practice work related to the module.

## Key Skills Developed

- **Python Programming**: Proficient in writing clean, efficient Python code, especially in the context of data analysis.
- **Data Handling and Cleaning**: Extensive experience using Pandas for reading, transforming, and cleaning datasets.
- **Data Visualization**: Skilled at creating insightful and informative visualizations using Matplotlib and Seaborn.
- **Machine Learning**: Implemented basic machine learning workflows, including model training, evaluation, and cross-validation using scikit-learn.
- **SQL Databases**: Practical knowledge of working with SQLite databases for storing and retrieving structured data.
- **Algorithmic Problem-Solving**: Developed algorithms to automate tasks, optimize processes, and handle large datasets efficiently.
  

## Project Overview
This project performs a data analysis on stock price data for NVIDIA (NVDA) and Tesla (TSLA) and compares their performance to the S&P 500 benchmark. The analysis includes:
- Fetching historical stock price data using the `yfinance` library.
- Calculating key financial metrics such as daily returns, Sharpe ratios, and cumulative returns.
- Visualizing the performance of a portfolio consisting of NVDA and TSLA stocks.
- Comparing the portfolio's performance to the S&P 500 benchmark.

The goal of this project is to evaluate the risk-adjusted returns of the portfolio and understand how it performs relative to the broader market.

## Installation
To run this project, you'll need the following Python libraries:
- `yfinance`
- `pandas`
- `matplotlib`

Install these libraries using `pip`:
`bash pip install yfinance pandas matplotlib`

## Usage
1. Clone this repository using:
   `git clone https://github.com/CianGallagher/programming-for-data-analytics.git`

2. Navigate to the project directory:
   `cd project/`

3. Open the Jupyter notebook:
    `jupyter notebook portfolio_analysis_tool.ipynb`

4. Run the notebook to perform the analysis and generate the plots.

## Methodology

### Data Fetching

Historical stock price data for NVDA, TSLA, and the S&P 500 (benchmark) was fetched using the yfinance library. The data covers the period from January 1, 2024, to December 31, 2024.

### Portfolio Analysis

The portfolio consists of equal weights (50% each) of NVDA and TSLA stocks. The following metrics were calculated:

    Daily Returns: Percentage change in daily closing prices.

    Excess Returns: Daily returns adjusted for the risk-free rate (derived from the 10-year Treasury bond yield).

    Sharpe Ratio: Risk-adjusted return of the portfolio and individual stocks.

    Cumulative Returns: Growth of the portfolio and individual stocks over time.

Benchmark Comparison

The S&P 500 was used as a benchmark to evaluate the portfolio's performance. The same metrics (daily returns, cumulative returns, and Sharpe ratio) were calculated for the benchmark.

## Results

The analysis revealed the following key insights:

    Portfolio Performance: The portfolio delivered strong cumulative returns but had a lower Sharpe ratio compared to the S&P 500.

    Benchmark Comparison: The S&P 500 outperformed the portfolio in terms of risk-adjusted returns.

    Stock Performance: NVDA showed more consistent growth, while TSLA exhibited higher volatility.

For detailed results, refer to the visualizations and summary tables in the Jupyter notebook.