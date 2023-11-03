"""
Uzrakstiet programmu definējot klasi,lai veselu skaitli pārveidotu par romiešu ciparu.

1) Kādus ciparus Jūs ziniet? Arābu cipari                      21
2) Kādus romiešu ciparus ziniet? I, V, C, M, X, L, D           XXI
3) Kas ir klase? Klase ir programmēšanas struktūra, kas var definēt datu uzvedību un metodes
4) Klase sastāv no konstruktora/desturktora un metodēm (Iekšējām funkcijām).
Iekavās raksta parametrus, kas ir klases mainīgie.
Konstruktors parāda kādi iekšējie mainīgie darbosies.
5) Kādas datu struktūras ziniet?
     -list(saraksts) a=""
     -arry(masīvs)
     -dict(vārdnīca) a={}   a=dict{}
Vārdnīcu var saprast kā tabulu ar 2 kolonām
Kolonai nav nosaukumu, viena kolona ir atslēga.
"""
class AAA:
    # jādefinē konstruktors
    def __init__(self):
        self.roma_sk={
            1:'I',
            4:'IV',
            5:'V',
            9: 'IX', 
            10: 'X', 
            40: 'XL', 
            50: 'L', 
            90: 'XC', 
            100: 'C', 
            400: 'CD', 
            500: 'D', 
            900: 'CM', 
            1000: 'M'
        }
    # definē nepieciešamās metodes
    def to_roman(self, num): 
        result = "" 
        for value, numeral in sorted(self.roma_sk.items(), key=lambda x: x[0], reverse=True): 
            while num >= value: 
                result += numeral 
                num -= value  #num=num-value
        return result
    
# piemērs
skaitlis=21
# definē objektu
kk=AAA()
#jaunajam objektam jāizsauc klases metodes
romieshu=kk.to_roman(skaitlis)

# noformēt izdruku
print(f"{skaitlis} ar romiešu cipariem ir {romieshu}.")