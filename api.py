# Library for interacting with the OpenAI API
import openai


def api_request(prompt):
    """
    It uses the OpenAI API to generate a response to the given prompt

    :param prompt: The prompt to generate a response to
    """
    response = openai.Completion.create(
        model="text-davinci-003",  # Use the 'text-davinci-003' model
        prompt=prompt,  # Provide the prompt
        temperature=0.9,  # Use a high temperature for more creative responses
        max_tokens=150,  # Limit the number of tokens in the response
        top_p=1,  # Use the full probability distribution
        frequency_penalty=0,  # Don't penalize less frequent tokens
        # Penalize tokens that are present in the prompt but not the training
        presence_penalty=0.6,
        # Stop generating the response at these sequences
        stop=[" You:", " E.C.H.O:"]
    )

    # Return the first response from the API
    return response.choices[0].text
