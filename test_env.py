print("RUNNING FILE...")
from env import SupportEnv, Action
from tasks import TASKS
from graders import grade

env = SupportEnv()

task = TASKS["easy"]

obs = env.reset(task)
print("Initial:", obs)

action = Action(action_type="respond")

obs, reward, done, _ = env.step(action)

score = grade(action.action_type, task["correct_action"])

print("Reward:", reward)
print("Score:", score)
print("Done:", done)