from .example_template import input_first_template_for_gen, output_first_template_for_clf


"""
8 existing instructions are randomly sampled from the task
pool for in-context demonstration. The model is allowed to generate instructions for new tasks, until it stops its
generation, reaches its length limit or generates “Task 16” tokens.
"""
def get_prompt_generate_new_task(tasks):
    prompt = "Come up with a series of tasks:\n\n"
    for i, task in enumerate(tasks):
        instruct = task["instruction"]
        prompt += f"Task {i+1}: {instruct}\n"

    prompt += '\nBase on the examples, please generate 8 more different and diverse tasks in the following format:\n\n'
    prompt += f"Task {len(tasks) + 1}: \nTask {len(tasks) + 2}: \n...\nTask {len(tasks) + 8}: \n"
    return prompt

def get_prompt_task_classification(task_example, test_example):
    prompt = "Can the following task be regarded as a classification task with finite output labels?\n\nHere are some examples\n\n"
    for task in task_example:
        instruction = task["instruction"]
        is_classification = "True" if task["is_classification"] else "False"
        prompt += f"Task: {instruction}\n"
        prompt += f"Is the classification? {is_classification}\n\n"
    prompt += "\nBase on the example, Please provide a Yes or No answer for the following tasks.\n"
    for i, task in enumerate(test_example):
        instruction = task["instruction"]
        prompt += f"Task {i}: {instruction}\n"
        prompt += "Is it classification?\n"
    prompt += f"\nAnswer in the following format:\n\nTask 1: Yes/No\nTask 2: Yes/No\n...\nTask {len(test_example)}: Yes/No\n"
    return prompt

def get_prompt_output_first_clf(test_example):
    prompt = output_first_template_for_clf
    prompt += test_example['instruction']
    return prompt

def get_prompt_input_first_gen(test_example):
    prompt = input_first_template_for_gen
    prompt += test_example['instruction']
    return prompt

