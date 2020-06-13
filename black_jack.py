import random

print ('welcome to BLACK JACK!!')
print ('this game is a simple card game.')
print ('Make your hand so that the total number of cards does not exceed [21].')
print ('The one closer to [21] is the winner!')

marks = ['spade', 'heart', 'diamond', 'club']
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

# デッキを作成
deck = []
for mark in marks:
    for num in nums:
        deck.append([mark, num])

# 手札を定義
playerHand = []
dealerHand = []

# 山札からカードを引く処理
def draw_a_card(hand):
    card = random.choice(deck)
    deck.remove(card)
    hand.append(card)

# playerとdealerが2枚ずつカードを引く
for i in range(2):
    draw_a_card(playerHand)
    draw_a_card(dealerHand)
