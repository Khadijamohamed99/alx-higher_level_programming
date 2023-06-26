<<<<<<< HEAD
#!/usr/bin/python3
safe_print_list = __import__('0-safe_print_list').safe_print_list
=======
afe_print_list = __import__('0-safe_print_list').safe_print_list
>>>>>>> 1fc026403d3f9aedff5e161396d5aabbc46b124b

my_list = [1, 2, 3, 4, 5]

nb_print = safe_print_list(my_list, 2)
print("nb_print: {:d}".format(nb_print))
nb_print = safe_print_list(my_list, len(my_list))
print("nb_print: {:d}".format(nb_print))
nb_print = safe_print_list(my_list, len(my_list) + 2)
print("nb_print: {:d}".format(nb_print))
