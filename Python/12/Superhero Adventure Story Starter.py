##########################################
# 슈퍼히어로 어드벤처
# 벤 & 쉬무엘 만듦
##########################################

# 게임 오프닝
def doOpening():
    print("어서 오세요, 히어로 여러분! 여러분에게는 상상하지 못할 힘이 있습니다!")
    print("혹은 음, 여러분은... 모든 힘을 잃었을지도... ")
    print("눈을 뜨니 거칠고 퀭한 빛만이 보입니다.")
    print("하늘을 보고 누운 상태입니다.")
    print("신음과 함께 몸을 일으킵니다.")

# 위치: 연구실
def doLab():
    # 텍스트 출력하기
    print("주위를 둘러보니 이상한 연구실 안임을 발견합니다.\n멋진 공상 과학 영화에 나올 법한 컴퓨터와 최신 기계가 있습니다.")
    print("이는 여러분이 지었던 이야기 하나를 생각나게 합니다.\n죽은 과학자, 외계인 조직, 화학 사고, 그 밖에 여러 가지로 구성된 이야기 말이죠.")
    print("방 앞에는 큰 문이 하나 있으며 옆에는 작은 문이 하나 있습니다.")
    # 플레이어 행동 선택 프롬프트
    choice = " "
    while not choice in "LSC":
        print("무엇을 하시겠습니까?:")
        print("L = 큰 문을 연다")
        print("S = 작은 문을 연다")
        print("C = 컴퓨터를 사용한다")
        choice = input("무엇을 하시겠습니까? [L/S/C]").strip().upper()
    # 행동 수행하기
    if choice == 'L':
        doHallway()
    elif choice == 'S':
        doLabCloset()
    elif choice == 'C':
        doLabComputer()

# 위치: 연구실 복도
def doHallway():
    # 텍스트 출력하기
    print("문을 지나 복도로 나갑니다.")
    print("아무도 없으며 희미한 불빛만이 복도를 비춥니다.")
    print("각각 \'무기\'와 \'죽음\'이 적인 문이 있습니다.")
    print("그리고 \'나가기\'라 적인 출입구와 \'연구실\'이라 적인 출입구가 있습니다.")
    print("바닥에도 작은 문이 하나 있습니다.")
    # 플레이어 행동 선택 프롬프트
    choice = " "
    while not choice in "WDELST":
        print("무엇을 하시겠습니까?:")
        print("W = 무기 문으로 들어간다")
        print("D = 죽음 문으로 들어간다")
        print("E = 나간다")
        print("L = 연구실로 간다")
        print("S = 주위를 살펴본다")
        print("T = 작은 문으로 들어간다")
        choice = input("무엇을 하시겠습니까? [W/D/E/L/S/T]").strip().upper()
    # 행동 수행하기
    if choice == 'W':
        doWeaponsDoor()
    elif choice == 'D':
        doDeathRoom()
    elif choice == 'E':
        doExit()
    elif choice == 'L':
        doLab()
    elif choice == 'S':
        doHallwaySearch()
    elif choice == 'T':
        doTrapdoor()

# 위치: 연구실 벽장
# 인벤토리 시스템을 완성했을 때를 위한 개발자 메모
# 인벤트로 시스템을 완성하면 이곳이 무언가를 숨긴다. 
def doLabCloset():
    # 텍스트 출력하기
    print("너무 작아서 여러분의 근육질 몸이 겨우 들어갈 정도입니다.")
    print("너무 불편합니다. 이곳에 오래 있으면 온몸이 쑤실 겁니다.")
    # 플레이어 행동 선택 프롬프트
    choice = " "
    while not choice in "ES":
        print("무엇을 하시겠습니까?:")
        print("E = 나가다")
        print("S = 주위를 둘러보다")
        choice = input("무엇을 하시겠습니까? [E/S]").strip().upper()
    if choice == 'E':
        doLab()
    elif choice == 'S':
        doLabClosetSearch()

# 위치: 죽음의 방
def doDeathRoom():
    print("아무것도 보이지 않는 깜깜한 방에 들어왔습니다.")
    print("어떤 슈퍼 파워로도 이 안은 보이지 않습니다.")
    print("경고 없이 갑작스레 머리가 혼란스러워집니다. 그리고 아무것도 기억할 수 없습니다...")
    print("아무리 소리쳐봐야 죽음뿐이다!")
    doDie()

# 위치: 바닥의 작은 문
# 이곳을 무엇으로 할지 정합니다. 방, 지하실, 여러 방으로 연결된 복도, 적 등. 
def doTrapdoor():
    print("이곳에는 아무것도 없습니다. 복도로 돌아갑니다.")
    doHallway()

# 행동: 연구실 컴퓨터 사용하기
# 인벤토리 시스템을 완성했을 때를 위한 개발자 메모
# 컴퓨터는 잠겼으며 컴퓨터에 접근하려면 비밀번호가 있어야 함
# 사용자가 비밀번호를 입력하도록 하거나(그 전에 비밀번호를 찾아야 함) 비밀번호 아이템을 찾으면 저절로 풀리도록 함
# 힘을 되찾는 데 컴퓨터를 사용할 수도 있음. 진행에 따라 저절로 될 수도 있고 특정 종류의 코인을 이용하여 살 수도 있음.
def doLabComputer():
    # 텍스트 출력하기
    print("초현대적인 모습으로 부팅하는 컴퓨터(그러나 화면은 Windows XP)와 \n잠기기 전 잠시 나타나는 짧은 메시지:")
    print("\'전원 차단기 제거 성공. 그러나 전원을 켜려면 다음... \'")
    print("메시지를 읽기도 전에 컴퓨터는 잠깁니다.")
    print("비밀번호 없이는 할 수 있는 일이 아무것도 없습니다.")
    doLab()

# 행동: 연구실 벽장 살펴보기
# 인벤토리 시스템을 완성했을 때를 위한 개발자 메모
# 슈퍼 비전을 되찾으면 무엇이 있는지 볼 수 있음
def doLabClosetSearch():
    print("너무 어두워 아무것도 볼 수 없으며 게다가 다리에 통증을 느끼기 시작합니다.")
    print("할 일이 없으므로 나가기로 합니다. (전략상 후퇴입니다. 히어로는 포기하지 않으니까요.)")
    doLabCloset()

# 행동: 복도 살펴보기
# 인벤토리 시스템을 완성했을 때를 위한 개발자 메모
# 컴퓨터 비밀번호는 쓰레기통에 있음
def doHallwaySearch():
    print("쓰레기통에서 메모지를 발견했습니다(으윽~).")
    print("비밀번호는 \'password123\'입니다. 정말?!")
    doHallway()

# 행동: 떠나려고 함
# 인벤토리 시스템을 완성했을 때를 위한 개발자 메모
# 이 문을 열려먼 슈퍼 머슬을 되찾아야 함
def doExit():
    print("\'나가는 문\'라 적힌 문은 꼼짝도 않습니다.")
    print("슈퍼 머슬이 있었더라면...")
    doHallway()

# 행동: 무기고 문 열기
# 인벤토리 시스템을 완성했을 때를 위한 개발자 메모
# 문을 열려면 장갑이 있어야 함. 이미 장갑을 꼈다면
# if 구문을 이용하여 이 메시지를 건너뛰고 doWeaponsRoom()과 같은 함수 호출하기 
def doWeaponsDoor():
    print("\'무기\'라 적인 문을 열려는 순간 어지러움을 느낍니다.")
    print("손잡이가 디크립토나이트임이 틀림없습니다.")
    print("어지럽고 몽롱한 느낌과 함께 온몸의 힘이 빠집니다!")
    print("손잡이를 건들지 않고 문을 열 방법을 찾는 것이 좋을 듯합니다.")
    doHallway()

# Game over
def doDie():
    print("그러자 우리의 히어로는 쓰러집니다. 그 이후로는 아무런 소식도 들을 수 없었습니다:")
    print("Game Over!")

# 여기서 게임 시작하기
doOpening()
doLab()