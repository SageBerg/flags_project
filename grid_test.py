#import flag_mapping

flags_html = open("flags.html", "w")

#flags_html.write("<!DOCTYPE html>\n")
flags_html.write("<html>\n")
flags_html.write("<body>\n")

l = list()
for i in range(60):
    l.append(list())
for sub_list in l:
    for i in range(118):
        sub_list.append(". ")

population_dict = dict()
f = open("pop.txt")                                 #open a file with populations of all countries
for line in f:                                      #look at each country and it's population
    line = line.strip()                             #strip whitespace off the ends of the input
    split_line = line.split(" ")                    #break the country name and population into two
    population_dict[split_line[0]] = split_line[1]  #put the two items into a mapping

abbrev_list = list()
for country in population_dict:                     #look through all the keys (which are country names)
    #print(population_dict[country])            
    pop_int = int(population_dict[country])         #assign a int equal to the population value
    while pop_int >=  1000000:                      
        abbrev_list.append(country[0] + country[1]) #append string of first two letters of country to list
        flags_html.write("<div style=\"height: 21px; width: 29px; float: left;\">\n")
        flags_html.write("<img border=\"1\" title=\"" + country + "\"src=""/grid_test_flags/" + country + ".png>\n")
        flags_html.write("</div>\n")
        pop_int -= 1000000

flags_html.write("</body>\n")
flags_html.write("</html>")

col = 0
row = 0
for abbrev in abbrev_list:
    l[row][col] = abbrev
    col += 1
    if col == 118:
        row += 1
        col = 0    

for sub_list in l:
    for string in sub_list:
        print(string,end="")
    print()

world_pop = 0
for country in population_dict:
    world_pop += int(population_dict[country])
#print(world_pop)
