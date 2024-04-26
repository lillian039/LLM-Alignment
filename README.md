# LLM-Alignment

Team members: Keya Hu, Yijin Guo, Hang Ruan

#### Automatic Instruction Data Generation

- [x] Instruction Generation
- [x] Classification Task Identification
- [x] Instance generation
  - For classification tasks: Output-first approach
  - For other tasks: Input-first approach
- [x] Filter out wrong answers

Run the following command to generate instructions.

```
bash run_generate.sh
```

#### Finetune LLM with instructions and Evaluation

Model: Qwen-1.5

Run the following instructions to fine-tune and evaluate.

```
bash run_fine_tune.sh
bash run_evaluation.sh
```

#### Results

We fine-tune iterations for 100 and 5000 and get two results. 100 yields better performance.

- Generated instructions: [genereated_instructions](Instruction_Generation/result/final_generate.jsonl)
- Fine-tune checkpoints: [checkpoints 100](Fine_tune/iteration_100/checkpoints/) and  [checkpoints 5000](Fine_tune/iteration_5000/checkpoints/)
  - Fine_tune model for 5000 rounds: https://jbox.sjtu.edu.cn/l/O1rapi
  - Fine_tune model for 100 rounds: https://jbox.sjtu.edu.cn/l/l1gyS2
  - Download the model named `model.safetensors` and put it into [qwen_sft](Fine_tune/checkpoints/qwen_sft)
- Evaluate results: [evaluation result](Evaluation/result)

#### :dizzy: Our win rate is 23.16% :dizzy: