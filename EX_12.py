import string
"""Користувач вводить рядок, Ваше завдання – перетворити рядок на hashtag.
Декілька правил:
ніяких символів з набору string.punctuation не повинно бути, у тому числі й пробілів;
підсумкова довжина hashtag має бути не більше 140 символів.
кожне слово починається з великої літери.
якщо довжина хештегу більше 140 символів - обрізати підсумковий рядок до 140 символів."""
hashtag_billet = input("Please enter hashtag :\n")
max_len_hashtag = 139
hashtag_arr = []
count_len = 0
for i in hashtag_billet:
    if i in string.punctuation or i == " ":
        hashtag_arr.append(" ")
        continue
    elif count_len == max_len_hashtag:
        break
    else:
        hashtag_arr.append(i)
        count_len += 1
hashtag = "#" + "".join("".join(hashtag_arr).title().split())
