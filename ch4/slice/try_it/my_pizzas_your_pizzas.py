my_pizzas = ['italian', 'american', 'pepperoni']
friend_pizzas = my_pizzas[:]

my_pizzas.append('new pizza')
friend_pizzas.append('diff pizza')

print("My favorite pizzas are:")

for my_pizza in my_pizzas:
    print(my_pizza)

print("My friend's favorite pizzas are:")

for friend_pizza in friend_pizzas:
    print(friend_pizza)
