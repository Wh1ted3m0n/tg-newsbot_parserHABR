Project Title: tg-newsbot_parserHABR

Description:

The tg-newsbot_parserHABR project is a Telegram bot designed to fetch and publish news articles from the habr.com website. The bot periodically checks for new articles in the "Develop" section of habr.com and sends them to a designated Telegram group. It operates with the command /start.

Files:

main.py:

This file contains the main functionality of the Telegram bot.
It imports parser_habr from parcer.py, as well as other necessary modules like telebot, config, time, and random.
The News_bot class initializes the Telegram bot with the provided token and channel ID.
It includes an ASCII art representation (self.art) for aesthetic purposes.
The send_news method fetches news articles using the parser_habr function and sends them to the designated Telegram group.
The run method sets up the bot, waiting for the /start command to activate the send_news method.
Finally, the script creates an instance of the News_bot class and runs the bot.
parcer.py:

This file contains the function parser_habr, responsible for parsing news articles from habr.com.
It imports necessary modules like BeautifulSoup, requests, and fake_useragent.
The parser_habr function scrapes the habr.com website for new articles in the "Develop" section.
It extracts relevant information such as article title, content, and URL.
If a new article is found, it returns a list containing the article ID, content, and URL. Otherwise, it returns None.
Usage:

To use the bot, start the main.py script.
Once the bot is running, send the /start command in the Telegram group where you want to receive news updates.
The bot will periodically fetch new articles from habr.com and send them to the group.
Dependencies:

This project relies on the following Python libraries: telebot, BeautifulSoup, requests, and fake_useragent.
Additional Notes:

Make sure to set up the Telegram bot token and channel ID in the config.py file before running the script.
This project serves as a simple example of web scraping and Telegram bot integration for fetching and sharing news content.
