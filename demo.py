from uniai import aliChatLLM, zhipuChatLLM

# chatLLM = aliChatLLM("qwen-turbo")
chatLLM = zhipuChatLLM("glm-3-turbo")

content = "请用一个成语介绍你自己"
messages = [{"role": "user", "content": content}]

resp = chatLLM(messages)
print(resp)

for resp in chatLLM(messages, stream=True):
    print(resp)
