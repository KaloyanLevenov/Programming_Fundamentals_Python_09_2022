ommand = input()
while command != 'end':
  reversed_word = command[::-1]
  print( F"{command} = {reversed_word}")
  command = input()