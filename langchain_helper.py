import os
import getpass
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.prompts import PromptTemplate
from langchain.chains import SequentialChain
from langchain.chains import LLMChain

load_dotenv()

if "GOOGLE_API_KEY" not in os.environ:
    os.environ["GOOGLE_API_KEY"] = getpass.getpass("Enter your Api key")

llm = ChatGoogleGenerativeAI(
    model = "gemini-1.5-flash",
    temperature=0.1
)

def generate_book_name_and_chapters(genre):
    prompt_template_title = PromptTemplate(
        input_variables=['genre'],
        template="Suggest only one title for a {genre} book."
    )

    title_chain = LLMChain(llm=llm, prompt=prompt_template_title, output_key="title")

    prompt_template_chapters = PromptTemplate(
        input_variables=['title'],
        template="Suggest name of first three chapters for {title} in a numbered list."
    )
    chapters_chain = LLMChain(llm=llm, prompt=prompt_template_chapters, output_key="chapters")

    chain_new = SequentialChain(
        chains=[title_chain, chapters_chain],
        input_variables=['genre'],
        output_variables=['title', 'chapters'],
        verbose=True
    )
    response = chain_new.invoke(genre)

    return response

if __name__ == "__main()__":
    print(generate_book_name_and_chapters("Fantasy"))
