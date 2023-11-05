import commands as c
from telegram.ext import Updater

def main():
    # Enter your API key here
    API_KEY = '6555907776:AAFbHnL9xUSsZ3DpAX6XiqJeEuoOTkzK8DQ'
    
    #Create updater and dispatcher using API key
    updater = Updater(API_KEY, use_context=True)
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
