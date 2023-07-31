import requests
import json

url = "http://localhost:8080/completion"

payload = json.dumps({
  "stream": False,
  "n_predict": 8,
  "temperature": 0.7,
  "stop": [
    "</s>",
    "llama:",
    "User:"
  ],
  "repeat_last_n": 256,
  "repeat_penalty": 1.18,
  "top_k": 40,
  "top_p": 0.5,
  "tfs_z": 1,
  "typical_p": 1,
  "presence_penalty": 0,
  "frequency_penalty": 0,
  "mirostat": 0,
  "mirostat_tau": 5,
  "mirostat_eta": 0.1,
  "prompt": "This is a conversation between user and llama, a friendly chatbot. respond in simple markdown.\n\nUser: {prompt}\nllama:"
})
headers = {
  'Content-Type': 'application/json'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)
