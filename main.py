from threading import Thread
from functools import reduce, wraps

mawad = [('fr', 2), ('fl', 3)] #, ('mt', 5), ('sex', 2), ('asd', 3)]
awkat = []
days = ['thnin', 'thlath', 'irb3a', '5mis', 'jim3a', 'sibt']
for d in range(6):
    awkat.append(days[d] + ' 8->9')
    awkat.append(days[d] + ' 9->10')
    awkat.append(days[d] + ' 10->11')
    awkat.append(days[d] + ' 11->12')

    awkat.append(days[d] + ' 14->15')
    awkat.append(days[d] + ' 15->16')
    awkat.append(days[d] + ' 16->17')
    awkat.append(days[d] + ' 17->18')

def generate(scheduleSoFar, availableTimes, subjsLeft): # glabetha english mani faddit mil 3arbi
    if len(subjsLeft) == 0: # no mo shit
        possib = map(lambda t: t + ': irta7', availableTimes)
        return [list(possib)]

    requiredTime = reduce(lambda a, t: a + t[1], subjsLeft, 0)
    if requiredTime > len(availableTimes): # fail state
        return None

    possibs = []
    for i, (s, t) in enumerate(subjsLeft):
        if not selection(scheduleSoFar, s, availableTimes[0]):
            continue

        newSubjsLeft = subjsLeft[:i] + ([(s, t-1)] if t > 1 else [])+ subjsLeft[i+1:]
        prefix = availableTimes[0] + ': ' + s
        childPossibs = list(filter(lambda p: p != None, generate(scheduleSoFar + prefix, availableTimes[1:], newSubjsLeft)))

        for p in childPossibs:
            possibs.append([prefix] + p)

    if selection(scheduleSoFar, 'irta7', availableTimes[0]):
        prefix = availableTimes[0] + ': irta7'
        childPossibs = list(filter(lambda p: p != None, generate(scheduleSoFar + prefix, availableTimes[1:], subjsLeft)))

        for p in childPossibs:
            possibs.append([prefix] + p)

    
    if len(possibs) == 0:
        return None
    return possibs

def selection(schedule, candidat, proposedTime): # This shall be where the fancyness lies
    if schedule == '':
        return True
    return True

def timeout(timeout): # atha copy paste 5ater windows kalb kbiir. ya3mel barka timeout lil generation kan tchid akthir millazem
    def deco(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            res = [Exception('function [%s] timeout [%s seconds] exceeded!' % (func.__name__, timeout))]
            def newFunc():
                try:
                    res[0] = func(*args, **kwargs)
                except Exception as e:
                    res[0] = e
            t = Thread(target=newFunc)
            t.daemon = True
            try:
                t.start()
                t.join(timeout)
            except Exception as je:
                print ('error starting thread')
                raise je
            ret = res[0]
            if isinstance(ret, BaseException):
                raise ret
            return ret
        return wrapper
    return deco

f = timeout(10)(generate)
try:
    print(f('', awkat, mawad))
except:
    print('generation took too long, try tweaking selection function')
