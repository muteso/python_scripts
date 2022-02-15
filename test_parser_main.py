from os import getcwd
import test_parser_lib as tp

def deb_main(qstn, answ):
    with open("test.txt", 'w') as file:
        end = int(input("Please, input max amount of lines for output:\n"))
        for i in range(end):
            text = f'{qstn[i][0][0]}. {qstn[i][0][1]} - {answ[i][1]}\n'
            file.write(text)
            for text in qstn[i][1:]:
                file.write(text)
            

def main(qstn, answ):
    line = range(len(qstn))
    if line == range(len(answ)):
        with open("test.txt", 'w') as file:
            for i in line:
                text = f'{qstn[i][0][0]}. {qstn[i][0][1]} - {answ[i][1]}\n'
                file.write(text)
                for text in qstn[i][1:]:
                    file.write(text)
    else:
        print("""
        Programm stopped via wrong formatting:\n
        - please format your docx-files if single style.
        """)

if __name__ == "__main__":
    path = getcwd() + "\\" + input("Please, input the file name:\n")

    qstn = tp.get_qstn(path)
    #qstn = tp.deb_get_qstn(path) # toggle for debugging
    answ = tp.get_answ(path)
    #main(qstn, answ)
    deb_main(qstn, answ) # toggle for debugging
