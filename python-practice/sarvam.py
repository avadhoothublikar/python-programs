from sarvamai import SarvamAI

client = SarvamAI(
    api_subscription_key="sk_m4lvoho4_7pztBnNMCwHWaXzFY4tw6t1k",
)
response = client.chat.completions(messages=[
    {"role": "user", "content": "Do you know anything about the company Sigmoid"}
])
print(response)
