def winning_sequence(cards, win_cards, n):

    sorted_cards = []
    win_cards_slice = []
    normal_cards = []
    
    for i in range(n):
        if win_cards[i] == cards[i]:
            normal_cards.append(cards[i])
        else:
            sorted_cards.append(cards[i])
            win_cards_slice.append(win_cards[i])
    sorted_cards = sorted(sorted_cards)
    if sorted_cards == win_cards_slice:
        return 'YES'
    else:
        return 'NO'

n = int(input())
a = input()
b = input()

a = a.split(' ')
cards = []
for i in a:
    cards.append(int(i))
    if len(cards) >= n:
        break

b = b.split(' ')
win_cards = []
for j in b:
    win_cards.append(int(j))
    if len(win_cards) >= n:
        break

result = winning_sequence(cards, win_cards, n)
print(result)