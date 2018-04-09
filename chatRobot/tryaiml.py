import aiml
import os

#切换路径到chatRobot
mybot_path = './'
aiml_path = './musicSearch.aiml'
os.chdir(mybot_path)

# Create the kernel and learn AIML files
mybot = aiml.Kernel()
mybot.learn(aiml_path)

# #brain加速。   如果删除文件mybot_brain.brn重新加载aiml文件
# if os.path.isfile("mybot_brain.brn"):
#     mybot.bootstrap(brainFile="mybot_brain.brn")
# else:
#     mybot.bootstrap(learnFiles="musicSearch.aiml", commands="load aiml b")
#     mybot.saveBrain("mybot_brain.brn")

# Press CTRL-C to break this loop
while True:
    print (mybot.respond(input("Enter your message >> ")))