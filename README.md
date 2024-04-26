
![logo](downloadrsi.jpg)


# Working with stock market data ?
# Wondering how to calculate Relative strength index values that matches exactly the same with your broker accounts?
# welcome to rsi package 0.2 
([click here for Pypi Link](https://pypi.org/project/rsi-package/))

## Why
This Python package provides an accurate calculation of the Relative Strength Index (RSI) using rolling averages. Unlike many existing packages that use simple 14-day averages, this package implements a rolling average formula that produces RSI values that closely match those seen in broker accounts and platforms like TradingView.

## Implementation Details
### CSV File format required as shown in  below 

|date|close|
|----|-----|
|29-01-2024	|2896.10
|30-01-2024	|2815.25
|31-01-2024	|2853.25
|01-02-2024	|2853.30
|02-02-2024	|2915.40

### Installation

#### You can install the RSI Calculator package using pip:
        pip install rsi-package

#### Copy and paste the following code 
    import pandas as pd
    from rsi_package.rsi_calculator.rsi_calculator import calculate_rsi

    # Load your data into a pandas DataFrame (replace 'your_data.csv' with your actual data file)
    df = pd.read_csv("yourfile.csv")

    # Calculate RSI
    rsi_values = calculate_rsi(df)

    # Add RSI values as a new column to the DataFrame
    df['RSI'] = rsi_values
    # Drop unnecessary columns
    df = df[['date', 'close', 'RSI']]
    # Display the DataFrame with RSI values
    print(df.tail())


## Dataset Details 

- For indian stock market You can download any stock data from NSE Website ([using this Link](https://www.nseindia.com/report-detail/eq_security))

- for example i chose to download "Reliance Industries Limited" data for one year (it is advised to use data atleast larger than 6 months for best results, you can download the same file from this repo.)


## Evaluation and Results

- the table below shows the value of RSI for the corresponding dates from the "Reliance Industries Limited" data using the rsi_package
          
|date      |   close  | RSI   |
|----------|----------|-------|
|19-04-2024|  2940.25 | 51.82 |
|22-04-2024|  2959.70 |54.82  |
|23-04-2024|  2918.65 |48.01  |
|24-04-2024|  2900.35 | 45.31 |
|25-04-2024|  2919.95 | 48.64 |



## Libraries 

**Language:** Python

**Packages:** , Pandas, rsi-package




## Contact

If you have any feedback/are interested in collaborating, please reach out to me at [<img height="40" src="https://img.icons8.com/color/48/000000/linkedin.png" height="40em" align="center" alt="Follow Kartikey on LinkedIn" title="Follow Kartikey on LinkedIn"/>](https://www.linkedin.com/in/kartikey-vyas-2a29b9273) &nbsp; <a href="mailto:kvsvyas@gmail.com"> <img height="40" src="https://img.icons8.com/fluent/48/000000/gmail.png" align="center" />





## License

[MIT](https://choosealicense.com/licenses/mit/)

