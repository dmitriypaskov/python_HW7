import string
"""Користувач вводить рядок, Ваше завдання – перетворити рядок на hashtag.
Декілька правил:
ніяких символів з набору string.punctuation не повинно бути, у тому числі й пробілів;
підсумкова довжина hashtag має бути не більше 140 символів.
кожне слово починається з великої літери.
якщо довжина хештегу більше 140 символів - обрізати підсумковий рядок до 140 символів."""
hashtag_billet = input("Please enter hashtag :\n")
max_len_hashtag = 140
hashtag = ""
count_len = 0
for i in hashtag_billet.title():
    if i in string.punctuation or i == " ":
        continue
    elif count_len == max_len_hashtag:
        break
    else:
        hashtag += i
        count_len += 1

