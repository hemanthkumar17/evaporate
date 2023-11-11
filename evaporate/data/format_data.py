import os
import json
import random
if __name__ == "__main__":
    json_list = {}
    path = "./10k_json/extracted/"
    for file in os.listdir(path):
    # for file in random.sample(os.listdir(path), 100):
        if file.endswith(".json"):
            with open(path + file) as f:
                json_list[file] = json.load(f)
    
    ret_json_list = json_list.copy()
    for file in json_list:
        for attr in json_list[file]:
            if json_list[file][attr]:   
                print(attr, ":", len(json_list[file][attr]))
                if len(json_list[file][attr]) > 200:
                    json_list[file][attr] = json_list[file][attr][:200] + "..."
                    print("New length for ", attr, ":", len(json_list[file][attr]))
    print(json_list.keys())
    with open("10k_collated.json", "w+") as f:
        json.dump(json_list, f)