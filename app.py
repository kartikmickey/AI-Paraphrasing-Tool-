from pydantic import BaseModel
from typing import List
from helpers import structured_generator

#Replace With Your Output
class Titles(BaseModel):
    titles: List[str]

#Replace with your input
input = " A Hello, World! program is generally a simple computer program which outputs (or displays) to the screen (often the console) a message similar to Hello, World! while ignoring any user input. "

#Replace with your prompt
prompt = f"paraphrase the following text: {input}" 

#Replace With Your Model
openai_model = "gpt-3.5-turbo"

result = structured_generator(openai_model,prompt,Titles)
print(result.titles)