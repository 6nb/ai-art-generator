from selenium.webdriver.support import expected_conditions
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.common.by import By
from selenium import webdriver
import requests

import warnings
import random
import json
import time
import csv
import re
import os

STYLES = [
    "Psychedelic",
    "Synthwave",
    "Ghibli",
    "Steampunk",
    "Fantasy Art",
    "Vibrant",
    "HD",
    "Psychic",
    "Dark Fantasy",
    "Mystical",
    "Baroque",
    "Etching",
    "S.Dali",
    "Wuhtercuhler",
    "Provenance",
    "Moonwalker",
    "Blacklight",
    "Ukiyoe",
    "No Style"
]

def main():

    # Check for webhook, saving
    with open('settings.json') as file:
        settings = json.load(file)
        if (
            settings['webhook'] and
            re.match(r'https:\/\/discord\.com\/api\/webhooks\/\d+\/.+', settings['webhook']) and
            (webhook_info := requests.get(settings['webhook'])).status_code == 200
        ): print(f"Using webhook \"{webhook_info.json()['name']}\".")
        else: settings['webhook'] = None

    # Read prompts csv content
    entries = []
    with open('prompts.csv') as file:
        reader = csv.reader(file, delimiter = ',')
        next(reader) # ignore format line
        for index, row in enumerate(reader, start=2):
            if not len(row) == 2: raise Exception(f"Prompt at line {index} is invalid.") 
            elif row[1] == 'All': entries.extend([row[0], style] for style in STYLES)
            elif row[1] not in STYLES: raise Exception(f"Style \"{row[1]}\" at line {index} is not valid.")
            else: entries.append([row[0], row[1]])
    
    # Set selenium browser settings
    warnings.filterwarnings("ignore", category=DeprecationWarning)
    if settings["browser"].lower() == "chrome":
        options = ChromeOptions()
        options.headless = True
        options.add_experimental_option("excludeSwitches", ["enable-logging"])
        driver = webdriver.Chrome(settings["driverPath"], options=options)
    
    elif settings["browser"].lower() == "firefox":
        options = FirefoxOptions()
        options.headless = True
        driver = webdriver.Firefox(executable_path=settings["driverPath"], options=options)

    else: raise Exception("Unsupported browser.")

    # Generate art
    if not os.path.exists("generated"): os.mkdir("generated")
    print("Driver started. Generating art...")
    for entry in entries:
        driver.get('https://app.wombo.art/')
        prompt, style = entry[0], entry[1]

        # Send keys to prompt textbox
        # Experiment with delay, it's mostly arbitrary but sometimes prevents failures on short prompts
        textbox = driver.find_element(By.XPATH, '//input[@label="Enter prompt"]')
        for char in prompt:
            textbox.send_keys(char)
            if settings['typingDelay']: time.sleep(random.uniform(.1, .3) if len(prompt) < 12 else random.uniform(.05, .15))
        if settings['typingDelay'] and len(prompt) < 3: time.sleep(.8)

        # Submit and wait for generation
        driver.find_element(By.XPATH, f'//img[@alt="{style}"]').click()
        driver.find_element(By.XPATH, f'//button[text() = "Create"]').click()
        try:
            wait = WebDriverWait(driver, settings['maxWait'])
            wait.until(expected_conditions.visibility_of_element_located((By.XPATH, '//input[@label="Name artwork"]')))
            image = driver.find_element(By.XPATH, '//img[@class="ArtCard__CardImage-sc-67t09v-1 bVtRRR"]')
        except TimeoutException:
            errormsg = f'[TIME OUT] Waited to long generating artwork for prompt "{prompt}" in style "{style}"'
            if settings['webhook']: requests.post(settings['webhook'], data={'content':errormsg})
            print(errormsg)
            continue
            
        # Save File
        filename = f'{time.time()}_{prompt}_{style}.jpg'
        with open(f'generated/{filename}', 'wb') as file:
            file.write(requests.get(image.get_attribute('src')).content)
        
        # (Optional) Send via webhook
        if settings['webhook']:
            with open (f'generated/{filename}', 'rb') as file:
                requests.post(settings['webhook'],
                    files={'file':file},
                    data={'content':f'**Prompt:** {prompt}\n**Style:** {style}'}
                )

        print(f'[SUCCESS] Created artwork for prompt "{prompt}" in style "{style}"')
        if not settings['keepFiles']: os.remove(f'generated/{filename}') # for temporary saving only
    
    driver.quit()

if __name__ == '__main__':
    try: main()
    except Exception as error:
        print("Error:", error)
    except KeyboardInterrupt:
        print("Stopped by user.")