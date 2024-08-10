from environments.robot_env import RobotEnv
from controllers.robot_controller import RobotController
from llm.prompt_handler import PromptHandler

def main():
    env = RobotEnv()
    controller = RobotController()
    prompt_handler = PromptHandler()

    obs = env.reset()
    done = False
    total_reward = 0

    while not done:
        prompt = input("Enter a command for the robot (or 'quit' to end): ")
        
        if prompt.lower() == 'quit':
            break

        llm_action = prompt_handler.process(prompt)
        
        if llm_action is not None:
            controller_action = controller.update(obs)
            action = llm_action + controller_action  # Combine LLM and controller actions
            action = np.clip(action, -1, 1)  # Ensure action is within bounds
            
            obs, reward, done, _ = env.step(action)
            total_reward += reward
            
            print(f"Action taken: {action}")
            print(f"New position: {obs[:2]}")
            print(f"Reward: {reward}")
        else:
            print("Invalid command. Please try again.")

    print(f"Episode finished. Total reward: {total_reward}")
    env.close()

if __name__ == "__main__":
    main()