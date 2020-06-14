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

# 初期手札を表示
print(f"あなたの手札は{playerHand}です")
print(f"ディーラーの手札は{dealerHand[0]}です")


while True:
    print("Is it a hit or a stand?  [hit/stand]")
    playerReply = input()
    if playerReply == "hit":
        draw_a_card(playerHand)
        print(f"あなたの手札は{playerHand}です")
    elif playerReply == "stand":
        while True:
            total = []
            for i in dealerHand:
                total.append(i[1])
            if sum(total) >= 17:
                break
            draw_a_card(dealerHand)
        break
    else:
        print("Choose between hit or stand.")

playerSum = []
for i in playerHand:
    playerSum.append(i[1])

dealerSum = []
for i in dealerHand:
    dealerSum.append(i[1])

# 手札を出力
print('<<< player >>>')
playerAddition = []
dealerAddition = []
for i in playerHand:
    playerAddition.append(i[1])
    print(f"|{i[0].ljust(7)} | {str(i[1]).rjust(2)}|")
print('--------------')
print(f"|total   | {str(sum(playerAddition)).rjust(2)}|")
print()
print('<<< dealer >>>')
for i in dealerHand:
    dealerAddition.append(i[1])
    print(f"|{i[0].ljust(7)} | {str(i[1]).rjust(2)}|")
print('--------------')
print(f"|total   | {str(sum(dealerAddition)).rjust(2)}|")

if sum(playerSum) > 21 and sum(dealerSum) > 21:
    print('ディーラーの勝ち')
elif sum(playerSum) > 21:
    print('ディーラーの勝ち')
elif sum(dealerSum) > 21:
    print('プレイヤーの勝ち')
elif sum(playerSum) > sum(dealerSum):
    print('プレイヤーの勝ち')
elif sum(playerSum) < sum(dealerSum):
    print('ディーラーの勝ち')
else:
    print('引き分けです')
