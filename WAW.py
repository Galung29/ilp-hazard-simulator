
  # Implementasi WAW (Write-After-Write)
# I1 menulis R1, kemudian I2 juga menulis ke R1

I1 = "R1 = 10"       # Instruksi pertama menulis ke R1
I2 = "R1 = R2 + 5"   # Instruksi kedua menulis ke R1

# Simulasi nilai
R2 = 50
R1 = 0

R1 = 10       # I1 menulis nilai 10 ke R1
R1 = R2 + 5   # I2 menulis nilai 55 ke R1

print("WAW:")
print("R1 =", R1)
print("R2 =", R2)
