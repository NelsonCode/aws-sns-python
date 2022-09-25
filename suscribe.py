from connection import sns_client

response = sns_client.subscribe(
    TopicArn="",
    Protocol="email",
    Endpoint="example@hotmail.com",
    ReturnSubscriptionArn=True
)

print(response)
