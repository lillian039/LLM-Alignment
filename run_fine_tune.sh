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

