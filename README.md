# Attabot
A nifty sandbox for experimenting with robots in MuJoCo using text prompts

## Setup

1. Install the required packages:
```console
$ pip install -r requirements.txt
```

2. Set up your OpenAI API key in `llm/prompt_handler.py`.

3. Run the simulation:
```console
$ python main.py
```

## Usage

Enter natural language commands to control the robot. For example:
- "Move forward"
- "Turn left"
- "Go to the right"

Type 'quit' to end the simulation.

## Project Structure

- `environments/`: Contains the MuJoCo environment setup
- `models/`: Contains the XML model file for the robot
- `controllers/`: Implements the robot control logic
- `llm/`: Handles natural language processing and LLM integration
- `utils/`: Contains helper functions
- `main.py`: The main script to run the simulation

## Customization

Modify the XML model, environment parameters, and control logic to suit your specific robot and task requirements.