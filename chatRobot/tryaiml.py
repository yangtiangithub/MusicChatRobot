import aiml
import os

#切换路径到chatRobot
path = './'
os.chdir(path)

# Create the kernel and learn AIML files
mybot = aiml.Kernel()

#brain加速
if os.path.isfile("mybot_brain.brn"):
    mybot.bootstrap(brainFile="mybot_brain.brn")
else:
    mybot.bootstrap(learnFiles="musicSearch.aiml", commands="load aiml b")
    mybot.saveBrain("mybot_brain.brn")

# Press CTRL-C to break this loop
while True:
    print (mybot.respond(input("Enter your message >> ")))