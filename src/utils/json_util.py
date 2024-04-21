import json
import os
def read_last_line_jsonl(file_path):
    last_line = ""
    with open(file_path, "r") as f:
        for line in f:
            last_line = json.loads(line)
    return last_line

def insert_new_instruct(file_path, new_inst):
    mode = "a" if os.path.exists(file_path) else "w"
    number = 0
    if mode == "a":
        last_line = read_last_line_jsonl(file_path)
        number = int(last_line["inst_id"]) + 1
    new_data = {"inst_id": number, "instruction": new_inst}
    with open(file_path, mode) as f:
        f.write(json.dumps(new_data) + "\n")
    return new_data

def insert_new_classification(file_path, inst, is_classify_str):
    mode = "a" if os.path.exists(file_path) else "w"
    number = 0
    if mode == "a":
        last_line = read_last_line_jsonl(file_path)
        number = int(last_line["inst_id"]) + 1
    is_classify = True if is_classify_str == "Yes" else False
    new_data = {"inst_id": number, "instruction": inst, "is_classification": is_classify}
    with open(file_path, mode) as f:
        f.write(json.dumps(new_data) + "\n")
    return new_data

def insert_new_answer(file_path, inst, input_list, output_list):
    mode = "a" if os.path.exists(file_path) else "w"
    number = 0
    if mode == "a":
        last_line = read_last_line_jsonl(file_path)
        number = int(last_line["inst_id"]) + 1
    inst["instance"] = []
    for i, (input, output) in enumerate(zip(input_list, output_list)):
        input_content = input
        input_content = input_content.strip()
        if input_content == "None":
            input_content = ""
        output_content = output
        output_content = output_content.strip()
        if output_content == "" and input_content == "":
            continue
        inst["instance"].append({"input": input_content, "output": output_content})
    with open(file_path, mode) as f:
        f.write(json.dumps(inst) + "\n")
    return inst

def insert_final(file_path, instruction):
    mode = "a" if os.path.exists(file_path) else "w"
    number = 0
    if mode == "a":
        last_line = read_last_line_jsonl(file_path)
        number = int(last_line["inst_id"]) + 1
    instruction["inst_id"] = number
    with open(file_path, mode) as f:
        f.write(json.dumps(instruction) + "\n")

def get_seed_machine(seed_path, machine_path):
    seed_instructions = []
    machine_instructions = []
    with open(seed_path) as f:
        for line in f:
            data = json.loads(line)
            seed_instructions.append(data)
    if os.path.exists(machine_path):
        with open(machine_path) as f:
            for line in f:
                data = json.loads(line)
                machine_instructions.append(data)
    return seed_instructions, machine_instructions

def get_classified_data(seed_path, machine_path):
    seed_instructions = []
    machine_instructions = []
    with open(seed_path) as f:
        for line in f:
            data = json.loads(line)
            seed_instructions.append(data)
    with open(machine_path) as f:
        for line in f:
            data = json.loads(line)
            machine_instructions.append(data)
    return seed_instructions, machine_instructions
