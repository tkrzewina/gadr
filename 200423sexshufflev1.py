import random 
sex_acts = ["anal","bj","doggy","69","fisting","cannilingus","lick balls","piss"]
print("Welcome to the porn script generator")
random.shuffle(sex_acts)
scene1=sex_acts[0:4]
print("Scene 1")
for sex_acts1 in scene1:
    print(sex_acts1)
print("Orgasm happend during " + random.choice(scene1))
print("Scene 2")
scene2=sex_acts[4:8]
for sex_acts2 in scene2:
    print(sex_acts2)
print("Orgasm happend during " + random.choice(scene2))
