try:
    file = open("q_file.tex")
except FileNotFoundError:
    file = open("a_file.txt", "w")
except KeyError as error_message:
    print("Key Error" + error_message)
else:
    content = file.read()
    print(content)
finally:
    file.close()
    raise KeyError("Banny")
