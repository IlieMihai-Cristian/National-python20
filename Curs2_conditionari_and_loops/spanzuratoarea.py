# cuvant = 'o r i c e'
#          'o _ _ _ e'
# - daca litera de inceput sau de sfarsit se mai gaseste in interior, aceasta se va afisa
# - 7 incercari;

word = 'teleenciclopedie'
start_letter = word[0]
end_letter = word[-1]
display_word = ''

for l in word.lower():
    if l != start_letter and l != end_letter:
        l = '_'
    display_word += l
# print(display_word)
attempts = 7

# de aici incepe jocul
tried_chars = []
while attempts > 0:
    print(f'Cuvantul este: {display_word}. Mai aveti {attempts} incercari!')
    letter = input('Introduceti litera: ').lower()
    if len(letter) != 1:
        print('Va rugam introduceti o singura litera!')
        continue
    elif not letter.isalpha():
        print('Va rugam introduceti doar litere')
        continue
    if letter in word.lower():
        if letter in tried_chars:
            print(f'Litera {letter} a mai fost folosita. Literele incercate pana acum sunt: {tried_chars}!')
        for index, character in enumerate(word.lower()):
            if letter == character:
                if letter not in tried_chars:
                    tried_chars.append(letter)
                display_word = display_word[:index] + letter + display_word[index+1:]
    else:
        if letter not in tried_chars:
            tried_chars.append(letter)
            attempts -= 1
        else:
            print(f'Litera {letter} a mai fost folosita. Literele incercate pana acum sunt: {tried_chars}!')
    if attempts == 0:
        print(f'Ati pierdut jocul! Cuvantul cautat era "{word}" ')
    elif not '_' in display_word:
        print(f'Felicitari! Ati castigat! Cuvantul gasit este: "{display_word}" ')
        break
