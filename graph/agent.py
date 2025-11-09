from __future__ import annotations

from dotenv import load_dotenv
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import Runnable
from langchain_openai import ChatOpenAI

# Load environment variables
load_dotenv()


def build_default_chain(model: str = "gpt-4.1") -> Runnable:
    """Return a basic LangChain runnable with default prompts."""
    prompt = ChatPromptTemplate.from_messages(
        [
            ("system", "Eres un asistente de IA que analiza el input del usuario y hace un analísis de lo que habla."),
            ("human", "{message}"),
        ]
    )
    llm = ChatOpenAI(model=model, temperature=0.1)
    parser = StrOutputParser()
    return prompt | llm | parser
