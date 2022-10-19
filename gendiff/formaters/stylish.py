NEW = "+"
REMOVED = "-"
CHANGED = "+", "-"
UNCHANGED = " "
SPLITTER = ":"

def format(diff):
    
    output = []

    for key, value in diff.items():
        item_name = key
        item_state = value.get("state")
        item_value = value.get("value")
      
        if item_state == "new":
            output.append([NEW, item_name,SPLITTER, str(item_value[1])])
        elif item_state == "removed":
            output.append([REMOVED, item_name, SPLITTER, str(item_value[0])])
        elif item_state == "changed":
            output.append([CHANGED[0], item_name,SPLITTER, str(item_value[0])])
            output.append([CHANGED[1], item_name,SPLITTER, str(item_value[1])])
        elif item_state == "unchanged":
            output.append([UNCHANGED, item_name,SPLITTER, str(item_value[0])])
        elif item_state == "node":
            output.append([' ', item_name,SPLITTER, format(value["value"])])
    
    output.sort(key=lambda json_key: json_key[1])

    return generate_output(output)


def generate_output(list):
    output = ''

    for item in list:
        output += ' '.join(item) + '\n'
    return '{\n' + output + '}'
