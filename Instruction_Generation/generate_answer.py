from openai import OpenAI
from src.utils.logger import get_logger
import random
from src.prompt import get_prompt_output_first_clf, get_prompt_input_first_gen
from src.utils.json_util import get_classified_data, insert_new_answer
from src.query_util import get_answer
import re
def filter_task(list):
    for i, task in enumerate(list):
        task = task.strip()
        if task == "":
            return False
    return True
def generate_answer():
    client = OpenAI()
    logger = get_logger("run5")
    random.seed(123)
    seed_dataset, classified_machine = get_classified_data("result/seed_tasks.jsonl", "result/classification_tasks.jsonl")
    for i, task in enumerate(classified_machine):
        input, output = [], []
        logger.info(f"task {i}")
        if task['is_classification']:
            prompt = get_prompt_output_first_clf(task)
            while len(output) < 1 or len(input) < 1 or len(output) != len(input):
                input, output = [], []
                answer = get_answer("", prompt, client, logger)
                pattern = r"Class label:(.*?)Input:(.*?)(?=Class label:|$)"
                matches = re.findall(pattern, answer, re.DOTALL)
                output = [match[0] for match in matches]
                input = [match[1] for match in matches]
                logger.info(f"answer: {answer}")
                logger.info(f"response: {input} {output}")
                if not filter_task(output) or not filter_task(input):
                    input, output = [], []
                    continue
        else:
            while len(input) < 1 or len(output) < 1 or len(output) != len(input):
                input, output = [], []
                prompt = get_prompt_input_first_gen(task)
                answer = get_answer("", prompt, client, logger)
                pattern = r"Input:(.*?)Output:(.*?)(?=Input:|$)"
                matches = re.findall(pattern, answer, re.DOTALL)
                input = [match[0] for match in matches]
                output = [match[1] for match in matches]
                logger.info(f"answer: {answer}")
                logger.info(f"response: {input} {output}")
                if not filter_task(output):
                    input, output = [], []
                    continue
        insert_new_answer("result/generate_data.jsonl", task, input, output)
generate_answer()