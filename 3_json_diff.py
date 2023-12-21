
class Empty:
    pass


def get_json_diff(diff_list, json_old, json_new):
    diff_dict = {}
    for param in diff_list:
        old_value = find_value(json_old, param)
        new_value = find_value(json_new, param)
        equal = compare_values(old_value, new_value)
        if not equal:
            diff_dict[param] = new_value
    return diff_dict


def find_value(obj, key: str):
    if isinstance(obj, dict):
        if value := obj.get(key):
            return value
        for k, v in obj.items():
            val = find_value(v, key)
            if val:
                return val
    elif isinstance(obj, list):
        for e in obj:
            val = find_value(e, key)
            if val:
                return val
    else:
        return None


def compare_values(val_1, val_2):
    type_1 = type(val_1)
    type_2 = type(val_2)
    if type_1 != type_2:
        return False
    if isinstance(val_1, (str, int, bool, float)):
        return val_1 == val_2
    if isinstance(val_1, list):
        if len(val_1) != len(val_2):
            return False
        for i, e in enumerate(val_1):
            res = compare_values(e, val_2[i])
            if res is False:
                return False
        return True
    if isinstance(val_1, dict):
        if len(val_1) != len(val_2):
            return False
        for k, v in val_1.items():
            res = compare_values(v, val_2.get(k, Empty))
            if res is False:
                return False
        return True


def main():
    from jsons import json_old, json_new

    diff_list = [
        'services',
        'staff',
        'datetime',
    ]

    result = get_json_diff(diff_list, json_old, json_new)
    print(result)


if __name__ == '__main__':
    main()
