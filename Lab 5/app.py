import utils

if __name__ == "__main__":
    print("-----Press q if you want to quit-----")
    flag = input("x = ")
    while (flag != "q"):
        print(utils.process_item(flag))
        flag = input("x = ")