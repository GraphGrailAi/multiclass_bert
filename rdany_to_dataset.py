import json

with open("rdany_conversations_2016-03-01.json", "r") as openfile:
    rdany = json.load(openfile)

for item in rdany:
    print('rdany:', item)
    print('rdany:', rdany[item])
    for reply in rdany[item]:
        print('reply:', reply["text"])