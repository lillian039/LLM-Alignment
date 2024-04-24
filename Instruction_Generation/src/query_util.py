from openai import OpenAI
import time
from .utils.calculate_cost import update_cost



def send_msg(system, user, client):
    prompt = [
            {"role": "system", "content": system},
            {"role": "user", "content": user}
        ]
    completion = client.chat.completions.create(
    model="gpt-3.5-turbo-0125",
    messages=prompt
    )
    update_cost(completion, "gpt-3.5-turbo-0125")
    return completion.choices[0].message.content

def get_answer(system, user, client, logger):
    try:
        answer = send_msg(system, user, client)
    except Exception as e:
        logger.info(e)
        time.sleep(10)
        try:
            answer = send_msg(system, user, client)
        except Exception as e:
            logger.info(e)
            time.sleep(10)
            answer = None
    return answer