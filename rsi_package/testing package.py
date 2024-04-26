import pandas as pd
from rsi_package.rsi_calculator.rsi_calculator import calculate_rsi

# Load your data into a pandas DataFrame (replace 'your_data.csv' with your actual data file)
df = pd.read_csv("C:/Users/kvsvy/Downloads/26-10-2023-TO-26-04-2024-RELIANCE-ALL-N.csv")

# Calculate RSI
rsi_values = calculate_rsi(df)

# Add RSI values as a new column to the DataFrame
df['RSI'] = rsi_values
# Drop unnecessary columns
df = df[['date', 'close', 'RSI']]
# Display the DataFrame with RSI values
print(df.tail())


