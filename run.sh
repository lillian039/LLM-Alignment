export OPENAI_BASE_URL=https://lonlie.plus7.plus/v1
# export OPENAI_API_KEY=[My_OPENAI_KEY]
mkdir modelscope_hub

git clone https://github.com/hiyouga/LLaMA-Factory.git
cd LLaMA-Factory/
mkdir dataset
pip install -r requirements.txt
cd ..

pip install modelscope
export MODELSCOPE_CACHE=/mnt/workspace/modelscope_hub
python load_qwen.py

python preprocess.py --dataset Instruction_Generation/result/final_generate.jsonl

mv instructions.jsonl LLaMA-Factory/dataset/
mv dataset_info.json LLaMA-Factory/dataset/

bash Fine_tune/finetune.sh
# bash download.sh

git clone https://github.com/tatsu-lab/alpaca_eval.git
cd alpaca_eval/
pip install -e .
cd ..
pip install scikit-learn==1.4.0

export HF_ENDPOINT=https://hf-mirror.com
cp -r Evaluation/llama_fine_tune/ alpaca_eval/src/alpaca_eval/models_configs/
alpaca_eval evaluate_from_model --model_configs 'llama_fine_tune' --annotators_config 'chatgpt'