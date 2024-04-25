import json
def extract():
    with open('result/model_outputs.json', 'r') as f:
        data = json.load(f)
    print(len(data))
    output_file = 'result/model_outputs_precessed.json'
    with open(output_file, 'w') as f:
        f.write('[')
        for i, task in enumerate(data):
            output = task['output']
            assistants = output.find('assistant\n')
            system = output.find('system\n')
            user = output.find('user\n')
            if assistants == 0 and system != -1:
                extract_instruction = output[len('assistant\n'): system]
                task['output'] = extract_instruction
            if user == 0 and assistants != -1:
                extract_instruction = output[len('user\n'): assistants]
                task['output'] = extract_instruction
            json.dump(task, f,indent=4, separators=(',', ': '))
            if i < len(data) - 1: f.write(',\n')
        f.write(']')
extract()