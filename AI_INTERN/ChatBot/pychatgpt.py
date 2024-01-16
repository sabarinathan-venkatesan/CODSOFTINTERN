import openai
openai.api_key='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'
messages=[{"role":"system","content":
           "You arw a intelloigent assistent."}]

while True :
    message=input("User :")
    if message:
        messages.append(
            {'role':"user", "content":message},

        )
        chat =openai.ChatCompletion.create(
            model="gpt-3.5-turbo",messages=messages
        )
    replay=chat.choices[0].message.content
    print(f'ChatGPT:{replay}')
    messages.append({'role':'assistant',"content":replay})