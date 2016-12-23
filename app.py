import aiml

# Create the kernel and learn AIML files
kernel = aiml.Kernel()
kernel.learn("aiml-en-us-foundation-alice/*");

# Press CTRL-C to break this loop
while True:
        print kernel.respond(raw_input("Enter your message >> "))
