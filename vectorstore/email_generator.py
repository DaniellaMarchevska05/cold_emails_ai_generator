import os

import chromadb
from langchain_groq import ChatGroq
from langchain_community.document_loaders import WebBaseLoader
from dotenv import load_dotenv

load_dotenv()

os.getenv("GROQ_API_KEY")

llm = ChatGroq(
    temperature = 0,
    model_name= "llama-3.3-70b-versatile"
)

loader = WebBaseLoader("https://careers.nike.com/lead-cloud-engineer-converse-technology-open-to-atlanta-beaverton-boston-location/job/R-43433")
page_data = loader.load().pop().page_content

from langchain_core.prompts import PromptTemplate

prompt_extract = PromptTemplate.from_template(
    """
           ### SCRAPED TEXT FROM WEBSITE:
           {page_data}
           ### INSTRUCTION:
           The scraped text is from the career's page of a website.
           Your job is to extract the job postings and return them in JSON format containing the 
           following keys: `role`, `experience`, `skills` and `description`.
           Only return the valid JSON.
           ### VALID JSON (NO PREAMBLE):    
           """
)

chain_extract = prompt_extract | llm
res = chain_extract.invoke(input={'page_data': page_data})


from langchain_core.output_parsers import JsonOutputParser

json_parser = JsonOutputParser()
json_res = json_parser.parse(res.content)

import pandas as pd
import uuid

df = pd.read_csv("my_portfolio.csv")

client = chromadb.PersistentClient('')
collection = client.get_or_create_collection(name="portfolio")

if not collection.count():
    for _, row in df.iterrows():
        collection.add(documents=row["Techstack"],
                       metadatas={"links": row["Links"]},
                       ids=[str(uuid.uuid4())])


job = json_res

links = collection.query(query_texts=job['skills'], n_results=2).get('metadatas', [])

prompt_email = PromptTemplate.from_template(
    """
    ### JOB DESCRIPTION:
    {job_description}

    ### INSTRUCTION:
    You are Gilly, a business development executive at AtliQ. AtliQ is an AI & Software Consulting company dedicated to facilitating
    the seamless integration of business processes through automated tools. 
    Over our experience, we have empowered numerous enterprises with tailored solutions, fostering scalability, 
    process optimization, cost reduction, and heightened overall efficiency. 
    Your job is to write a cold email to the client regarding the job mentioned above describing the capability of AtliQ 
    in fulfilling their needs.
    Also add the most relevant ones from the following links to showcase Atliq's portfolio: {link_list}
    Remember you are Gilly, BDE at AtliQ. 
    Do not provide a preamble.
    ### EMAIL (NO PREAMBLE):

    """
)

chain_email = prompt_email | llm
res = chain_email.invoke({"job_description": str(job), "link_list": links})
print(res.content)
