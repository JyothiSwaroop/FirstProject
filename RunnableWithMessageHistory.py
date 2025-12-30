"""
Docstring for RunnableWithMessageHistory

"""

from transformers import pipeline
from langchain_huggingface import HuggingFacePipeline
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.runnables.history import RunnableWithMessageHistory
from langchain_community.chat_message_histories import ChatMessageHistory
from langchain_core.output_parsers import StrOutputParser

# 1. The "Backend" (Your Local Model)
print("[init] Loading model 'gpt2' for RunnableWithMessageHistory...")
pipe = pipeline(
    'text-generation', 
    model='gpt2', 
    max_new_tokens=50, 
    return_full_text=False
    )

llm = HuggingFacePipeline(pipeline=pipe)

# 2. The Prompt with MEMORY Support
# We use `ChatPromptTemplate` which supports roles: System, User, AI
# We add a `MessagesPlaceholder` to indicate where the message history goes.
prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful AI assistant."),
    MessagesPlaceholder(variable_name="history"), # <--- The Magic Slot
    ("human", "{input}")
])

chain = prompt | llm | StrOutputParser()

# 3. The Memory Wrapper
# We create a Dictionary to store history for different sessions_ids
store = {}

def get_session_history(session_id: str):
    if session_id not in store:
        store[session_id] = ChatMessageHistory()
    return store[session_id]

# We wrap the chain so it knows how to read/write message history
conversation = RunnableWithMessageHistory(
    chain,
    get_session_history,
    input_messages_key="input",  # The key in the input dict for user message
    history_messages_key="history"  # The key in the prompt for message history
)

# 4. Execution - Simulate multiple interactions
print("\n--- Turn 1 ---")
# We use a session_id to track the conversation
response1 = conversation.invoke(
    {"input": "Hi, my name is Dave."},
    config={"configurable": {"session_id": "user_123"}}
)
print(f"AI: {response1}")

print("\n--- Turn 2 ---")
# Notice we don't tell it the name again. It has to remember.
response2 = conversation.invoke(
    {"input": "What is my name?"},
    config={"configurable": {"session_id": "user_123"}}
)
print(f"AI: {response2}")