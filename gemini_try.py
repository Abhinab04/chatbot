import google.generativeai as genai
genai.configure(api_key="AIzaSyCkHKFFUiSL6vLGr4gpDL6tWSljnYVFkiE")
model=genai.GenerativeModel("gemini-pro")
#chatting
chat=model.start_chat(history=[])
ini=input()
response=chat.send_message(ini)
print(response.text)
while True:
    ini=input()
    response=chat.send_message(ini, stream=True)
    for chunk in response:
        print(chunk.text)
        print("_"*80)
#one response
ini=input()
response=model.generate_content(ini)