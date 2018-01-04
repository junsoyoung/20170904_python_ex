def safe_sum(a, b):
    if type(a) != type(b):
        print("더할 수 있는 값이 아닙니다.")
        return
    else:
        return a+b


if __name__ == "__main__":
    print(safe_sum(4,5))




