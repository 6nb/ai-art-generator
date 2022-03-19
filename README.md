# WomboAI Art Generator

Automate AI art generation using [wombot.art](https://app.wombo.art/).

Also integrated into [SnailBot](https://snail.monster/invite) for you to try out.

## Setup

### Install Python

Go to the [python download page](https://www.python.org/downloads/) and install version 3.10 or higher.

## Requirements
Install the packages in the `requirements.txt` file using python's package manager. Open command prompt and type:

    pip install -r requirements.txt

If "pip" isn't found on your machine you have a python installation issue

## ChromeDriver

This tool uses [Selenium](https://selenium-python.readthedocs.io/) to scrape artwork, which requires ChromeDriver to automate web browsing.

The version that works for me (Chrome 99) is included. If you have a different version of chrome, download the corresponding driver [here](https://chromedriver.chromium.org/downloads) and replace it.

## Usage

Run `python main.py`

This will generate artwork for all entries your provide in `prompts.csv`:

```csv
prompt,style
first prompt,first style
second prompt,second style
```

Generated art is saved in the `/generated/` folder.

If you include a webhook url in `settings.json` it will be sent there to.

Supported styles:
- Etching
- Baroque
- Mystical
- Festive
- Dark Fantasy
- Psychic
- Pastel
- HD
- Vibrant
- Fantasy Art
- Steampunk
- Ukiyoe
- Synthwave
- No Style

...or "All" to run EVERY style for the prompt.