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

def get_prompt_task_classification(tasks):
    # prompt = "Can the following task be regarded as a classification task with finite output labels?\n\n"
    # instruction = [task["instruction"] for task in tasks]
    # prompt += f"Task: {tasks[0]["instruction"]}\n"
    # prompt += "Is it classification?"
    pass