import requests
import re
import pyperclip

url = "https://ai.hackclub.com/chat/completions"

def get_data():
    relation = input("Before I generate the perfect birthday wish, please let me know who is it for (E.g Sibling, friend, parent etc.)  ")
    name = input("Please type the name of the person receiving this wish.  ")
    age = input(f"Okay! How many years will {name} be on their birthday?  ")
    tone = input("What is your desired tone for the message? Leave blank for no preference (e.g., Funny, Heartfelt/Sentimental, Formal, Casual, Inspirational, Poetic, etc.)  ")
    length = input ("Please select the desired length of the messagage (e.g., Short & Sweet, Standard, Detailed)  ")
    memory = input(f"Please input a shared memory or an inside joke between you and {name}, leave blank if none.  ")
    hobbies = input(f"What are the hobbies or interests of {name}?")
    special = input("If you want it in a specific style like a poem or modified lyrics of a special song etc., let me know.  ")

    return relation, name, age, tone, length, memory, hobbies, special

def main():
    print("Hi, this simple script would help you in crafting the perfect birthday message for your loved ones!")
    relation, name, age, tone, length, memory, hobbies, special = get_data()

    data = {
    "messages": [
        {"role": "user", "content": f"I will provide you a list of parameters and you need to generate the perfect birthday wish. The parameters are: Relation: {relation}, Name: {name}, Age: {age}, Tone: {tone}, length: {length}, memory: {memory}, hobbies: {hobbies}, Special Request: {special}"}
    ]
    }

    try:
        response = requests.post(url, json=data)
    
        response.raise_for_status()
        message = response.json()
        content = message['choices'][0]['message']['content']

        final_content = re.sub(r'<think>.*?</think>', '', content, flags=re.S)

        print(final_content.strip())

        copy = input("\n Thank you for using the script, Press 1 if you want to copy the text to your clipboard.  ")

        if copy == "1":
            pyperclip.copy(final_content.strip())
            print("\n Text successfully copied to cipboard!")

    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")

if __name__=="__main__":
    main()