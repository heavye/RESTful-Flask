friends = ["Rolf", "Sam", "Samanta", "Seba", "Jen"]
starts_s = [x for x in friends if x.startswith("Se")]

for friend in friends:
    if friend.startswith("Sa"):
        starts_s.append(friend)

print(id(starts_s))