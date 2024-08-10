import openai

class PromptHandler:
    def __init__(self):
        openai.api_key = "your-api-key-here"
        self.action_map = {
            "move": self.move,
            "turn": self.turn,
        }

    def process(self, prompt):
        llm_response = self.query_llm(prompt)
        action, params = self.parse_llm_response(llm_response)
        return self.execute_action(action, params)

    def query_llm(self, prompt):
        response = openai.Completion.create(
            engine="text-davinci-002",
            prompt=f"Translate the following command into a robot action (move or turn): {prompt}",
            max_tokens=50
        )
        return response.choices[0].text.strip()

    def parse_llm_response(self, response):
        parts = response.split()
        action = parts[0].lower()
        params = parts[1:] if len(parts) > 1 else []
        return action, params

    def execute_action(self, action, params):
        if action in self.action_map:
            return self.action_map[action](*params)
        else:
            return None

    def move(self, distance=1):
        return np.array([float(distance), 0])

    def turn(self, angle=90):
        return np.array([0, float(angle) / 90])  # Normalize angle to [-1, 1]