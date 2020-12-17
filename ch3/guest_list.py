guests = ['Joko', 'Gambiro', 'Bambang']

print(f"Ayo, Pak {guests[0]}, makan malam.")
print(f"Ayo, Pak {guests[1]}, makan malam.")
print(f"Ayo, Pak {guests[2]}, makan malam.")

print(f"\nPak {guests[1]} tidak bisa ikut makan.")

guests[1] = 'Margono'

print(f"\nAyo, Pak {guests[0]}, makan malam.")
print(f"Ayo, Pak {guests[1]}, makan malam.")
print(f"Ayo, Pak {guests[2]}, makan malam.")

guests.insert(0, 'Sukri')
guests.insert(2, 'Marjo')
guests.append('Sidul')

print(f"\nAyo, Pak {guests[0]}, makan malam.")
print(f"Ayo, Pak {guests[1]}, makan malam.")
print(f"Ayo, Pak {guests[2]}, makan malam.")
print(f"Ayo, Pak {guests[3]}, makan malam.")
print(f"Ayo, Pak {guests[4]}, makan malam.")
print(f"Ayo, Pak {guests[5]}, makan malam.")

print("\nMaaf, tempatnya masih terbatas. Hanya cukup untuk 2 orang saja sekarang.")

popped_guest = guests.pop()
print(f"Tunggu sebentar ya, Pak {popped_guest}")
popped_guest = guests.pop()
print(f"Tunggu sebentar ya, Pak {popped_guest}")
popped_guest = guests.pop()
print(f"Tunggu sebentar ya, Pak {popped_guest}")
popped_guest = guests.pop()
print(f"Tunggu sebentar ya, Pak {popped_guest}")

print(f"\nMonggo, Pak {guests[0]} makan duluan.")
print(f"Monggo, Pak {guests[1]} makan duluan.")

print(f"Number of guest: {len(guests)}")

del guests[0]
del guests[0]

print(guests)