# LLM-Alignment

Team members: Keya Hu, Yijin Guo, Hang Ruan

#### Automatic Instruction Data Generation

- [x] Instruction Generation
- [x] Classification Task Identification
- [x] Instance generation
  - For classification tasks: Output-first approach
  - For other tasks: Input-first approach

- [x] Filter out wrong answers

#### Finetune LLM with instructions and Evaluation

Model: LLaMa

Run the following instructions to fine-tune and evaluate.

```
bash run_fine_tune.sh
bash run_evaluation.sh
```

#### Results

- Generated instructions: [genereated_instructions](Instruction_Generation/result/final_generate.jsonl)
- Fine-tune checkpoints: [checkpoints](Fine_tune/checkpoints/)
- Evaluate results: [evaluation result](Evaluation/result)

#### :dizzy: Our win rate is 14.68% :dizzy: