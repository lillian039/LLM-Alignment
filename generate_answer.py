from openai import OpenAI
from src.utils.logger import get_logger
import random
from src.prompt import get_prompt_output_first_clf, get_prompt_input_first_gen
from src.utils.json_util import get_classified_data, insert_new_answer
from src.query_util import get_answer

def generate_answer():
    client = OpenAI()
    logger = get_logger("run4")
    random.seed(123)
    seed_dataset, classified_machine = get_classified_data("result/seed_tasks.jsonl", "result/classification_tasks2.jsonl")
    for task in classified_machine:
        if task['is_classification']:
            prompt = get_prompt_output_first_clf(task)
        else:
            prompt = get_prompt_input_first_gen(task)
        answer = get_answer("", prompt, client, logger)
        insert_new_answer("result/generate_data.jsonl", task, answer)
        exit(0)

generate_answer()