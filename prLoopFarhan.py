# ------------------------------------ PR ------------------------------------

# SOAL 1
z = ''
for i in range(0,5):
    for j in range(0,5-i):
        z += ' * '
    z += '\n'
print(z)

# SOAL 2
z = ''
for i in range(0,5):
    for j in range(0,5-i):
        z += ' * '
    z += '\n'
for i in range(0,5):
    for j in range(0,i+1):
        z += ' * '
    z += '\n'
print(z)

# SOAL 3
z = ''
for i in range(0,19,2):
    for j in range(0,19-i):
        z += ' '
    for k in range(0,i+1):
        z += ' *'
    z += '\n'
print(z)

# SOAL 4
z = ''
for i in range(0,19,2):
    for j in range(0,i+1):
        z += ' '
    for k in range(0,19-i):
        z += ' *'
    z += '\n'
print(z)

# SOAL 5
z = ''
for i in range(0,9,2):
    for j in range(0,9-i):
        z += ' '
    for k in range(0,i+1):
        z += ' *'
    z += '\n'
for i in range(0,9,2):
    for j in range(0,i+1):
        z += ' '
    for k in range(0,9-i):
        z += ' *'
    z += '\n'
print(z)