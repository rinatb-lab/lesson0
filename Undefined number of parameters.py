def single_root_words(root_word ='berry' , *other_words):
    same_words =[]
    for i in other_words:
        if len(i) >= len(root_word):
            b = i.lower()
            a =root_word.lower() # а : меньшей длины
            if a in b:
                same_words.append(i)
        else:
            b = root_word.lower()
            a = i.lower()
            if a in b:
                same_words.append(i)
    print(same_words)


single_root_words( 'Рома', 'Роман' , 'sometimes' , 'роМаны' , 'аэродром')
single_root_words('sunnys' , 'sun' , 'sunny' , 'sunsilk')
