import commands as c
import apikey as key
from telegram.ext import Updater

def main():
    #Create updater and dispatcher using API key
    updater = Updater(key.API_KEY, use_context=True)
    dispatcher = updater.dispatcher

    #Add commands
    dispatcher.add_handler(c.helpFunc)
    dispatcher.add_handler(c.startFunc)
    dispatcher.add_handler(c.stopFunc)
    dispatcher.add_handler(c.persistFunc)
    dispatcher.add_handler(c.IOFunc)

    # Start the bot
    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main()
