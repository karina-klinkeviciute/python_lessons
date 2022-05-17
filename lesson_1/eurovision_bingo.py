things = ["Fake instruments", "Outfit change", "Any joke about Australia", "Ukrainian flag", "Flames", "Fake rain",
"Wind machine", "Semi-naked male dancers", '"Good morning Australia"', "Synchronized dancing", "Happy tears", 
"Middle finger", "Hosts speaks in unison", "Strobe light", "Hosts are complimented", "Слава Україні!", "Children singing",
"Stop war", "Abba reference", "12 points to Ukraine"
]

# things_happened = ["Abba reference", "12 points to Ukraine", "Ukrainian flag", "Hosts speaks in unison", "Stop war"]
things_happened = ["Any joke about Australia", "12 points to Ukraine" ]



# for thing in things:
#     print(thing)
    
    
from termcolor import colored

for thing in things:
    if thing in things_happened:
        print(colored(thing, "green"))
    else:
        print(thing)
