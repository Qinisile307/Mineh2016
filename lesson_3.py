#Advanced concepts -Strings

message = ' Hello, World!'

print(message.strip())

print(len(message)) #Remove leading and trailing whitespace
print(message.lower()) #Convert all characters to lowercase
print(message.split(',')) #Split the string into a list of the coma

#upper method
print(message.upper()) #Convert all characters to uppercase

#replace method
print(message.replace('World', 'Python')) #Replace 'World' with 'Python'