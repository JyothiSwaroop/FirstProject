"""
Docstring for LangChainWithOutputParser.py
This module demonstrates how to use LangChain with a data adapter | Output Parser.
Note: Data Adapter in AI Engineering context is Output Parsers.
"""

from transformers import pipeline
from langchain_huggingface import HuggingFacePipeline
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser # Parser class in python.

# 1. The "Backend" (Your Local Model)
# Engineering fix: We add 'return_full_text=false'
# This ensures the model returns only the generated part, not the full input + output.
pipe = pipeline(
    'text-generation',
    model='gpt2',
    max_new_tokens=50,
    return_full_text=False  # Important for cleaner outputs
)

llm = HuggingFacePipeline(pipeline=pipe)

# 2. The "Frontend" (The Prompt Template)
template = """
You are a technical writer explaining concepts to a junior engineer.
Concept: {topic}
Explanation:"""

prompt = PromptTemplate.from_template(template)

# 3. The Data Adapter (Output Parser)
# Thius component takes the raw object from LLM and converts it to a clean string.
output_parser = StrOutputParser()

# 4. The "Chain" (Connecting them)
# We chain: prompt -> llm -> output_parser with unix style piping.
chain = prompt | llm | output_parser

# 5. Execution
print("\n--- Running Chain with Data Adapter ---\n")
# Instead of "Recursion", it can be dynamic via Microservices.
result = chain.invoke({"topic": "Recursion"}) 

# Notice we don't need to dig into nested dicts/lists. The output parser handled that.
# The result is a clean string.
print(result)


'''
This code is giving me garbage output. Can you help me fix it?
'''