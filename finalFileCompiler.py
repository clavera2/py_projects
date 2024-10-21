import os

user_input = input("Enter absolute path to directory: ")

dir_contents = os.listdir(user_input)

compiled_file_map = {}

for file in dir_contents:
    with open(f"{user_input}/{file}") as f:
        compiled_file_map[file] = f.readlines()

final_file = open(input("What would you like to call the output file: "), "w")

#print(compiled_file_map["test.js"])

for key in compiled_file_map.keys():
    final_file.write(key + ":")
    final_file.write("\n")
    for line in compiled_file_map[key]:
        final_file.write(line)
    final_file.write("\n")
        