def p2(problem2):
    
    a1,a2,a3 = problem2()
    
    c1 = (6**2 - 4**3 + 7*6*5)/(42**2)
    c2 = (78**76)/(45**54)
    c3 = 1444**(1/37)-19**(13/4) + (38)**(59+121)
    
    if a1 == c1:
        print("Answer 1 is correct")
    else:
        print("Answer 1 is incorrect")
    
    if a2 == c2:
        print("Answer 2 is correct")
    else:
        print("Answer 2 is incorrect")
    
    if a3 == c3:
        print("Answer 3 is correct")
    else:
        print("Answer 3 is incorrect")
    
    return

def p3(problem3):
    
    a1,a2,a3 = problem3()
    
    if not a1:
        print("Answer 1 is correct")
    else:
        print("Answer 1 is incorrect")
    
    if a2:
        print("Answer 2 is correct")
    else:
        print("Answer 2 is incorrect")
    
    if a3:
        print("Answer 3 is correct")
    else:
        print("Answer 3 is incorrect")

    return

def p4(problem4):
    
    cases = ['catto', 'OrangegnarO', 'asds a', 'qwertvf', 'palindromemordnilap', 'tacocaT', 'amanaplanacanalpanama', '12344321']
    
    tcases = [False, True, False, False, True, False, True, True]
    
    for i in range(len(cases)):
        
        y = problem4(cases[i])
        
        if y == tcases[i]:
            
            print(f"Test Case {i+1} was successful")
        
        else:
            
            print(f"Test Case {i+1} was unsuccessful")
    
    return

def p5(problem5):
    
    cases = [[1,6,3,765,4,6,7,232323,7,445,6556,3434,434342134,234,98],[66565656564,5656565,656565656,655656345,3632453452,2342342,234234,234234,222],[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],[1,1,1,1,1,1,1,1,1,1,6,5,6,4,5,5,6,7,8,9,7,6,6,66,66,66,66,66,666],[123123,123123,123123,13123,123123123,123,123123123]]
    
    tcases = [11475, 599090909076, 16, 29, 861861861]
    
    for i in range(len(cases)):
        
        y = problem5(cases[i])
        
        if y == tcases[i]:
            
            print(f"Test Case {i+1} was successful")
        
        else:
            
            print(f"Test Case {i+1} was unsuccessful")
    
    return
    
def p6(problem6):
    
    cases = [['walrus','cat','dog','seal','frog'], ['green','red','blue','yellow','silver'],['Mary','Mat','Mac','Martin','Makayla'],['math','biology','geology','physics','english'],['tea','coffee','water','soda','juice']]
    
    tcases = [{'walrus': ('a', 'l', 'r', 's', 'u', 'w'), 'cat': ('a', 'c', 't'), 'dog': ('d', 'g', 'o'), 'seal': ('a', 'e', 'l', 's'), 'frog': ('f', 'g', 'o', 'r')}, {'green': ('e', 'e', 'g', 'n', 'r'), 'red': ('d', 'e', 'r'), 'blue': ('b', 'e', 'l', 'u'), 'yellow': ('e', 'l', 'l', 'o', 'w', 'y'), 'silver': ('e', 'i', 'l', 'r', 's', 'v')}, {'Mary': ('M', 'a', 'r', 'y'), 'Mat': ('M', 'a', 't'), 'Mac': ('M', 'a', 'c'), 'Martin': ('M', 'a', 'i', 'n', 'r', 't'), 'Makayla': ('M', 'a', 'a', 'a', 'k', 'l', 'y')}, {'math': ('a', 'h', 'm', 't'), 'biology': ('b', 'g', 'i', 'l', 'o', 'o', 'y'), 'geology': ('e', 'g', 'g', 'l', 'o', 'o', 'y'), 'physics': ('c', 'h', 'i', 'p', 's', 's', 'y'), 'english': ('e', 'g', 'h', 'i', 'l', 'n', 's')}, {'tea': ('a', 'e', 't'), 'coffee': ('c', 'e', 'e', 'f', 'f', 'o'), 'water': ('a', 'e', 'r', 't', 'w'), 'soda': ('a', 'd', 'o', 's'), 'juice': ('c', 'e', 'i', 'j', 'u')}]
        
    for i in range(len(cases)):
        
        y = problem6(cases[i])
        
        if y == tcases[i]:
            
            print(f"Test Case {i+1} was successful")
        
        else:
            
            print(f"Test Case {i+1} was unsuccessful")
    
    return

def b1(bonusproblem1):
    
    cases = ['catto', 'OrangegnarO', 'asds a', 'qwertvf', 'palindromemordnilap', 'tacocaT', 'amana pla nac analpanama', '12344321']
    
    tcases = [False, True, True, False, True, True, True, True]
    
    for i in range(len(cases)):
        
        y = bonusproblem1(cases[i])
        
        if y == tcases[i]:
            
            print(f"Test Case {i+1} was successful")
        
        else:
            
            print(f"Test Case {i+1} was unsuccessful")
            
    return

def b2(bonusproblem2):
    
    cases = [[1,6,3,765,4,6,7,232323,7,445,6556,3434,434342134,234,98],[66565656564,5656565,656565656,655656345,3632453452,2342342,234234,234234,222],[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],[1,1,1,1,1,1,1,1,1,1,6,5,6,4,5,5,6,7,8,9,7,6,6,66,66,66,66,66,666],[123123,123123,123123,13123,123123123,123,123123123]]
    
    tcases = [6557, 656565658, 3, 67, 123123]
    
    for i in range(len(cases)):
        
        y = bonusproblem2(cases[i])
        
        if y == tcases[i]:
            
            print(f"Test Case {i+1} was successful")
        
        else:
            
            print(f"Test Case {i+1} was unsuccessful")
    
    return