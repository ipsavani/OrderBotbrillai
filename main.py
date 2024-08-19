import chainlit as cl
import openai_functions

@cl.on_chat_start
async def start():
    await cl.Message(author="Chatbot", content="""What you do want to eat today?                  """).send()

@cl.on_message
async def main(message):
   # Your custom logic goes here…
   print(message.content)
   answer = openai_functions.get_answer(message.content)
   # Send a response back to the user
   await cl.Message(author="Chatbot",
     content=answer,
   ).send()

if __name__ == "__main__":
    from chainlit.cli import run_chainlit
    run_chainlit(__file__)
