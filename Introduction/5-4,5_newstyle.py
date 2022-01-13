from tabnanny import verbose


letter = "Dear {salutation} {name}, \n \n Thank you for your letter. Weare sorry that our {product} {verbed} in your {room}. Plaese note that it should never be used in a {room}, especially near any {animals}. "

print(letter.format(salutation = "hello",name = "Mike",product = "stand", verbed = "ran" ,room = "bedroom",animals = "gorilla"))