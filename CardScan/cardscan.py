from mtgsdk import Card, Supertype
import easygui, json
with open("./CMM.json", "r") as file:
    data = json.load(file)
    #print(data)
    for i in data['data']['cards']:
        print(i['name'])
    search = easygui.enterbox("Enter card name to search:")
    for i in data['data']['cards']:
        if i['name'] == search:
#            print(i['text'])
            effect = i['text']
#     #returnlist = Card.where(name=search).all()
    #print(returnlist)
# f = open('./PMH1.json')
# #cards = Card.all()
# data = json.load(f)
# 
# for i in data['data']['cards']:
#     print(i['name'])
# f.close()

#supertypes = Supertype.all()
#cards = Card.all()
#search = easygui.enterbox("Enter card supertype to search:")

#cards = Card.where(Supertype=search).all()

print(effect)