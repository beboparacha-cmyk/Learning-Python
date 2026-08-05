import pandas as pd

print("....PART 1: PANDAS SERIES....")
scores = [98500, 87200, 76400, 65100, 54800]
players = pd.Series(scores, index=["NightWolf", "StarBlaze", "PixelKing", "CyberFox", "IronStore"])
print(players)

print()
print("....PART 2: PANDAS DATAFRAME....")
data = {
    'Player': ["NightWolf", "StarBlaze", "PixelKing", 'CyberFox', "IronFox"],
    'Score': [98500, 87200, 76400, 65100, 54800],
    'Level': [42, 38, 50, 29, 15],
    'Wins': [210, 185, 162, 140, 118]
}
df = pd.DataFrame(data)
print(df)

print()
print('....PART 3: ACCESSING ROWS....')
print('Row 0 (top player):')
print(df.loc[0])
print('Rows 2 and 3 :')
print(df.loc[2:3])

print()
print('....PART 4: READING A CSV FILE....')
full_df = pd.read_csv('leaderboard.csv')
print('First 5 rows (head):')
print(full_df.head())
print()
print('Last 3 rows (tails):')
print(full_df.tail(3))
print()
print('Dataset info:')
print(full_df.info())

print()
print('....PART 5: CLEANING DATA....')
print('Rows with missing values removed (dropna):')
clean_df = full_df.dropna()
print(clean_df.to_string())
print()
print('Missing values filled with 0 (fillna):')
filled_df = full_df.fillna(0)
print(filled_df.to_string())
