import random


subjects=[
    'Akshay Kumar',
    'Virat Kohli',
    'Nirmala Sitaraman',
    'Mumbai Cat',
    'Group Of monkeys',
    'Prime Minister Modi',
    'Auto Rickshaw driveer from kurar'
]

actions=[
    'launches',
    'cancels',
    'dances with',
    'eats',
    'declares war on',
    'orders',
    'celebrates'
]

places_or_things=[
    'at red fort',
    'in mubai loca; train',
    'a plate of samosa',
    'inside parliamnet',
    'at ganga ghat',
    'during ipl match',
    'at india gate' 
]

while True:
    subject = random.choice(subjects)
    action = random.choice(actions)
    place_or_thing = random.choice(places_or_things)
    
    headline = f"BREAKING NEWS! {subject} {action} {place_or_thing}"
    print('\n' + headline)
    
    user_input = input("\nDo you want another firing headline? (yes/no) ").strip().lower()
    if user_input == 'no':
        break
    
print('thanks for using my fake news generator system!')