from transformers import pipeline
import time

print("1. Downloading/Loading model (this happens once)...")
# The 'pipeline' downloads the default model (distilbert) if not cached
classifier = pipeline("sentiment-analysis")

print("\n2. Running inference...")
start_time = time.time()

# The inputs - feel free to change these!
inputs = [
    "I seriously love how easy Python is for prototyping.",
    "Debugging async race conditions is the absolute worst nightmare."
]

# The inference call
results = classifier(inputs)
end_time = time.time()

# 3. Processing the output
print("-" * 30)
for text, result in zip(inputs, results):
    print(f"Input:  {text}")
    print(f"Output: {result['label']} (Confidence: {result['score']:.4f})")
    print("-" * 30)

print(f"Inference time: {(end_time - start_time):.4f} seconds")

# We've run a deterministic task (Classification).