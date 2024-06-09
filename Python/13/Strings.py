############################################
# Strings.py
# 문자열 외부화하기
############################################

def get(id):
    if id == "Welcome":
        return ("탐험가 여러분을 환영합니다!\n"
                "혼란스러운 상태에서 잠을 깬 여러분은 아무것도 떠오르지 않습니다.\n"
                "방문까지 겨우 기어가 손잡이를 돌렸더니 문이 열립니다.\n"
                "밖으로 나가 봐도 모든 것이 낯설기만 합니다.\n"
                "바깥 풍경은 척박하고 황량한 붉은 흙만이 흩날릴 뿐입니다.\n"
                "우주복을 입은 자신을 발견하곤 모든 것이 궁금해집니다.")
    elif id == "Start":
        return ("주위를 둘러봐도 붉은 사막과 바위 더미와 먼지뿐입니다.\n"
                "여러분 앞에는 이상하게 생긴 팔각형 구조물이 있습니다.\n"
                "가까이 가니 삐 소리가 들립니다. 그리곤 멈춥니다. 아니, 계속됩니다.")
    elif id == "Boulders":
        return ("정말인가요? 그건 바위 더미입니다.\n"
                "크고 무겁고 단순한 바위입니다.")
    elif id == "Structure":
        return ("여러분은 이상한 구조물을 조사합니다.\n"
                "안에서는 오싹하면서도 기이한 소리가 들립니다.\n"
                "문도 없고 창문도 없습니다.\n"
                "아니, 문처럼 보여서 한번 열어 보려고 합니다.\n"
                "그리고 삐 소리가 들립니다. 어디서 나는 소리일까요?")
    elif id == "StructureDoor":
        return ("문은 잠긴 듯합니다.\n"
                "둥근 구멍이 보입니다. 열쇠 구멍일까요?")
    elif id == "StructureDoorNoKey":
        return ("그쪽으로 손을 내밀지만 파란빛이 번쩍이며 닫혀 버립니다!\n"
                "계획한 대로는 잘 안 되는군요.")
    elif id == "Run":
        return ("한동안 달립니다.\n"
                "그리곤 허공에 뜬 자신을 발견합니다. 아래로, 아래로, 아래로.\n"
                "아주 깊은 골짜기로 떨어지며 다시는 빛을 보지 못하리라는 생각이 듭니다.\n"
                "그리 용감한 행동은 아니었네요. 그렇죠?")
    elif id == "GameOver":
        return "게임 오버!"
    else:
        return ""