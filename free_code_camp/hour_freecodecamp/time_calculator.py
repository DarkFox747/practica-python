def add_time(start, duration,weak=False):
  time = start.split(' ')
  entrada_hora = int (time[0].split(':')[0])
  entrada_min = int (time[0].split(':')[1])
  momento = time[1]
  string =''

  if momento == 'PM':
    entrada_hora +=12
  add_hora = int(duration.split(':')[0])
  add_min = int(duration.split(':')[1])

  #minutos:
  total_min = ''
  a = entrada_min + add_min
  if a >= 60:
    b = int(a/60)
    add_hora += b
    if a-b*60 <10:
        total_min +='0'
        total_min += str(int(a-(b*60)))
    else:
        total_min += str(int(a-(b*60)))
  else:
      if a <10:
          total_min += '0'
          total_min += str(a)
      else:
          total_min = str(a)

  #Horas:
  total_horas = ''
  dias =0
  c= entrada_hora + add_hora
  momento2 = ''
  if c >=25:
    d = int(c/24)
    dias = d
    if c-d*24 >= 12:
        if c-d*24 >= 13:            
            total_horas = str(c-d*24-12)
            momento2 = 'PM'
        else:
            total_horas = str(c-d*24)
            momento2 = 'AM'
    elif c-d*24 ==0:
      total_horas = str(12)
      momento2 = 'AM'
    else:
      total_horas = str(c-d*24)
      momento2 = 'AM'
  else:
    if c >=12:
        if c >=13:
            total_horas = str(c-12)
            momento2 = 'PM'
        else:
            total_horas = str(c)
            momento2 = 'PM'
    else:
      total_horas = str(c)
      momento2 = 'AM'

  #dias:
  total_dias=''
  if dias == 1:
    total_dias = '(next day)'
  elif dias >1:
    total_dias = '({} days later)'.format(str(dias))

  lst = ["Sunday","Monday","Tuesday","Wednesday","Thursday","Friday","Saturday"]
  lst2 = ["sunday","monday","tuesday","wednesday","thursday","friday","saturday"]  
  day_of =''
  if weak:
    weak = weak.lower()
    indexz= lst2.index(weak) + dias 
    if indexz > 6:
      e = indexz%7
      day_of = lst[e]
    else:
        day_of = lst[indexz]
    if dias >=1:
      string = total_horas+ ':'+total_min + ' '+momento2+ ', '+ day_of + ' ' + total_dias
      return string
    else:
      string = total_horas+ ':'+total_min + ' '+momento2+ ', '+ day_of
      return string
  else:
    if dias >= 1:
      string = total_horas+ ':'+total_min + ' '+momento2+ ' '+ total_dias
      return string
    else:
      string = total_horas+ ':'+total_min + ' '+momento2
      return string



print(add_time("8:16 PM", "466:02", "tuesday"))

