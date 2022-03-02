import pandas as pd
import os


def write_csv(path: str, df: pd.DataFrame):
    df.to_csv(path, index=False)


def read_tsv(path: str) -> pd.DataFrame:
    return pd.read_csv(path, sep='\t')


original_folder = os.path.join(os.getcwd(), "data", "original")
processed_folder = os.path.join(os.getcwd(), "data", "processed")

print("Reading titles...")

titles_df = read_tsv(os.path.join(original_folder, "titles.tsv"))
us_titles_df = titles_df[["titleId", "title"]].loc[titles_df["region"] == "US"]
write_csv(os.path.join(processed_folder, "us_titles.csv"), us_titles_df)

print("Reading casts...")

title_principals_df = read_tsv(os.path.join(original_folder, "principals.tsv"))
casts_df = title_principals_df[["tconst", "nconst"]].loc[title_principals_df["category"] == "actor"]
casts_df.rename(columns={"tconst": "titleId"}, inplace=True)
write_csv(os.path.join(processed_folder, "casts.csv"), casts_df)

print("Reading actor names...")

names_df = read_tsv(os.path.join(original_folder, "names.tsv"))
names_df = names_df[["nconst", "primaryName"]]
write_csv(os.path.join(processed_folder, "names.csv"), names_df)
