import json

 def save_contact(details):
     with open('detail.json','w') as file:
         json.dump(details, file, index=4)


def load_contact():
             with open('ditail.json','r') as file:
                 return json.load(file)


