import aiml

# Create the kernel and learn AIML files
kernel = aiml.Kernel()
<<<<<<< HEAD
kernel.learn("chatTemplete/test1")
kernel.respond("你好")
=======
kernel.learn('./chatTemplate/test2.aiml')
kernel.respond("hello")
>>>>>>> eb7150784644b3e65536d89bb0c63f05ad3f073b

# Press CTRL-C to break this loop
while True:
    print (kernel.respond(input("Enter your message >> ")))