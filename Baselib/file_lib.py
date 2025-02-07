import json

def read_json_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        data = json.load(f)
    return data


def write_json_file(filepath, data:json):
    with open(filepath, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)


def write_txt_file(filepath, text:str):
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(text)