from transformers import pipeline

# from transformers import BertTokenizer, BertForSequenceClassification
# TODO: Explore BertTokenizer & BertForSequenceClassification in FinBERT model

# 1. Setup the Specialized Model
# We point to specific repo on the Hub: ''ProsusAI/finbert'
classifier = pipeline("sentiment-analysis", model="ProsusAI/finbert")

print("/n--- Running Financial Sentiment Analysis with FinBERT ---/n")

# 2. The Input Prompts
inputs = [
    # A sentence that sounds bad in real life, but might be good for a company's bottom line
    "The company announced a restructuring plan to cut operational costs by 20%.",
    
    # A generic sentence that FinBERT might find confusing or irrelevant
    "I hate waiting in line at the grocery store." 
]

results = classifier(inputs)

# 3. Print the Outputs
for text, result in zip(inputs, results):
    print(f"Input:  {text}")
    print(f"Label:  {result['label']}")
    print(f"Score:  {result['score']:.4f}") # Confidence level (0-1)
    print("-" * 40)

print("END of Inference-FinBERT.py")