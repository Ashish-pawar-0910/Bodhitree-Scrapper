# Bodhitree-Scrapper
A simple script to notify about pending quizzes and assignments(in progress).

This script uses Chrome version 86. If you have some other version, then download it's driver from the below link and place it in the assets folder.
https://sites.google.com/a/chromium.org/chromedriver/downloads

If you want to use any other browser, download the driver from the below links.

- **Safari** : Safari’s executable is located at /usr/bin/safaridriver
- **Firefox** : https://github.com/mozilla/geckodriver/releases
- **Opera** : https://github.com/operasoftware/operachromiumdriver/
- **Edge** : https://developer.microsoft.com/en-us/microsoft-edge/tools/webdriver/
- **Internet Explorer** : Really?

# Usage
Clone the repo.

Provide your credentials in the resources.py file in the assets folder.

Use the command below to run program.

``` 
python bt-scrapper.py 
```
Selenium is required for the script to run. You can install it with ```pip install -U selenium```

If you are on linux **and** using the driver from the assets folder, set the driver executable by ``` chmod +x <driver name>```
