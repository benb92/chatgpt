# ChatGPT - Discover Historical Asset Class Narratives

This project uses ChatGPT to find historical narratives within any chosen asset class and chosen year. 
Previous answers are stored and passed to future questions to iteratively dig deep into history to rediscover narratives of the era.

## Installation

### create a .env file with ChatGPT token
- Navigate via command line to the folder you want to store the repo, run the following three commands:

```
git clone https://github.com/benb92/chatgpt.git
cd chatgpt
touch .env  
```

- Store your chatgpt token in the following format within the .env file:

Get the token from https://platform.openai.com/ (1) Click your account top right then "View API Keys" (2) click "+ Create new secret key"

```
CHATGPT=HereIsTheVeryLongChatGPTToken
```

### Install the required python libraries to run the program
```
pip install -r requirements.txt
```

### Run the dashboard 
```
python dashboard.py
```

![image](https://github.com/benb92/chatgpt/assets/32384270/6e6b1257-e2f2-49c2-b6a6-a12f14b177e8)
