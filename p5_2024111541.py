def standrad_weigth(weigth):
    return(height - 100) * 0.9

def difference_weigth(weigth, standrad_weigth):
    return weigth - standrad_weigth

def obesity_weigth(weigth, standrad_weigth):
    return (weigth / standrad_weigth) * 100

def obesity_verdict(obesity_weigth):
    if obesity_weigth < 100:
        return "저체중"
    elif obesity_weigth <= 100:
        return "표준"
    elif obesity_weigth <= 120:
        return "과체중"
    else:
        return "비만"

name = input("이름 : ")
height = float(input("키 : "))
weight = float(input("몸무게 : "))

standrad = standrad_weigth(height)
difference = difference_weigth(weight, standrad)
obesity = obesity_weigth(weight, standrad) 


print(f"이름 : {name}")
print(f"표준체중 : {standrad:.1f}kg")
print(f"체중차 : {'+' if difference > 0 else ''}{difference:.1f}kg")
print(f"비만도 : {obesity:.1f}%")
print(f"판정 : {obesity_verdict(obesity)}")
