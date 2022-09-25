from connection import sns_client


response = sns_client.publish(
    TopicArn="",
    Message="Hello!",
    Subject="Este es el tema"
)

print(response)
