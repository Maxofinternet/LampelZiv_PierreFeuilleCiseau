import random

CORES = {1: 'Pierre',
         2: 'Feuille',
         3: 'Ciseau',}
TOWIN = {1:2,
         2:3,
         3:1}
TOULOUSE = {1:3,
            2:1,
            3:2}

scorehumain = 0 
scoreskynet = 0

round = 0
lastcomplexity = 1
memory = []

def lempel_ziv_complexity(sequence):
    sub_strings = {}
    n = len(sequence)

    ind = 0
    inc = 1
    while True:
        if ind + inc > len(sequence):
            break
        sub_str = sequence[ind : ind + inc]
        if sub_str in sub_strings:
            inc += 1
            sub_strings[sub_str] += 1
        else:
            ind += inc
            inc = 1
            sub_strings[sub_str] = 1
    return len(sub_strings), sub_strings

def skynet(observation):
    global memory, lastcomplexity
    MOVES = {}
    memory.append(observation)
    if round == 0 : 
      action = random.choice([1,2,3])
    else :
      for i in range(0,3) :
        MOVES[i] = lempel_ziv_complexity(str(memory).replace("[\\[\\]]", "").replace(",", " ") + str(i))[0]
      maxentropy = max(list(MOVES.values()))
      complexity = lempel_ziv_complexity(str(memory).replace("[\\[\\]]", "").replace(",", " ") + str(observation))[0]
      if complexity < maxentropy :
        action = TOULOUSE[observation]
      else : 
        action = TOWIN[observation]
      lastcomplexity = complexity 
    return action

def jouons () :
  global round, scorehumain, scoreskynet
  val = input("Pour jouer Pierre : 1, Feuille : 2, Ciseau : 3  ") 
  while val not in ['1','2','3'] :
    val = input("Vous devez entrer un chiffre correspondant a  une option  telle que Pierre : 1, Feuille : 2, Ciseau : 3  ")
    if val in ['1','2','3'] :
      break
  val = int(val)
  print('vous avez joue '+CORES[val])
  reponse = skynet(val)
  print('Skynet joue ' + CORES[reponse])
  if reponse == TOWIN[val] : 
    round += 1
    scorehumain += 1 
    print ('Victoire')
  elif reponse == TOULOUSE[val] : 
    round += 1
    scoreskynet += 1 
    print ('Defaite')
  else :
    round += 1
    print ('Egalite')
3


while round < 25 :
  jouons()
