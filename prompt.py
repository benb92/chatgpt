import openai
import os
from decouple import config
import json
openai.api_key = config('CHATGPT')

def Question_Builder(asset_class, year):
    question = f"Tell me the top narratives affecting financial markets in {asset_class} during {year}." \
               f"Do not repeat any previous answers. Talk professionally and with clarity. Bullet point answers using " \
               f"• as the bullet point with each bullet point on a new line in seperated paragraphs. " \
               f"Don't return any information about not using the information as financial advice or the limitations " \
               f"of the model not being trained on most recent data and fast changing current narratives."

    return question

def Historical_ChatGPT_Answers(asset_class, year):
    directory = f'data/{asset_class}'
    if not os.path.exists(directory):
        os.mkdir(directory)

    filepath = f'{directory}/{year}.json'

    if not os.path.exists(filepath):
        messages = [{"role": "system",
                     "content": "You are an expert teacher of Financial market history. "},]
        with open(filepath, 'w') as file:
            json.dump(messages, file)  # create the new file containing initial message if doesn't exist

    with open(f'{filepath}', 'r') as openfile:
        messages = json.load(openfile)  # load the messages

    return messages


def Ask_ChatGPT(asset_class, year):
    question = Question_Builder(asset_class, year)

    messages = Historical_ChatGPT_Answers(asset_class=asset_class, year=year)
    messages.append({"role": "user", "content": question},)

    chat_completion = openai.ChatCompletion.create(model="gpt-3.5-turbo",messages=messages)
    answer = chat_completion.choices[0].message.content
    messages.append({"role": "assistant", "content": answer})

    with open(f'data/{asset_class}/{year}.json', 'w') as file:
        json.dump(messages, file)  # create the new file containing initial message if doesn't exist

    return answer


if __name__ == "__main__":
    print("Hello, World!")
