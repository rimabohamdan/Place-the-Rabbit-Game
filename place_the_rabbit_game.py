print("Welcome to Place the Rabbit 🐰")
bord = [['🌿', '🌿', '🌿'], ['🌿', '🌿', '🌿'], ['🌿', '🌿', '🌿']]
print(f'{bord[0]}\n{bord[1]}\n{bord[2]}')
print("\nWhere should the Rabbit go ? 🐇")
position = input('Please choose a row and a column...')
row = int(position[0])
column = int(position[1])
bord[row-1][column-1] = '🐇'
print('\n Success...\n')
print(f'{bord[0]}\n{bord[1]}\n{bord[2]}')
