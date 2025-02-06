import random

escolha = int(input("\tVamos jogar pedra papel tesoura? \nDigite [0] para pedra, [1] para papel e [2] para tesoura: "))
pedra = """
                                                    .......                  .                    
            .     .                              ...=*###+....            .        .   .         
                .       .                      ....+#=::--+#+:...   .. .....               .      
                .       .              ........-*#=::::::.:+#+:....:=****=.... .       .      .  
.     .               ...                ......-+#+:::::::::::.-*%*+*%#+===+#%+...                  
.                     .                ..:=**=:.::::----=---:::-+###%%*-::=+%-.                   
                    .          . .     .+=:..::-::::::-+%*--:::-*=:..-%-::-+%:....                 
                            .    .     .+=.::::::::---=+#@*=----=*%%%%*.:=+%@%#-....              
                .                      .*+--::::::::-+#%@@@%*++++++*%#:=+*@%=++#%+...             
        .                  .             -*-::::::::--=+#@%+--+*###*+==++%@%-::--=+#*..             
                                    ..++:::::-=+%@@@@%#@#=---===++*%@#=-:::::-+*#*..  .   . .    
    .  .           .             .   .-#-.:::::------*#*%@%*+*#%%%*+=-.......--+*%=...     .    . 
                        .         ....**:::::::::::-*#=+#@%%%#+=--::.....::-==+#%*...             
        .   .                       ..-#=.:-::::::::--:--+%%++#+::::::::--=++#%#***... .          
                .     .              ..+#-::::::::::::-::-=#%+-*+-::---==++#%%*===+*+..             
                    ..               .-#+.:::::::::::::::-=*%#==++==++**#%%+--:--=#**:.        .    
    .                   .         .=#=.:::::::::::::::--+%@##%@@%%%#+-:....:--=+#*..             
                ..    .             .+#-::::::::::::::::--*%@#==+=--::...:--==+++##:.     .    .  .
                    .       .   .....+#=-:::::::::::::::--*@%#++#*=----=+++=++#@@%*:..             
.  .         .       .   .  .  ...=%#%%+-:::::::::::::::=%#+#*+%%*++++*#@@@@%*+++++.              
.        .                . .:*%#=::-----:::::::::::::-----=%@#%@%@@@#*++=-:---+**..             
                        ....=#%*=:...:::==-::::::::::::-=+-:-:-*#++%#+---:...:--=+#*..             
.              . .    .-*%#+-....::::::-+*-::::::::::::---=++=+#*=%#+--:-::::-=+%#:..   .         
    .            ...:+*@#+:...:::::::::::-=**=--:::-:::::::::::-#%#%@#+=--=+*#%@@*..           .   
                ..=*%#*=:...::-:::::::::::-:-=*=--*=:::::::::::::-=*#%%@@@@%##*%%-... .             
            ...:++--::::::::::::::::::::-+#+--=---*-::::::::::::::---=++++++#@+..                  
            .....::-:::::::::::::::::-=*#+-:--+%*-::::::::::::::::::--=+++#@#...                   
                ...::::::::::-::--==*#+--=+#+--+%*---::-::::::::---=+++*%@%:..           .        .
                ..:::..:-::::--=%%*-::=#%*+=---=+#+=--:::::----=++++*@@@+...   ..         .        
.                  ..::::-=%%=.:-*@%*+=-::::-+++#+#+=====++++++#@@%-...                          
            .       ...::-*=-:-*%*++=--:::::-=+++%+%*+++++*#%@@%+:......                .         
        .   .     ......:::--+++=--:::::::-=+++*@@#+#%@@%*-::......                          .   
..        . . .          :::::::---::::::::-=++++#%@%+=-:......                .        .          
            .             .:::::::-::::::--=++*#%*=-......                   .         .            
.  .                     .:--::::::----==+*##+:...             .     .                             
                        ...-=-:----==++*##+:.....                                                   
            .           :=++==+++++#%#=....                                            .        . 
        .               .:-==+++#%#=....   .     .                                      .   .                       
"""

papel = """
                .                                                    ......=##*++==+##-......::...  
.      .                 .              .....                  ......-*##++----::-=**..=*#####-.  
                .                ........:-==-:............ ......-+##*----##-:--=+#%#**+----=%=.  
                            .......-=*%%#+-=*#%%#*++++=====+=-=#%#=-:::::-+**=+*%@%*=:::::-=*#:.  
    .  .     .              ...:=*#%%#+---:-::::::::---=*#++=-*#=-++-::::--+++*#@%*+#=:::--=*%#-....
                            ..:%#-:-:::----::::::::::::-+#@%%@%+--=%#=---++*@@#=::--*#=--+*%@%%%@*..
                        ..:%*:::::-=+**+==-----------=++#%*-::--=+#+*%@@*-:.:----+##*%@%+:::-+%*.
                        .:%*.:::::::---*%@@%#****##%@@%#+=-::-=++*@@%+---:::::--=+*@@#=:..:-=*%:.
                        . .%#.::-:::::=+++**%@@%*@=-------=*#+++#@@*-::-*@=-:--=+*%@#=-:.::-=+%+...
                        +%::::::::::-=#%#**#%%+##-:::---*#%@@#=:::::-:-*@===*%@#=-=*=-:-=+#%-....
    .            .    . ..@=.::::::::-===---=+#%=+%+--:::=**=**=::--:::-=+#*#%%+-:::-*#+=+#%+....  
.           .     . ...#%.::::::::::::::::=+##-=*%-:::-=#+-:-=-:-:---=+#%@*=:::::-=+#%%#=......  
                    ..-@::-:::::::::::::.:=+%#--+%+-::-+%+-:-------+*#@#=--:::--=+*#%@@%%#-..    
                    ..@+.:-::::::::::-::.:=+@#--+%#----*%+-:--**++#@#=:.:*#---=*#@@#+===+*#:.    
            .      .   .*%.:::::::::::::::::-=+@+--=*%---+*%=---:-#@%+-..::-+@=+#@@%+=-::-=*%+..    
                ....:@=::::::::::::::::::=+%%-:---+-+%+*%=-::::+#=:::--=++#@@#+=*#=--=*%#:...    
                .....%@*:-::::::::::::-:.:-=*@=-:-:-=%#--*%=-:::::---:-=++@@%++=::=#%+=##-... .    
    .     .......:#@#-@-:::::::::::::::.:-=*@+--:-+@@#:--*%=-::::::+#++%@@++=-:.:=+#@@#-.....      
        ....:*%@*-:.-*-:-::::::::::::::-=*%+-:-+@%=+#---+%+--::::-+%@@*+-+%=:-=+#@%=....          
    .....=#%#+-:.:::-*-:::::::::::::::-=*#=-+%@#=--+*::-=%*-:::::-+%*=::-+*%*%@%=:..              
....:+##=-:..:::::::--:::::::::::::::-----**=--:--#+:::-##=-:-::-=#+---++%@%=:...                
....-*#*+-:.::::::::::::==::::::::::::::---:--:::::-=%-:::-+%+--::-=+%%==*%@+:....                  
..:=+=::::::::::::::::::-#=:::::::::--:::::::::::::-**-:::--+*=---=++%%#@#+...                      
...::::::--::::::::::::-:--::::::::::::::::::::::::+%-::::--=++++++*%@#+...          .              
..:-::::::::::::::::::::-:::::::-::::-::::::::::::-%-:::::--=++++*%%=....               .           
...::::::::::::::::::::-=*%------::::::::::::::::-=-:-::--==++*#%#-....                .  .    .    
....:::::::::::-::---+%@+-*%#==*%*--:-:::::::::::-:::--=+++*%@#-...                   .             
...::-::::::::::-*%@*-*@@*+--:--+*%+--:::::::::--:-=+++++%@#:..                                     
...:--:::::::::---+#%#*+=--::::--+##++==--::--==+++++#@@*-.....                 .                   
.....::::::::::-+**+=---:-:::::-=+++*#+++++++++++#%@%=:.....                                        
......::::::::::----:::::::-:--=+++++#@%%%%%@%#+==:.......... ..                                    
...:::::::::::::::::::::--=+++++*#%*=::..........           .            .                       
.  ....::--::::::::::::----=+++*#%%*-...........                          .                         
.....:=--::::::::-:--=++*#%%*=:...                                                               
......-+=--:::----==+*#%%#=......            .                            .      . .              
    ..-=+=---==++++#%%#:...            .                     .                          ..        
    ...=+++++++#%%=.....                                                                         
    ......:+#@%-...    .      .                          .       .       .     .   .             
    .............    .               .                          .                               .       
"""

tesoura = """
.                 .                          .                   ....-%%*#@=..                     
    .                         . .                                ...*%+-==+@=.                    .
            .             .          .    .                      .=%*:::-++%%.                     
                                        .                    .. .-#%=::::-++@:.  .      .           
                            .                              .:*%+---:-=++@=..            .        
    ..   .     .                       .              .     ..+%*===---=+*@=...          .          
                                        .                 ..=##-::=#*=++#@-....  .    .             
                            .      .                ....=#*-::::-=#%#%*..                         
                                            .      .....+%*-::-:--=++%#-...     .    .............. 
                                                ...=##=::-:--=++#%=....   .       ....-*%%%+.... 
.                 .       .                    ...=%#==-----=++#%=....     ........:=*#*=-:=%=... 
    .           .                            . .:##-:-*%#++++#%*:...       .....:=#%=:::::-=#+... 
            .              .            ......+%-.::--+*%#*%*:...  ........-*%%+-:::-::--+*%-... 
                .                          ....+%-.:--:--++#@#:..     ....-%%*----==-----=+#@+...   
                                .. ...... ..:#*=-:::-:-=++#%=.... ...-*%#+:::::::-+%*==+*%%=...     
                            ...=****####%@%#*****+==+*%*:....=*+===-:::::::::--=##*#%*-..... .   
                    .          .:**-:-::::--==++++++@*+#%+-+**+=-::::--+-::::::-==+#@#=.... ...     
.                             .-#=::::::::::-::::::=%@@%#+=:::::::---=#*-----=+*%%+:..             
    .  .                    :**-::::::::::::::::.:-*%#+=--:::::-:--=*%==+*#%#+:.....           . 
                    .  .....=%=:::::::::-:::-==::::--#%#+=---:----=+%%%%*+.. .      .            
.  .                      ...-%=:::::::::::::-=%#=:::---=*%%#*++++*#%%#-.. .            .          
                        ..-%=:::::::------=+#@++-:::-*+...=%%#%#*++%+...                    .    
                        .=@-:::::::-=*@@@@@%%#@@+=---#%-:.=%*-::---+%=.. .                      .
                        .:@-:::::::::--=+++++#%+*@@@*+++*#%@*-:::---=+@..             .           
.         .              .%#-:::::::::::::--=++@*+++%#+++==---::...:=++@:.        .           .    
.                     ..+@+-:::--:::::::::::=+@#*%#=+%=-::-::::-==++#%#..                   .     
.                   ..:%@*=-:-::::::::::::.:=+@#@*=--#%=--===+#%%@@##%:..                         
. . .          ....+%%*+--:-:::::::::::::.:-#@++@*=-=%%**#%@%#*+=-=+%:..                         
            ...:=#@#*+++#=-:::::::::::::.::=%+-:=%%%%%%%*+=----:::-+%=..           .            .
        .....-#@%*==----*#+-::::::::::::::-==--::=#%*--+=-:::::::-=+%*..        .          .     
        ....:-*%%+=--::::::-=*=-::::::::--==---:-::--*%=--*#------=+*%@@:..  .                      
......:=%@@%*=-:::::--::::-::::::::::--*#=--:::::--=#%++*%+++*#%@%#@%-...                         
...=%@@%*=--:--:::::::-:-:-:::-==-:::----:::::::::---+%@@@@@%*+++#@=....                          
. .:++--:::::::::::::::::::.:=#--=#+-:::::::::::::::::::----=++++##:....                     .      
...::::::::::::-:::-::.:*%#=-::-*#-::::::::::::::::::-::--=+*%*-.. ..                             
...:-:::::::::::::..:=%%=--*#+--*#=-:::::::::::::::::--==+*%*:....        .         .            .
.  ..::::::::::::..::+%#=-+%#+=-:-*#=--::::::-=-:::--===++*#*:...                                   
...:-::::::..:-+#%*-+#%*=--:-:-+*+--::::::=%=-==++*#%%*-.....                    .           ..  
....::--::-=*##*==*%#+--::::::-=+++=-----==+**#%%*+=:.......       .        .             .     .
.....::::-=+=-=*##+-::-:::::::-=*#++++++*#%##+:......                                .           
. ........:::::-=--:::::::::-:--=++++++#%%#=........     .                            .            
.      ....::::::::-::::::::---=++++*#@%*-...                                                       
        .....::-::::::::::--=++++*#@%+:.....                                                        
        ...:::::::::-:-=+++#@@@+:...      .  .              .                 .            . .   
.        ....-=----:-=++*@@@*:....       ..     .     .                                           
        ...-===++=+++%@@+:...                                .                                  .
            .....:=+++*@#-..                   .                       .         .                .                        .                      .             
"""
if escolha == 0:
    print(f"Você escolheu pedra: \n{pedra}")
elif escolha == 1:
    print(f"Você escolheu papel: \n{papel}")
elif escolha == 2:
    print(f"Você escolheu tesoura: \n{tesoura}")
else:
    print("Escolha a opção correta!")


opcoes = [pedra, papel, tesoura]
computador = random.randint(0, 2)
print("O computador escolheu:")
print(opcoes[computador])


if (escolha == 0 and computador == 1) or (escolha == 1 and computador == 2) or (escolha == 2 and computador == 0):
    print("Você perdeu, mais sorte na próxima vez!")
elif (escolha == 0 and computador == 2) or (escolha == 1 and computador == 0) or (escolha == 2 and computador == 1):
    print("Você ganhou, parabéns!")
elif escolha == computador:
    print("Empate")