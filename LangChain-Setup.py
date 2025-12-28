from transformers import pipeline
from langchain_huggingface import HuggingFacePipeline
from langchain_core.prompts import PromptTemplate

# 1. The "Backend" (Your Local Model)
# We reuse the specific pipeline you built before
print("[init] Loading model 'gpt2' for LangChain...")
pipe = pipeline('text-generation', model='gpt2', max_new_tokens=50)

# We wrap the raw pipeline into a LangChain object so it can be "chained"
llm = HuggingFacePipeline(pipeline=pipe)

# 2. The "Frontend" (The Prompt Template)
# This is where we define the behavior. {topic} is our variable.
# Providing system persona. "technical writer explaining concepts to a junior engineer"
template = """
You are a technical writer explaining concepts to a junior engineer.
Concept: {topic}
Explanation:"""

prompt = PromptTemplate.from_template(template)

# 3. The "Chain" (Connecting them)
# This is LCEL syntax. It means: "Take input, format it with prompt, pass to LLM"

chain = prompt | llm

# 4. Execution
print("\n--- Running Chain ---\n")
user_topic = "Docker" #"Recursion"

# invoke() is the standard method to run a chain
result = chain.invoke({"topic": user_topic})

print(result)