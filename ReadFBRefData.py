import pandas as pd


def read_csv(filename):
    df = pd.read_csv(filename, header=[0, 1])
    df.columns = rename_columns(df)
    return df


def rename_columns(df):
    new_cols = []
    for col in df.columns:
        if "Unnamed:" in col[0]:
            new_cols.append(col[1])
        else:
            new_cols.append(col[0] + " " + col[1])
    return new_cols
