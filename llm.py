import os 
import json 
import requests
from fastapi import Response
from dotenv import load_dotenv

load_dotenv()

class ChatGPTLLM:
    def __init__(self):
        self.url = "https://api.openai.com/v1/chat/completions"
        self.headers = {
            "authority": "contextretreival.csnonprod.com",
            "accept": "*/*",
            "accept-language": "en-GB,en-US;q=0.9,en;q=0.8",
            "authorization": "Bearer " + os.environ.get("OPENAI_API_KEY"),
            "content-type": "application/json",
            "origin": "https://thunderous-ganache-431e7c.netlify.app",
            "referer": "https://thunderous-ganache-431e7c.netlify.app/",
            "sec-ch-ua": '"Not.A/Brand";v="8", "Chromium";v="114", "Google Chrome";v="114"',
            "sec-ch-ua-mobile": "?0",
            "sec-ch-ua-platform": '"macOS"',
            "sec-fetch-dest": "empty",
            "sec-fetch-mode": "cors",
            "sec-fetch-site": "cross-site",
            "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36",
        }

    def answer(self, query, model):
        payload = json.dumps(
            {
                "model": model,
                "messages": [{"role": "user", "content": query}],
                "temperature": 0,
                "max_tokens": 4096,
                "stream": False,
                "top_p": None,
            }
        )

        response = requests.request(
            "POST", self.url, headers=self.headers, data=payload, stream=False
        )
        return response
