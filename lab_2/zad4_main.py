def censorship(path: str):
    with open(path, "r") as file:
        with open("data/censored_letter.txt", "w") as censored:
            i = 1

            line = file.readline()
            while line:
                if i % 3 == 0:
                    censored.write("****\n")
                elif line.lower().find("kocham") >= 0:
                    censored.write("****\n")
                else:
                    censored.write(line)
                i += 1
                line = file.readline()
            censored.close()
        file.close()
censorship("data/letter.txt")