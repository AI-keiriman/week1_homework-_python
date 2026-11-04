class Fighter:
    def __init__(self, name, hp, attack, defense):
        self.name = name
        self.hp = hp
        self.attack = attack
        self.defense = defense

    def super_saiyan(self):
        return self.attack * 2

    def punch(self, opponent):
        damage = self.attack - opponent.defense
        opponent.hp -= damage
        print(
            f"{self.name}の攻撃！{opponent.name}に{damage}のダメージ！({opponent.name}のHP: {opponent.hp})"
        )


gokuu = Fighter("悟空", 1000, 100, 50)
vegita = Fighter("ベジータ", 1000, 80, 100)

gokuu.attack = gokuu.super_saiyan()

print("悟空はスーパーサイヤ人に変身した! 攻撃力:" + str(gokuu.attack))

turn = 1
while True:
    print(f"--- ターン{turn} ---")
    # 攻撃して、相手の HP が 0 なら勝者を表示して break
    gokuu.punch(vegita)

    # 悟空の攻撃のすぐ後で相手のHPを調べます
    if vegita.hp <= 0:
        print("ベジータは倒れた! 悟空の勝利!")
        break

    vegita.punch(gokuu)

    # ベジータの攻撃のすぐ後で相手のHPを調べます
    if gokuu.hp <= 0:
        print("悟空は倒れた! ベジータの勝利!")
        break

    turn += 1
