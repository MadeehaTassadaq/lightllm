from litellm import completion
from dotenv import load_dotenv, find_dotenv
from crewai.flow import Flow,start,listen

load_dotenv(find_dotenv())
class LightllmFlow(Flow):
    @start
    def start(self):
        response = completion(
            model="gemini/gemini-1.5-flash",
            messages=[
                {"role": "user", "content": "who is the founder of Pakistan?"}
            ],
            max_tokens=100,
            temperature=0.5,
        )
        return response["choices"][0]["message"]["content"]

def run_lightllm():
    flow = LightllmFlow()
    flow.kickoff()
    


