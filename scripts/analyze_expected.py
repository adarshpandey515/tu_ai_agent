import pandas as pd
from pathlib import Path

def main():
    p = Path('Expected Output.xlsx')
    xl = pd.ExcelFile(p)
    print('Sheets:', xl.sheet_names)
    for s in xl.sheet_names:
        df = xl.parse(s)
        print('---')
        print('Sheet:', s)
        print('Shape:', df.shape)
        print(df.head().to_string(index=False))

if __name__ == '__main__':
    main()
