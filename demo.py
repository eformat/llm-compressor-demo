from transformers import AutoModelForCausalLM

MODEL_ID = "meta-llama/Meta-Llama-3-8B-Instruct"
model = AutoModelForCausalLM.from_pretrained(MODEL_ID, device_map="auto")

from llmcompressor.modifiers.quantization import QuantizationModifier

# choose a recipe memory optimized for chat
recipe = QuantizationModifier(
    targets = "Linear",
    scheme = "W4A16",
    ignore = ["lm_head"]
)

from llmcompressor import oneshot

oneshot(
    model = model,
    recipe = recipe,
    output_dir = "compressed"
)
