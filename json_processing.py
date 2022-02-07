import json

def type_filtering(input_dict, type_id):
    input_dict['features'] = [x for x in input_dict['features'] if x['properties']['type_id'] in type_id]
    return input_dict

def type_cleaning(input_dict):
    for item in input_dict['features']:
        item['properties']['type_id'] = 1
    return input_dict

if __name__ == "__main__":
    input_json = 'xView_train.geojson'

    with open(input_json) as f:
        output_dict = json.load(f)

    output_dict = type_filtering(output_dict, [79])

    #output_dict = type_cleaning(output_dict)

    output_json = json.dumps(output_dict)
    with open('new_train.geojson', 'w') as outfile:
        json.dump(output_dict, outfile)




