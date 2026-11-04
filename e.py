"""問題：guitar_shop!
以下の条件を満たすPythonコードを作成してください

①以下のギターをPythonで作成
・Stratocaster
・Telecaster
・Les Paul
・ES-335
Guitar クラスでジャンルとブランドを作成

②好きな音楽のジャンルとギターブランドを入力

③好みに応じておすすめのギターを提案

"""


class Guitar:
    def __init__(self, name, genre, brand):
        self.name = name
        self.genre = genre
        self.brand = brand

    def match(self, genre, brand):
        return self.genre == genre or self.brand == brand


def find_recommendations(guitars, genre, brand):
    recommendation = []
    for guitar in guitars:
        if guitar.match(genre, brand):
            recommendation.append(guitar)
    return recommendation


genre_answer = input("好きな音楽のジャンルは：")
brand_answer = input("好きなギターブランドは：")

stratocaster = Guitar("ストラトキャスター", "blues", "fender")
telecaster = Guitar("テレキャスター", "funk", "fender")
les_paul = Guitar("レスポール", "jazz", "Gibson")
es_335 = Guitar("ES-335", "R&B", "Gibson")

guitars = [stratocaster, telecaster, les_paul, es_335]

recommendation = find_recommendations(guitars, genre_answer, brand_answer)

if recommendation:
    for guitar in recommendation:
        print(f"{guitar.name}がおすすめです！")
else:
    print("おとといきやがれ！")
