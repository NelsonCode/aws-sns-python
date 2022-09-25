from connection import sns_client


response = sns_client.list_subscriptions_by_topic(
    TopicArn=""
)

EMAIL = "example@hotmail.com"

SUBSCRIPTIONS = response["Subscriptions"]

result = list(filter(lambda subs: subs["Endpoint"] == EMAIL, SUBSCRIPTIONS))

print(result)