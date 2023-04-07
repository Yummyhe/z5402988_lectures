f_suburbs = {"Randwick": 29986, "Kensington": 15004, "Frenchs Forest": 13473, "Flemington": None}
f_suburbs.pop('Randwick')
f_suburbs.pop('Kensington')

f_suburbs.update({
'Fairfield': 18081,
'Fairfield East': 5273,
'Fairfield Heights': 7517,
'Fairfield West': 11575,
'Fairlight': 5840,
'Fiddletown': 233,
'Five Dock': 9356,
'Flemington': None,
'Forest Glen': None,
'Forest Lodge': 4583,
'Forestville': 8329,
'Freemans Reach': 1973,
'Frenchs Forest': 13473,
'Freshwater': 8866,
})


print(f_suburbs)


list_a = ['this', 'list', 'has', 'bad', 'words', 'in', 'it', 'bad', 'naughty', 'impish']
list_b = ['good', 'nice', 'friendly']

sol = list_a[1:7]
sol.pop(2)
sol.append('including')
sol.insert(2,'good')
sol.extend(list_b)
print (sol)

f_suburbs = {"Randwick", "Kensington", "Frenchs Forest", "Flemington"}

nof_suburbs = ["Randwick", "Kensington"]
for s in nof_suburbs:
    f_suburbs.remove(s)
print(f_suburbs)

f_suburbs.update({
'Fairfield',
'Fairfield East',
'Fairfield Heights',
'Fairfield West',
'Fairlight',
'Fiddletown',
'Five Dock',
'Flemington',
'Forest Glen',
'Forest Lodge',
'Forestville',
'Freemans Reach',
'Frenchs Forest',
'Freshwater'
})
print(f_suburbs)
