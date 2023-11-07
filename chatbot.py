from gpt4all import GPT4All
import threading

#select LLM
model = GPT4All("gpt4all-13b-snoozy-q4_0.gguf")

isRunning = False
persistance = False
prompt = ""
response = ""

promptEvent = threading.Event()
responseEvent = threading.Event()

def startConversation():
    global isRunning
    global prompt
    global response
    global promptEvent
    global responseEvent

    with model.chat_session():
        while isRunning:
            promptEvent.wait()
            promptEvent.clear()
            print("Working on prompt: " + prompt)
            response = generateResponse(prompt)
            print("Finished processing")
            responseEvent.set()
        print("exited...")

def generateResponse(prompt):
    return model.generate(
        prompt,
        max_tokens=200,
        temp=0.7,
        top_k=40,
        top_p=0.4,
        repeat_penalty=1.18,
        repeat_last_n=64,
        n_batch=8,
        n_predict=None,
        streaming=False
    )
