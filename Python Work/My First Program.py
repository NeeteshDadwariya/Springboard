import pandas as pd

A = [(0, 1),
     (1, 1)];
new_df = df_A = pd.DataFrame(data=A);

for i in range(0, 3):
    new_df = new_df.dot(df_A);
    print(str(i))
    print(new_df)
