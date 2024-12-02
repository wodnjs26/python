from character import Hero, Goblin, Orc, Dragon
from battle import Battle

def main():
    print("게임 시작")
    name = input("이름 입력:")
    role = input("직업 입력(전사/마법사/궁수)")
    hero = Hero(name,100,20,5,speed=12,role=role)
    print(hero)
    
    monster_pool = [
        Goblin(name : "고블린", hp : 10, attack : 10, defense: 2, speed : 10),
        Orc(name : "오크", hp : 150, attack : 25, defense: 35, speed : 5),
        Dragon(name : "드래곤", hp : 300, attack : 100, defense: 50, speed : 150),
    ]
    
    battle = Battle()
    while hero.is_alive():
        monster = random.choice(monster_pool)
        # random.choice 인자로 들어오는 list 중에 하나를 뽑아줌
        print(f"\n 몬스터 {monster.name} 등장")
        print(monster.description())
        
        if not battle.fight(hero, monster):
            break

if __name__ == '__main__':
    main()