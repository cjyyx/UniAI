from uniai import aliChatLLM, deepseekChatLLM, zhipuChatLLM

# chatLLM = aliChatLLM("qwen-turbo")
# chatLLM = zhipuChatLLM("glm-3-turbo")
chatLLM = deepseekChatLLM()

content = "请用一个成语介绍你自己"
messages = [{"role": "user", "content": content}]

resp = chatLLM(messages)
print(resp)

for resp in chatLLM(messages, stream=True):
    print(resp)
