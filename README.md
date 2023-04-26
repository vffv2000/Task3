
# Telegram Bot

This is Telegram bot written in Python using the aiogram library. The bot provides the following features:

1.  Greet the user and offer them to choose a certain function of the bot.
2.  Determine the current weather in a specific city using a public weather API (e.g. OpenWeatherMap) and provide the user with relevant information.
3.  Convert currencies using a public currency exchange API (e.g. Exchange Rates API) and provide the user with the conversion result.
4.  Send a random picture with cute animals.
5.  Create polls and send them to a group chat with a specific question and answer options.

## Installation

1.  Clone this repository to your local machine using `git clone https://github.com/<your_username>/telegram-bot.git`.
2.  Install the required packages using `pip install -r requirements.txt`.
3.  Create a bot on Telegram using the BotFather and get the bot token.
4.  Set the `TELEGRAM_API_TOKEN` environment variable to the bot token.
5.  Set the required environment variables for the weather API and currency exchange API (e.g. `WEATHER_API_KEY`, `CURRENCY_API_KEY`).

## Usage

To start the bot, run the `main.py` script using `python main.py`.

The bot will greet the user and offer them to choose a certain function using inline keyboard buttons. The user can select one of the following options:

-   Get the current weather
-   Convert currency
-   Get a cute animal picture
-   Create a poll

### Get the current weather

To get the current weather in a specific city, the user should type the name of the city in the chat. The bot will use the OpenWeatherMap API to get the current weather information and provide the user with relevant information.

### Convert currency

To convert currency, the user should type the amount, source currency, and target currency in the chat (e.g. "10 USD to EUR"). The bot will use the Exchange Rates API to convert the currency and provide the user with the conversion result.

### Get a cute animal picture

To get a cute animal picture, the user should select the "Get a cute animal picture" option using the inline keyboard buttons. The bot will use the Unsplash API to get a random picture with cute animals and send it to the user.

### Create a poll

To create a poll, the user should select the "Create a poll" option using the inline keyboard buttons. The bot will ask the user to enter the poll question and answer options. The bot will then create a poll with the specified question and answer options and send it to the group chat.

## Testing

To run the tests, use the `pytest` command. The tests are located in the `tests` directory and cover the main functionalities of the bot.

## Credits

This bot was created by [your_name].
