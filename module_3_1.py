calls = 0

def count_calls():
   global calls
   calls = calls + 1

def string_info(string):
    count_calls()
    return (len(string), string.upper(), string.lower())

def is_contains(string_, list_):
    count_calls()
    for i in range(len(list_)):
        if( string_.upper() == list_[i].upper() ):
            return True
    return False



print(string_info('Capybara'))
print(string_info('Armageddon'))
print(string_info('Fild'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN']))
print(is_contains('cycle', ['recycling', 'cyclic']))
print(is_contains('Bye', ['Hi', 'bye', 'Goodbye']))
print(calls)

