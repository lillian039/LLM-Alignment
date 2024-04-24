import json
import argparse

parser = argparse.ArgumentParser(description='')

parser.add_argument('--dataset', help='dataset', default="generate_tasks.jsonl")
args = parser.parse_args()

with open(args.dataset, 'r') as f:
    data = f.readlines()

with open('instructions.jsonl', 'w') as f:
    for line in data:
        instance = json.loads(line)
        instances = instance["instance"]

        other_fields = {key: value for key, value in instance.items() if key != "instance"}

        for item in instances:
            new_item = other_fields.copy() 
            new_item.update({"input": item["input"], "output": item["output"]})  
            json.dump(new_item, f)
            f.write('\n')

# 创建包含要写入JSONL文件的字典
data = {
    "instructions.jsonl": {
        "file_name": "instructions.jsonl",
        "formatting": "alpaca",
        "columns (optional)": {
            "prompt": "instruction",
            "query": "input",
            "response": "output"
        }
    }
}

json_str = json.dumps(data, indent=4)

# 写入JSONL文件
with open('dataset_info.json', 'w') as file:
    file.write(json_str)

print('dataset_info is ok。')
