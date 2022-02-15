import requests as re
import requests.exceptions as ex

wrong_url = (OSError, ex.HTTPError, ex.URLRequired, ex.MissingSchema)

while True:
    com = input("""
    Input any command:
    d - dowload
    e - exit\n
    """)
    if com == "e":
        break
    elif com == "d":
        url = input("Input URL:\n")
        name = url.split("/")[-1]
        try:
            req = re.get(url)
            while req.status_code == 401:
                log = input("Input login:\n")
                pas = input("Input password:\n")
                if log == "" or pas == "":
                    break
                req = re.get(url, auth=(log, pas))
            with open(name, "wb") as file:
                file.write(req.content)
        except wrong_url:
            print("Error.")
    else:
        print("Invalid command. Please try again.")