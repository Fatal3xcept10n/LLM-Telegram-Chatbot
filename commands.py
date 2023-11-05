from telegram.ext import CommandHandler, MessageHandler, Filters
import threading
import time
import chatbot as cb

#Handles input and output from LLM to user and vice versa
def IOhandler(update, context):
    if cb.isRunning:
        cb.prompt = update.message.text
        print("\nbot running, got prompt: " + cb.prompt)
        context.bot.send_message(chat_id=update.effective_chat.id, text='Thinking...')
        cb.promptEvent.set()
        cb.responseEvent.wait()
        cb.responseEvent.clear()
        print("done, responding with: " + cb.response)
        context.bot.send_message(chat_id=update.effective_chat.id, text=cb.response)

IOFunc = MessageHandler(Filters.text, IOhandler)

#Displays help using /help command
def help(update, context):
    update.message.reply_text("This bot allows you to communicate with a LLM using telegram!\n\n/help displays this help page\n/hello initiates a conversation\n/stop halts a conversation\n/persistence [on|off] toggles conversation retention")

helpFunc = CommandHandler('help', help)

#Starts the LLM using /hello command
def hello(update, context):
    if cb.isRunning == False:
        cb.isRunning = True
        conversationThread = threading.Thread(target=cb.startConversation)
        conversationThread.start()
        context.bot.send_message(chat_id=update.effective_chat.id, text='Hello! Input a prompt to start the conversation...')
    else:
        update.message.reply_text("Conversation already in progress..")

startFunc = CommandHandler('hello', hello)

#Stops the LLM using /stop command
def stop(update, context):
    if cb.isRunning == False:
        update.message.reply_text("Nothing to halt..")
    else:
        update.message.reply_text("halted..")
        cb.isRunning = False

stopFunc = CommandHandler('stop', stop)

#Enables experimental conversation persistance between chat sessions
def persistence(update, context):
    if cb.isRunning == False:
        if len(context.args) == 1:
            param = context.args[0].lower()
        
            if param == "on":
                cb.persistance = True
                update.message.reply_text("Conversation persistence is ON..")
            elif param == "off":
                cb.persistance = False
                update.message.reply_text("Conversation persistence is OFF..")
            else:
                update.message.reply_text("Unknown parameter: " + param)
        else:
            update.message.reply_text("Usage: /persistence [on|off]")
    else:
        update.message.reply_text("Conversation must be halted before persistence can be toggled..")

persistFunc = CommandHandler('persistence', persistence, pass_args=True)
