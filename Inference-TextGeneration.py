from transformers import pipeline, set_seed

# 1. Setup the generator
# We use 'gpt2', a lightweight ancestor of GPT-4.
# 'set_seed' ensures we get reproducible results for this demo.
print("[init] Loading model 'gpt2'...")
generator = pipeline('text-generation', model='gpt2')
set_seed(42)

print("[init] Model loaded. Starting generation...")

# 2. The Inputs Prompts
# We give it a nudge, and it completes the throught.
prompts = [ 
    "The future of software engineering is",
    "To fix a segmentation fault, you must"
]

# 3. The Inference
# max_new_tokens=30 limits the output length to 30 new tokens.
# num_return_sequences=1 means we just want one version of the output.
print("[generate] Running inference...")
outputs = generator(prompts, max_new_tokens=30, num_return_sequences=1)
print("[generate] Inference complete.")

# 4. Print the Outputs
print("[output] Printing results")
print("-" * 30)
for prompt, output in zip(prompts, outputs):
    # result is a list of dictionaries, we grab the first one
    generated_text = output[0]['generated_text']

    print(f"Prompt: {prompt}")
    print(f"Result: {generated_text}...")
    print("-" * 30)

print("END of Inference-TextGeneration.py")