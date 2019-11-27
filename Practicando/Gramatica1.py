# Crear una gramatica
import nltk
from nltk import CFG
from nltk.parse.generate import generate
#1) <frase>::= <sujeto><predicado>
#2) <sujeto>::= juan | pedro | maría | salgado
#3) <predicado>::= <verbo transitivo><objeto directo>
#4) <predicado>::= <verbo intransitivo>
#5) <verbo transitivo>::= ama | lava | peina | adora
#6) <objeto directo>::= paula | antonio | sultán
#7) <verbo intransitivo>::= corre | salta | camina

Gramtica1 = CFG.fromstring("""

F -> SU P
SU -> 'juan' | 'pedro' | 'maria' | 'salgado'
P -> VT OD
P -> VI
VT -> 'ama' | 'lava' | 'peina' | 'adora'
OD -> 'paula' | 'antonio' | 'sultan'
VI -> 'corre' | 'salta' | 'camina'
""")

print('La gramatica:', Gramtica1)
print('Inicio =>', Gramtica1.start())
print('Productiones =>')

# Mostrar las producciones de la gramatica
print(Gramtica1.productions())

print('Cobertura de palabras ingresadas a la gramatica:')

try:
    #maría ama antonio
    Gramtica1.check_coverage(['maria', 'ama', 'antonio'])
    print("Todas las palabras estan cubiertas")
except:
    print("Error")

#try:
#    print(grammar.check_coverage(['a','toy']))
#except:
 #   print("Algunas palabras no estan cubiertas")

for sentence in generate(Gramtica1, n=50):
    print(' '.join(sentence))

Frese = ['maria', 'ama', 'antonio']
parser = nltk.ChartParser(Gramtica1)
for Arbol in parser.parse(Frese):
    print(Arbol)

