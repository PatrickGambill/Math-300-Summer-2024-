def p1(problem1):
    cases = [0, 2, 4, 6, 8, 10]
    tcases = [0, 15, 54768, 8997203251306077939, 6552848481417445081192528320741544679280209591555622764519201089735020258588, 1843828418200484015817458697832759970765190919695865329180001673512292967320150773365209751811566449940856627288502075161094047434138383679593449914431116587293202124562616074089582632336072470304504501452116053087503366087318707138518850433393600070789872466939452054932765483220452037054476326924720471]
    
    for i in range(len(cases)):
        if problem1(cases[i]) == tcases[i]:
            print(f"Test case {i+1} was successful.")
        else:
            print(f"Test case {i+1} was unsuccessful.")
    return

def p2(problem2):
    cases = [[1,[2323,1,232,[],[[1,2]]]],[],[1,2,3,[3],[4,[5,[[[]]]]]], [1,[2,[3,[4,[5,6,[7]]]]],['sta','qwe',['qwe','qwed']],[[[1,[]]]]],1,'cat']
    tcases = [5, 1, 7, 12, 0, 0]
    
    for i in range(len(cases)):
        if problem2(cases[i]) == tcases[i]:
            print(f"Test case {i+1} was successful.")
        else:
            print(f"Test case {i+1} was unsuccessful.")
    return
def p4(problem4):

    deck = ['2c', '2d', '2h', '2s', '3c', '3d', '3h', '3s', '4c', '4d', '4h', '4s', '5c', '5d', '5h', '5s', '6c', '6d', '6h', '6s', '7c', '7d', '7h', '7s', '8c', '8d', '8h', '8s', '9c', '9d', '9h', '9s', 'ac', 'ad', 'ah', 'as', 'jc', 'jd', 'jh', 'js', 'kc', 'kd', 'kh', 'ks', 'qc', 'qd', 'qh', 'qs', 'tc', 'td', 'th', 'ts']
    
    if sorted(problem4()) == deck:
        print("This is correct.")
    else:
        print("This is incorrect.")
    return
def b1():
    
    samplemeans = [0.284046, 0.287311]
    for i in range(2):
        print(f"Scenario {i+1} has an approximate proportion of {samplemeans[i]}")
    return 
def b2():
    
    samplemeans = [20.326892, 20.367076]
    for i in range(2):
        print(f"Scenario {i+1} has an approximate proportion of {samplemeans[i]}")
    return 