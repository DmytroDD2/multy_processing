from multiprocessing import Process,Queue

list_numbers = [i for i in (range(150)) if i != 0 and i % 2 == 0]


def proces1(num):
    num = num[0:len(num) // 2]
    print(f"proces1: {sum(num)}")


def proces2(num):
    num = list_numbers[len(num) // 2:]
    print(f"proces2: {sum(num)}")


if __name__ == "__main__":
    p1 = Process(target=proces1, args=(list_numbers,))
    p2 = Process(target=proces2, args=(list_numbers,))

    p1.start()
    p2.start()

    p1.join()
    p2.join()
