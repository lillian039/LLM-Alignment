import openai
from openai import OpenAI
import json
from src.query_util import get_answer
from src.prompt import get_prompt_task_classification
from src.utils.logger import get_logger
import random
import os
from rouge_score import rouge_scorer
from src.utils.json_util import insert_new_classification, get_seed_machine
import re

def classify_instruction():
    
    client = OpenAI()
    logger = get_logger("run2")
    random.seed(123)
    seed_instructions, machine_instructions = get_seed_machine("seed_tasks.jsonl", "generate_tasks2.jsonl")
    seed_is_classification = []
    seed_not_classification = []
    for instruction in seed_instructions:
        if instruction["is_classification"]:
            seed_is_classification.append(instruction)
        else:
            seed_not_classification.append(instruction)
    seed_classification_example = random.sample(seed_is_classification, 12) + random.sample(seed_not_classification, 12)
    random.shuffle(seed_classification_example)
    random.shuffle(machine_instructions)

    for i in range(0, len(machine_instructions), 10):
        sub_list = machine_instructions[i:i+10]
        prompt = get_prompt_task_classification(seed_classification_example, sub_list)
        answer = get_answer("", prompt, client, logger)
        classification_result = re.findall(r"Task (\d+): (.+)", answer)
        logger.info(prompt)
        logger.info(f"response: {classification_result}")
        for inst, (num, is_classification) in zip(sub_list, classification_result):
            insert_new_classification("classification_tasks3.jsonl", inst["instruction"], is_classification)

classify_instruction()

