import pandas as pd

pd.set_option('display.max_columns', 50)  # display columns
df = pd.read_json(r'/Users/vikentijzerebov/PycharmProjects/PyParserHabr/scrapped_data/parsed_vacancies.json')
df.to_csv("recruiters.csv")