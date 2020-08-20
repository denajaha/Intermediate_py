import multiprocessing


# GIL stops python th around 16% usage of the CPU, that is why we are using multiprocessing
# launching separate python processes that not necessarily talk to each other

def spawn(num):
    print('Spawned! {}'.format(num))


if __name__ == '__main__':
    for i in range(55):
        p = multiprocessing.Process(target=spawn, args=(i,))
        p.start()
        p.join()
