from openai import OpenAI
    
endpoint = "https://"
deployment_name = "gpt-4.1-mini"
api_key = ""
    
client = OpenAI(
     base_url=endpoint,
     api_key=api_key
)
    
response = client.responses.create(
     model=deployment_name,
     input=[{
         "role": "user",
         "content": [
             {"type": "input_text", "text": "what's in this image?"},
             {"type": "input_image", "image_url": " "},
         ],
     }],
)
    
print(f"answer: {response.output[0]}")