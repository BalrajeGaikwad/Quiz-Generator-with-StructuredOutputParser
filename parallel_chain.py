from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
import os
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableParallel

load_dotenv()   

# Models
model1 = ChatOpenAI()
model2 = ChatOpenAI()

# Prompts
prompt1 = PromptTemplate(
    template="Generate short and simple notes from the following text: {text}",
    input_variables=["text"],
)

prompt2 = PromptTemplate(
    template="Generate 5 short question answer from the following text: {text}",
    input_variables=["text"],
)

prompt3 = PromptTemplate(
    template="Merge the provided notes and quiz into a single document:\n\nNotes:\n{notes}\n\nQuiz:\n{quiz}",
    input_variables=["notes", "quiz"],
)

# Parser
parser = StrOutputParser()

# Run notes + quiz generation in parallel
parallel_chain = RunnableParallel(
    {
        "notes": prompt1 | model1 | parser,
        "quiz": prompt2 | model2 | parser,
    }
)

# Merge results
merged_chain = prompt3 | model1 | parser

# Combine full chain
chain = parallel_chain | merged_chain

# Run chain
result = chain.invoke({
    "text": "The LangChain framework is designed to facilitate the development of applications that can process and generate natural language. It provides a set of tools and components that can be used to build complex workflows involving language models, data processing, and more. The framework is modular, allowing developers to easily integrate different components and customize their applications according to specific needs."
})

print(result)
chain.get_graph().print_ascii()
