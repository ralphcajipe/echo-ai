import os

# Library for creating interactive interfaces
import gradio as gr

from api import openai, api_request
from api_key import openai_api_key
from file_handler import read

# If the OpenAI API key is stored as an environment variable, retrieve it.
# openai.api_key = os.getenv("OPENAI_API_KEY")

# If the OpenAI API key is stored as a string, use it directly
openai.api_key = openai_api_key

# String to signal the start of an AI's response in the conversation history
start_sequence = "\nE.C.H.O: "

# String to signal the start of a human's response in the conversation history
restart_sequence = "\nYou: "

# Initial prompt to start the conversation
prompt = read("initial.txt")

# Calling the `api_request` function with the `prompt` string as an argument.
api_request(prompt)


def chat_brain(input, history):
    """
    It takes an input and a history, and returns the updated history

    :param input: The latest input from the user
    :param history: The conversation history, which is a list of input-output pairs
    :return: The history is being returned.
    """
    # Initialize the history if it is not provided
    history = history or []

    # Flatten the history into a list of input-output pairs
    s = list(sum(history, ()))

    # Append the latest input to the list
    s.append(input)

    # Join the input-output pairs into a single string
    inp = " ".join(s)

    # Generate a response from the OpenAI API
    output = api_request(inp)

    # Append the input-output pair to the conversation history
    history.append((input, output))

    # Return the updated conversation history
    return history, history


# Create the interface using gradio's Blocks API
block = gr.Blocks()
block.title = "E.C.H.O"

with block:
    # Add a title
    gr.Markdown(
        """<h1><center>Enhanced Chats and Helpful Outputs</center></h1>
    """
    )

    # Add a chatbot component to display the conversation history
    chatbot = gr.Chatbot()

    # Add a textbox for the user to enter their message
    message = gr.Textbox(placeholder=prompt, label="You", lines=3)

    # Add a state component to store the conversation history
    state = gr.State()

    # Add a button to send the message
    submit = gr.Button("SEND")
    # Bind the button's click event to the chat_brain function The function
    # will be called with the user's message and the conversation history as
    # inputs The function will return the updated conversation history and
    # the chatbot component
    submit.click(chat_brain, inputs=[message, state], outputs=[chatbot, state])

    gr.Markdown(
        """<center>Created by <a href="https://twitter.com/ralphcode">Ralph Cajipe</a> 2022 <br> 
        <a href="https://github.com/ralphcajipe">GitHub</a> 
        </center> """
    )


def main():
    """It launches the interface."""
    block.launch(
        debug=True,
        show_api=False,
    )


if __name__ == "__main__":
    main()
