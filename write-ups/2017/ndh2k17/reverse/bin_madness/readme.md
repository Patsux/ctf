# [WARGAME NDH 2017] Write-Up - Reverse: bin_madness (100 points)

## Description

Le challenge contenait un fichier texte appelé « bin_madness » avec du
code binaire:

```
10111010100111101000110010000110110111111000100010011110100011001001000111011000
10001011110111111001011010001011110111111100000011011111101100011001000010001000
11011111100111011000110110010110100100011001100011011111100100101001101011011111
10011110110111111001110110011010100110101000110111011111110111101101111111010010
11011111101101111001111010011100100101001001011010001101100111101111001011110101
10011001100100111001111010011000110111111100010111011111100100011001101110010111
11001101100101001100111011001000101000001100100111001101110010111001100111001011
10011110110010101100100011000111110001101001110010011010110011101100110111000110
11000111100110011100101111001001110001101001110010011010110110011101110011001101
11001110110011111100010011011001110111001100110111001110110011111100010011011001
11011100110011011100111011001111110001001101100111011100110011011100111011001111
11000100110110011101110011001101110011101100111111000100110110011101110011001101
11001110110011111100010011011001110111001100110111001110110011111100010011011001
11011100110011101100011111001101110001001101100111011100110001111100101111000111
11001101110001001101100111011100110011011100110111001100110001001101100111011100
11000111110011011100110111001011110001001101100111011100110011101100101111001011
11000100110110011101110011001100110010101100110111000100110110011101110011001101
11001101110011001100010011011001110111001100110011001100110001101100010011011001
11011100110011001100011111001101110001001101100111011100110001111100110111001110
11001001110001001101100111011100110011011100110111001100110001001101100111011100
11001110110010111100111011000100110110011101110011001100110010101100110011000100
11011001110111001100110011000111110011011100010011011001110111001100011111001101
11001010110011111100010011011001110111001100110111001101110011001100010011011001
11011100110001111100110111001011110001101100010011011001110111001100011111001101
11001110110011011100010011011001110111001100011111001101110011101100111011000100
11011001110111001100110011001100110001111100010011011001110111001100110111001110
11001110110001001101100111011100110011011100110111001100110001001101100111011100
11000111110011011100110111001011110001001101100111011100110011101100101111001011
11000100110110011101110011001100110010101100110111000100110110011101110011001101
11001110110010011100010011011001110111001100111011001011110011101100010011011001
11011100110011001100101011001100110001001101100111011100110011011100110111001100
11000100110110011101110011000111110011011100111011001001110001001101100111011100
11001110110010111100101111000100110110011101110011000111110011011100101111000110
11000100110110011101110011001101110011011100110011000100110110011101110011000111
11001101110011101100100011000100110110011101110011001100110001111100110111000100
11011001110111001100011111001101110010101100111111000100110110011101110011001101
11001101110011001100010011011001110111001100110011001010110011001100010011011001
11011100110001111100110111001110110010011100010011011001110111001100111011001011
11001011110001001101100111011100110011001100101011001101110001001101100111011100
11001000110011001100110111000100110110011101110011000111110011011100111011001101
11000100110110011101110011001101110011101100111011000100110110011101110011001101
11001101110011001100010011011001110111001100011111001101110010111100011011000100
11011001110111001100111011001011110011101100010011011001110111001100011111001101
11001101110010111100010011011001110111001100110111001101110011001100010011011001
11011100110011001100011111001101110001001101100111011100110010001100110011001101
11000100110110011101110011001100110001111100110111000100110110011101110011000111
11001101110011101100111011000100110110011101110011000111110011011100111011001001
11000100110110011101110011001101110011111100011011000100110110011101110011001101
11001111110001101100010011011001110111001100110111001101110011001100010011011001
11011100110011101100011011001000110001001101100111011100110011011100111011001111
11000100110110011101110011001101110011101100101111000100
```

Il était accompagné du petit texte suivant:

```
You'd better to start to move your feet To the rockin'est, rock-steady beat Of Madness.
```

## Parti à la recherche d'un binaire imaginaire

Poussé par la catégorie « reverse » du challenge, je me suis dit que le fichier
texte était peut-être le code binaire d'un programme. À l'aide d'un script python,
j'ai converti le format ascii du code en fichier binaire:

```python
import struct
import sys

if (len(sys.argv) < 2):
	print("Please set arguments %%u <file>")
	sys.exit(-1)

f = open(sys.argv[1], 'r')

# Replace the '\n' to remove 80-chars columns
data = f.read().replace("\n", "")

data_str = ""
for i in range(0, len(data) // 8):
	byte = data[i*8:i*8+8]
	data_str = data_str + str(hex(int(byte, 2))) + " "

# Write the output file
f_out = open("out.bin", "wb")
data_list = data_str.split(' ')[:-1]
for i in data_list:
		f_out.write(struct.pack("B", int(i, 16)))

f.close()
f_out.close()
```

En quelques mots, ce script supprime le formatage sur 80 colonnes du
texte (suppression des "\n") et forme les octets en hexa au format texte pour
déboguer rapidement. Enfin, il ouvre un fichier binaire et pack les octets
pour les écrire. Bon, même si j'ai un peu nettoyé le code, il reste moche et
non optimisé, mais au moins il fonctionne. L'avantage du script maison, c'est
de pouvoir manipuler les données par la suite.

```
00000000   BA 9E 8C 86  DF 88 9E 8C  91 D8 8B DF  96 8B DF C0  DF B1 90 88  DF 9D 8D 96  ........................
00000018   91 98 DF 92  9A DF 9E DF  9D 9A 9A 8D  DF DE DF D2  DF B7 9E 9C  94 96 8D 9E  ........................
00000030   F2 F5 99 93  9E 98 DF C5  DF 91 9B 97  CD 94 CE C8  A0 C9 CD CB  99 CB 9E CA  ........................
00000048   C8 C7 C6 9C  9A CE CD C6  C7 99 CB C9  C6 9C 9A D9  DC CD CE CF  C4 D9 DC CD  ........................
00000060   CE CF C4 D9  DC CD CE CF  C4 D9 DC CD  CE CF C4 D9  DC CD CE CF  C4 D9 DC CD  ........................
00000078   CE CF C4 D9  DC CD CE CF  C4 D9 DC CE  C7 CD C4 D9  DC C7 CB C7  CD C4 D9 DC  ........................
00000090   CD CD CC C4  D9 DC C7 CD  CD CB C4 D9  DC CE CB CB  C4 D9 DC CC  CA CD C4 D9  ........................
000000A8   DC CD CD CC  C4 D9 DC CC  CC C6 C4 D9  DC CC C7 CD  C4 D9 DC C7  CD CE C9 C4  ........................
000000C0   D9 DC CD CD  CC C4 D9 DC  CE CB CE C4  D9 DC CC CA  CC C4 D9 DC  CC C7 CD C4  ........................
000000D8   D9 DC C7 CD  CA CF C4 D9  DC CD CD CC  C4 D9 DC C7  CD CB C6 C4  D9 DC C7 CD  ........................
000000F0   CE CD C4 D9  DC C7 CD CE  CE C4 D9 DC  CC CC C7 C4  D9 DC CD CE  CE C4 D9 DC  ........................
00000108   CD CD CC C4  D9 DC C7 CD  CD CB C4 D9  DC CE CB CB  C4 D9 DC CC  CA CD C4 D9  ........................
00000120   DC CD CE C9  C4 D9 DC CE  CB CE C4 D9  DC CC CA CC  C4 D9 DC CD  CD CC C4 D9  ........................
00000138   DC C7 CD CE  C9 C4 D9 DC  CE CB CB C4  D9 DC C7 CD  CB C6 C4 D9  DC CD CD CC  ........................
00000150   C4 D9 DC C7  CD CE C8 C4  D9 DC CC C7  CD C4 D9 DC  C7 CD CA CF  C4 D9 DC CD  ........................
00000168   CD CC C4 D9  DC CC CA CC  C4 D9 DC C7  CD CE C9 C4  D9 DC CE CB  CB C4 D9 DC  ........................
00000180   CC CA CD C4  D9 DC C8 CC  CD C4 D9 DC  C7 CD CE CD  C4 D9 DC CD  CE CE C4 D9  ........................
00000198   DC CD CD CC  C4 D9 DC C7  CD CB C6 C4  D9 DC CE CB  CE C4 D9 DC  C7 CD CD CB  ........................
000001B0   C4 D9 DC CD  CD CC C4 D9  DC CC C7 CD  C4 D9 DC C8  CC CD C4 D9  DC CC C7 CD  ........................
000001C8   C4 D9 DC C7  CD CE CE C4  D9 DC C7 CD  CE C9 C4 D9  DC CD CF C6  C4 D9 DC CD  ........................
000001E0   CF C6 C4 D9  DC CD CD CC  C4 D9 DC CE  C6 C8 C4 D9  DC CD CE CF  C4 D9 DC CD  ........................
000001F8   CE CB C4                                                                      ...
00000210
```

Sans gros mystère, ce n'est pas un ELF ni du code x86. Il n'y a pas de magic particulier,
ni de chaîne visible. Par contre, je suis surpris par la redondance des valeurs et les
MSB à 1. 

Je me suis attardé un peu sur l'indice du challenge. Une rapide recherche permet
d'identifier la musique à laquelle elle fait référence
https://www.youtube.com/watch?v=SPlQpGeTbIE.

La redondance des valeurs exprime bien le style répété de la musique et le fait
de devoir commencer par bouger ses pieds suppose que nous devons faire quelque
chose sur les bits. On perçoit aussi que le flag est probablement au début, car
les valeurs diffèrent ensuite. Je ne vais pas cacher que j'ai longuement tourné
en rond, tout en étant persuadé que cela devait être simple (challenge à 100 points).
J'ai commencé à changer les MSB, mais rien de concret et pas de code à reverser
connu.

## Inverser les pieds

Après plusieurs heures sans savoir quoi faire, j'abandonne pour un autre chall
de reverse. Au détour d'une discussion d'apparence sans intérêt avec mon voisin
à propos de la musique, j'ai en tête l'idée simple d'inverser les bits comme
si l'on changeait de pied sur une danse. Je modifie rapidement le script pour
ajouter l'étape d'inversion :

```python
import struct
import sys

if (len(sys.argv) < 2):
	print("Please set arguments %%u <file>")
	sys.exit(-1)

f = open(sys.argv[1], 'r')

# Replace the '\n' to remove 80-chars columns
data = f.read().replace("\n", "")

# [NEW] Reverse bit 
data = data.replace("1", "2").replace("0", "1").replace("2", "0")

data_str = ""
for i in range(0, len(data) // 8):
	byte = data[i*8:i*8+8]
	data_str = data_str + str(hex(int(byte, 2))) + " "

# Write the output file
f_out = open("out.bin", "wb")
data_list = data_str.split(' ')[:-1]
for i in data_list:
		f_out.write(struct.pack("B", int(i, 16)))

f.close()
f_out.close()
```

Et là, magie, le fichier de sortie contient:

```
Easy wasn't it ? Now bring me a beer ! - Hackira..fl
ag : ndh2k17_624f4a5789ce1298f469ce&#210;&#210;&#210
;&#210;&#210;&#210;&#210;&#182;&#8482;&#223;&#8224;&
#144;&#352;&#223;&#339;&#382;&#8216;&#223;&#141;&#35
3;&#382;&#8250;&#223;&#8249;&#8212;&#8211;&#338;&#21
1;&#223;&#8224;&#144;&#352;&#216;&#141;&#353;&#223;&
#8216;&#144;&#8249;&#223;&#8217;&#382;&#8250;&#223;&
#353;&#8216;&#144;&#352;&#732;&#8212;&#211;&#223;&#8
249;&#141;&#8224;&#223;&#382;&#732;&#382;&#8211;&#82
16;&#209;&#209;&#223;&#197;&#210;&#214;
```

Et vlà notre flag : **ndh2k17_624f4a5789ce1298f469ce**

Bon, des heures pour une simple inversion de bits, c'est un peu con. 
Mais le nom de la catégorie prend tout son sens...


