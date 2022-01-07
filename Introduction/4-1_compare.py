import random

secret = random.randint(1,10)
guess = random.randint(1,10)

print("secret:" + str(secret))
print("guess:" + str(guess))

if secret == guess:
    print("just right")
elif secret > guess:
    print("too low")
else :
    print("too high")