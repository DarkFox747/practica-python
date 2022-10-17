import re

def arithmetic_arranger(problems, solve = False):
  if len(problems) > 5 :
    return 'Error: Too many problems.'
  fNum = ''
  sNum = ''
  lines =''
  sumN =''
  string = ''
  for problem in problems:
    if (re.search("[^\s0-9.+-]",problem)):
      if (re.search("[/]",problem) or re.search('[*]',problem)):
        return "Error: Operator must be '+' or '-'."
      return 'Error: Numbers must only contain digits.'

    firstN = problem.split(' ')[0]
    operator = problem.split (' ')[1]
    secondN = problem.split(' ')[2]

    if  len(firstN) >=5 or len(secondN)>=5:
      return 'Error: Numbers cannot be more than four digits.'

    sum = ''
    if operator == '+':
      sum = str(int(firstN) + int(secondN))
    elif operator == '-':
      sum = str(int(firstN) - int (secondN))

    lenght = max (len (firstN),len(secondN)) +2
    top = firstN.rjust(lenght)
    bottom = operator + secondN.rjust(lenght -1)
    line = ''
    res = str(sum).rjust(lenght)
    for l in range(lenght):
      line += '-'
    if problem != problems[-1]:
      fNum += top + '    '
      sNum += bottom + '    '
      lines += line + '    '
      sumN += res + '    '
    else:
      fNum += top 
      sNum += bottom 
      lines += line 
      sumN += res 
  if solve:
    string = fNum + '\n' + sNum + '\n' + lines + '\n' + sumN  
  else:
    string = fNum + '\n' + sNum + '\n' + lines
  return string

print(arithmetic_arranger(['32 - 698', '1 - 3801', '45 + 43', '123 + 49', '988 + 40'],True))