## Caleb Mouritsen
## 10/22/18
## text-based RPG game
#This game involves coding through using multiple different functions that are called, they will lead into different functions when the game is started.
#Each function is basically structured the same, with ASCII art used to show the user images, with choices involved in each choice. If there are no choices in the function, this means it's a choice where the user just dies


# Victory Screen if game is completed normally
def victory():
    print("you transcend to godhood and become the most powerful being in existence.")
    print(""" __     __  __              __                                    __ 
|  \   |  \|  \            |  \                                  |  \
| $$   | $$ \$$  _______  _| $$_     ______    ______   __    __ | $$
| $$   | $$|  \ /       \|   $$ \   /      \  /      \ |  \  |  \| $$
 \$$\ /  $$| $$|  $$$$$$$ \$$$$$$  |  $$$$$$\|  $$$$$$\| $$  | $$| $$
  \$$\  $$ | $$| $$        | $$ __ | $$  | $$| $$   \$$| $$  | $$ \$$
   \$$ $$  | $$| $$_____   | $$|  \| $$__/ $$| $$      | $$__/ $$ __ 
    \$$$   | $$ \$$     \   \$$  $$ \$$    $$| $$       \$$    $$|  \
     \$     \$$  \$$$$$$$    \$$$$   \$$$$$$  \$$       _\$$$$$$$ \$$
                                                       |  \__| $$    
                                                        \$$    $$    
                                                         \$$$$$$ """)
    print("if you're here from choosing to die in space I'm sorry I ran out of ideas")

    #Victory screen used if very specfic conditions are met during the first choice

def instant_win1():
    print("you transcend to godhood and become the most powerful being in existence.")
    print(""" __     __  __              __                                    __ 
|  \   |  \|  \            |  \                                  |  \
| $$   | $$ \$$  _______  _| $$_     ______    ______   __    __ | $$
| $$   | $$|  \ /       \|   $$ \   /      \  /      \ |  \  |  \| $$
 \$$\ /  $$| $$|  $$$$$$$ \$$$$$$  |  $$$$$$\|  $$$$$$\| $$  | $$| $$
  \$$\  $$ | $$| $$        | $$ __ | $$  | $$| $$   \$$| $$  | $$ \$$
   \$$ $$  | $$| $$_____   | $$|  \| $$__/ $$| $$      | $$__/ $$ __ 
    \$$$   | $$ \$$     \   \$$  $$ \$$    $$| $$       \$$    $$|  \
     \$     \$$  \$$$$$$$    \$$$$   \$$$$$$  \$$       _\$$$$$$$ \$$
                                                       |  \__| $$    
                                                        \$$    $$    
                                                         \$$$$$$ """)
    
#Death screen used whenever the user leads into a scenario where they get a game over
def death():
    print("""      ...
             ;::::;
           ;::::; :;
         ;:::::'   :;
        ;:::::;     ;.
       ,:::::'       ;           OOO\
       ::::::;       ;          OOOOO\
       ;:::::;       ;         OOOOOOOO
      ,;::::::;     ;'         / OOOOOOO
    ;:::::::::`. ,,,;.        /  / DOOOOOO
  .';:::::::::::::::::;,     /  /     DOOOO
 ,::::::;::::::;;;;::::;,   /  /        DOOO
;`::::::`'::::::;;;::::: ,#/  /          DOOO
:`:::::::`;::::::;;::: ;::#  /            DOOO
::`:::::::`;:::::::: ;::::# /              DOO
`:`:::::::`;:::::: ;::::::#/               DOO
 :::`:::::::`;; ;:::::::::##                OO
 ::::`:::::::`;::::::::;:::#                OO
 `:::::`::::::::::::;'`:;::#                O
  `:::::`::::::::;' /  / `:#
   ::::::`:::::;'  /  /   `#""")
    print("\n lol, got your soul, loser. \n maybe go spend some money on an actually decent game\n")
    print("Game Over")

def ask_question(question):

    print(question)

    return

    
#Initial screen that everyone opens to when running the game
def opening():
    print("""
 ^  ^  ^   ^        ^  ^   ^  ^  ^   ^  ^
/|\/|\/|\ /|\      /|\/|\ /|\/|\/|\ /|\/|\\
/|\/|\/|\ /|\      /|\/|\ /|\/|\/|\ /|\/|\\
/|\/|\/|\ /|\      /|\/|\ /|\/|\/|\ /|\/|\\
""")
    
           
       
    print("You just entered the woods completely against your will! \nGood job idiot, no going back from here. \nLet's see what happens.")

#Redirect here if the user chooses to slice the tentacle in choice6
def choice10():
    print("You slice the tentacle, but another one instantly grabs your leg. \nThe octopus is pissed now and just slams you head first into the ground. Killing you instantly")
    death()

#Redirect here if the user chooses to throw the sword in choice6
def choice11():
    print("You throw the sword straight at the octopus, it slices through it, ultimately killing it.")
    print("You're unsure if you have the will to keep going, but you soon realize that you're too tired to go on after this battle")
    print("You grab the sword off of the octopus' body and begin to suffer from existential dread, you kill yourself with the sword")
    print("You wake up, not seeing a game over screen, you grow confused \n input 1 to go further input 2 to kill yourself again")
    choice = int(input())
    if choice == 1:
        print("You continue on, accidentally chewing off your own fingers from being too nervous. \nAfter days of walking through the unknown area, you finally just lay down and go to sleep")
        print("Game Over, sweet dreams loser")
    elif choice == 2:
        print("I like you, however you still have to get a game over \n It's ok though you would've gotten one regardless")
        death()

#Redirect here if the user chooses to drink the pond water within choice2
def choice5():
    print("you disobeyed everything you learned as a kid and drank from the weird gravity pond. \n I seriously don't know what's wrong with you")
    print("The water is actually really tasty, unfortunately it makes you very sick and you die. Your last words were \"I'm an idiot\" haha")
    death()

#Redirect here if the user chooses to continue down the path within choice2
def choice6():
    print("You ignore the strange pond, taking the smart move and not trusting anything (good job). \n As you continue down the path a tentacle emerges from the pond and grabs you")
    print("""           .---.         ,,
                 ,,        /     \       ;,,'
                ;, ;      (  o  o )      ; ;
                  ;,';,,,  \  \/ /      ,; ;
               ,,,  ;,,,,;;,`   '-,;'''',,,'
              ;,, ;,, ,,,,   ,;  ,,,'';;,,;''';
                 ;,,,;    ~~'  '';,,''',,;''''  
                                    '''""")
    print("A not so friendly octopus has you by the leg, dangling you and making the blood rush to your head. \n It isn't going to eat you or anything, it just wants to watch you slowly die, psychotic weirdo.")
    print("Luckily, something within you awakens and deposits you a fully fledged sword through your mouth (gross). \n Input 1 to slice the tentacle dangling you, input2 to throw the sword at the octo's head")
    choice = int(input())
    if choice == 1:
        choice10()
    elif choice == 2:
        choice11()
    else:
        print("Honestly, you're too far in to be inputting things that you aren't told to. I'm just gonna kill you now.")
        death()

#Redirect here if the user chooses to go inside the hole in choice4
def choice7():
    print("You fell down the hole, a giant skeleton holding the key to godhood stands before you.")
    print("""           _..--""---.
          /           ".
          `            l
          |'._  ,._ l/"\
          |  _J<__/.v._/
           \( ,~._,,,,-)
            `-\' \`,,j|
               \_,____J     Hey Loser
          .--.__)--(__.--.
         /  `-----..--'. j
         '.- '`--` `--' \\
        //  '`---'`  `-' \\
       //   '`----'`.-.-' \\
     _//     `--- -'   \' | \________
    |  |         ) (      `.__.---- -'\
     \7          \`-(               74\\\
     ||       _  /`-(               l|//7__
     |l    ('  `-)-/_.--.          f''` -.-"|
     |\     l\_  `-'    .'         |     |  |
     llJ   _ _)J--._.-('           |     |  l
     |||( ( '_)_  .l   ". _    ..__I     |  L
     ^\\\||`'   "   '"-. " )''`'---'     L.-'`-.._
          \ |           ) /.              ``'`-.._``-.
          l l          / / |                      |''|
           " \        / /   "-..__                |  |
           | |       / /          1       ,- t-...J_.'
           | |      / /           |       |  |
           J  \  /"  (            l       |  |
           | ().'`-()/            |       |  |
          _.-"_.____/             l       l.-l
      _.-"_.+"|                  /        \.  \
/"\.-"_.-"  | |                 /          \   \
\_   "      | |                1            | `'|
  |ll       | |                |            i   |
  \\\       |-\               \j ..          L,,'. `/
 __\\\     ( .-\           .--'    ``--../..'      '-..
   `'''`----`\\\\ .....--'''
              \\\\                            ''""")
    
    print("Only two ways to go here, input 1 to fight, input 2 to run")
    choice = int(input())
    if choice == 1:
        print("Your will resonates within you, your hands grow four times as big. \n You gorilla punch the skeleton with your massive fists, achieving godhood
        victory()
    elif choice == 2:
        print("The skeleton laughs at your cowardice, it uses its alien eyes and explodes your head.")
        death()
    else:
        print("Nope, dead")
        death()

#Redirect here if the user decides to eat the stick within choice4
def choice8():
    print("You eat the stick (idiot) \n It travels through your digestive system, puncturing several vital organs, killing you")
    death()

#Redirect here if the user decides to chase the blob within choice4
def choice9():
    print("I don't know where you're going with this but I have no choice but to be here")
    print("The blob turns around, and unhinges its jaw, swallowing you whole")
    print("""                    ..;===+.
                                                                  .:=iiiiii=+=
                                                               .=i))=;::+)i=+,
                                                            ,=i);)I)))I):=i=;
                                                         .=i==))))ii)))I:i++
                                                       +)+))iiiiiiii))I=i+:'
                                  .,:;;++++++;:,.       )iii+:::;iii))+i='
                               .:;++=iiiiiiiiii=++;.    =::,,,:::=i));=+'
                             ,;+==ii)))))))))))ii==+;,      ,,,:=i))+=:
                           ,;+=ii))))))IIIIII))))ii===;.    ,,:=i)=i+
                          ;+=ii)))IIIIITIIIIII))))iiii=+,   ,:=));=,
                        ,+=i))IIIIIITTTTTITIIIIII)))I)i=+,,:+i)=i+
                       ,+i))IIIIIITTTTTTTTTTTTI))IIII))i=::i))i='
                      ,=i))IIIIITLLTTTTTTTTTTIITTTTIII)+;+i)+i`
                      =i))IIITTLTLTTTTTTTTTIITTLLTTTII+:i)ii:'
                     +i))IITTTLLLTTTTTTTTTTTTLLLTTTT+:i)))=,
                     =))ITTTTTTTTTTTLTTTTTTLLLLLLTi:=)IIiii;
                    .i)IIITTTTTTTTLTTTITLLLLLLLT);=)I)))))i;
                    :))IIITTTTTLTTTTTTLLHLLLLL);=)II)IIIIi=:
                    :i)IIITTTTTTTTTLLLHLLHLL)+=)II)ITTTI)i=
                    .i)IIITTTTITTLLLHHLLLL);=)II)ITTTTII)i+
                    =i)IIIIIITTLLLLLLHLL=:i)II)TTTTTTIII)i'
                  +i)i)))IITTLLLLLLLLT=:i)II)TTTTLTTIII)i;
                +ii)i:)IITTLLTLLLLT=;+i)I)ITTTTLTTTII))i;
               =;)i=:,=)ITTTTLTTI=:i))I)TTTLLLTTTTTII)i;
             +i)ii::,  +)IIITI+:+i)I))TTTTLLTTTTTII))=,
           :=;)i=:,,    ,i++::i))I)ITTTTTTTTTTIIII)=+'
         .+ii)i=::,,   ,,::=i)))iIITTTTTTTTIIIII)=+
        ,==)ii=;:,,,,:::=ii)i)iIIIITIIITIIII))i+:'
       +=:))i==;:::;=iii)+)=  `:i)))IIIII)ii+'
     .+=:))iiiiiiii)))+ii;
    .+=;))iiiiii)));ii+
   .+=i:)))))))=+ii+
  .;==i+::::=)i=;
  ,+==iiiiii+,
  `+=+++;""")
print("The blob's mouth turned out to be a portal to the cold depths of space, you are left adrift in the cosmos, somehow being unable to die. \n You eventually stop thinking")
print("input 1 to die, input 2 to die")
choice = int(input())
if choice == 1:
   print("You Die")
   death()
if choice == 2:
    print("You die, but in this instance you don't really care, death is a sweet release to you")
    print("Finding this, you finally find inner peace, you ascend to godhood")
    victory()
 
              
    
    
    
    
#Redirect here if the user chooses to poke the mush within the choice1 class    
def choice3():
    print("you poke the mush, it turns out to be a blob creature, it spits extremely corrosive acid in your face, leaving you dead and also ugly. Sorry.")
    death()

#Redirect here if the user chooses to poke the mush with a stick within the choice1 class    
def choice4():
print("you poke the mush with a stick (good, why would you touch a pile of mush with your bare hands?) \n it turns out to be a blob creature, it spits acid at you \n since you kept your distance and used a really long stick, the acid misses you and hits the ground.")
print("""
                             8a .
                               `.  _
    ___________  s,    _____     /_/   ____________________a:f____
               .Jktbc._       _ ./
              xft#kTJ:   _.  (_)/)  -._
             cf8#6C. ,  (   ( ,-'      )
           ` `"P:'.     '-._\_\___.---""")
print("The acid on the ground eats through the dirt, revealing a hollow cave below, who knows what could be inside. \n the blob creature runs away since it's no match for your really long stick.")
print("3 choices here. Input 1 to go inside the hole \n input 2 to eat the stick \n input 3 to chase the blob")
choice = int(input())
if choice == 1:
    choice7()
elif choice == 2:
    choice8()
elif choice == 3:
    choice9()
else:
    print("I'm begging you to not go outside the desired inputs, you do what I tell you, end of story.
    
#Redirect here if user chooses the right path in the first choice
def choice1():
    print("You took the right path, the problem being that right isn't always right.\n That wasn't me telling you that you took the wrong way, I can't tell you that, it was just a word of advice.")
    print("""                                                                                                                                                                                            .........                                                                                                       
                                                                                                                                                                                       ..................                                                                                                   
                                                                                                                                                                                     ..................... ....                                                                                             
                                                                                                                               ..                  ........'',,,,,,,,;;,,,,,''.......   .......................                                                                                             
                                                                                                                                          ...',;::clloooddddddxxxxxxkkkkkkkkkkxxdoool:;;'.....................                                                                                              
                                                                                                                                    ..,;:lodxkOOOOkkkkkkxxxkOOOkkkkkkkOkkkkkOOkOOkkkkkxxxdol:;;,'.............                                                                                              
                                                                                                                               ..,:ldxOOOOOOOOOOOOOOkkkkkkkOOOOkkkOOkkkkkkOkOOOkOOkkkkkkkkkxxxxdool:;'........                                                                                              
                                                                                                                          ..';coxkOOOOOOOOOOOOOkkkkkkkkkkkkkkkkkkkkkkkkkkkOkOOkOOkkkkkkkkOOOOkkkkkOkkxdlc:,..                                                                                               
                                                                                                                      ..,:ldxkkkkOOOOOOOOOkkkkkkxxkkkkkkkkkkkkkkkkkkkkkkxxkOkkkkkkkkkkkkkkkOOOOOOOOOOOOOOOkdl:'..      .  .                                                                                 
                                                                                                                  ..,:ldxkkkOOOOOOOOOOkkOkkkkkkkkkkkkxxxkkkkkkkxxkkkkkkkkO00OOkkkkkkkkkkkkkkOOOOOOOOOOOOOkkkxxxo:,............                                                                              
                                                                                                               .';coxxkkOOOOOOOOOOOOkkkkkkkkkkkkkkkkxxxxxxxkkkkOOOO0000KKK00OOOOkkkkkkkkkkkkkkOOOOOkkkkOOOOOOOOkkxdl;'.........                                                                             
                                                                                                            .';ldxxkOOOOOOOOOOOOkkkkkkkkkkkkkkxxxxxxxxkkkkOOO0000000KKXXXXKKK0000000OOOOOOkOkkkkkkkkkkkkOkkOOO0000OOOxoc,........                                                                           
                                                                                                         ..;lddxkOO00000OOOOOOOOOOOOOkkkkkkkkkkkkkkkkOOO0000000KKKKXXXXXXXK00O00OOOOOOO00O000OOkkkkkkkkkOOOOOO0K00KKK00Okdc,........                                                                        
                                                                                                       .,coddxkkOOOOOOO000OO00OOOOOOOOOOOOOkkkOOOO000000KKKKKKKXXXXXXXXKKK0OOOOOkkkOOkkkOOO00000OOOO000KXXX00XNNNNNXXXKK00Oxl;.....                                                                         
                                                                                                    .':lddxxkkOOOOOOOOOOOOOOOO0OOOOOOOOOOOOOOO000KKKKKKKKKXXXXXNXKXXXKKKKKKK000000OOOOOOOOOOOO00000KNWWNNNX0KXNWWWWWWWWWNXXKOko:'...                                                                        
                                                                                                  .,cdddxxxkOOOOOOOOOOOOOOOOOOOOOOO000000000KKKKKKKKKKKXXXKKKXXXXXXXKKKKKKKKKKKKK0OOOOOOOOOOOOOO0KKXNWWNX0OkO000KKXXNNNWWNXKK0Okdc'.                                                                        
                                                                                                .,lddxxxxkkkkkkkkkkkkkkkkkOOOO000000000KKKKKKKXXXXXXXKKKKKKKKKKKKKKKKKKKKKKKKKKKKKK0000OOOOkkOOO00KKXK0OOOkkkkkOOOO0000KKKKKKK00Okxl,.                                                                      
                                                                                              .,lddxxxxxxxxxxxxxxxxxxkkkOO000000000000KKKKKXXXXKKKKKKKKKKK0000000000K0000KKKKKKKKKKKKK0OOOkkkkk0KKKKK0OkkOOkkkkkkkkOOOOOOO000KKKK0Okxl'.                                                                    
                                                                                            .,lddxxxxxddddxxxxkkkkkkOOO00000OOO00000KK0KKKKKKK00KKKKKKKK00000000000000000000000KKKK000000000OO00XNXK000OOOOOOOkkkkkkkkkkkkOOO00KKKK0Okxc.                                                                   
                                                                                          .,ldxxxxdddxxxkOOOOOOOOOOO00OOOOOOOOO000O00000KK000000KKKK000000000000OOO0OOOOOOOOOOOOOO0OOOOOO0000O0XNWWX0OOOOOOO0KK00OkkxxxxxkkkkkO000KKK00Od;.                                                                 
                                                                                        .;ldxxxddddxkOOOOOOO0OOOOOOOOOOOOOOOOOOOOO00000000000000000K00000000OO00000OOOOOOOOOOOOOOOOOOOOOOOOOOO0NWMMWX0OkO0K0KKKKKK0OkkxxxxxxxkkkkkO0KKK00Oo'.                                                               
                                                                                     ..;odxddddodxxkkkOOOOOOOOOOOOOOOOOOOOOOOOOOOO0000000000000000000000000OOOO0OOOOOOOOOOOOOOOkkOOOOOOkOOkkkkOXWWWWNXK00KXNNNNNXXX0OOkkkkxxxxxkkkkkO0KK000kc.      .  .. ..                                                
                                                                                   .':oddooooooodxxkkkOOOOOOOOOOOOOOOOOOOOOOOOOOO00000000000000000OO00000OOOOOOOOOOOOOOOOOOOOOkkkkkkkkkkkkkkkkk0KKNNXXXX0KXXXNXXNNK0OOOOOkkkkxxxxkxxkOO0K00OOx;. .........   ..                                             
                                                                                 .,codoollcllloddxxkkOkkkOOOOOOOOOOOOOOOOOOOOOOOOOOOO00OO00000000OOO000OOOOOOOOOOOOOOOOOOOOkkkkkkkkkkkkkkkkkkkkkOOO0K0KKXXKKKXKKK0O0K00OOkkkkOkkkxxkkOO000000Oko,. ..                                                       
                                                                             ..,:looollll:;,:loddxxkkkkkkOOOOOOOOOOOOOOOOOOOOOOOOOOOO00OOOOO0000OOOOOOOOOOOOOOOOOOOOOOOOOOkkkkkkkkkkkkkkkkkkkkkkkkkOKNWWWNK000OOOOkO0000OOOOkkOOOOOO00O000000000kl'....                                                     
                                                                          ..;cooddddooll:,,',coodxkkkkkkkkkOOOOOOOOOOOOOOOOOOOOOOOOOOOO00OOOOOOOOOOOOOOOOOOOOkkkkkkkkkkkOOkkkkkkkkkkkkkkkkkkkkkkxkOO0XNNXK0kkxxxkOkkkkkkxxxkkxkO00KXXK00O0000000OOx:....                                                    
                                                                       ..,cloodxxxdddolc,',,,lddxkkkkkkkkkkOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkxxxxkkxxxxxxxkkkkOOOOOOOkkkkkxxkkkdl::;:looxO0KKKKKK0000K00O0Oko,.                                                     
                                                                     .,:loddxkxxxdddxdl:,'',looxxkkkkkkkkkkOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOkkOkkkkkkkkkkkkkkkkkkkkkkkkkkkkkxxxxxxxxxxxxxdxxxkkkkkOOO00000Okkxxkkxc....,:cldkOXNNNXXK0000OOOOkkdc'.                                                   
                                                                 ..,:loddxxxxkxxxkkxxdol,.,loodxkkkkkkOOOOkkOOOOOOkkkkOOOOOOOOOOOOOOOOOOOOOOkkOOOkkkkkkkkkkkkkkkxxkxxkkkxkkxkkxxxxxxxxxxxxxxxxdxxxkOkkkkkOOO0KK00OkkkkO0x;.....',lxxk0KKXXXXXK0OOkkkxxxd:'.                                                 
                                                               .':loodxxxxxxkkkkkkkkxxdoccoddxxkkkkkkkOOOOkkkOkkkkkkkkkOOOkkOOOOOOOOOOOOOOkkkkkkkkkkkkkkkkkkkkxxxxxxxxxxxxxxxxxxxxdddddddddxxddxxxxxxxxkkkOOO00KK00OkxkKKx:......;odxxkkkOO0XNNX0OOkxxxxdo:'.                                               
                                                            ..;looddxxxxxkxxkkkkkkkkkxxdxxxdxkxkkkkOkkkkOOOOOkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkxxxxxxxxxxxxxxxxxxxxdddddddddddddddddddxxxxxxkkkkkOO00000OOkO00xc.....'codxkOOOOOO0KXXKK0Okxxdddoc'.                                             
                                                          .,coooddxxxkkkkkkxkkxkkkxxxxxxxxxxxkkkkOOOkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkxxxxxxxxxxxxxxxxdddddddddddddddddddddddddxxxxxkkkxxxkkOOO0KXXK0O00xl,...'cddxkOOOOOOOO00XNXKK0Okxddddc'                                            
                                                        .,cooodddxxxkkkkkxxxxxxxxxxxxkxxkxxxkkkkkOOOkkkkkkkkkxxxkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkxxxxxxxxxxxxxddddddddddddddddoddooddooodddxxxxkkkxxxxxkkkO00KXXKKK0kd:',:lxxxkOO00000000KXNXKKK0Okxdddo:'.                                         
                                                      .,cooodddxxxxkkkkxxxxxxxxxxxxxkkkkkxxkkkkkkkkkkkkkkkkkkkkxxxxxxkkkkkkkkkkkkkkkkxkkkkkkkkkkkkkkkkkkkkxxxxxxxxxxxxdddddddddddddddddoooooooodddddxxxkkkxxxxxxkkkkkOO0KKKKXK0OO000OOO00KKKXK000KNWWNXKK000Oxddooc,.                                       
                                                   ..;clodddddxxxxkkkkkxxxxxxxxxxxxxkkkxxxkkxkkxxxxxxkkkxxxxxxxxxxxxkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkxxkxxxxxxxxxxxxdddxxdddddddddddooooooooododoodddxxkkxxxxxxkkkOOOOOO000KKXXXXXXKKKKKKXXXKKKNWWWMMWX00000OOkxoooc,.                                     
                                                  .;:looddddxxxxkkkxxxxxxxxxxxxxxxxxxxxxxxxxdddddddxxxxxxxxxxxxxxxxxxxxxxxxxxxkkkkkkkkkkkkkkkkkkkkxxxxxxxxxxxxxxxxxxxdddddddddddodddoooooolooooooooooodddxxxxxxkkkkkkOOOOOO0000KKKKKKXKKKKXXXNNWMMMWWNXXKK00OO00Okxollc;.                                   
                                               ..;:cooodddddxxxkkxxxxxxkkkxxxxxxxxxxxxxxkkxdddoooddddxxxxddxxxdddxxxxxxxxxxkkkkkkkkkkkkkkkkkkkkxxxxxxxxxxxxxxxxxxxxxxdddddddddoddddddddoooooooooooooodddxxxxxxxxxxkkkkkOOOOO0000000000KKKXXNNNWWWWNNX0000000OOOOOkkxdollc;.                                 
                                              .,:cloodddddddxdxxxxxkxxxxxxxxxxxxxkkxxxkkkkkxxxxollooddddddddddxxddxxxxxxxxxkkkkkkkkkxkkkkkxxxxxxxxxxxxxxxxxxdddddddddddddddddddddddddoooooooolllllloooddxxxxxxxxxxxxkkkkkkOOOOOOOOOOOOOOO000KKKKKKKK000000OOOOOOOkddxxdolcc;.                               
                                            ..;:looodddddddddddxxxxxxxxxxxxxxxxkkxxxxkkkkkkkxxxdolloooddddddddxxxxxxxxxxxxxkkkkkOkkxxkkkkkxxxxxxxxxxxxxxxxxxddddddddddddddddddddddddoollllllcccccc:ccloddddxxxxxxxxxxxkkkkkkkkkkOOOOOOOOOOO0OOOOOO0000OOOOOOOOOOOOkxxxxddolc:'.                             
                     ... ......          . .';clooddddddddddddxxxxxxxxxxxxxxxxkxdxxxkkkkkkkkkxdolcclooddddddddxxxxxxxxxxxxxkkkkkkxxxxxxxxxxxxxxxxxxxxxxxdddddddddddddddddddddddddddoollllcccc:;;;;;;;:clooddxxxxkkkkxxxxxxkkkkkkkkkkkkOOOOOOOOOOOOOOOOOOOOOkkOOOOOOkxxxxxddoc:;..                           
...........................''..............':looodddddddooddddxxxxxxxxxxxxxxxkxddxxxxxkkkkkxxdolllcloddddddddddddxxxxxxxxxxxkkxxxxxxxxxkkxxxxxxxxxddxxddddddddddddddddddddddddddooolllccc::;;,,,,;;::ccllodddxxxkkkkkkxxxxxxxxkkkkkkkkkkkOOOOOOOkkkkkkkkkkxxkkkkkkkkxxxxxxxdool:,.                          
........'''''''''........''',''''''''''''',:looooddddddoodddxxdxxxxxxxxxxxkxxxdxxxdxxxxxxxddoolcclllooddddddddddddxxkkkkkkxkkxxxxxxkxxkkxxxxxxxxxxxdddddddddddddddddddddddooooolllllcc:c::;;,,,;:cclllllloodddxkkkkkkkkkkkxxxxkkkkkkkkkkkkkkkkkkkkkkxxdxxxdxxxdxkxdxkkkxxkkxxddlc:'.                        
.........'''''....'''....''''''..''''''',,:llododdddddooddddxxxxxxxxxxxxxkxxxxddxxdoooddddollccccllloooooooooddddddxkxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxdddddddddddddddddddooooollllcllcccc::;;;,,,;:clloooooolooddxxxkOOOOOOOkkkkkxxkkkkkkkkkkkkkkkkkkkxxxddddddddddxxxdxkkkxxxkkkdolcc:.                       
..'......''''......'......''''...''.'''',:looddddddoddooddddxxxxxxxxxxxxkkxxxxxxdddolllolccllcccccclllllooooododdddxxxxxxxxxxxxxxxxxxxxxxxxdddddddddddddddooooooooooooooolllllccccc::::;;;,,,;;:cllllloooooodddddxxkOOO00OOOkkkkkkkkkkkkkkkkkxxxkkxxxxxdoodddodddddxxkkkkkxxxxxxdolc:,.                     
......................................',:cloddddddoooooooddxxxxxxxxxxkxxxxxxxxxxxdooddxkOOdccclllccllllllooodddddoddddddxxxxxxxxxxxxxxdddxxddddddddddddddooooooooooooollllllcccc::::;;:;;,'',;;:cclllloodddxxxddooodxxkOOOOOOOOOkkkkkkkkkkkkkxxxxxxxdddddoodddooooooodxxkxxddddxxddolc;'.                   
......................................,:cllodxdoooooloooddxxxxxxxxxxxxxxxxxxxxxddoodx0NWWWNOdlcccccccccllloooooooooodddddddxxxxddddddddddddddddddoooooooooooooooooolllllllcccc:::::;;;;,''',,,;:cccllooodxxxkkkxxxxxxdxkOOOOOOO00OOOOOkkkkkkkxxxxxxxdddddddoodoooloolloddddddddddxxxdolc;.                  
.....................................';clllddxdoolllloooooxxxxxxdddxddxxxxxxxxddddddOXXKK0kxolllccccccccclllllolllooooooooodddddddddddddddddoooooooooooooolllllllllllllcccc::::;;;;;;;,''',,,,;:cclllloodxxxxkkxxxkkkkkkkkkOOOO0000OOOOkkkxxxxxxxxxxddddoddoooooooollllloodxddxdddxkkxdol:'.                
'...............''..................':ccllodddoollcllllooodddddooodxxdddxxddddddddodkOkdloolllloxxoc::ccccccclllllllooooooooooooooooooooooooooooooooooollllllcccccccccccc::;;;;;;;,,''''',,,,;;::clddoooddxxxxxxxxkkkkkxxxxkkkkkOOOOO00kkkxxxxxxxxxxdddooooooloooollllllloooddxxddxdk0kxdoc,.               
'............................ ......;llllloooollclcclllloodddoooodxxdddxxxddxdxxxdddddxkOOxllllodoc:::;:::cccccclllllllloolooolllooollllllllllllllllllllcccccccccccc::::::;;;;,,,,'....''',,;;::ccclolddoddddddddxxkkxxxxxkkkkkkkkkkkkkkxxxxxxddddddddooollooolloollllllllllloddxxxxdxkkOOxo:.              
;,'.''''''''........................;lllllollllcllcclllloooodoooddddddddddddddxxxddk0XNNXXkdolcll:::;;,,;;:::ccccccccllllllllllllllllllllcccccccllccccccccc:::::::::;;;;;;,,'''..........'',,;;::cclllllodxxxoodddddxxxxxxxkkkxxxxxxxxxxxxxxxddddoodddoollllooolloolllllllllllloddxxxxkkxOXKkl,.            
cc;;:ccc:,'......................',':llloollclllllllllloooooooooodddddddddoddddxkkOK0kxdooollccc:;;;;::::;;;;;::::::ccccccccccccccccccclccc::::::::::::::::;;;;;;;,,,,''.........''',,,,,;;;;;::::cccclllooxkolodooddddddxxxxxxkxxxxxddddddddddxxdoooooooollloollllllllllllllllloddxxxxxdx0KK0d;.           
,,,,:ccc:,'''...................',,;llclolccccllcllllloooooooooooodddddddddddxxxxddddllllc:::;;;;::ccccc::::;;;;;;;;;;;::::::::::::::::::::;;;;;;;;;;;;;;;,,,,,'''...........''',,,,,;;;;;:::::::ccccccccc:clc:cllloooddddddddxxdddddddddddooodddooooollllllllllllllllllllllllllloooxxxddxxO0K0xc,.         
,;;:::;,,,;:cc:,,;;;;;;:;;;;;;:::;ldlccllccccccccccclllllllloodoooodooodxxdooollllllc::;;;;;::ccccccccc:ccc::::::;,,,,,,,,,,,,,;;;;,,,,;;;,,,,,,,,,,'''''''.................''',,,,,;;;;;;;:::::cccccccccc::;,;;::::cllllloooooolooooooddddoooooooooollolllloooolllllllllllllllllcclodxddxddk00kddl'        
::ccc:;;;;:ccc:;;:cccccclccclcc::ccc::ccc::ccccccccccclloooddddooooddkOOxdollllccc:;;,;;;:cc:::cccccccc::::::;;;;,,,''.........................................................''',,,,,,;;;;;:::::cllolccccc::;,,,,,;:ccccccclllllloloooooooolllllllllllollllllollllllllllcccccllccccldooooddxkxxddo,       
ccc:::::cclllc:;;:ccc:;ccc::::::::::::::::::::::cccccloooooddoooooodxkxooolllcc:;;,,;:::cccc:::cccc:::::::;;,,,''..................................................................'''',,;;;;;;;;::ccc::::::::::;,,,,,;::;::ccccccllooooooooollllllllllllllllclllllllllcclcccccccc:::clollllodddooodl.      
c::;;:cc:cllc:;;:ccc::;:c::;:;:::::::;;;::::::::ccccooddooooooooooooollllccc:;,,,;;::::::::::;;;;;;;;;,,'''......'..;:'''','.............................................................''',,,,;;;;;;;;;;:::::;:::;,,,,;;;;;:::ccllllooooolllllllllcccccllllllllllllllccccccccc::::cclllcc:cllllccloc.     
:;:cccc::ccccccccc::;;;;::;;;::::::::;;;:::::ccclllloooooollllollollllccc:;,,,,;:::;;;;;;;;,,,'',,''.........,,';:;:kklccc;,',''...................................'.....''''''''''''...........'''',,;;;;;::;;;;;;;;;;;,,,,,;;::cccclooooolllllccc:::ccclllolclcclllcccccccccc:::::::cccc:::clllc:ccl;.    
;;:cc::::ccclllc:;,,,;;:::::::::::::c:::cccccllllllllllloolllllllcc:::;;,',,;;;::;;,,,,,,''.''''............,:oxkocdkxc,,;;,,,,,;,,,,''...................'',,;;;:::ccc::cc:::::::::;;;,''............'',,,,,,,,;;;;;;;;;;,,,,,;;;::cclllollccccccccc::cccccccccccccccccccccccc:::::::::::::::cccc::clc'    
;;;::;;:cc::cc:,,,,;;:::cc::;;::::ccccccllloolllllllllllllllolcol:;,,,,,;;:;;;;;;;,,,,,'....''........''',codxdol:,,,''''''''''',,,,''','''............'',;;::ccclllllllllllllcccccc::c:::;,,''............''',,,,;;;;;;;;;;;;;;;;;;::ccclllccccccllcc:::cccc::::::::;::::ccccccc::::;;:::::::::::::::c;.   
;;;:::::c:::;,,,;;::cccc::;;:::ccccccllllllllllllllllccccldddccol:;;;;:::;,,,,,,,,,'''',;,,,''.....',;;;,,::;','''.''.............................'''''',;;;::cccccccccllllllllllllcccccccccc::;,,,''''........'',,,;;;;;::::c:::;:::::cccllccccccclc:::::::::::::::;;;;;;;::::cc::::;;:::::::::;;:::::;,.  
::::ccc::;;,,,;;::cc:;;;;;:::ccccccclllllllllllcccc::;;;::::::::c::::::;,,;;,,,,,,''',:::c:;,''',,',;;,,''...'''.......................'...'''''''',;,',;;;::::ccccccccccccccccccccccccclcllllcccc::;;;,,,'''....'',,,,;;cooddlcccc:::cccclllllllllcc::::::::::::::;;;;;;,;;;;;::::::;;:::::::::;;:::::;;;'.
:cccclccc::;::cccclc:;;::::::ccccccllllllllcc::::::::;::ccccccc::::;;;,'',;;,;,,,,,,:cccccc;,,,,'''''''...........''''''.............'',,,,,,,,,,,;cc;,;;;:ccc::::c:cccccccccccc:::::ccccccllllllllcccc:::::;;,''.''',,,;cdxkxdlccclllcccccllllllllollccc:::::::::;;;;;;,,,;;,;;;;;;;;;;:::::::;;;:::::;;::'
:ccccccccccccccllc::;;::cccccccllcclccccclllcc:::::::::cc:ccccc::;;,,',,,,,,,,,,,,:looooddo:,::,''.......  ...';lc:;;;::'',;,''''','.,;,;:::::coc::::llccllcloccccc::cc:::::::::::::::::ccccllodddoolllllc::::::;;,,,,,;:cloddollclllollllllllllllldddoolc:::::::;;;;;;,,,,;;,;;;;;;;;;;::::::;;;;:::::;;:::
;;::ccccccclcccc:;;;:::cccccccllllccc:::clllllcc:cccccccc::::::;;,,'',,,,,,,,,,,,;codkdodoc,,:;''........'c::ok0K0xoodxoldolc;,:cccl:;:c:clc:ccldc;:cllllododxolllcccc::::::::::::::::::::::ccldxxxdolollllccc:::::c:ldlcdollllllloooooooooollllllloododdolc:;:::::;;;;,,,,,,,,,;;;::;;;;;;;;;;;;:::::;:::::
::ccccccccllcc::;;::::ccccccccllllc:::ccllloolcccclddc:::::;;;;;,'.',,,,,,;;lo::::lxOkoloc;''..'.......';ododOKXXKxxxdxkkOOOkdx0KK0kxkdllll::::locccclllloooddooooolllcc::ccc::::::ccccccccccccloddolloolllllllccccccldlcclllllllooooooooooddolllllllooooooo:;::::::::;;;;,;;;;;:::::;;;;;;,,;;::::;;;::;::;
cccc::::::ccc:;;;;;;::::ccccclllllcc::cllcloolccc:ccc::::::::::;;'..'''',cl:;;;;;coxxoolc:;'......''.,;::::codxdddddxkkO0KNNNKOkkk0Oxxdodxxcccc:::ccccccclddddddoodddolcllclcccccclllllllcc:ccccccccccllllllllllllcllcclllloddooooooooooooooddooollllllllllc:;;;:::::::::;;;;:::;::::;;;;;,,,,,;;;;;;;;;;;;;
ccc:;;;:::cccc;;;:::::::ccccclllllllcccllllllccc::::::::::::::;;;'...''',,,,,,;;:clooolc:;'......;lc;;;clccoolc:;,,:ldxOKXK0NWX0kxxxddxdodddolllc::cccclllooloodoodooollllllollllllllllccc:::::cccc::::::cclllllllcccclllllokkddoooooooooooodddooddollllcccc:;;;::ccc::::;:;;;;;;::::::::;;;,,,,,,,,;;;;;;;;
clcccccccllcc::;::ccccccccccclccccclllccclllc::::::::::::::;;;;,,,...',,;,,,,,,,;:cclcc::,'..';;;;;;:cok0Ok0x:;;,;,,;ldd0XOk0NKkOK0ddOOdllooooddollllccllcclooddooooooooooooddooddoollccccccccccc:::;;;;;;::ccccllccllllllooddddddooooooooooooooodddoollcccc::::::cccc:::::::;;;;;:::::::;;;;;;;:;;,;;;;:;;,
cccclccclc:;;;;::ccccccclllllccc::clllcccc:::::::;::;;;;;;;;;,''';c:,:oolc::cc:cllcclcc:;,,,,,;;;;;;clokkxdol;,,;:cclolcoxOkdodddddlcdxo:clcccldddddooool:clllloooooddooooodxkxdxxdlcc::cclccccccc::::;;,,,;;;:::ccclllllllooooooooollllccllllooooddooolcccc:::::ccccc:::::::::;;;;;;::::;;;;;;;;;;;;;;;;;;,
ccccllcc:;;;::ccccccccccllllcc::ccccccccccc:::;;;;::;;;;;,,,''''',;:ldkxdodxkxxddlc:::,;c;;;::;;;;;:cl:cc::;;;,,,;coddoodxolc:::;;:ccc::;cllcc:ccclllloolc::ccclooooooooooooooooodolcccc:::::::ccccc::::;;;,,,,,;;::cccclllllooooooollllcc:cllllooooollllc:::::;;:cccc:::::::;;,,;;;;;;;;;;;;;;;;;;;;::;;;,,
::::cl:;;;::c:cclllcccccccllllllcccc::::lllccccccc:;;;,'''',,,,,,,'',;clooooolc:;,,,,;,;;;::cllc::cll:::clc;;;;;;cooolclollccccl:;::cloccccccc::ccccc:::cccc:cccllllllllooollllccdoccclcc::::;;::::;;;;::;;;;;,,,,;;::cccllllllllllloolllccccllloollcccccc;;;;;;;:::c::c::;::;,,,,,,,,;;;::;;;;:::;:::::;;;;
:::::c:;;::c:cclllllcclllllllllccccc:::clllccccccccc:,'.'',,,,,,,,,''',,,;;;,,,'',;;;;;;::::;lkkoloooc,;clc;,;:::c:;;;;;:cooc::lc;;:;:c:::::cc:::cccccccccc::ccccclllllllooollccccc:::::::ccc:::::::;;;;;::;;;;;,,,,;;:::ccclllllllllooooollllooolcc::::;;;,,,'',;:::::::;;;;;;;;,;;;;;:;::;;:;;;;;::::::::;
clccccc::ccccloollclllllllllccccccccccccccccc:::cllllc;......''''''''',,,,;,;;;,,,,;;;;;;;;:::clcoo:;:;clc:;,;:clccol:::;;cl:::;::;;;;:::::::::::::::ccccccccclllllllllllllllccccc:::cc::::cccc:::cccc:::;:;;,,,,,,,,,,,;::::cccllllllooodddddoollcc:;;;,,''''..',;;;;;;;;;;:::;;;;::::;::;;;;::;;;;::::::::
ccccccccllllclllcccclcclcclccccccccccccccccccccccclllll,..  .............''''',,,,,,,,,,;;;;::;;::;;;;;;;;;,,,;:llclc;;:;;;;;;;:::;;::::::::::::::::ccccccccccccllllllllcccccccc:cl::::::::::::;;;;;::;;;,,,,,,,,,''''''''',;;:ccc:::ccllllllllccc::;;,,'.........''''''',,',;;;;;;;;;;;:::;;;;::::;;;::::::
cccccllloolclllc:cccccclcccccccccllccccccllccccccccllll:,'.. ....... .............''''''',,;;;;;;'',;;,,,,,,,,;;;;:::;'',,,,,,,;;;;;;:::::;;;:::c:::cccccccccccccccccccllllc:::;;::,,;;;;;;;,,,,,,,'''''',,,,,;;;,'''''........'',;;;;;;;;;;;;;:;;;;,''........................',:::;;;;:::::::::::::;;:::;;
cccccllccccccc:::cccccccccccllcccccccccllllccccccccccc:;,,..  .. ... ..   .....................''''''''''....''',,,,,,'',,,,,,,,,,;;;,;;;;,,;;;;;;;;:;;;;::::::;;;;;;;:::cc:,,,,,,,,,,,'''''..............''''',,'.'''''''..............'''',,,,'''.........    .  ..........'.';:::::;;;;;::::::::::::;;;;;
cccccc::::::::::::ccccccccclllccc::c:cccccclccccllllc;,'.'.. ...  .....  .... .     ...............................................''''.''''''','''''....',,,,,,,,,,'''''''.............................................'...             ........         ............',;;:;;::::;;::::::;;;;;;;::::::::;;;:
llc::::::::;;;:::ccccccccccllccccccccllccccccccclllc:,............        ............. ......... ..........        .       ...   ......................................................                               ..        ..............''..'''',''',,;;;;;;:::::::::::::::;;::::::;;;;;;::::;::::;::
c::::::::::;;::ccccccccccccccccccccllllcccc:ccccccl:'.............         ...      ...     .     ........... .............  .....     ...                                                           ....     .................''',,,,,;;,,,,;;;;;;;:;::c::::::::cccc::::::::::cc::;;;;::::::;;;;;;;;;;;;;::
::::c:::::::::ccccccclllcccccc:::cccllccccccclclcc:,................ ........     .......        ..     .. ... ..  .....   ..........  ...............     ....        ..  ..    .   .         ...  ................',''''''',,,'',;;;;;::;::;;;;;;:::cc;:::cc::ccccc::::::::::::::;;;;;::::;::;;;;;::;;;;;:""")
    print("\n You come across a really gross pile of mush, could be flesh, but I don't know, I can't really see your perspective, \n I can only dictate what happens to you based on your poor choices.")
    print("\n you have three choices this time, lucky you. \n input 1 to poke the mush. \n input 2 to poke the mush with a stick \n input 3 to run back the way you came because you have a weak stomach.")
    choice = int(input())
    if choice == 1:
        choice3()
    elif choice == 2:
        choice4()
    elif choice == 3:
        print("Who actually runs in these kind of situations? You're literally just going backwards \n progress! Never go backwards!\n now you have to do the first choice again. Good job")
        first_choice("choice")

#Redirect here if the user decides to go left in the first choice
def choice2():
    print("You went left! Cool, did you know 73% of people would've typically chosen the right path?\n Did you know that's a completely made up statistic?")
    print("""           ............      . .'..';;:cccccldxddoc:ccoxkxxkkOOOxc;''.'''..........,:::::'..'..
            .    ...........    .   .. ..,,'...;:cccll:,'::;coddxdlclcc;;;'',.....'''....;:;,,...'..
           .........   ......  .,::;;'.,',;,,:coxo:;:ol:;;'.':c;:;;:::c:;,'.',..,',:lc,''''..'......
          ..''...''.',,,'.. ..',:lddc,lkxxkxdl;,:ll:cxxodxdc:do'.'...........'.,c::l;.'.','.''..... 
          ..........''.','''''.';::cccoOKXXOd:;;;:::cddodxdoldkko:;,,,... ..'''..',;,'.'............
              .......',:cclc;,,'':,;ccccooodl,'.....':dlcododOOOkolc,...........'''''''.............
          ..''.,,,,''.:OKXK0kxx:,;,,,;ldxkOKOo,..'.',::,,cc,.;;,......,:c:;''.''''''''..............
         ..,:;;c:;,',:kWWWWWWNKkc,,'..lkkkkO0Oolldxdl:,.;c;........''.''',;'.''.....',.......... ...
         .',;cldl,...oNWWNXWWXXNKd:;:;,,,,;;'..,cdko:;',cl:;,'''..;;...,;::;,''''''.............    
      ..';;::;:c:c:,:KWWWNWWWNXXXXK0kl;;;,'.  .'':ldkdcc;,,;,.....,...,:lllc'....................   
     ..,;;;:;'.,:cllo0NNNNNWWWNNWXxdoc:,'''.....,xKKkcc:...............''',,''''..'''............   
    ...,;c::;,;cc:lolcoOXNO0NWX0Od'.;,,........:OOdo;.';. ....',..... .......',...''''...........   
  ......':l:,;cl;''..,lk0kclxocc;. .  ......   .'.         .';::;.....c:..''.,;'',;'........'...... 
......';,,,..'''....;dkkxl. .,..........    .'..    ..      ..',;,...';'...'''''','.''..............
.',..'.,;,'......'clddxkO0xo0Xkoodlcl;.,,..','      .        ....'.........';'...'.............  ...
,...:lc:;,;:,....;ddxdlloddloddkkdlc;...............         .....  .......''.................  ... 
,;''co:.....'... .,:cc,,;;,',c:;;'.........    ..''..                ...  ...       .     .'     .. 
','..'...    .    ..','',,'':ol;'........       .'''...      ..        . ...            ..,'...',,,,
..        .....  .'''...';;';lc;'.. ... ...     .::cc;'.......'.              ......   ...,;;ldolcc:
        ..','..        .,:;.'ll:;:'....  ..',,...:cccc:,'.';cc:'              .......,oxxxxxddlcccc:
     ............'''.. .',:;:do::c;'... ..';;'..     ..    ...                ......;x00OOkddoolc::;
 ...  ..',,,,;;::c:;,'.';:::cl;',,'.......''.     ..........  ..               ... .cOOxdddoolllc:;,
  .....',,.......',,'...';;;;;'....     ...',;::c:;'.... .,,....              ..',.'okxddddolllc:;;,
......''''......         ......         .:d0KK0kolc;,;;..,;,,....        .    .....;clddddolcc::;;,,
....''..'''''...                       .;kXNNNKxlcloxxxxxxd:'.';,'.  .............'lcoxxdollcc::;;,,
.',,,;;::::;,'..                         .,:;,;;codxxkkkO0Oo,':c:::;,';cc:cc:;;,...codddolllcc:;;;,,
...',,;;,,:llodo;'..                     ..'',,....',;;:xXWKo;::;,;:ldddollc:::,..;lllllllcc::;;,,,'
 ...''.. ..,:;,,;:ll:'.. ....    ..   .,..:;.'ldollooc',:cdO0Oxl:c::oxooolc:;;;,';lc::;;:::;,,,,''..
  ....    ..'....':odddooddddddddollccodolol:cxKXXXXXK00OxdkXNNK0xlccloool::,,,';cccc:;;;;,,,''''...
   ..    ..... .,cooddoooddxxkkkOOOO00000KK000OOOOkkkkOOOkkkkOOOkkxdoodolc;,'..,cc::::;;,,''''......
..............;clolllllooooooodddxxxxkxkkkkOOOOOOOOOkkxxkxxxxdddddddddooolc;'..;c::::;,,,'..........
...  ...  ..;:ccccccccllllllloooooodddodxdddxxxxkkkkkkkxxxodddolodddddollccc:;',,;;:;,'..... .......""")
    print("You come across a pond, gravity is clearly out of wack as water droplets are slowly ascending to the sky. \nIt's fantasy, it's a terribly programmed rpg game, don't question these things.")
    print("You're kind of parched but only kinda, you could go without a drink. Input 1 to drink from the pond \n Input 2 to continue down the path")
    choice = int(input())
    if choice == 1:
        choice5()
    elif choice == 2:
        choice6()
    else:
        print("Seriously dude, if you keep putting in crap that I don't even tell you is an option, \n then I'm seriously gonna manifest through the screen and make some rude gestures at you.")
    

# First choice function, 2 realistic options, one option to instantly win.    
def first_choice(choice):
    print("""....................''''''''''',,,,,,,,,,,,,,'',,,,,,'''''''''''''''.''.........................    
 ....................''''','''',,,,,,,,,,,,;,,,,,,,,,,,'''''''''''''''''........................    
.................'''''',,'',,,,,,,',;,,,,,,,,,,,,,,,,,,,',,,''''''',,''''.........................  
................'''''',,,'',,,,,,;;,,,,,,;;,,;;;,,;;;;;,,;;,,,,,,,'',,'''.......................... 
...............'''''''',,,',,,,,,;;,,;;;,;;;;,,;;;;;;;;;;;;,',,;;,,'',,''....''.................... 
...............''''''''',,',,,,,;;;;;;;;;;;;;;;;;;;;;;;;;,,,,,;;,,,,''''''''........................
................''''',',,',;,',;;;;;;;;;;;;;;;;::;;;;;;;;;;;,,,,;,,,,,''..'''.......................
...............''''',,,,,,,;;,;;;;;;::;;;;;;:;::;,,;;;,;;;,,,,,,;;,,;,'''''....''...................
............''''',''',,,;;;;;;;;;;:::::::;;:::::;;;;;;;;;;,,;;;;;;,,'''''''....'....................
.............''..'',,,;;;;;,,,,,;;;;;::::::::::::;;;;,;;;;;;;,,,;;;,''''''''''......................
........'''''''''',,,,;;;lxxdoolc:::cc::::;;;;::;;;::;;;;;;;;,,,;;:cclodxl,'''.''...................
.............'''',,,'',,,:OXXXXXK0OOkkxol::;;;;;;;;;:;;;;:cllodxkkO00KXX0l,,'''''''.................
............''''',,,,,;;;,oKXXXXXXNNNXXNKxc;;;;;;;;;;:;;;oOKKKKKKKK00KKKx;,,'''''''.................
.........''''''',',,,;,;;;:kXXXXXXNXXNXOo:;;;;;;:;;;;;;;,;cd0KKK0KK0KXX0c',,,''''...................
.........'''''''',,,,,;;;;;dXXXXXNNNNNKo;;::;;;;;;;,;;:;,,,ckKKKKKK0000d,',,,,'''.....''............
.............'',,,,,,,,,;;,cONNNNNNNNNNKkl:;;;;:;;,,,;;;,:dOKKKKKK0000Oc'',,,'''...'................
.........'...''',,,,,;;;,,;:xKXNN00XXXNNX0xl;;:;;;:;;;;:okKKK0KKOxOKKKk:'',,,'....''................
............'''''',,,,,,,,;;c0XOdc:d0XNNNXKKkc:;;:::;:oOKKKK00Oo:,:xK0o,,'''''....'...''............
.............''''',,,,,,,;,,;odc;:;;cdOXNXXXXKkc;;;cdOKXKKKKOo:,,,,;cl;',''''...''....''............
..............'''',,,,,,;;;;;;;;;;;;:::oOKXXNNX0dodOKKKXXKko:,,,''''''''''''....''..................
..............''''',;;,,,,;;;;;;;;;;;;;;cdOKXKKXKKKKKKKKOd:,,,,,''''''''''''...'.........'..........
............'''','',,,,,,,,;;,,,;;;;;;,;:;:lk0KKK000KKOd:,,,,',,,'''','''.'''.'''''.................
............''''',,''',,,,,,,;;;;;:;;;;;,,,,;d000000Kx:,,,',,''''''',''''..''''''''.................
..............''''''''',,,,,,,,,,,,,;;,,,,,,'cOO00O0Ko''''',''''''..''..''.'........................
......................'',,',,,'',,,,,,,,,,''.:O00OOO0o''..''.'''''..................................
...................'.''''''''''''',,',;llc,..:kOOOOOkc..;oddc'.''...................................
.................'''''''','''''''''.,lOXXKx;.;kOkOOkx:.c0NNNKd'.................................... 
.....................'..''''''''''..;okOkko;.;xOkkxxd;':odddo:;'....................................
......................'''..'''''''''.,:ccc'..;dkxxdxx:..,::c:.......................................
..........................''.........:kkxdc. ,dkkkxkkl..;dxdl' .................................... 
  ..................................,oxxxoc. ,dxkOOkxxo',dkdc.  ..................................  
    ................................,okxxxl' ,dxkOOkxc::col:;. ..................................   
     ............................... .';,,.. 'oxkOOOO:.... ..  ..............................  .    
     ................................        'oxkOO0Oc         .............................. """)
    
    ask_question("\nyou're stuck in the woods and see two paths going left and right, input 1 to go right, input 2 to go left.")

    choice = int(input())

    print("I'm also gonna be super vague and say that if you can type in a certain phrase when prompted, you'll just instantly win the game. \n To make it easier you can only type it in on this first choice \n good luck")

    if choice == 1:
        choice1()
    elif choice == 2:
        choice2()
    elif choice == 11112113311464115101051161520156117213535217118285670562881:
          instant_win1()
          
    else:
        print("Why are you typing in things that are outside the given instructions? \n Do it again, see what happens.")



    
    

opening()
first_choice("choice")
          
