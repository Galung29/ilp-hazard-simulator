# Implementasi WAR (Write-After-Read)
# I1 membaca R1, kemudian I2 menulis ke R1

I1 = "R1 = 10"  # Misalkan I1 membaca atau menggunakan nilai awal R1
I2 = "R1 = R2 + 5" # I2 menulis ulang nilai ke R1

# Simulasi nilai
R2 = 50
R1 = 10         # Dibaca oleh instruksi sebelumnya
R1 = R2 + 90     # Menimpa R1 (terjadi WAR hazard)

print("WAR:")
print("R1 =", R1)
print("R2 =", R2)
