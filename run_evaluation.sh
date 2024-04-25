export OPENAI_BASE_URL=https://lonlie.plus7.plus/v1
# export OPENAI_API_KEY=[My_OPENAI_KEY]

git clone https://github.com/tatsu-lab/alpaca_eval.git
cd alpaca_eval/
pip install -e .
cd ..
pip install scikit-learn==1.4.0

export HF_ENDPOINT=https://hf-mirror.com
cp -r Evaluation/llama_fine_tune/ alpaca_eval/src/alpaca_eval/models_configs/
alpaca_eval evaluate_from_model --model_configs 'llama_fine_tune' --annotators_config 'chatgpt'