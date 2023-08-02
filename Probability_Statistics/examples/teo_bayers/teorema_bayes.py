#from tokenize import Double
print ("TEOREMA DE BAYES:")
print ("FÓRMULA:")
print ("P(Ak|B) =       P(B|Ak) x P(Ak)\n          --------------------------\n       somat.(até n) de P(B|Ai) x P(Ai)")
pbak = float(input("Digite o P(B|Ak): "))
pak = float(input("Digite o P(Ak): "))
n = int(input("Digite a quantidade de somas de P(B|Ai) x P(Ai): "))

i = 1
soma = 0
while i<=n:
    mais0 = float(input("Digite o P(B|A%d): " %i))
    mais1 = float(input("Digite o P(A%d): " %i))
    soma  += (mais0*mais1)
    i+=1

total = ((pbak * pak)/soma)
print("P(Ak/B) =", total)
