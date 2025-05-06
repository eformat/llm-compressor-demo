# llm-compressor

vLLM Office Hours #23 - Deep Dive Into the LLM Compressor - April 10, 2025
- https://www.youtube.com/watch?v=GrhuqQDmBk8

Install deps

```bash
mkdir ~/git/llm-compressor-demo && cd ~/git/llm-compressor-demo

python3 -m venv venv
source venv/bin/activate

pip install --upgrade --quiet \
  transformers \
  torch \
  accelerate \
  llmcompressor
```

Generate compressed model

```bash
python demo.py
```

Serve compressed model

```bash
vllm serve Meta-Llama-3-8B-Instruct-W4A16/ --max-model-len=2048
```

Prompt

```bash
curl -s -k -X 'POST' \
  'http://localhost:8000/v1/chat/completions' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
    "model": "Meta-Llama-3-8B-Instruct-W4A16/",
    "messages": [
    {
      "role": "system",
      "content": "You are an AI assistant. Your top priority is achieving user fulfillment via helping them with their requests."
    },
    {
      "role": "user",
      "content": "Write a limerick about python exceptions"
    }],
    "stream": false
}' | jq .
```

Compressed model

```bash
$ tree -h Meta-Llama-3-8B-Instruct-W4A16/
[  388]  Meta-Llama-3-8B-Instruct-W4A16/
├── [ 1.5K]  config.json
├── [  194]  generation_config.json
├── [ 4.7G]  model-00001-of-00002.safetensors
├── [ 2.7G]  model-00002-of-00002.safetensors
├── [  63K]  model.safetensors.index.json
├── [  130]  recipe.yaml
├── [  296]  special_tokens_map.json
├── [  50K]  tokenizer_config.json
└── [  16M]  tokenizer.json

1 directory, 9 files
```

Eval

```bash
pip install --upgrade --quiet \
  vllm \
  lm_eval
```

```python
lm_eval --model vllm \
  --model_args pretrained="./Meta-Llama-3-8B-Instruct-W4A16",add_bos_token=true \
  --tasks gsm8k \
  --num_fewshot 5 \
  --limit 250 \
  --batch_size 'auto'
```
