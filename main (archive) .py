#A program that supposed to mail you on your birthday, in future but it sadly doesn't work as the service that was going to be used (FutureMe) is now paid.

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from datetime import datetime
import time, math

def send_letter(email, body, date_object, years_future):

    options = Options()
    options.add_argument('--headless=new')
    driver = webdriver.Chrome(options=options)

    driver.get("https://futureme.org/")

    dateToggle = driver.find_element(By.XPATH, '//button[@data-letter-editor-delivery-type-param="date"]')

    dateToggle.click()


    monthButton = driver.find_element(By.XPATH, f'//option[@value="{date_object.month}"]')
    dateButton = driver.find_element(By.XPATH, f'//*[@id="letter_send_date_3i"]/option[{date_object.day}]')
    yearButton = driver.find_element(By.XPATH, f'//option[@value="{date_object.year+years_future}"]')
    submitButton = driver.find_element(By.ID, 'send_to_the_future')

    bodyBox = driver.find_element(By.ID, 'letter_body')
    privateButton = driver.find_element(By.XPATH, '//label[@for="letter_public_false"]')
    emailBox = driver.find_element(By.ID, 'letter_email')

    bodyBox.clear()
    bodyBox.send_keys(body)
    

   
    monthButton.click()
    dateButton.click()
    yearButton.click()

    privateButton.click()

    emailBox.send_keys(email)

    submitButton.click()

    driver.close()

def main():
    print("This Python script let's you travel to the future and deliver a letter to your future self, on their birthday!")

    name = input("Input your name: ")

    while True:
        
        bday = input("Please enter your Date of Birth in YYYY-MM-DD format: ")
        try:
            date_object = datetime.strptime(bday, '%Y-%m-%d')
            #print("Valid date and time object created:", date_object)
            break
        except ValueError:
            print("Invalid date. Please ensure the format is YYYY-MM-DD and that the date is a real calendar date (e.g., no month 15 or February 30th).")

    email = input("Please enter you E-mail ID: ")

    current_datetime = datetime.now()

    years = ((current_datetime-date_object).days)/365
    age = math.floor(years)

    print(f"Before you start writing the letter, how old is {name} when the letter is delivered? (You are currently {age} years old.)")

    while True:
        try:

            years_future=int(input("Enter a valid age: "))
            if years_future>age:
                break
            else:
                print("That's not a valid age! Please enter an age greater than you current age.")
        except:
            print("Please enter a valid age.")

    lines = []
    print("Enter your text. Press Enter on an empty line to finish:")
    while True:
        line = input()
        if line != "":
            lines.append(line)
        else:
            break
        body = "\n".join(lines)
    
    try:

        print("Sending your letter... please wait.")

        send_letter(email, body, date_object, years_future)

        print("Your letter has been successfully sent! Please verify your email once, you would've received an email from FutureMe.org")
    
    except Exception as e:
        print("Something went wrong. Make sure Google Chrome is installed and try again.")
        print(e)

main()





