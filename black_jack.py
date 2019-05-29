# -*- coding:utf-8 -*-
import random
from enum import Enum


CARDS_TEXT = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
CARDS_VALUE = [i for i in range(1, 14)]


class Suits(Enum):
    """纸牌花色"""
    spade = "黑桃"
    heart = "红桃"
    diamond = "方片"
    club = "梅花"


def hint_theme(text):
    """主体提示"""
    return "*"*30 + str(text) + "*"*30

def warn_theme(text):
    """警告提示"""
    return "-"*20 + str(text) + "-"*20


class FoulException(Exception):
    """犯规提示 结束游戏"""
    pass


class WinException(Exception):
    """获胜提示 结束游戏"""
    pass


class Card:
    """一张扑克牌"""
    def __init__(self, suits, text, value):
        """
        suits: class Suits
            牌的花色:（红桃，黑桃，梅花，方片）
        text: str 
            显示文本: one of CARDS_TEXT
        value: int
            真实值: A为1点，J为11点.. one of CARDS_VALUE
        """
        self.suits = suits
        self.text = text
        self.value = value

    def show(self):
        return self.suits.value + self.text


class Poker:
    """一副扑克牌, 不包含大小王"""
    def __init__(self):
        self.cards = []

        for item in Suits:
            for index, value in enumerate(CARDS_VALUE):
                self.cards.append(
                    Card(
                        suits=item,
                        text=CARDS_TEXT[index],
                        value=value
                    )
                )

        #洗牌
        random.shuffle(self.cards)


class Player:
    """参与游戏的玩家"""
    def __init__(self, name, alive=True, win=False):
        self.name = name
        self.alive = alive
        self.win = win
        self.cards = []

    def check(self):
        """检测手中的牌是否超过21点"""
        price = sum([item.value for item in self.cards])
        print(
            "{name} 【{cards}】 {price}点".format(
                name=self.name,
                cards=" ".join([i.show() for i in self.cards]),
                price=price
            )
        )
        
        if price > 21:
            self.alive = False
            print(warn_theme("玩家 {} 超过21点，出局！".format(self.name)))
        elif price == 21:
            raise WinException(hint_theme("恭喜 {} 获胜！！！".format(self.name)))
        else:
            pass



class Dealer:
    """荷官"""
    def __init__(self):
        self.poker = Poker()
        self.players = []

    def begin(self):
        """开始"""
        self._rule()
        print(hint_theme("开始游戏"))
        while True:
            self.deing()

    def deing(self):
        """发牌"""
        for item in self.players[:]:
            if item.alive:
                item.cards.append(self.poker.cards.pop())
                self._check(item)
        print('==='*20)

    def _rule(self):
        """检测牌和玩家是否就位"""
        if len(self.players) < 2:
            raise FoulException(warn_theme("玩家未就位, 请等待！"))

    def _check(self, item):
        """检测玩家手牌"""
        item.check()
        if not item.alive:
            self.players.remove(item)

        if len(self.players) == 1:
            raise WinException(hint_theme("恭喜 {} 获胜！！！".format(self.players[0].name)))


def desk():
    dealer = Dealer()
    a = Player(name="高进")
    b = Player(name="仇笑痴")
    c = Player(name="周星星")
    dealer.players.append(a)
    dealer.players.append(b)
    dealer.players.append(c)
    try:
        dealer.begin()
    except (FoulException, WinException) as e:
        print(e)

if __name__=="__main__":
    desk()
