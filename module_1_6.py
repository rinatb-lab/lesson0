my_dict={'Sasha':1984,'Lena':1989,'Gena':2002 }
print('Dict:               ',my_dict)
print('Existing value:     ', my_dict['Lena'])
print('Not existing value: ', my_dict.get('Rita'))
my_dict.update({'Masha':2001,
                'Roman':1996})
a=my_dict.pop('Gena')
print('Deleted value:      ',a)
print('Modified dictionary:',my_dict)
print(' ')
my_set={1,2,3,8,3,2,1,'string',True,(1,2,3)}
print('Set:                ',my_set)
my_set.add('str1')
my_set.add((7,8))
my_set.remove(8)
print('Modified set:       ',my_set)