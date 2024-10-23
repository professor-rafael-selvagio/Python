import pandas as pd
df = pd.DataFrame({
    'A': [1, 2, 3, 4],
    'B': [4, 3, 2, 1]
})
df.plot(x='A', y='B')
