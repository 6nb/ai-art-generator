# WomboAI Art Generator

Automate AI art generation using [wombot.art](https://app.wombo.art/).

![photos](https://user-images.githubusercontent.com/77910109/159138009-f769a4e3-466d-4b9f-ab9d-2c571c75d5ab.png)

Also check out [SnailBot art integration!](#snailbot)

# Setup

## 1. Install Python

Go to the [python download page](https://www.python.org/downloads/) and install version 3.10 or higher. Make sure the `pip` package manager is included.

Install required packages with:

    pip install -r requirements.txt

## 2. Set up drivers

This tool uses [Selenium](https://selenium-python.readthedocs.io/) to scrape artwork, which requires either chrome or firefox to automate web browsing.

### Chrome

Download chromedriver [here](https://chromedriver.chromium.org/downloads) for the correct version of chrome.

Check version in `settings > about chrome`. The version included works with Chrome 99.

### Firefox

Download geckodriver [here](https://github.com/mozilla/geckodriver/releases).

Linux installation:
```
wget https://github.com/mozilla/geckodriver/releases/download/v0.30.0/geckodriver-v0.30.0-linux32.tar.gz

tar -xf geckodriver-v0.30.0-linux32.tar.gz

mv geckodriver /usr/local/bin/
```

## 3. Add prompts

Wombo.art requires a prompt and a style for each artwork.

`prompts.csv` contains all the prompts/styles you want to generate for under the `prompt,style` heading:

```csv
prompt,style
first prompt,first style
second prompt,second style
```

Supported styles:
- Psychedelic
- Synthwave
- Ghibli
- Steampunk
- Fantasy Art
- Vibrant
- HD
- Psychic
- Dark Fantasy
- Mystical
- Baroque
- Etching
- S.Dali
- Wuhtercuhler
- Provenance
- Moonwalker
- Blacklight
- Ukiyoe
- No Style

...or "All" to run EVERY style for the prompt.

## 4. Check settings

Edit `settings.json` to your liking:

### browser

The browser you are using: either "chrome" or "firefox"

#### driverPath

location of either chromedriver or geckodriver. (For linux + firefox: `/usr/local/bin/geckodriver`)

#### webhook 
optional discord webhook url to send art to

#### keepFiles
whether to keep files after creation (as opposed to sending to webhook then deleting)

### typingDelay
add (somewhat arbitrary) delay to prompt typing. slower but improves success rate

#### maxWait
number of seconds to wait for art to generate before reporting an error

## 5. Run

Run `python main.py`

Generated art is saved in the `/generated/` folder.


# <span id="snailbot">SnailBot /art integration</span>

No setup required. [INVITE FROM TOP.GG!](https://top.gg/bot/833071346632228915)

![snail style menu](https://user-images.githubusercontent.com/77910109/159137863-a0ec2d65-c83a-49d0-885b-b7c3e8328e1c.png)

![snail art result](https://user-images.githubusercontent.com/77910109/159137887-6539a7dd-20f6-405d-ad68-de503849eb40.png)