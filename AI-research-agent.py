import os
from tavily import TavilyClient
from openai import OpenAI
from dotenv import load_dotenv

# Initialize clients

load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
load_dotenv()
TAVLI_API_KEY = os.getenv("TAVILY_API_KEY")
tavily_client = TavilyClient(api_key=TAVLI_API_KEY)
openai_client = OpenAI(api_key=OPENAI_API_KEY)
# Initialize knowledge base
knowledge_base = ""

print("Welcome to the Research Assistant! Type 'quit' to exit.\n")

while True:
    user_question = input("What do you want to research on? ")

    match user_question.lower():
        case "quit":
            print("Goodbye!")
            break
        case _:
            try:
                # Tavily Search
                search_response = tavily_client.search(
                    query=user_question,
                    topic="general",
                    search_depth="advanced",
                    include_answer="advanced",
                    include_raw_content=True
                )

                # Get new data and append it to the knowledge base
                text_data = search_response['answer']
                knowledge_base += "\n" + text_data
                question = user_question

                # OpenAI Chat Completion
                response = openai_client.chat.completions.create(
                    model="gpt-4",
                    messages=[
                        {
                            "role": "system",
                            "content": "You are a research assistant who gives detailed answers to the user's question based on the provided knowledge base."
                        },
                        {
                            "role": "user",
                            "content": f"Here's the knowledge base:\n{knowledge_base}\n\nNow format this data to answer this question in extreme detail: {question}"
                        }
                    ],
                    temperature=0.7
                )

                print("\nAnswer:\n" + response.choices[0].message.content + "\n")

            except Exception as e:
                print(f"Error occurred: {e}")
