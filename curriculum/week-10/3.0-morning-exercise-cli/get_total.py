import sys
import pandas as pd

states = dict()
columns = sys.stdin.readline().split(',')
columns = map(str.strip, columns)
df = pd.DataFrame(columns=columns)

for i, line in enumerate(sys.stdin):
    line = line.split(',')
    line = map(str.strip, line)
    df.loc[i] = line

df['Verbal'] = df['Verbal'].astype(int)
df['Math'] = df['Math'].astype(int)
df['Rate'] = df['Rate'].astype(int)

df['Sum'] = df['Math'] + df['Verbal']

print df['Sum'].to_string(index=False)