try:
    file = open("USPopulation.txt","r") 
    pop_list = [line.rstrip() for line in file] #Creating a list for the population data without spaces.
    years = [] #Creating a list for the years to match the index with the population data.
    for element in range(1950,1991): #Adding years
        years.append(element)
    inc_list = [] #Creating a list for the population increase data
    counterA = 1 
    counterB = 0
    while counterA < len(pop_list):
        val = int(pop_list[counterA]) - int(pop_list[counterB])
        counterA += 1
        counterB += 1
        inc_list.append(val)
    print("The year with the greatest increase in population was", years[inc_list.index(max(inc_list))+1])
    print("The year with the smallest increase in population was", years[inc_list.index(min(inc_list))+1])
except FileNotFoundError:
    print("File not found!")
except IndexError:
    print("Index Erro!")