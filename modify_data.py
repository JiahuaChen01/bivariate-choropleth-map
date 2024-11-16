import pandas as pd
import json

df = pd.read_json("state_obesity_fastfood_data.json")

df_sorted = df.sort_values(by="obesity_percentage")

least = df_sorted.iloc[[0]]

most = df_sorted.iloc[[-1]]

middle_index = len(df_sorted)//2
middle = df_sorted.iloc[[middle_index]]

second = df_sorted.iloc[[middle_index//2]]

fourth = df_sorted.iloc[[middle_index + middle_index//2]]

five_states = pd.concat([least, second, middle, fourth, most]) 

five_states = five_states[["name", "obesity_percentage", "McDonalds", "Starbucks", "Subway", "Taco_Bell"]]

target_df = five_states.melt(id_vars=['name', 'obesity_percentage'], 
value_vars=['McDonalds', 'Starbucks', 'Subway', 'Taco_Bell'],
var_name='restaurant', value_name='count')

json_data = target_df.to_dict(orient="records")

print(json.dumps(json_data))


