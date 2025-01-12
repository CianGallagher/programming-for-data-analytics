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
- Detecting anomalies in stock price data using the Isolation Forest algorithm.

The goal of this project is to evaluate the risk-adjusted returns of the portfolio, understand how it performs relative to the broader market, and identify unusual price movements.

## Installation
To run this project, you'll need the following Python libraries:
- `yfinance`
- `pandas`
- `matplotlib`
- `scikit-learn` (for Isolation Forest) 

Install these libraries using `pip` in a terminal:
`pip install yfinance pandas matplotlib scikit-learn`

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
The `yfinance` library was chosen for its simplicity and effectiveness in fetching historical stock data. It provides free, easy-to-use access to a wide range of financial instruments (e.g., stocks, indices) and integrates seamlessly with Pandas for data analysis. Its intuitive API and flexibility in specifying time periods make it ideal for projects like this one.

### Portfolio Analysis

The portfolio consists of equal weights (50% each) of NVDA and TSLA stocks. The following metrics were calculated:

- Daily Returns: Percentage change in daily closing prices.

- Excess Returns: Daily returns adjusted for the risk-free rate (derived from the 10-year Treasury bond yield).

- Sharpe Ratio: Risk-adjusted return of the portfolio and individual stocks.

- Cumulative Returns: Growth of the portfolio and individual stocks over time.

### Benchmark Comparison

The S&P 500 was used as a benchmark to evaluate the portfolio's performance. The same metrics (daily returns, cumulative returns, and Sharpe ratio) were calculated for the benchmark.

### Anomaly Detection

The Isolation Forest algorithm was used to detect unusual patterns in the stock price data for NVDA. With a contamination parameter of 0.01 (1% of the data considered outliers), the model identified specific days where the stock prices deviated significantly from normal behavior. These anomalies could indicate significant market events, such as earnings reports, news releases, or external shocks.

## Results

The analysis revealed the following key insights:

1. Portfolio Performance: The portfolio delivered strong cumulative returns but had a lower Sharpe ratio compared to the S&P 500.

2. Benchmark Comparison: The S&P 500 outperformed the portfolio in terms of risk-adjusted returns.

3. Stock Performance: NVDA showed more consistent growth, while TSLA exhibited higher volatility.

4. Anomaly Detection: The Isolation Forest model successfully identified anomalies in NVDA's stock price data, highlighting days with unusual price movements. These anomalies are visualized in the Jupyter notebook.

For detailed results, refer to the visualizations and summary tables in the Jupyter notebook.

## References

1. **Markdown Guide:**  
   Used for formatting README and notebook file.  
   - [Markdown Cheatsheet](https://www.markdownguide.org/cheat-sheet/)  
   - [Mastering Markdown](https://guides.github.com/features/mastering-markdown/)  

2. **yfinance Documentation:**  
   Used to fetch historical stock price data for NVDA, TSLA, and the S&P 500 benchmark.  
   - [yfinance Documentation](https://pypi.org/project/yfinance/)  
   - [yfinance GitHub Repository](https://github.com/ranaroussi/yfinance)  

3. **Pandas Documentation:**  
   Used for data manipulation, cleaning, and analysis, including calculating daily returns, cumulative returns, and portfolio metrics.  
   - [Pandas Documentation](https://pandas.pydata.org/docs/)  
   - [Pandas User Guide](https://pandas.pydata.org/pandas-docs/stable/user_guide/index.html)  

4. **Matplotlib Documentation:**  
   Used for visualizing stock prices, cumulative returns, and anomalies.  
   - [Matplotlib Documentation](https://matplotlib.org/stable/contents.html)  
   - [Matplotlib Tutorials](https://matplotlib.org/stable/tutorials/index.html)  

5. **Risk-Free Rate:**  
   The 10-year Treasury bond yield was used as the risk-free rate in the Sharpe ratio calculation.  
   - [CNBC: US10Y](https://www.cnbc.com/quotes/US10Y)  
   - [Treasury Yield Explanation](https://www.investopedia.com/terms/t/treasury-yield.asp)  

6. **Sharpe Ratio Calculation:**  
   Methodology based on financial theory to evaluate risk-adjusted returns.  
   - [Investopedia: Sharpe Ratio](https://www.investopedia.com/terms/s/sharperatio.asp)  
   - [Modern Portfolio Theory (MPT)](https://www.investopedia.com/terms/m/modernportfoliotheory.asp)  

7. **Scikit-learn Documentation:**  
   Used for anomaly detection with the Isolation Forest algorithm.  
   - [Scikit-learn Isolation Forest](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.IsolationForest.html)  
   - [Scikit-learn User Guide](https://scikit-learn.org/stable/user_guide.html)  

8. **Isolation Forest Algorithm:**  
   A machine learning algorithm for anomaly detection, based on isolating outliers in the data.  
   - [Original Isolation Forest Paper](https://cs.nju.edu.cn/zhouzh/zhouzh.files/publication/icdm08b.pdf)  
   - [Isolation Forest Explained](https://towardsdatascience.com/outlier-detection-with-isolation-forest-3d190448d45e)  

