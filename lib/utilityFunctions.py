import datetime, re, os
def generateUniqueID(prefix=False):
    if prefix != False:
        string = str(prefix) + str(datetime.datetime.now().microsecond)
        return str(string)
    else:
        return str(datetime.datetime.now().microsecond)
        
def askMenu(choices, text):
    counter = 1
    choice_list = []
    for choice in choices:
        new_choice = str(counter) + ". " + str(choice)
        choice_list.append(new_choice) 
        counter += 1
    separator = "\n"
    menu = separator.join(choice_list)
    print(menu)
    print(text)
    user_input = input("Selection: ")
    try:
        index = int(user_input)
        index <= len(choices) == True
        index >= 0 == True
    except ValueError:
        print("Function error! Please make sure choose one of the chosen options!")
    except TypeError:
        print("Function error! Please make sure to input numbers for menu selections!")
    else:
        return index
        
def check_regex(string, regex):
    regex_string = re.compile(regex)
    if re.search(regex_string, string):
        return 1
    else:
        return -1

def validate_and_compare(data_to_validate, data_type, comparator, target_value):
    # check if data is correct type
    if not isinstance(data_to_validate, data_type):
        print("Data to validate is not stated type!")
        return -1
    # check if target value is same type
    if not isinstance(target_value, data_type):
        print("Mismatched data types when comparing data!")
        return -1
    # if data and data type is int
    if data_type == int and isinstance(data_to_validate, int):
        if comparator == ">":
            if data_to_validate > target_value:
                return 1
            else:
                print("Data to validate is not greater than target value!")
                return -1
        elif comparator == "<":
            if data_to_validate < target_value:
                return 1
            else:
                print("Data to validate is not less than target value!")
                return -1
    if comparator == "=" or comparator == "==":
        if data_to_validate == target_value:
            return 1
        else:
            print("Data to validate is not equal to target value!")
            return -1
    else:
        print("Do not use > or < for strings!")

def reverseIterable(iterable):
    return iterable[::-1]

def backupFile(old_path):
    file_path = reverseIterable(reverseIterable(old_path)[0:reverseIterable(old_path).index("/")])
    dot_index = str(file_path).index(".")
    extension = file_path[dot_index:]
    file_name = file_path[:dot_index]
    path_to_save_to = f"./backups/{file_name}"
    # print(file_path, file_name, path_to_save_to, os.path.exists(path_to_save_to))
    if os.path.exists("./backups/") == False:
        os.mkdir("./backups/")
    if os.path.exists(path_to_save_to) == False:
        os.mkdir(path_to_save_to)
    try:
        if os.path.exists(old_path):
            if os.path.exists(path_to_save_to):
                now = datetime.datetime.now()
                new_path = path_to_save_to + "/" + file_name + str(now.year) + str(now.day) + str(now.hour) + str(now.minute) + str(now.second) + extension
                os.rename(old_path, new_path)
            else:
                print("Unable to backup!")
                return -1
        else:
            print("File to backup does not exist!")
            return 1
    except FileNotFoundError:
        print("File not found!")
        return -2
    else:
        return 1    

def importToDict(path, fields):
    try:
        with open(path, "r") as file:
            open_file = file.read()
            lines = (str(open_file).strip()).split("\n")
            # print(open_file, lines)
            items = {}
            anti_overwrite_counter = 0#this is the best way I found to modify the id so that they wouldn't overwrite eachother, as I don't want to wait for a name field to come up for each line and then append that instead
            for line in lines:
                item = {}
                id = generateUniqueID(str(anti_overwrite_counter))
                anti_overwrite_counter += 1
                # print(id)
                for field in fields:
                    value = re.search(re.escape(field) + r"(\w*): ([A-Za-z0-9 @-]+([.][0-9]*)?|[.][0-9]+)", line)
                    if value != None:
                        value_index = str(value.group(0)).index(":")+2
                        value = str(value.group(0))[value_index:]
                        # print(value)
                        isFloat = re.search(r"^[0-9]+" + re.escape(".") + r"[0-9]+$", value)
                        isInt = re.search(r"^[0-9]+$", value)
                        value = float(value) if isFloat != None else value
                        value = int(value) if isInt != None else value
                        key_value = {field: value}
                        # print(value, type(value), isFloat, isInt)
                        item.update(key_value)
                        # print(str(value.group(0)), str(value.group(0))[split_value:])
                        # id = str(value.group(0))[split_value:] + 
                    else:
                        key_value = {field: "undefined"}
                        item.update(key_value)
                    # print(field, key_value)
                if len(item) >= 1:
                    # print("item", item)
                    items[id] = item
    except FileNotFoundError:
        print("File not found!")
    # except Exception as e:
    #     print("Error!", e)
    else:
        return items

def exportItemsToFile(source, export_path):
    try:
        backup = backupFile(export_path)
        string_to_write = compileToString(source)
        file_path = reverseIterable(reverseIterable(export_path)[reverseIterable(export_path).index("/"):])
        if os.path.exists(file_path) == False:
            os.mkdir(file_path)
    except FileNotFoundError:
        print("File not found!")
    except Exception as e:
        print("Error!", e)
    else:	
        if backup != -1 and string_to_write != -1:
            with open(export_path, 'w') as file:
                file.write(string_to_write)
            print(f"Saved {export_path}!")
            return 1
        elif backup != -1 and string_to_write == -1:
            print()
        else:
            print(f"Failed to backup previous file at {export_path} so prevented overwrite")
            return -1

def compileToString(source):
    try:
        strings = []
        if isinstance(source, dict):
            first_layer = source.values()
            for key_value in first_layer:
                second_layer = key_value.items()
                item = []
                for key, value in second_layer:
                    print(key, value, type(value))
                    if isinstance(value, set) or isinstance(value, list):
                        values = []
                        for x in value:
                            values.append(str(x))
                            print(x)
                        value_string = "+".join(values)
                        print(value_string)
                        item.append(f"{key}: {value_string}")
                    else:
                        item.append(f"{key}: {value}")
                item = ", ".join(item)
                strings.append(item)
        elif isinstance(source, list):
            for item in source:
                parameter_list = []
                for parameter in item[1].items():
                    parameter_list.append(f"{parameter[0]}: {parameter[1]}")
                item = ", ".join(parameter_list)
                strings.append(item)
        else:
            print("Unknown data type!")
        string_to_write = "\n".join(strings)
    except Exception as e:
        print("Error!", e)
    else:	
        if string_to_write != "":
            return string_to_write
        else:
            print(f"Failed to compile data to writable string")
            return -1
# data_to_validate = [-4, 1, "1", 1.0]
# for data in data_to_validate:
#     print(validate_and_compare(data, int, ">", 0))
#     print("-------")
# print("===================")
# mixed_to_validate = [-4, "no", "potato", 1.0]
# for mixed_data in mixed_to_validate:
#     print(validate_and_compare(mixed_data, str, ">", "potato"))
#     print("-------")
# print("===================")
# strings_to_validate = ["test", "no", "potato", ""]
# for string in strings_to_validate:
#     print(validate_and_compare(string, str, ">", "potato"))
#     print("-------")

# print(check_regex("tasfasgfsdgdgsdgsd#hgshsdfhest", "[A-Za-z0-9]{1}"))



