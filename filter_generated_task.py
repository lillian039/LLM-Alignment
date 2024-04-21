from openai import OpenAI
from src.utils.logger import get_logger
import random
from src.prompt import get_prompt_output_first_clf, get_prompt_input_first_gen
from src.utils.json_util import get_classified_data, insert_final
from src.query_util import get_answer
import re

def filter_task():
    client = OpenAI()
    logger = get_logger("run5")
    random.seed(123)
    seed_dataset, generated_data = get_classified_data("result/seed_tasks.jsonl", "result/generate_data2.jsonl")
    for i, task in enumerate(generated_data):
        flag = True
        instance = task['instance']
        for pair in instance:
            if pair['output'] == 'None':
                flag = False
                break
        if flag:
            insert_final("result/final_generate.jsonl", task)
    for i, task in enumerate(seed_dataset):
        instruction = {"instruction": task['instruction'], "is_classification": task['is_classification'],"instance":task['instances']}
        insert_final("result/final_generate.jsonl", instruction)
filter_task()