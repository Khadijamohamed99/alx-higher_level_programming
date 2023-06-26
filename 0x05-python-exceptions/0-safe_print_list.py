<<<<<<< HEAD
#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
=======
afe_print_list(my_list=[], x=0):
>>>>>>> 1fc026403d3f9aedff5e161396d5aabbc46b124b
    try:
        num = 0
        for i in range(x):
            print(my_list[i], end="")
            num += 1
            for x in range(num):
                print("", end="")
        print()
        return num
    except IndexError:
        print()
        return num
