'''
게임 메뉴 만들기
숫자 1입력 : "게임을 시작합니다" 출력
숫자 2입력: "실시간 랭킹" 출력
숫자 3입력 : "게임을 종료합니다." 출력 후 프로그램 종료
(단, 3을 입력할 때까지 프로그램은 계속 진행됨
1~3외 다른 숫자입력한 경우 "다시 입력해주세요"를 출력
'''


while True :
    print("메뉴를 입력하세요")
    menu = input("1.게임시작 2.랭킹보기 3.게임종료>>>")
    if menu == '1' :
        print("게임을 시작합니다.")
    elif menu == '2':
        print("실시간 랭킹을 출력합니다.")
    elif menu == '3' :
        break
    else:
        print("다시 입력해주세요")
