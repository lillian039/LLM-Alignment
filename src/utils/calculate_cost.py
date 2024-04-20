cost = {"gpt-4":(0.03, 0.06), "gpt-3.5-turbo-0125":(0.0005, 0.0015), "gpt-4-0125-preview":(0.01, 0.03), "gpt4t":(0.01, 0.03)}

def update_cost(completion, model_type):
    with open('result/total_cost.txt', 'r') as file:
        cost_record = float(file.read())
    new_input_token = completion.usage.prompt_tokens
    new_output_token = completion.usage.completion_tokens
    i_cost, o_cost = cost.get(model_type)
    cost_record += (i_cost * new_input_token + o_cost * new_output_token)/1000
    
    with open('result/total_cost.txt', 'w') as file:
        file.write(str(cost_record))