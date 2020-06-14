import random

print ('welcome to BLACK JACK!!')
print ('this game is a simple card game.')
print ('Make your hand so that the total number of cards does not exceed [21].')
print ('The one closer to [21] is the winner!')

marks = ['♠︎', '❤︎', '♦︎', '♣︎']
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
    print("カードを追加で引きますか？")
    print("1.はい")
    print("2.いいえ")
    playerReply = int(input())
    if playerReply == 1:
        draw_a_card(playerHand)
        print(f"あなたの手札は{playerHand}です")
        # ディーラーの挙動を設定中、エラー出る
    elif playerReply == 2:
        while True:
            total = []
            for i in dealerHand:
                total.append(i[1])
            if sum(total) > 17:
                break
            draw_a_card(dealerHand)
        break
    else:
        print("※1か2を選択してください")


print(f"あなたの手札は{playerHand}です")
print(f"ディーラーの手札は{dealerHand}です")

playerSum = []
for i in playerHand:
    playerSum.append(i[1])

dealerSum = []
for i in dealerHand:
    dealerSum.append(i[1])

print(f"あなたの手札は{sum(playerSum)}です")
print(f"ディーラーの手札は{sum(dealerSum)}です")

if 