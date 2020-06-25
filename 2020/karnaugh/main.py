import re

class KMap:
  def __init__(_, vars, terms):
    vars = vars[::-1]
    _.vars = vars
    _.table = [0] * (2 ** len(vars))

    for term in terms:
      for j in range(2 ** len(vars)):
        ok = True
        for k in range(len(vars)):
          if vars[k] not in term: continue
          if term[vars[k]] == 1:
            if ((2 ** k) & j == 0):
              ok = False
              break
          else:
            if ((2 ** k) & j != 0):
              ok = False
              break

        if (ok):
          _.table[j] = 1

  def draw3(_):
    for i in [0, 1]:
      for j in [0, 1, 3, 2]:
        print(_.table[i*4+j], end=" ")
      print()

  def draw4(_):
    for i in [0, 1, 3, 2]:
      for j in [0, 1, 3, 2]:
        print(_.table[i*4+j], end=" ")
      print()

  def draw(_):
    if (len(_.vars) == 3): _.draw3()
    if (len(_.vars) == 4): _.draw4()


def parseterm(s, v):
  term = {}
  lastc = None
  for c in s:
    if c == "'":
      term[lastc] = -1
    else:
      term[c] = 1
      lastc = c
      v.add(c)

  return term

def parseexp(s):
  t = s.split('+')

  terms = []
  vars = set()
  for term in t:
    terms.append(parseterm(term, vars))

  vars = sorted(list(vars))
  return KMap(vars, terms)

def parsemin(s):
  vars = list(range(int(s[0])))
  s = s[2:].split(',')
  terms = []
  for t in s:
    term = {}
    for i in vars:
      if int(t) & (2 ** (len(vars)-i-1)): term[i] = 1
      else: term[i] = -1
    terms.append(term)

  return KMap(vars, terms)

def parse(s):
  if s.count(',') > 0:
    return parsemin(s)
  else:
    return parseexp(s)

def main():
  kmap = parse(input())
  kmap.draw()

main()
