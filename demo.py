from uniai import aliChatLLM

chatLLM=aliChatLLM("qwen-turbo")

content = "请用一个成语介绍你自己"
messages = [{"role": "user", "content": content}]

resp = chatLLM(messages)
print(resp)

for resp in chatLLM(messages, stream=True):
    print(resp)