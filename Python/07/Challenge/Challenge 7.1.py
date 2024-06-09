# 빈 animals 리스트 만들기
animals = []
 
# 입력용 변수
userInput = " "
 
# 사용자에게 설명문 출력하기
print("여러분 대신 동물을 정렬합니다.")
print("한 번에 한 동물씩 입력하세요.")
print("입력이 끝나면 엔터를 누르세요.")
 
# 빈 문자열이 될 때까지 루프
while userInput != "":
    # 입력받기
    userInput = input("동물을 입력하세요. 끝내려면 빈칸으로 두세요: ").strip()
    # 비었는지와 중복이 아닌지 확인하기 
    # 참고: 'not in'은 '사용자 입력이 animals 리스트에 없다면'이라는 뜻
    if len(userInput) > 0 and userInput not in animals:
        # 비지 않았다면 추가하기
        animals.append(userInput)
 
# 데이터 정렬하기
animals.sort()
 
# 출력 형식을 적용하여 리스트 출력하기 
for animal in animals:
    print(animal)