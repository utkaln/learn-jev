from langchain_typesafe import Noul, TypeSafeClassifier

classifier = TypeSafeClassifier()
resp = classifier.invoke(
    {
        'state':(
            "The deployment just failed. Lot of cusomers are reporting 500 error.  Can someone take a look at it right now ?"
        ),
        'questions':{
            "urgent": Noul(
                instructions="Does this need urgent attention ?"
            ),
        },
    }
)

urgency = resp.nouls["urgent"].noul 

print(f'urgency: {urgency}')