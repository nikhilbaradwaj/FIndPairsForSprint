import json

def read_json_file(file_name):
    with open(file_name) as json_file:
        data = json.load(json_file)

    return data

def write_to_file(weeks):
    file = open("app/output.txt", "w")
    for index, week in enumerate(weeks):
        file.write(f"Week {index + 1}:\n")
        for pair in week:
            if len(pair) == 1:
                file.write(f"Name: {pair[0]['name']}, Title: {pair[0]['title']}\n")
            else:
                file.write(f"Name: {pair[0]['name']}, Title: {pair[0]['title']}, Name: {pair[1]['name']}, Title: {pair[1]['title']}\n")

    file.close()

def print_output(weeks):
    for index, week in enumerate(weeks):
        print(f"Week {index + 1}:")
        for pair in week:
            if len(pair) == 1:
                print(f"Name: {pair[0]['name']}, Title: {pair[0]['title']}")
            else:
                print(f"Name: {pair[0]['name']}, Title: {pair[0]['title']}, Name: {pair[1]['name']}, Title: {pair[1]['title']}")
