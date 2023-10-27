def AND_게이트(*nums):
    result = 1
    for num in nums:
        result = result * num
    return result

def OR_게이트(*nums):
    result = 1
    for num in nums:
        result = result * (1 - num)
    return 1 - result

print("결함수분석기법(FTA)에서 AND 게이트와 OR 게이트를 계산할 수 있는 계산기입니다.")

while True:
    print("\n1 또는 2의 번호를 입력해서 계산하려는 게이트를 선택해 주세요.")
    choice = input("1 AND 게이트 2 OR 게이트\n선택:")

    if choice == "1":
        nums = list(map(float, input("확률들을 띄어쓰기로 구분하여 입력하세요. (예: 0.1 0.2): ").split()))
        print(f"결과: {round(AND_게이트(*nums), 5)}")
    elif choice == "2":
        nums = list(map(float, input("\n확률들을 띄어쓰기로 구분하여 입력하세요. (예: 0.1 0.2): ").split()))
        print(f"결과: {round(OR_게이트(*nums), 5)}")
    else:
        print(" 숫자 1, 2 를 사용해서 AND 게이트와 OR 게이트를 선택하세요.")
