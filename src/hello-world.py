import os
from dotenv import load_dotenv
from typesafe_sdk import Choice, Noul, Score, TypeSafeClient
client = TypeSafeClient()
ticket = "Hi, I've been trying to connect my Stripe account for 3 days and the integration keeps failing. I am trying to test out. Do you think I can do something to address this ?"
response = client.system_one(
    state=ticket,
    questions={
        "department": Choice(
            instructions = "What team should handle this ?",
            criteria= {
                "billing": "Payment or Subscription Issues",
                "technical": "integration issue or a new bug",
                "sales": "Pricing or Account issues",
            },
        ),
        "frustration": Score(
            instructions = "How frustrated does the customer appear ?",
            criteria= [
                "Calm, just stating the facts",
                "Frustrated, but not aggressive",
                "Very Frustrated and angry"
            ],
        ),
        "is_urgent": Noul(
            instructions = "The message conveys urgency or time sensitivity",
        ),
    }
)

print(f'Department: {response.answers["department"].choice}')
print(f'Frustration: {response.answers["frustration"].score}')
print(f'Is Urgent: {response.answers["is_urgent"].noul}')
