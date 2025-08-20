#strings son colecciones igual que las listas y las tuplas y son INMUTABLES. 
message = 'Hola mundo!'
print(len(message)) #11
print(type(message)) # str
print('!' in message) # True
print('w' in message) # False
new_message ='h' + message[1:]
print(new_message) # ola mundo!
new_message2 = message[-1::-1] # !odnum aloH
print(new_message2) # !odnum aloH
print(message[0:5]) # Hola
message[2]='z'
print(message) # TypeError: 'str' object does not support item assignment, porque las cadenas son inmutables