import pandas as pd

def calculate_rsi(df, close_column='close', window=14):
    df['Gain'] = df[close_column].diff()
    df['Gain'] = df['Gain'].apply(lambda x: x if x > 0 else 0)
    df['Loss'] = df[close_column].diff()
    df['Loss'] = df['Loss'].apply(lambda x: abs(x) if x < 0 else 0)

    def custom_rolling_average(data, window):
        rolling_avg = []
        for i in range(len(data)):
            if i < window - 1:
                rolling_avg.append(None)
            else:
                if i == window - 1:
                    rolling_avg.append(data.iloc[:i + 1].mean())
                else:
                    prev_avg = rolling_avg[-1]
                    current_val = data.iloc[i]
                    prev_val = data.iloc[i - window]
                    new_avg = ((prev_avg * (window - 1)) + current_val) / window
                    rolling_avg.append(new_avg)
        return pd.Series(rolling_avg, index=data.index)

    df['Average Gain'] = custom_rolling_average(df['Gain'], window=window)
    df['Average Loss'] = custom_rolling_average(df['Loss'], window=window)

    df['RS'] = df['Average Gain'] / df['Average Loss']

    df['RSI'] = 100 - (100 / (1 + df['RS']))

    return df['RSI']

