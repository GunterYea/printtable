#  get_multtables( [1, 2], 3)   -> {1: [1, 2, 3], 2: [2, 4, 6]} 

def get_multtables(arg1, arg2):   
    output_dict = {}
    for i in range(len(arg1)):
        work_list=[]    
        for y in range(1, arg2+1):
            work_list.append(arg1[i]*y)
        x = arg1[i]
        if x not in output_dict.keys():
            output_dict[x] = work_list
    print(output_dict)

#get_multtables([10,3], 5)


    



# get_powertable(2, 3) -> [1, 4, 9]

def get_powertable(arg1, arg2):
    output_list = []
    for i in range(1, arg2+1):
        output_list.append(pow(i, arg1))
    print(output_list)

#get_powertable(2,3)




# get_powertables([2, 3], 4) -> {2: [1, 4, 9, 16], 3: [1, 8, 27, 64]}

def get_powertables(arg1, arg2):   
    output_dict = {}
    for i in range(len(arg1)):
        work_list=[]    
        for y in range(1, arg2+1):
            work_list.append(pow(y, arg1[i]))
        x = arg1[i]
        if x not in output_dict.keys():
            output_dict[x] = work_list
    print(output_dict)

#get_powertables([2,3], 4)
