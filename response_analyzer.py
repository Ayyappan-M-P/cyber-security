# response_analyzer.py

import pandas as pd

def analyze_responses(response_data):
    df = pd.DataFrame(response_data, columns=['Email', 'Clicked'])
    click_rate = df['Clicked'].mean() * 100
    print(f"Click Rate: {click_rate:.2f}%")

    vulnerable_employees = df[df['Clicked'] == True]['Email'].tolist()
    return vulnerable_employees
