#working on it
# 5 kinds of units(Soldiers)
import random
import time
import asyncio
unitconverger = {}
AIunits = {}
maxunits = 15
board=[]
rows=23
columns=57
#The board
for i in range(rows):
  row=[]
  for i in range(columns):
    row.append("~")
  board.append(row)
def printboard():
  Boardstring=""
  for row in board:
    for cell in row:
      Boardstring+=cell
    Boardstring+="\n"
  print(Boardstring)
printboard()
print("\033c")
#Starting income
income=500
AIincome=500
#the units
AIunitconverger={}
giant="|_[]-|"
wizard="o!"
c4u710nc0l0rch4n63 = "\033[0m"
r3dch4n63c0l0r = "\033[91m"
archer="0|"
knight="|O|"
swordsmen="{O/"
AIgiant="|_()-|"
AIwizard="a!"
AIarcher="A|"
AIknight="|A|"
AIswordsmen="{A/"
MaxUnitLength = len(giant)
unitconverger["giant"] = giant
unitconverger["wizard"] = wizard
unitconverger["archer"] = archer
unitconverger["knight"] = knight
unitconverger["swordsmen"] = swordsmen
AIunitconverger["AIgiant"] = AIgiant
AIunitconverger["AIwizard"] = AIwizard
AIunitconverger["AIarcher"] = AIarcher
AIunitconverger["AIknight"] = AIknight
AIunitconverger["AIswordsmen"] = AIswordsmen
#The projectiles
laser="!"
arrow="|"
#Making towers
towerLtop= "______________"
towerLmid="|_    - _   - |"
towerLbottom="______________"
for i in range(len(towerLtop)):
  board[rows-3][i]=towerLtop[i]
for i in range(len(towerLmid)):
  board[rows-2][i]=towerLmid[i]
for i in range(len(towerLbottom)):
  board[rows-1][i]=towerLbottom[i]
towerL=towerLtop+towerLmid+towerLbottom
printboard()
print("\033c")
#Setup
healthR=500
healthL=500
healthM=2000
AhealthR=500
AhealthL=500
AhealthM=2000
towerMtop= "______________"
towerMmid="|_    - _   - |"
towerMbottom="______________"
towerM=towerMtop+towerMmid+towerMbottom
for i in range(len(towerMtop)):
  board[rows-3][i+columns//3]=towerLtop[i]
for i in range(len(towerMmid)):
  board[rows-2][i+columns//3]=towerMmid[i]
for i in range(len(towerMbottom)):
  board[rows-1][i+columns//3]=towerMbottom[i]
printboard()
print("\033c")
towerRtop= "______________"
towerRmid="|_    - _   - |"
towerRbottom="______________"
towerR=towerRtop+towerRmid+towerRbottom
for i in range(len(towerRtop)):
  board[rows-3][columns-len(towerRtop)+i-1]=towerRtop[i]
for i in range(len(towerMmid)):
  board[rows-2][columns-len(towerRmid)+i-1]=towerRmid[i]
for i in range(len(towerMbottom)):
  board[rows-1][columns-len(towerRbottom)+i-1]=towerRbottom[i]
#Printing the board for the game  
printboard()
AItowerRtop= "______________"
AItowerRmid="|_    - _   - |"
AItowerRbottom="______________"
AItowerMtop= "______________"
AItowerMmid="|_    - _   - |"
AItowerMbottom="______________"
AItowerLtop= "______________"
AItowerLmid="|_    - _   - |"
AItowerLbottom="______________"
print("\033c")
#Making towers
for i in range(len(AItowerLtop)):
  board[0][i]=AItowerLtop[i]
for i in range(len(AItowerLmid)):
  board[1][i]=AItowerLmid[i]
for i in range(len(AItowerLbottom)):
  board[2][i]=AItowerLbottom[i]
for i in range(len(AItowerMtop)):
  board[0][i+columns//3]=AItowerLtop[i]
for i in range(len(AItowerMmid)):
  board[1][i+columns//3]=AItowerMmid[i]
for i in range(len(AItowerMbottom)):
  board[2][i+columns//3]=AItowerMbottom[i]
for i in range(len(AItowerRtop)):
  board[0][columns-len(AItowerRtop)+i-1]=AItowerRtop[i]
for i in range(len(AItowerMmid)):
  board[1][columns-len(AItowerRmid)+i-1]=AItowerRmid[i]
for i in range(len(AItowerMbottom)):
  board[2][columns-len(AItowerRbottom)+i-1]=AItowerRbottom[i]
printboard()
#Defeat enemy AI
# Use your units to destroy their castly thingy
#AI:Randomly spawn random AVAILABLE units at random times and - cost from your bank account 
#different attack damage
'''
for unit in uniƒts:
  if unit."attackWithWeapon":
    Ahealth-=15
'''
#Costs
giantcost=70
wizardcost=45
archercost=40
knightcost=35
swordsmencost=20
AIgiantcost=70
AIwizardcost=45
AIarchercost=40
AIknightcost=35
AIswordsmencost=20
playerunits={}
playerunits["wizard"] = []
playerunits["giant"] = []
playerunits["archer"] = []
playerunits["knight"] = []
playerunits["swordsmen"] = []
AIunits["AIwizard"] = []
AIunits["AIgiant"] = []
AIunits["AIarcher"] = []
AIunits["AIknight"] = []
AIunits["AIswordsmen"] = []
#counting to see how many characters are on the board at a certain time.
def countUnits():
  numPlayerUnits=0
  numAIUnits = 0
  for unit in playerunits:
    numPlayerUnits += len(playerunits[unit])
  for unit in AIunits:
    numAIUnits += len(AIunits[unit])
  return numPlayerUnits, numAIUnits
#Moving characters!
def move_characters(mode):
  global playerunits, AIunits
  units = playerunits
  
  if mode == "player":
    units = playerunits
  if mode == "AI":
    units = AIunits
  for unit in units:
    coordinate_index=0
    for coordinate in units[unit]:
      row=coordinate[0]
      column=coordinate[1]
      if mode == "player":
        #newrow=row-1
        newrow = row
        newcolumn=column+random.randint(1,1 )
        #newcolumn = column
      elif mode == "AI":
        newrow = row+1
        #newcolumn = column+random.randint(-3, 3)
        newcolumn = column
      if newcolumn <= MaxUnitLength:
        newcolumn = MaxUnitLength
      if newcolumn >= columns-MaxUnitLength:
        newcolumn = columns-MaxUnitLength
    #  print(str(newrow))
   #   print(str(newcolumn))
      if mode == "player":
        if newrow < 3:
#TODO
# stop before the castlemobobber
#Things to change for AI units to move: AIunits instead of playerunits, Names of units, and direction of movement,
#  and attacking the player's castle instead of the AI's castle, where they stop and spawn
#        wizard."attack"
   
          pass
        else:
          playerUnitLength = len(unitconverger[unit])
          
# #           print(len(wizard))
#           for i in range(playerUnitLength):
#             board[newrow][newcolumn+i]=unitconverger[unit]
#             board[row][column+i]="~"
            
          # playerunits[unit][coordinate_index]=[newrow,newcolumn]
          # coordinate_index+=1
          if unit == "giant":
            for i in range(len(giant)):
              board[newrow][newcolumn+i]=giant[i]
              # board[row][column+i]="~"
              if newcolumn-column == 1 or newcolumn-column == -1:
        #        for i in range(1):
                  board[row][column+i] = "~"
             # else:
              #  for i in range(2):
               #   board[row][column+i] = "~"
            playerunits[unit][coordinate_index]=[newrow,newcolumn]
            coordinate_index+=1
          if unit == "archer":
            for i in range(len(archer)):
              board[newrow][newcolumn+i]=archer[i]
              board[row][column+i]="~"
            playerunits[unit][coordinate_index]=[newrow,newcolumn]
            coordinate_index+=1
          if unit == "knight":
            for i in range(playerUnitLength):
              board[newrow][newcolumn+i]=knight[i]
              board[row][column+i]="~"
            playerunits[unit][coordinate_index]=[newrow,newcolumn]
            coordinate_index+=1
          if unit == "swordsmen":
            for i in range(len(swordsmen)):
              board[newrow][newcolumn+i]=swordsmen[i]
              board[row][column+i]="~"
            playerunits[unit][coordinate_index]=[newrow,newcolumn]
            coordinate_index+=1
      elif mode == "AI":
        if newrow > rows-3:
          pass
        else:
          if unit == "AIwizard":
            for i in range(len(AIwizard)):
              board[newrow][newcolumn+i]=AIwizard[i]
              board[row][column+i]="~"
            AIunits[unit][coordinate_index]=[newrow,newcolumn]
            coordinate_index+=1
          if unit == "AIgiant":
            for i in range(len(AIgiant)):
              board[newrow][newcolumn+i]=AIgiant[i]
              board[row][column+i]="~"
            AIunits[unit][coordinate_index]=[newrow,newcolumn]
            coordinate_index+=1
          if unit == "AIarcher":
            for i in range(len(AIarcher)):
              board[newrow][newcolumn+i]=AIarcher[i]
              board[row][column+i]="~"
            AIunits[unit][coordinate_index]=[newrow,newcolumn]
            coordinate_index+=1
          if unit == "AIknight":
            for i in range(len(AIknight)):
              board[newrow][newcolumn+i]=AIknight[i]
              board[row][column+i]="~"
            AIunits[unit][coordinate_index]=[newrow,newcolumn]
            coordinate_index+=1
          if unit == "AIswordsmen":
            for i in range(len(AIswordsmen)):
              board[newrow][newcolumn+i]=AIswordsmen[i]
              board[row][column+i]="~"
            AIunits[unit][coordinate_index]=[newrow,newcolumn]
            coordinate_index+=1

# An asynchronous(seperate) function
#passive income.
async def passiveIncome(delay):
  global income
  #Says to wait then move on
  await asyncio.sleep(delay)
  income+=50
#setting the keys of spawning and spawning them
def spawnUnit():
  wizardspawn="w"
  giantspawn="g"
  archerspawn="a"
  knightspawn="k"
  swordsmenspawn="s"
  # This is how to spawn a wizard.
  numplayerunits, numAIunits =  countUnits()

  print(str(numAIunits))
 # spawn=input("To spawn a wizard, press w.:)Cost: $45 To spawn giant, press g:70 dollRS.Archer:40 and a, knight: 35 and k, for swordsmen,  20 and s")
  spawn = random.choice(["w", "g", "a", "k", "s"])


  if numplayerunits <= maxunits:
    if spawn==wizardspawn:
      for i in range(len(wizard)):
        board[rows-4][columns//2+i]=wizard[i]
      playerunits["wizard"].append([rows-4,columns//2])
    elif spawn==giantspawn:
      for i in range(len(giant)):
        board[rows-4][columns//2+i]=giant[i]
      playerunits["giant"].append([rows-4,columns//2])
    elif spawn==archerspawn:
      for i in range(len(archer)):
        board[rows-4][columns//2+i]=archer[i]
      playerunits["archer"].append([rows-4,columns//2])  
    elif spawn==knightspawn:
      for i in range(len(knight)):
        board[rows-4][columns//2+i]=knight[i]
      playerunits["knight"].append([rows-4,columns//2])  
    elif spawn==swordsmenspawn:
      for i in range(len(swordsmen)):
        board[rows-4][columns//2+i]=swordsmen[i]
      playerunits["swordsmen"].append([rows-4,columns//2])
  if numAIunits <= maxunits:
    aKeys = AIunits.keys()
    aKeys = list(aKeys)
    aUnit = random.choice(aKeys)
    for i in range(len(AIunitconverger[aUnit])):
      board[4][columns//2+i]=AIunitconverger[aUnit][i]
    AIunits[aUnit].append([4, columns//2])  
async def mainGamePlayLoop():
  #This print statement clears everything
  print("\033c")
  board[0]="~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
  printboard()

  #await passiveIncome(5)
  #spawnUnit()

  move_characters("AI")
  move_characters("player")
  timeIncome = asyncio.create_task(passiveIncome(1))
  await timeIncome
#Shortest but most important part of the thing
#^
#| is the computer
#The while loop is CPU
for i in range(1):
  spawnUnit()
  printboard()
#while True:
#  asyncio.run(mainGamePlayLoop())
#Get coins if you defeat enemy unit chlorofluorocarbon
'''
if AIgiant."defeat":
  income+=50
if AIwizard."defeat":
  income+=25
if AIarcher."defeat":
  income+=15
if AIknight."defeat":
  income+=20
if AIswordsmen."defeat":
  income+=10
if giant."defeat":
  AIincome+=50
if wizard."defeat":
  AIincome+=25
if archer."defeat":
  AIincome+=15
if knight."defeat":
  AIincome+=20
if AIswordsmen."defeat":
  AIincome+=10
'''
#Subtract money from your income if you spawn a unit

#Passive income
time.sleep(5)
income+=50
#Units next to each other will attack each other
'''
if "close":
  "unit".attack("AIunit")
'''
#Archers and wizards are long ranged
'''
archer."range"=6"spaces"
wizard."range"=8"spaces"
AIarcher."range"=6"spaces"
AIwizard."range"=8"spaces"
'''
#Real time
'''                                                                                                    
                                                                                                    
                   ..                                                                               
                  .-*-.                                                                             
                  :*#*:...                                                                          
                  .**#*#:.                                                                          
                  .*%*.                                                                             
              .. .:##=.                                                                             
              .=##**+%+.                                                                            
        ..=-.. ....-#*%-. ..:.                                                                      
        .+#++*. .=+*##%%...+*.    .......                              .                            
       .=##=+#+..+#***#@%-..*+..:+#########=..                        .-.                           
       .#%###*#.=***-***#%==#:-%%%#####*##*###=.                     .:::..                         
        .-%%+#+.+*#*****#*+#+. .*####********###+..                  ..:-:..                        
          .-**++=*###**#*%%*. ..####****+++#%#%%%%:                   .:::::...                     
            .:=*#%%%#*#%@*.   .######**+*#####%%%@-.                  ..:::--::.                    
                 ...##%%%#.  .=######***##%@%%#%@@:.                 .:::::-::.                     
                   .+*#%@%. .-#######**===**+*#%@@:.               ..::.-=:--:..                    
                   .-%##%@+.:#######**++++-+++#%@@=.              ..:..::::=+-:....                 
                    .*%#%@%-#######*+*##**##**@%%%%+.             ..:.-+=::-=--...                  
                     :#%#%@####*****#**===+*#%%#%%###..            .:.=---:::::.:.               
                     =+##%%###***#%##+#+=-:=#%#*#%%###.             .::=--::::...                   
                     .==###%#**%%###**#*+==+**%+#%%###-.             ..:.::...... .                  
                     ...***%####*****+**+==+*+%*@%%%#+.               .:.......--:+.           
                      :****#+*****+*##+*#*=:=**%#%%%*..               ..:. .--=-**..                
                    .+**---+**#******+++**#*+==%#*%###+.             .:-:...:=*#*.                  
                  ..*##*-=-=+*#**++++-==+###+=*#%###%###*.         ..-:::::--+#*.                   
                 .:##*#*--==++#*#*====+*###%%+*#%%%%######=.       ..--:::--+#=                     
                .=#####---==+*###*=-+#####*#%#*%%*##%%#####*.      .----=+*#=..                     
               .:####+=--==##%%***#%%#%*==**#%%@%#*##%%%%%%%+.  ..+---+*#-..                        
               :##**%%=-=+%@*#%#%%%%#=++=+***%+%%%***%%%%%%%%-..===-=+#=.                           
              .=###**=-=+%@@#*%@@%%*+-=--=**##*#%%***%@%%@%%#**==++**#%=.                           
             .=###+*#*+*#%@@%+%@@@%%*++==+%##+=##%%**%@@%%#***=+#++#%*-                             
            .=*#%*#=-=+#@@@@@#*%@@@%##+=+#%#%%%%%@@%#%@@%%#*****#%%%%*.                             
            .%@%##*++++#%@@@@%+#@@%%%%%#*%%%##@@%%@@%@@@%%#*####%%@@%%%+..                          
            ..+###%#%%%%%@@%@@*+%@@%%%%%%%@@@@@@@@@@@@@@%%###%%%%@@@@%%%%#.                         
              .###%#*%%%@@@@@@%*%@@@@@@%%%%@@%@@%@@@@@@@@@%##%%@@@@@@@@%%%%*.                       
              :##%%%%#%%@@@@%@@*#%@@@@@@%@@@@@@@@@@@@@@@@@%%##%@@@@@@@@%%%%%%-                      
              :####%%%@@@@@@%#@@#%@@@@@@@@@@@@@@@@@@@@@@@@@%%%%%%@@@@@@@@%%%%%+.                    
             .=####%###@@@@@%*%@%%@@@@@%@@@@@@@@%%@@@@@@@@@@%%%%%%%%%@@@@@@@%%%*.                   
             .*####@%##*%@@%%##@%#%%@@@@@@@@@@@@@@@@@@@@@@@@@%%%%%%%%%%%%%%@@%%%+.                  
            .=####*%@%**#%@%%%#%%*#@@@%@%%@@@@@@%@%@%@@@@@@@@@%%%%%%%%%%%%%%%%%@@-                  
            .#####*#@@#+*%@%%%%#@#*%@%@%%%%@@@@@@@@@@@@@@@@@@@@@%%%%%%%%%%%%####%%.                 
           .=#####**@@@#+#%%%%%#@%+*@@@%%%%%@@@@@@@@@@@@@@@@@@@@@@@@%%%%%%%%%%%#%##..               
           .#######*@@@@***#%%%%%@#+%@%%%%%%@%%@@@@@@@@@@@@@@@@@@@@@#:...:-=*#%%%%##+.              
          .=#######*@@@@@***#%%%#@#+#%%%%%%%%%%%@@@@@@@@@@@@@@@@@@@@@@%%+..     ..=*##.             
          .*#######*%@@@%%*++#%%%@%**%%%%%%%@%%%@@@@@@@@@@@@@@@@@@@@@%%%%%%#:.      ....            
          :###%######@@@%#*++*#%%@@*#%%%%%%%@%%%@@@@@@@@@@@@@@@@@@@@@%%%%%%%%%+..                   
          =###%#####*@@@%***=+#%%@@#+#%%%%%%%%%%@@@@@@@@@@@@@@@@@@@@@@%%%%%%%%%%#-.                 
         .+##%######*@@@%#***+*%%@@@**%#%%%%%%%@@@@@@@@@@@@@@@@@@@@@@@%%%%%%%%%%%%%*.               
         .*##%######*@@@%#***+*%%%@@#**%#%%%%%%@@@@@@@@@@@@@@@@@@@@@@@@%%%%%%%%%%%%%%*..            
         .*%########*@@@##***++#%%@@%**%##%%%%%@@@@@@@@@@@@@@@@@@@@@@@@@%%%%%%%%%%%%%%%*.           
         .#%########*@@@##**#*##%%@@%#+%###%%%%%@@@@@@@@@@@@@@@@@@@@@@@@%%%%%%%%%%%%%%%%%-.         
         .#%%%#######@@@##****#%%%%@@#*#%###%%%%@@@@@@@@@@@@@@@@@@@@@@@@@%%%%%%%%%%%%%%%%%*.        
        .:%%%%%%%####@@@##****#%%%%@@##*%####%%%%@@@@@@@@@@@@@@@@@@@@@@@@@@%%%%%%%%%%%%%%%%#.       
        .-%%%%%%%%%##@@@##**###%%%%%@%#*#%#####%%@@@@@@@@@@%#@@@@@@@@@@@@@@@%%%%%#:*=::=+%%%#:      
        .+%%%%%%%%%##@@@###*###%%%%%@%##*%###%%%%%@@@@@@@@@@#%@@@@@@@@@@@@@@@%%:..       ...+%:.    
        .+%%%%%%%%%##@@@%#######%%%@@@##*#%##**#%%%@@@@@@@@@%#%@@@@@@@@@@@@@@@#.             .:.    
        .+%%%%%%%#%%#@@@%#######%%%@@@%##*%##***#%%%@@@@@@@@@##%@@@@@@@@@@@@@@@#.                   
        .+%%#%%%##%%#@@@%#######%%%@@@@###%%#*+**#%%%%@@@@@@@##%%@@@@@@@@@@@@@@@#.                  
        .+%%%##%###%#%@@@%%%%%%%%%%@@@@%###%##++*#%%%%@@@@@@%##%%@@@@@@@@@@@@%@@@#.                 
        .=%%##########@@@%%%%%%%%%%@@@@%%%#%%**+**##%@@@@@@%%#%%%%@@@@@@@@@@%%@@@@#.                
        .-%###########%@@@%%%%#%%%%@@@@@%%##%+++***###%%@@@%%%#%%%@@@@@@@@@@@@%%@@@%.               
        .:%#####*######@@@@%%%%%%%%@@@@@%###%****+**##%%%@@@%####%%@@@@@@@@%@@@@%%@@%.              
        .:%%#**########@@@@%%%%%%%%@@@@@#**##%*****#####%@@@@%#%#%%@@@@@@@@@@@@@%%%%@*.             
        .:%%############@@@@%%%%%%%@@@@@#**##%*+***#*#####@@@@###%%%@@@@@@@@@@@@@@@@@@=.            
        .:%%###***##%%##%@@@@%@@%%%@@@@@#***#%%+***#######@@@@@###%%%@@@@@@@@@@@@@@@@@%.            
        .-%%#%@@@@@@@@%##@@@@%@@%@@@@@@@%**+##%*+**#######%@@@@%###%%%%@@@@@@@@@@@@@@@=.            
        .-%%@@@@@@@@@@@@@@@@@%@@%@@@@@@@%*++##%#**#########%@@@@%%%%%%%@@@@@@@@@@@@@#..             
        .-%@@@@@@@@@@@@@@@@@@@@@%@@@@@@@@*+**%%%***#######%%@@@@@%%%%%%%@@@@@@@@@@=.                
        .-%%@@@@@@@@@@@@@@@@@@@@@@@@@@@@@****##%#***#######%%@@@@@%%%%%%@@@%@%*:.                   
        .-%%%%@@@@@@@@@@@@@@@@@@%@@@@@@@@*#***#%%*#*########%@@@@@%%#%%%#+...                       
        .:%%%%@@@@@@@@@@@@@@@@@@%@@@@@@@@##***%#%##*########%%@@@@@%%%%%=.                          
        ..%@@@@@%%%%%@@@@@@@@@@@%@@@@@@@@#***#%#%#############@@@@@%%%%%:.                          
         .%@@@%%%%%%%%%@@@@@@@@@%@@@@@@@%##*###%%%##########%%%@%@%-%%%#.                           
          .#@%%%%%%%%%%@@@@@%@@@%@@@@@@@%##*###%%%#########%%%%%=...=%%#.                           
          .%%%%%%%%%%%%@@@@%%=-+%@@@@@@@%######%%%###########%%=    .#%+.                           
          .#%%%%%%%%%%%@@@@%%...%@@@@@@@########%#%###%#%##%%#%+.   .=+.                            
           .+%%%%%%%%%%@@@@%#...%@@@@@@*#########%%#####%%#####*.                                   
            ..:+%%%%%%%%%@%%*...%@@@@-. ...#@@@@@%%%%:..........                                    
               ...-#%%%%@@%%+..:%%+:.     .%@@@@@%#%@@@*..                                          
                 .=%%%%@@@+..   ..       ..@@@@@@@%%@@@@@@%+:..                                     
                .=%%%%%@@@:               .#@@@@@@@%%@@@@%@@@@@%:.                                  
               .#%%%%%%@@*.                  ......#%%%%%%%%%%%*..                                  
              :%%%%%##%%=.                         =#%.                                             
              .#@%%%%%%%.                          .##-.                                            
               ...:--:..                           ....                                             
                                                                                                    
'''

'''                                   .......-=:........                                               
                                   .....-*%%%##+.....                                               
                                   ...=%%@%%%%%%%+:..                                               
                                   ...+@@@@@@%%@%%#:.                                               
                        .............-%%%@@@@@@@%*+*:.....                                          
                        .....++-:...:#%#***#%%%*+-=#*.....  ...  ..                                 
                        ......-*@%+-*@%#*+=-:-+-=--*%-.... ........                                 
                      ..........-*@@@@%%#+++==-+*+##%+......r...:=:.                                 
                      ...+#%%@@@@@@@%@@@@@@@##%%@%##%#+..-+*#%%*-..                                 
                     ........::-+#%@@@%##*#%*+##*##+#%%%%@@*=:.....                                 
                     ......:+##@@@@@@@@@@@@%%#**@%####%@@#........                                  
                     ..:+%@@@@#+==-+@@@@@@@%%%%##%####=*@@-............                             
                     ..--::......-#@@@@@@@%%%##*%###*#*%@%*+==--::.....                             
                     .........-*%@%%%@@@@@@%%%%%#%#*#*##*##%%%%%##=....                             
                     ....:-+*%@%####%%@@@@@@@%%%%%%%%#%##*+==-.......                               
           ............*%%##**+****%%%%@@@@@@%%#%%%%%##*====:=--..........                          
           ..............-=+++**+*#%%%%#%@@@@@@@%%%%%#**+=+:+=+=+-:.......                          
           ..........:-===+++*****###%%#**#%%%%%#%%#**+===+=+##+****-.........                      
           ......:-===+===++**++********###%%%%%%#=--::::--:-+*=++-:.=+:.........                   
           ....-=+++++===+**++*****+++++++**+***=:..:---::::-=*+==+=.==..--......                   
        .....-+**+*++==+***++***++==+++++++++++=..-+****+++=-+++*==:.-+::-++-:....                  
       .....+##*****+++***+++++++==++++++**++++..:+++*+=-:-+*=+++**+=-=*--=+*+-.....                
       ....+########*****+*+++++======+++++====..:=+++++*+::+**+++**+++=*+=--=-=:....               
    ......-%%%%######***##**+++========++++=-==...:++++++:.-++******+##+*##*##*-.......            
    ......*%%%%%######%%##*+++*++++*+++++*##=-+++-::.:..::::=+==+%%%#*#%#*====+==:......            
    .....:#%%%%%%%%%%%%%%#*******+++*+===+++=.:==+==------=*#*##%@@@%###%%#%%**##=......            
    .....-%%%%%%@%%%%@@@%%#**+**+++++**+++#+--:..-====++++++=*#%@@@@%#*+*#@@**#%*+......            
    .....-%%%%@@@@@@@@@@%###**##*******###%*==-===-:::--==+****#%@@@@@@%*#%##%###+......            
    .....=%%%@@@@@@@@@@@@%%%##########%%%%%%#*##*==+++++*****###%@@@@@@%@%#@@###**=.....            
     ...-#%%%@@@@@@@%%%@@@@%%%%##%%%%%%%#*##*#%%##******##%%@%###%@@%#%@%%%%#%%@%#+-....            
    ....+%%%%%######%%@@@@@@@%%%%%%%##***##%#**##%%@@@@@@@%%%%#*#%@@#+#*+**+=*%*+++-....            
    ...-#%%###***##%%@@@@@@@@@%%###****###%#%%#****##%%@@@@@%###%%%@%##*+*++=**+=*%#-...            
......-#%%####**##%@@@@@@@%%%%##%########%####%#####%%%%#%%%%#%%%%%@@%%*++*+=*++*#%%*......         
....:=##%######%%%%@@@%@@@@@%%%%%%%%%##%%%%%%%##%%%%%%%%%%%@%%%%#%%%@@%**##+=**+*###*=-.......      
...+#%%##%###%%%%@@@@%+%%@@@@@%%%%%%%%%%%@@@@%%%%%%%%%%%%%@%%%#%##%%@@@##%%*+##++##*++#*=:....      
..+%%%%#####%%%@@@@@#-=@@%%%%@@@%%%%%####***###%%%%@%@@@@%%%###%%##*+%@@#%%#+*#*==*###%###=...      
.-#%%######%%%@@@@@%=.=@@%%%%@@@@%##**************##%@@@@%###%%%%##+.:%@%#%%#+*#*==###%%%#-...      
.=%@@@%##%%%@@@@@@#*=.:%%@@@@@@%%########%%%########%%%%@@%%%%%#**#=...#@%#%%#*+*#*###%@@*....      
.:#@@@%%##%@@%%%%##=...#@@@@@@%%%%%##%%%%%%%%%%%%%%%%%%%%%@@%%#####-..-@@@%####**##%%%%%%+....      
..+%%%%@@@%%@@@@%%+-...-@@@@%%%%%%%%%#***####*##%%%%%%#####%%@%%##*...#@%%##%#*###**%####=....      
.:#%%%####%%%%@%*-......%@@@%%%%%%%%%###%%%%%###%%%%%%%%%%%%#%%###=....*%%%%#%%%%###%%###+....      
.+%%%###########-.......-%%@@@@@%%%%%%%%%@@@%%%%%%%%%%%@@%%%%%##*+.....:*%@@%%%%%##****+*+=-:.......
:#%%#%%%########-........#@@@@@@@@@%%%%%%##%%%%%%%@@@@@@@%%%@%###=.....-*#%%##*****####%%%##**+=-:..
:%%%%###%#%%%%%#+........+@@@@%%%###*##%@%%@@%##**+*#*#%%@%@@@%%#:....:@@@@%%%#######%%%%@%#+:......
=%%%##%%###%%%%%=.......:#@@@#****+***#*++++*##+++====--+%@@%%***-....:%@@@%%%%%%@@@@@@@@@%*:.......
#%%%%%%%%%%%%%%*:......-##*########%%#+==---==*%%#*****+=+***+**+++:...*@@@@@@%%%%#######*=::.......
#%%%%##%@%%@@%-.......=%%%#%#*%%##%##%@%%%%%@@%#####%%#*##+****++*+=....+%%%###**+++*#####%%%%#++=-:
%%#####%@@@%=........:*%*%%#*##%#**+++==========++*#%%%#***++*++****-..+%@@@@%%%%#####%%%%%%%*=-....
%%##%%%%%%*..........+#%##%%%##%%#*++++=+=====+++*####*###*+++***++**=.:*#%@@@@@@@%%%%%%@@%%*+-.....
##%%%%%%#+..........=#%#####%#*++++*###%%######**++++**###%#****#*##*++...-%@%%##**+++*##%%#*##*+-..
#####%%#*:..      .:*#%%##%%#####****+++++++++****######%%%%###*%##**-+:..-%@%%###**####%%%%#=:.....
#####%%%*:..      .:*%%%%%%#%%%%%#***************#%%%%%%##%#@@%#*%###=-...-%@@@@@@@@@@@@@@@%=.......
%%%%%###*:.........-#%@@@@@@%%##*****###%%%#####***###%%@%%%%@%%%%###*:....-%@@%%%%#%%####+:......  
*+++++***-........-#@@@@@@%@@@@@@%#*++++*++++++*%%@@@@@@%%%@%%%%%%#***=:..=#@@%#**#**###%#*###+-....
*++**+*#*=.......*%%@@@@@%%%%%%%@@@@@@@@@@@@@@@@@@@%%%%%%*####%%%%#***+++*+*@@%%#*###########%%#*=:.
*+*####*#*:.....+%%%@@@%%%%%%%###%%@@@@@@@@@@@@%%######%%##***#%%##*#**++*##%@@@@@@@@@@@@@@@%=:.....
#**#%%%%%#-....-*%@@@@%%%%%#***#######%####%%#*##*#****########%%#*****+++:..:-*%%@%%%%%%#=-:.......
%%%%%@@%%%*.....+%@@@%%%%%%#***####*##%#***%##****#****#%##%**#****##*#**+-...-#%@@@@%%%%#:...      
%%%%%%*%%##:...=%@@@%%%%#%%#**##*#*#%%%#**#%%%#*#*###*##%%%%%##%###%%**#**=...=%%%@@@%%%%*....      
@%%%%-.+%%%:..=%@@@@%%%%#%%%#*#**#*###%%##%%###*#**#**#%%%%@@###%%%%%*+#***-..=%%*-@%%%%%+....      
%%%%+..-#%#:.+%@@@%@%%%%%%%##*#**#####%%#%%######*##*##%%%%@@%%#*#%%#*#%###*-.+%%=.#@%%@%-....      
#%%##=..=#*.#%@@@@%@%%%%%%%##*##****#*##%#####*#***#*##%%%%@@@%**##*#**%#*#**--%%:.-%%%%*.....      
-#%%%%#*-..+#%@@@@%@%%%%%%%%#*#*####**#****#**##***###%%%%%@%%@%%####%%%#*#**+:=-.:+%%#*......      
.:+#%@%%#=.:+%@@@@%@%%%%%%%%###**####*****##***#***###%%#%@@%%%@%%%%@%%%###**+-..=@@@%#-......      
.....:---:.=%@@@@@%@%%%%%%@%%#**#*#**###**###****####%%%%%@%%%%%%%%%%%%%#**#*+=.=%%%*-........      
    ......:#@@@@@@%@%%%%%%@%%%###*##*#######*##*####%%%@%%@%%%%%%%%%%%%%#**#*+-.:=-:....            
    .......+%@@@@@%%%%%%%%@%%%###**########**#*##%##%%%%%@@%%%%%%%%%%%%%#**#**=.........            
    .......:%@@@@@@%@@%%%%%%%%#%%#######*#****#%%%##%%@%%@@%%%%%%%%%@@%%#**##*-.........            
        ....%@@@@@@@@@@@%%%@%%##%######***#########%%@@%@@@@%%%%@@@@@%%%%#####-..                   
        ....%@@@@@@@@@@@@%@@@@%##########*#*######%%%@%%@@@@%%%@@@@@@@@%#*###%+...                  
          ..#@@%@%@@@@@@@@@@@%%%####################%%@@@@@@@@@@@@@@@@@%=-*##%*...                  
          ...==-=:#@@@@@@@@@@%%%##%%#####*###%#####%@%@@@@@@@@@@@@@@@@%*..+%%%*...                  
           .......=@@@@%@@@@@%%%%%%%#%%#%##%%%%%%%%%@@@@@@@@@@@@@@@@@@%=..-#+#=..                   
            ......-%@@%%@@@@@%%%###%%%##%#%%%###%%%@@@@@@@@@@@@@@%@%@@%-....:-...                   
                 .:#@@%%%@@@@%%%%%#%%##%%##%##%%%%%@@@@@@@@@@@@@@%@%%%%:.........                   
               ...:%@@@%%%@@@@%@%%%@%#%%%%##%%%%@%@@@@@@@@@@@@@%%%@@@%#:...  ....                   
               ...:%@@%%%%@@@@@@@@%@@%%%@%%%@%@@@@@@+%@@@@@@@@%%%%%@@%#:..                          
                 ..#@@%%%%%@@@@@@@@@**%@@%%%*#%@%##@-+@@@@@@@@%%#%%%%%#...                          
                 ..*@@@@@@@@@@@@@@@%*-#%%@%*:+@%-:+*..*@@@@@@@@@@@@@%%#...                          
                 ..+@@@@@@@@@@@@@@@*:..+@%+..:#+..-:..-%@@@@@@@@@@@@@%#...                          
                 ..*%%%@@@@@@@%%%%#-....:.....+:......:#@@@@@@@@@@@@%#*-..                          
                 .:%%%%%%%@@@@@@%%#-..................:#@@@@@@@@%%%%%%#+....                        
              ....-%@@%%%%@@@@@@@%%#...........     ..-%@@@@@@@%%%%%%%%*-...                        
               ...=%%%@@@@@@@@@@@@%%:...            ..=@@@@@@@@@@@@@@@%#-..                         
               ...-%%%%%%%%%%%@@@@%#-...            ..+@@@@@@@@@@@%%%%%#=...                        
                 .:#@@@%%%%%%%%####*:...            ..+@@@@%%%%%%%%%%@@%:...                        
                 ..*%%%%%%%%%%%%%%%*....            ..=@@@@%%%%%%%%%%%%#....                        
                 ..=%%%%%%%%@@@@@%%-....            ..:*@@@@@@%%%%%%%%%+....                        
                 ..-%%%%%@@@@@@@@%+.....            ...:#@@@@@@@@%%%%%%-....                        
                  .:#@@%%%%%%%##%%-......           ....=%@@@%%%%%%%@@%:..                          
                  ..+@@@%%%%%%@@%*:.....             ...:#@%%%%%%%%@@@%:..                          
                  ..=%%##%%@@@@@%=......            .. ..*@@@@%%%%%%%%#:..                          
                  ..=%%%%%@@@@@@%:.....             .....-@@@@@%%%%%%#*...                          
            .......:*@@@%%@@@@@@*:......            .....:%@@@@@@%%%%%*......                       
           .....:+*#%%@%%@@%%###*-......            .....-%@@@@@@%%%@%#+:.....                      
           .......:#%%%%%%%%%%%%#%#+-:..            ..-*%@%%%%%%%#%%######=:..                      
                  .*%%%%%%%%%%%%#-......            .....*@%%%%%%%%%%%%#=.....                      
           ........:#@@@%%%%%%%*:.......            ......+@%%%%%%#%%%#-.........                   
           ........+##%####**%%=..                     ....*@%%%####*++:.........                   
           ......-*##%%###***#%=..                     ....-@@%%%%#+++=-.........                   
           ....:+**####*##**#%%=..                     ....-@@@%###*=++=-:.......                   
    .........:=****##*******#%%-..                      ....%@@%###*+=++=--.......                  
    .......=+*#*+*##*+***++*#%-..                          .+@%#**##*==+*=---....                   
     ....-###%%###%%#*##*****....                          ..*%*=+##*+=+****=*-:....                
    ....:*%%%%#%@@@%###%%#*#=.....                         .:#%##%%#####%%###%##-...                
     . ..-::######@@%%%@@@%#:....                          .:#%#%@@@%#%%@@@%#%%%*:..                
       ............-:...:-=:..                             ..-*#+-+*#%%*+=+**=......                
       '''