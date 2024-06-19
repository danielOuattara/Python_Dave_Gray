#  Dictionaries: store data in key-value pair

band = {
    'vocals': 'Plant',
    'guitar': 'Page'
}
print(band)

band_2 = dict(
    vocals='Plant',
    guitar='Page'
)
print(band_2)

#  type & length

print(type(band))  # <class 'dict'>
print(len(band_2))  # 2

#  access items

print(band["vocals"])  # Plant
print(band.get("guitar"))  # Page

#  List all keys

print(band.keys())  # dict_keys(['vocals', 'guitar'])

#  List all values

print(band.values())  # dict_values(['Plant', 'Page'])

#  List of key/value pairs as tuple

print(band.items())  # dict_items([('vocals', 'Plant'), ('guitar', 'Page')])

#  Verify a 'key' in dictionary

print('guitar' in band)  # True
print('triangle' in band)  # False

#  Update values

band["vocals"] = "Coverdale"  # change a value
print(band)

band.update({'bass': "JPJ"})  # add a new K-V pair
print(band)

#  Remove items

print(band.pop('bass'))  # JPJ
print(band)  # {'vocals': 'Coverdale', 'guitar': 'Page'}

band['drums'] = 'Bonham'  # Add a new KV pair
print(band)

print(band.popitem())  # ('drums', 'Bonham') as tuple
print(band)  # {'vocals': 'Coverdale', 'guitar': 'Page'}

#  Delete KV pair and Clear dict

band['drums'] = 'Bonham'  # Add a new KV pair again

del band['drums']
print(band)  # {'vocals': 'Coverdale', 'guitar': 'Page'}

print(band_2)  # {'vocals': 'Plant', 'guitar': 'Page'}
band_2.clear()
print(band_2)  # {}

del band_2
# print(band_2)  # NameError: name 'band_2' is not defined. Did you mean: 'band'?

#  Copying dictionary

band_3 = band  # does not create a copy BUT a reference in memory
print(band)
print(band_3)

band_3['drums'] = 'Dave'
print('band = ', band)
print('band_3 = ', band_3)

del band['drums']

band_4 = band.copy()  # Good !
print('band_4 = ', band_4)
band_4['drums'] = 'Dave'
print('band = ', band)  # {'vocals': 'Coverdale', 'guitar': 'Page'}
print('band_4 = ', band_4)  # {'vocals': 'Coverdale', 'guitar': 'Page', 'drums': 'Dave'}

band_5 = dict(band)  # Good !
print('band_5 = ', band_5)
band_5['drums'] = 'Dave'
print('band = ', band)  # {'vocals': 'Coverdale', 'guitar': 'Page'}
print('band_5 = ', band_5)  # {'vocals': 'Coverdale', 'guitar': 'Page', 'drums': 'Dave'}

#  Nested dictionaries

member_1 = {
    'name': 'Plant',
    'instrument': 'vocals'
}

member_2 = {
    'name': 'Page',
    'instrument': 'guitar'
}

band = {
    'member_1': member_1,
    'member_2': member_2
}

print('band = ', band)

print("band['member_1'] = ", band['member_1'])  # {'name': 'Plant', 'instrument': 'vocals'}
print("band['member_1']['name] = ", band['member_1']['name'])  # Plant
