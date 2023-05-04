## AI and Advanced Game Programming Final Project

### Kenneth Burt
### Professor Agrawal
### CMPSC 441
### May 5th, 2023
<br />

#### Abstract:
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Artificial intelligence is a plague on humanity that will bring about the crash of
the job market and destruction of the global economy. Or so some people out of the loop would like everyone to believe.
In actuality, artificial intelligence (AI) is far from bringing the end of humanity and is actually not as new as some
people would know. Surprisingly to some, AI has been being leveraged in video games for a long time. The first instance
of AI in video games was "Space Invaders" in 1978, nearly 50 years ago. 
Due to the vast amount of time since then, AI in video games has advanced beyond belief.
This project's goal is to showcase some of those advancements in video game AI.
Using the Python language, the pygame library, and a variety of other libraries. Though rudimentary, this project uses AI techniques such as genetic algorithms,
path finding functions, and model based reflex agents. this project will give a glimpse of how
AI can be leveraged to improve games.

<br />

### AI Techniques:
* Model based reflex agent to beat a computer player at rock paper scissors.
* Genetic algorithm to generate a realistic world.
* Path finding algorithm to find the best path to a destination city.
* A Reinforcement learning agent to beat a computer player at rock paper scissors.
* (Extra AI Algorithm) AI text generator to give encouraging messages

<br />

### Problems Solved

#### Problem 1: Beating an AI at rock paper scissors
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; The main battle mechanic for this game is a rock paper scissors game. When traversing
through the world the player has a chance to start a random battle encounter. In this encounter the player must play rock
paper scissors against a computer until either one is completely out of health. This could be difficult for a human
because they are unaware of how the computer would act. To solve this, the system implements two AI mechanics to reduce
health lost in an encounter.
<br />
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;The first of the AI techniques used was a model based reflex agent. The model based
reflex agent works by reading a percept of the current environment and storing it in its memory. Each percept is used as
a different state if the environment. From those, the AI constructs a model to decide the best following actions to take
against the computer player. The AI, originally, has three different computer behaviors that it reacts to. It beats each behavior
with a 96% success rate.
<br />
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Though this form of AI is good, it is not as optimal as it could be. The model based
reflex agent takes three turns to recognize which computer it is fighting against. This is three turns of a nondeterministic
outcome. Also, if the computer's behavior is not in the three described behaviors that the model based reflex agent is looking
for, it will not recognize the computer's pattern. That is where the reinforcement learning algorithm comes in. The
reinforcement learning algorithm will play a large number of simulation games against the computer. During these simulation
games, the algorithm will keep track of the state of the battle, just like the model based agent. However, the reinforcement
learning algorithm will attribute different rewards to the actions it takes in each state. Based on those rewards, the reinforcement
learning algorithm will construct a strategy to take actions that will grant the most reward to the AI during the actual battle.
This is the way that the game beats the computer player in a more effective way than a human player.

<br />

#### Problem 2: Cities are not generating realistically according to terrain and other cities spacing
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;The second problem that was solved by an AI in this game project was how cities
should be distributed across a map. Ideally a video game would want to have realistically spread cities to make a game's
environment more engaging for a player. To get the cities' distributions to be realistic, randomly placing cities on the
mad would not work. To solve this a genetic algorithm AI was used to choose the cities' locations. The genetic algorithm
works in two parts. The first part of the genetic algorithm is it creates a large number of children off of a parent. In
this case the parent is the original randomly distributed cities. Those children are all slightly different based off of
the parent's components. The second part of the genetic algorithm involves analyzing each child with a fitness function.
This fitness function attributes a fitness value to each child based on certain factors in the function. In this case, some
of these factors include closeness to another city and elevation of the city. Based on the results a new generation of children
are created from parents with the highest fitness values. Over the course of many generations the children will get progressively
better. This progression will make the cities on the map more realistic.

<br />

#### Problem 3: Navigating the map in the most efficient way
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Though the map displays the topography of the land, the travel cost between cities is
somewhat ambiguous. Also, it is hard to trust a human player to travel in the most efficient way. To solve this, the game
uses another AI mechanic to map out the most efficient path to the destination city. To achieve this the system uses a 
dijkstra's shortest path algorithm. Dijkstra's creates a graph of the game board consisting of vertices representing the cities
and edges representing the paths between the cities. Each of the vertices is weighted based on the travel cost between cities.
Dijkstra's will then take the graph and find the shortest and most efficient path to the destination city. As it arrives at each
vertex it constructs a table representing the current most efficient path to each. The algorithm finishes once every vertex
has been mapped. From the start location to the end location, one just needs to grab the end vertex from the crafted table to
know the most efficient path.

<br />

#### Problem 4: AI cheering bot
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Lastly, playing a video game can be very stressful, therefore the system will encourage
the player as they progress through the game. To do this the system generates an encouragement message based on a set of training data.
The game leverages a trained language model to generate encouraging messages based on a language prompt. In this case the 
prompt that is used to generate messages is, "I believe you can make it to the destination city." This pre-trained model
will take the prompt and continue to generate messages for the user. This will solve the issue of them losing hope in 
completing the game and have them play for longer.

<br />

### Conclusion
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;The AI techniques described in this game only scratch the surface in what can be used
for game development. The game development industry are evolving new techniques to incorporate AI every day. Let alone
game development, artificial intelligence is advancing across all sectors at a blistering pace. Those who are not informed
of its capabilities are at risk of falling far behind in the future. That future, path found by AI, is far more advanced than
anyone can imagine at this moment in time.
<br />

### Appendix
#### Chat GPT discussion transcript:
Kenneth - "Using an AI programming technique generate encouraging messages in python"

ChatGPT - "One AI programming technique for generating encouraging messages in Python is to use a pre-trained language model that can generate text based on a given prompt or seed text. Here's an example of how to use the GPT-2 language model from the transformers package to generate encouraging messages:

```python
import random
import torch
from transformers import GPT2LMHeadModel, GPT2Tokenizer

# Load pre-trained GPT-2 model and tokenizer
tokenizer = GPT2Tokenizer.from_pretrained('gpt2')
model = GPT2LMHeadModel.from_pretrained('gpt2')

# Set device to use GPU if available
device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
model = model.to(device)

# Generate an encouraging message
def generate_encouragement():
    prompt = "You can do it! "
    encoded_prompt = tokenizer.encode(prompt, add_special_tokens=False, return_tensors="pt")
    encoded_prompt = encoded_prompt.to(device)

    # Generate text using the model
    output_sequences = model.generate(
        input_ids=encoded_prompt,
        max_length=50,
        temperature=1.0,
        top_k=0,
        top_p=0.9,
        do_sample=True,
        num_return_sequences=1,
    )

    # Decode the generated text
    generated_sequence = output_sequences[0].tolist()
    text = tokenizer.decode(generated_sequence, clean_up_tokenization_spaces=True)
    return text.strip()

print(generate_encouragement())
```
This code loads the pre-trained GPT-2 language model and tokenizer using the GPT2LMHeadModel and GPT2Tokenizer classes from the transformers package. The generate_encouragement() function defines a prompt ("You can do it! ") and encodes it using the tokenizer. The generate() method of the model is then used to generate text based on the encoded prompt. The temperature, top_k, and top_p parameters control the randomness and diversity of the generated text, and the num_return_sequences parameter sets the number of generated texts to return. Finally, the generated text is decoded using the tokenizer and returned as a string.

Note that the generated text may not always be grammatically correct or make perfect sense, as language models are trained on large amounts of text data and generate text based on statistical patterns rather than understanding the meaning of words and sentences."