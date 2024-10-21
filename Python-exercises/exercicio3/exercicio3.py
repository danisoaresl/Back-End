# Faça um programa que peça a quqantidade de quilômetros, transforme em metros, centímetros e milímetros.


quilometros = float(input("Digite a quantidade de quilômetros: "))

metros = quilometros * 1000
centimetros = quilometros * 100000
milimetros = quilometros * 1000000

print(f"{quilometros} quilômetros equivalem a:")
print(f"{metros} metros.")
print(f"{centimetros} centímetros.")
print(f"{milimetros} milímetros.")

