import pandas as pd
from pathlib import Path

# Script's location
print(Path.cwd())

BASE_DIR = Path(__file__).parent

RAW_DATA = BASE_DIR / "raw" / "data_long.csv"

OUTPUT_DATA = BASE_DIR / "processed" / "data.csv"

OUTPUT_DATA_VITE = (
    BASE_DIR.parent
    / "hg-story"
    / "public"
    / "data"
    / "data.csv"
)


GROUPS = ['nausea_vomiting', 'no_nausea_vomiting', 'hospitalization'] 


def to_percentage(value, TOTAL_PARTICIPANTS):
    try:
        return float(value) / float(TOTAL_PARTICIPANTS) * 100
    except ValueError:
        return value


def add_rows(df, TOTAL_PARTICIPANTS):
    rows = []

    for month in range(1, 9):
        for group in GROUPS:
            
            subset = df[
                (df['month'] == month) &
                (df['group'] == group)
            ]

            main = subset[subset['symptom'] == group] # series

            if main.empty:
                continue

            total_subgroup = main.iloc[0]['prevalence']

            for _, row in subset.iterrows():
                pop_prevalence = to_percentage(row['prevalence'], TOTAL_PARTICIPANTS)
                group_prevalence = to_percentage(row['prevalence'], total_subgroup)

                rows.append({
                    'month': month,
                    'group': group, 
                    'symptom': row['symptom'], 
                    'population_pct': pop_prevalence, 
                    'within_group_pct': group_prevalence
                })
         

    return rows


if __name__ == "__main__":

    ## Load data

    df = pd.read_csv(RAW_DATA)
    TOTAL_PARTICIPANTS = 102810 # participants

    ## Process data

    rows = add_rows(df, TOTAL_PARTICIPANTS)

    ## Store rows in a table

    processed = pd.DataFrame(rows)
    processed.to_csv(OUTPUT_DATA, index=False)

    ## Fetch data into Vite application 

    processed.to_csv(OUTPUT_DATA_VITE, index=False)

