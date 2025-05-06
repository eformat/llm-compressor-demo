from transformers import AutoModelForCausalLM

MODEL_ID = "meta-llama/Meta-Llama-3-8B-Instruct"
#MODEL_ID = "meta-llama/Llama-3.2-3B-Instruct"
DEVICE = "auto" # "auto" # cpu
model = AutoModelForCausalLM.from_pretrained(MODEL_ID, device_map=DEVICE)

from llmcompressor.modifiers.quantization import QuantizationModifier

SCHEME = "W4A16"

# choose a recipe memory optimized for chat
recipe = QuantizationModifier(
    targets = "Linear",
    scheme = SCHEME,
    ignore = ["lm_head"]
)

from llmcompressor import oneshot

oneshot(
    model = model,
    recipe = recipe,
    output_dir = MODEL_ID.split("/")[1] + "-" + SCHEME
)
