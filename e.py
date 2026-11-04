"""問題：guitar_shop!
以下の条件を満たすPythonコードを作成してください

①以下のギターをPythonで作成
・Stratocaster
・Telecaster
・Les Paul
Guitar クラスでジャンルとブランドを作成

②好きな音楽のジャンルとギターブランドを入力

③好みに応じておすすめのギターを提案

"""

class Guitar:
    def __init__(self, name, genre, brand):
        self.name = name
        self.genre = genre
        self.brand = brand

genre_answer = input("好きな音楽のジャンルは：")
brand_answer = input("好きなギターブランドは：")

stratocaster = Guitar("ストラトキャスター", "blues", "fender")
telecaster = Guitar("テレキャスター", "funk", "fender")
les_paul = Guitar("レスポール", "jazz", "Gibson")

guitars = [stratocaster, telecaster, les_paul]

recommendation = []

for guitar in guitars:
    if genre_answer == guitar.genre or brand_answer == guitar.brand:
        recommendation.append(guitar)
        
if recommendation:
    for guitar in recommendation:
        print(f"{guitar.name}がおすすめです！")
else:
    print("おとといきやがれ！")
