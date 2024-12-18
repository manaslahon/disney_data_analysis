from save_json import load_data
import json



movie_info_list = load_data("disney_data.json")

#Convert runtime to int

def minutes_to_integer(runtime):
    if runtime =="N/A":
        return None
    elif isinstance(runtime, list):
        return int(''.join(filter(str.isdigit, runtime[0])))
    else:
        return int(''.join(filter(str.isdigit, runtime)))

for movie in movie_info_list:
    movie["Running Time (int)"] = minutes_to_integer(movie.get("Running time", "N/A"))


#def budget_to_integer(budget):
#    if budget == 'N/A':
#        return None
#    else:
#        return int(''.join(filter(str.isdigit, budget)))


#for movie in movie_info_list:
#    movie['budget (int)'] = budget_to_integer(movie.get("Budget", "N/A"))


print(movie_info_list[0])
