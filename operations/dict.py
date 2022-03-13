user = {
    'name': 'happy',
    'age': 34,
    'is_metro': True,
    'info': {
        'area': 1234.87,
        'population': 3400987,
        'coordinates': (91.07, 89.56),
        'landmarks': ['qutab minar', 'red fort'],
        'address': {
            'line1': 'house 222',
            'pin': 148101
        }
    }
}

# Accessibility - bracket notation dict[key]
landmarks = user['info']['landmarks'][0]
print(landmarks)

user['age'] = 40
print(user)