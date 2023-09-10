# Convert the list below from Celsius to Farhenheit, using the map function with a lambda...

# Output: [('Nashua', 89.6), ('Boston', 53.6), ('Los Angelos', 111.2), ('Miami', 84.2)] 

# F = (9/5)*C + 32
# places = [('Nashua',32),("Boston",12),("Los Angelos",44),("Miami",29)]
# converted_temp=list(map(lambda num: (num*9/5) + 32,[3,12,44,29,]))
# print(converted_temp)

# print(places)


# print(places[0][0])


# new_lst=[]

# for city in places:
#     new_lst.append(city[0])
# print(new_lst)


# fer_temp=[]
# for i in range(len(new_lst)):
#     fer_temp.append((new_lst[i],converted_temp[i]))
# print(fer_temp)














lst=[('Nashua', 32), ('Boston',12), ('Los Angelos', 44), ('Miami', 29)]


def sel_fer(anything):
    #### im making a list of all the temps from the list of tuples converted to f
    celcius_temp=[]
    for city, temp in anything:
        celcius_temp.append(temp)
    converted_temp=list(map(lambda num: (num*9/5) + 32,celcius_temp))
    
    ###### im creating a new list of of just the citys from list of tuples
    new_lst=[]
    for city in anything:
        new_lst.append(city[0])
    

    ##### im bringing together my newley created list of cities and  converted temps to make a list of tuples like i recieved 
    # fer_temp=[]
    # for i in range(len(new_lst)):
    #     fer_temp.append((new_lst[i],converted_temp[i]))
    

    ########## i am returning my newly created list of tuples to whoever called them out im zipping together two list to return 
    return list(zip(new_lst,converted_temp))


#### i am displaying the return of my sel_fer function when its fed a list of tuples
print(sel_fer(lst))