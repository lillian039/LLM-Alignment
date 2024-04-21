上实例步骤（截至于sft阶段）：
1. 上实例前需要传输的文件：
   
   generate_tasks.jsonl
   
   preprocess.py
   
   finetune.sh

2. 配环境：

   ```
   mkdir Homework
   cd Homework
   mkdir modelscope
   conda activate base
   
   ## clone llama-factory as sft codebase
   git clone https://github.com/hiyouga/LLaMA-Factory.git
   cd LLaMA-Factory/
   pip install -r requirements.txt
   cd ..
   
   ## Qwen
   pip install modelscope
   export MODELSCOPE_CACHE=/root/Homework/modelscope_hub
   python
   >>> from modelscope.models import Model
   >>> model = Model.from_pretrained('qwen/Qwen1.5-0.5B')
   ```

3. 文件移动和生成

   ```
   python preprocess.py --dataset [instructions_file_name]
   ```

   生成的`instructions.jsonl`和`dataset_info.json`，移动到`LLaMA-Factory/dataset`中。

   修改`finetune.sh`中的`BASE_MODEL`路径

4. 运行

   ```
   bash finetune.sh
   ```

   