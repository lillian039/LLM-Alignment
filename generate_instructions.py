from openai import OpenAI
import json
from src.query_util import get_answer
from src.prompt import get_prompt_generate_new_task
from src.utils.logger import get_logger
import random
import os
from rouge_score import rouge_scorer
from src.utils.json_util import insert_new_instruct, get_seed_machine
import re

def main():
    client = OpenAI()
    random.seed(123)
    logger = get_logger("run3")
    seed_instructions, machine_instructions = get_seed_machine("seed_tasks.jsonl", "generate_tasks2.jsonl")
    seed_is_classification = []
    seed_not_classification = []
    for instruction in seed_instructions:
        if instruction["is_classification"]:
            seed_is_classification.append(instruction)
        else:
            seed_not_classification.append(instruction)
    whether_classify = len(seed_is_classification) / len(seed_instructions)
    # generate instructions
    while len(machine_instructions) < 1000:
        prompt_instructions = []
        select_instruction = seed_is_classification if random.random() < whether_classify else seed_not_classification
        iter_seed = 6 if len(machine_instructions) > 1 else 8
        prompt_instructions += random.sample(select_instruction, iter_seed)
        if iter_seed == 6:
            prompt_instructions += random.sample(machine_instructions, 2)
        prompt = get_prompt_generate_new_task(prompt_instructions)
        answer = get_answer("", prompt, client, logger)
        new_instions = re.findall(r"Task (\d+): (.+)", answer)

        logger.info(prompt)
        logger.info(f"response: {new_instions}")
        for id, new_inst in new_instions:
            # check if the response is valid
            if new_inst == "":
                continue
            # filter out too short or too long instructions
            if len(new_inst.split()) <= 3 or len(new_inst.split()) > 150:
                continue
            # filter based on keywords that are not suitable for language models.
            if any(word in new_inst for word in ["image", "images", "graph", "graphs", "picture", "pictures", "file", "files", "map", "maps", "draw", "plot", "go to"]):
                continue
            # filter based on rougescorer
            all_instructions = seed_instructions + machine_instructions
            scorer = rouge_scorer.RougeScorer(["rougeL"], use_stemmer=False)
            rouge_scores = []
            for exist_inst in all_instructions:
                score = scorer.score(new_inst, exist_inst["instruction"])["rougeL"].fmeasure
                rouge_scores.append(score)
            if max(rouge_scores) > 0.7:
                continue

            # add new response
            new_data = insert_new_instruct("generate_tasks2.jsonl", new_inst)
            machine_instructions.append(new_data)

main()
