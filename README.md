# llm-compressor

vLLM Office Hours #23 - Deep Dive Into the LLM Compressor - April 10, 2025
- https://www.youtube.com/watch?v=GrhuqQDmBk8

```bash
mkdir ~/git/llm-compressor-demo && cd ~/git/llm-compressor-demo

python3 -m venv venv
source venv/bin/activate

pip install --upgrade --quiet \
  transformers \
  torch \
  accelerate \
  llmcompressor  

vllm serve compressed/ --max-model-len=2048

curl -s -k -X 'POST' \
  'http://localhost:8000/v1/chat/completions' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
    "model": "compressed/",
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
