calls = 0
def count_calls():
    global calls
    calls = calls+1

def string_info(i = ''):
    j = (len(i),i.upper(),i.lower() )
    #print(j)
    count_calls()
    return j

def  is_contains(string_info = '', is_contains = ()):
    string_info = string_info.lower()
    for i in is_contains:
        if string_info == i.lower():
            j = True
        else: j = False
    #print(j)
    count_calls()
    return j

print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN']))
print(is_contains('cycle', ['recycling', 'cyclic']))
print(calls)



