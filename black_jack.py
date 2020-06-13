print ('welcome to BLACK JACK!!')
print ('this game is a simple card game.')
print ('Make your hand so that the total number of cards does not exceed [21].')
print ('The one closer to [21] is the winner!')

marks = ['spade', 'heart', 'diamond', 'club']
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

all = []
for mark in marks:
    for num in nums:
        all.append([mark, num])

