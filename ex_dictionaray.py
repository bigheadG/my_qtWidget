Dict = {}
print("Initial nested dictionary:-")
print(Dict)
gate = ['g0','g1']

#(2)check key in Dictionary if not initial dictionary
if Dict.get(102) == None:
    Dict[102] = {}

#(3)initial gate for nest key
for i in gate:
    Dict[102][i] = ['N','idle',30]
print("----first Dict------")
print(Dict)
  
#(4) update elements one at a time 
Dict[102]['g0'] = ['A','idle',5]
Dict[102]['g1'] = ['B','iAs',6]
print("\nupdate dictionary Dict")
print(Dict)
  
# Adding whole dictionary
Dict[103] = {}
Dict[103]['g0'] = ['A','idle',7]
Dict[103]['g1'] = ['B','As',8]
print(Dict)

print("----count down data and minus -1 for data item----")
for key, value in list(Dict.items()):     
    for ikey, ival in list(Dict[key].items()):
        #x = Dict[key][ikey][2]
        Dict[key][ikey][2] =  Dict[key][ikey][2] - 1
        print(Dict[key][ikey][2])
print(Dict)

print("----check key:g2 is exist or not ----if not add")
if Dict[103].get('g2') == None:
    print("add g2 in Dict")
    Dict[103]['g2'] = ['B','iAs',6]

print(Dict)    
