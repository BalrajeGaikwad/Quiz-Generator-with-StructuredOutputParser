# Quiz-Generator-with-StructuredOutputParser
This project is designed to generate and parse structured quiz content using Large Language Models

(LLMs). It leverages LangChain’s components such as:

PromptTemplate → Controls how prompts are sent to the LLM.

ChatOpenAI → The core LLM for generating responses.

StructuredOutputParser → Ensures outputs are in structured formats (like JSON).

ParallelNotes (quizInput / quizOutput) → Enables handling multiple quiz questions and answers simultaneously.

The pipeline guarantees that raw model outputs are transformed into well-structured JSON, making them reliable for downstream use (e.g., web apps, grading systems, or dashboards).

⚙️ Architecture Flow
1. Input Stage
ParallelNotes_quizInput
Accepts multiple quiz questions as input.

PromptTemplate
Defines how each input should be presented to the LLM (e.g., "Create a multiple-choice question about {topic}").

ChatOpenAI
Processes the template and generates quiz content.

StructuredOutputParser
Ensures the generated quiz follows a structured format (e.g., JSON with keys: question, options, answer).

2. Output Stage
ParallelNotes_quizOutput
Collects multiple structured quiz responses.

PromptTemplate
Formats the output request (e.g., "Summarize the quiz questions and answers").

ChatOpenAI
Generates the structured response.

StructuredOutputParser
Ensures final results are valid JSON and parseable.

StructuredOutputParserOutput
Final parsed JSON object that can be consumed by the application.

✅ Benefits
Consistency → All quiz data is structured (no random text).

Scalability → Handles multiple quiz inputs and outputs at once.

Flexibility → Can adapt to different subjects or formats by changing templates.

Reliability → Parsers validate outputs to prevent malformed responses.
