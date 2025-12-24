full_dot = '●'
empty_dot = '○'
def create_character(name, strength, intelligence, charisma):
    if not isinstance(name, str):
        return 'The character name should be a string'
    if name == '':
        return 'The character should have a name'
    if len(name) > 10:
        return 'The character name is too long'
    if ' ' in name:
        return 'The character name should not contain spaces'

    stats = (strength, intelligence, charisma)
    if not all(isinstance(stat, int) for stat in (strength, intelligence, charisma)):
        return 'All stats should be integers'
    if not all(stat >= 1 for stat in stats):
        return 'All stats should be no less than 1'
    if not all(stat <= 4 for stat in stats):
        return 'All stats should be no more than 4'
    if sum(stats) != 7: 
        return 'The character should start with 7 points'
    
    def make_dots(value):
        return full_dot * value + empty_dot * (10 - value)

    return (
        f'{name}\n'
        f'STR {make_dots(strength)}\n'
        f'INT {make_dots(intelligence)}\n'
        f'CHA {make_dots(charisma)}'
    )

print(create_character('ren', 4, 2, 1))