import json
filename = 'data.csv'
dict1 = {}
with open(filename) as fn:
    for line in fn:
        command,description = line.strip().split(None,1)
        dict1[command] = description.strip()
out_file = open("csv_to_json_out.json","w")
json.dump(dict1,out_file,indent=5,sort_keys=False)
out_file.close()