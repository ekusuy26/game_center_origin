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
    elif playerReply == 2:
        total = [dealerHand[1][1]]
        while True:
            draw_a_card(dealerHand)
            for i in dealerHand:
                total.append(i[1])
            if sum(total) > 17:
                print(total)
                print(dealerHand)
                print(sum(total))
                break
        break
    else:
        print("※1か2を選択してください")

