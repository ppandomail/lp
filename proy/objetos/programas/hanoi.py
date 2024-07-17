def hanoi(n, inc='1', temp='2', fin='3'):
  if n > 0:
      hanoi(n-1, inc, fin, temp)
      print('se mueve de torre', inc, 'a torre', fin)
      hanoi(n-1, temp, inc, fin)

hanoi(5)