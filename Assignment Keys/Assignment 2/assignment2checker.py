def p1(problem1):
    
    l = [True,False]
    cases = [(a,b,c,d,e,f,g,h) for a in l for b in l for c in l for d in l for e in l for f in l for g in l for h in l]
    
    tcases = [True, False, True, False, True, False, False, False, True, False, True, False, True, False, False, False, True, False, True, False, True, False, False, False, True, False, True, False, True, False, False, False, True, False, True, False, True, False, False, False, True, False, True, False, True, False, False, False, True, False, True, False, True, False, False, False, False, False, False, False, False, False, False, False, True, False, True, False, True, False, False, False, True, False, True, False, True, False, False, False, True, False, True, False, True, False, False, False, True, False, True, False, True, False, False, False, True, False, True, False, True, False, False, False, True, False, True, False, True, False, False, False, True, False, True, False, True, False, False, False, False, False, False, False, False, False, False, False, True, False, True, False, True, False, False, False, True, False, True, False, True, False, False, False, True, False, True, False, True, False, False, False, True, False, True, False, True, False, False, False, True, False, True, False, True, False, False, False, True, False, True, False, True, False, False, False, True, False, True, False, True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False]

    for i in range(len(cases)):
        case = cases[i]
        checked = tcases[i]
        if not problem1(case) == checked:
            print(f"Your function did not return the correct output for the {case} input.")
            return
        else:
            print("All test cases successful")
            return
def p2(problem2):
    cases = [1,15,34,543,122,120]
    tcases = [1, 2027025, 46620662575398912000, 127423670254689222306958579516236955229806080965509644850318322971361496757823908686411552755405323997538491332339663018676750595205252233243736032809192098994021513519593022984059983470391306880363164793757618371923479761365883958028498591419943020712206611956922397557855362556822936432938772905401976661961632572379080183654317912258971650366388157149848513158565275599973488164060577607086810008650368692474404663727511970589184758510138550359343025596405765429040234885464596922822631517675110603165502854622968977921129078900393560612947813680685263537401009908798769260572809739785749005847037551575340330600738525390625, 1170400287783990408496816673615657306592263772998223567356419491825904038249635041719091200000000000000, 9593444981835986954891939947669322185182489942608389896364094195294295395488811817369600000000000000]
    
    for i in range(len(cases)):
        if problem2(cases[i]) == tcases[i]:
            print(f"Test case {i+1} was successful.")
        else:
            print(f"Test case {i+1} was unsuccessful.")
    return
def p3(problem3):
    cases = [([2,3,5],33),([1,2],330),([7,11],1001),([3,5,10],205),([3,4,5],2),([5,3,7],91)]
    tcases = [410, 54615, 111111, 9978, 0, 2257]
    
    for i in range(len(cases)):
        if problem3(cases[i][0],cases[i][1]) == tcases[i]:
            print(f"Test case {i+1} was successful.")
        else:
            print(f"Test case {i+1} was unsuccessful.")
    return
def p4(problem4):
    tcase = set([(40, 399, 401), (56, 390, 394), (105, 360, 375), (120, 350, 370), (140, 336, 364), (168, 315, 357), (210, 280, 350), (240, 252, 348)])
    studentset = set(problem4())
    
    fails = False
    
    dif1 = tcase - studentset
    dif2 = studentset - tcase
    for triple in studentset:
        a = triple[0]
        b = triple[1]
        c = triple[2]
        
        if a>=b or a>=c:
            print(f"The first number in the triple should be smaller than the other numbers. In {triple}, this is not the case.")
            fails = True
        elif b>=c:
            print(f"The last element of the tuple should be the largest. In {triple}, this is not the case.")
            fails = True
    if not len(dif1) == 0 :
        print(f"Your code includes the triples {dif1}. These do not satisfy the considitions laid out in the problem.")
        fails = True
    if not len(dif2) == 0:
        print(f"You are missing some of the tuples.")
        fails = True
    
    if not fails:
        print("Your output is correct.")
    return
def p5(problem5):
    cases = [[1,2,3,4,5],[12,543,123,0,0,3],[34,0,0,43,2,32],[0,0,0],[-1,3-65,0,2323,56656,2323],[1234,31,4.3,434.4,3434.4,3434,5656,2323]]
    tcases = [[2, 6, 12, 20], [543, 246, 0, 0, 15], [0, 0, 129, 8, 160], [0, 0], [-62, 0, 6969, 226624, 11615], [31, 8.6, 1303.1999999999998, 13737.6, 17170, 33936, 16261]]
    
    for i in range(len(cases)):
        if problem5(cases[i]) == tcases[i]:
            print(f"Test case {i+1} was successful.")
        else:
            print(f"Test case {i+1} was unsuccessful.")
    return
def p6(problem6):
    cases = [([1,3,65,456],0),([4,0,0,1],5),([4,234,6,5.6,123,3],3.141),([2323,2,454,232],12),([323,323,252,23.5,0,232,1],0.2),([1231,3,2,2323,1,0,3],4)]
    tcases = [1, 129, 13861.199392195158, 468619, 397.942304, 162491]
    
    for i in range(len(cases)):
        if problem6(cases[i][0],cases[i][1]) == tcases[i]:
            print(f"Test case {i+1} was successful.")
        else:
            print(f"Test case {i+1} was unsuccessful.")
    return
def b1(bonusproblem1):
    cases = [([1,43,123,3],[0,1]),([3],[1]),([0,-1,0,1,0,1],[-2323,3232,1,32]),([i for i in range(50)],[i for i in range(25,51)]), ([0,0,0,1],[1,1,1,1,1]),([3.4,3.2,0.12,23.3,123.1],[0.2,0.2,-0.2,0.3,0.4])]
    tcases = [[0, 1, 43, 123, 3], [3], [0, 2323, -3232, -2324, 3200, -2322, 3264, 1, 32], [0, 25, 76, 154, 260, 395, 560, 756, 984, 1245, 1540, 1870, 2236, 2639, 3080, 3560, 4080, 4641, 5244, 5890, 6580, 7315, 8096, 8924, 9800, 10725, 11700, 12675, 13650, 14625, 15600, 16575, 17550, 18525, 19500, 20475, 21450, 22425, 23400, 24375, 25350, 26325, 27300, 28275, 29250, 30225, 31200, 32175, 33150, 34125, 33850, 33500, 33074, 32571, 31990, 31330, 30590, 29769, 28866, 27880, 26810, 25655, 24414, 23086, 21670, 20165, 18570, 16884, 15106, 13235, 11270, 9210, 7054, 4801, 2450], [0, 0, 0, 1, 1, 1, 1, 1], [0.68, 1.3200000000000003, -0.015999999999999924, 5.064, 31.576, 21.276, -17.582, 46.25, 49.24]]
    
    for i in range(len(cases)):
        f,g = cases[i]
        if bonusproblem1(f,g) == tcases[i]:
            print(f"Test case {i+1} was successful.")
        else:
            print(f"Test case {i+1} was unsuccessful.")
    return
def b2(bonusproblem2):
    cases = [([2,5,7,14,21,22,22,15], [1,1,2,3]),([1,2,1],[1,1]),([1,1],[1,2,3]),([12,232,433,123,0.4,1],[232,123,32]),([0,1,0,1,0,1,0,2],[1,0,1,0,2]),([7],[14])]
    tcases = [([1.0, 2.0, 3.0, 4.0, 5.0], [1.0, 2.0, 0.0]), ([1.0, 1.0], [0.0]), ([0], [1, 1]), ([-1.1820707321166992, 4.030841064453125, -0.1076171875, 0.03125], [286.2404098510742, -557.7604269027711]), ([0.0, 0.0, 0.0, 1.0], [0.0, 1.0, 0.0, 0.0]), ([0.5], [0])]
    
    for i in range(len(cases)):
        case = cases[i]
        f,g = case[0],case[1]
        
        if bonusproblem2(f,g) == tcases[i]:
            print(f"Test case {i+1} was successful.")
        else:
            print(f"Test case {i+1} was unsuccessful.")
    return