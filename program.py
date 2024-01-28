import pandas as pd
import random

lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)
data = pd.DataFrame({'whoAmI':lst})
print(data.head(n = 20))

human = []
robot = []
for el in lst:
    if el == 'robot':
        robot.append(1)
        human.append(0)
    if el == 'human':
        robot.append(0)
        human.append(1)
data = pd.DataFrame({'whoAmI_human': human, 'whoAmI_robot': robot})
print(data.head(n = 20))
