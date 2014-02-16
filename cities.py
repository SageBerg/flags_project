f = open("cities.txt", "r")
output = open("city_pop.txt", "w")

for line in f:
    index = line.find("\"><a href=\"/wiki/")
    index_population = line.find("<td>")
    index_country = line.find("</a></td>")
    print(index_country)
    if index > 10:
        s = ""
        for char in line[index + 17:]:
            if char != "\"" and char != " ":
                s += char
                print(char)
            elif char == " ":
                s += "_"
            else:
                output.write(s)
                break
    if index_population == 0:
        n = ""
        for char in line[index_population + 4:]:
            if char.isnumeric() or char == ",":
                if char != ",":
                    n += char
            else:
                break
        if len(n) > 6:
            output.write(" " + n + "\n")
    if index_country > 0:
        go = True
        cnt = 1
        c = ""
        while go:
            var = index_country - cnt
            char = line[var]
            cnt += 1
            if char != ">" and char != " ":
                c += char
            elif char == " ":
                c += "_"
            else:
                go = False
        c = c[::-1]
        if len(c) > 0:
            output.write(" " + c)

f.close()
output.close()
