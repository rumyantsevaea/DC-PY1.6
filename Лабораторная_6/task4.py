import json

INPUT_FILE = "input.csv"
OUTPUT_FILE = "output.json"

def csv_to_list_dict(input_file, delimiter=",", new_line="\n") -> list[dict]:
    with open(input_file) as file:
        headlines = file.readline().replace(new_line, "").split(delimiter)
        for line in file:
            line = line.replace(new_line, " ")
            return dict(zip(headlines, line.replace(new_line, "").split(delimiter)))

def json_(input_file, delimiter=",", new_line="\n", indent=" "):
    with open(input_file, 'w') as file:
        file.write('[')
        for count_output_file_lines, output_data in enumerate(csv_to_list_dict(INPUT_FILE)):
            if count_output_file_lines > 0:
                file.write(delimiter + new_line + indent + '{')
            else:
                file.write("" + new_line + indent + '{')
            for count_output_data, (key, value) in enumerate(output_data.items()):
                if count_output_data > 0:
                    file.write(delimiter + new_line + f'{indent}{indent}"{key}": "{value}"')
                else:
                    file.write("" + new_line + f'{indent}{indent}"{key}": "{value}"')
            file.write(new_line + indent + '}')
        file.write(new_line + ']')

json_(OUTPUT_FILE)

print(json.dumps(csv_to_list_dict(INPUT_FILE), indent=4))
