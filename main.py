def parse(query: str) -> dict:
    words_dict = dict()
    if len(query.split("?")) > 1:
        words_list = query.split("?")[1].split("&")
        for i in words_list:
            if len(i) > 0:
                words_dict[i[0: i.index("=")]] = i[i.index("=") + 1:]
    return words_dict


if __name__ == '__main__':
    assert parse('https://example.com/path/to/page?name=ferret&color=purple') == {'name': 'ferret', 'color': 'purple'}
    assert parse('https://example.com/path/to/page?name=ferret&color=purple&') == {'name': 'ferret', 'color': 'purple'}
    assert parse('http://example.com/') == {}
    assert parse('http://example.com/?') == {}
    assert parse('http://example.com/?name=Dima') == {'name': 'Dima'}


def parse_cookie(query: str) -> dict:
    words_dict = dict()
    words_list = query.split(";")
    for i in words_list:
        if len(i) > 0:
            words_dict[i[0: i.index("=")]] = i[i.index("=")+1:]
    return words_dict


if __name__ == '__main__':
    assert parse_cookie('name=Dima;') == {'name': 'Dima'}
    assert parse_cookie('') == {}
    assert parse_cookie('name=Dima;age=28;') == {'name': 'Dima', 'age': '28'}
    assert parse_cookie('name=Dima=User;age=28;') == {'name': 'Dima=User', 'age': '28'}

print("ok")
