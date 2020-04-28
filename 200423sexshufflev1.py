import random 
sex_acts = ["anal","bj","doggy","69","fisting","cannilingus","lick balls","piss"]
print("Welcome to the porn script generator")
random.shuffle(sex_acts)
scene1=sex_acts[0:4]
print("Scene 1")
for act in scene1:
    print(act)
print("Orgasm happend during " + random.choice(scene1))
print("Scene 2")
scene2=sex_acts[4:8]
for act in scene2:
    print(act)
print("Orgasm happend during " + random.choice(scene2))
