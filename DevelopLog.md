# 麻雀（Try）
Trial for 麻雀 program using Python

**2020/08/23**
  * defined data structure for the communication between client and server (json style)
  * changed GameManager.py for transfering json style data
  * created explanation file for this data structure

Sato

**2020/08/14**
  * Checked socket will work for different computer
  * Introduced multiProcess to the code for client become server too (main.py).
  * Refactored game_client.py for main.py
  * Refactored GameManager.py for main.py

Sato

**2020/08/12**
  * Updated some loop in GameManager.py for better efficiency
  * Changed GameManager.py, Player.py in Python_Socket_Ver for socket programming
  * Created game_client.py for running game on different Terminal(PC)

Sato

**2020/08/12**
  * Added single socket proggraming example, single_server.py and single_client.py
  * Added multi sockets proggraming example, multi_server.py and multi_client.py

Sato

***2020/08/04***
  * added some new tests in test_Player including yiqiguantong and qingyise
  * new issues made in GitHub

Jiugeng

**2020/08/02**
  * Produced structured File version "Structured"
  * Adjusted import part in codes
  * Modified GameMaster.py for printing Wiiner

Sato


**2020/07/25**
  * Updated the GameManager.py

Sato

**2020/07/25**
  * Updated the GameManager.py in NewGUI for GUI expression
  * Created the GameGUI.py in NewGUI for GUI expression (this is just a test version)

Sato

**2020/07/07**
  * Updated the Concept of 宝牌 to GameManager class
  * Updated the Concept of Red 宝牌

Sato

**2020/07/01**
  * Added the Concept of 宝牌 to GameManager class

Sato

**2020/06/25**
  * Updated JudgeRonTest.py for 九莲宝灯 and 纯正九莲宝灯
  * Updated JudgeRon_Test_Report.txt for 九莲宝灯 and 纯正九莲宝灯

Sato

**2020/06/22**
  * Added 槍槓 to GameManager.py
  * Modified GameManager.py
  * Modified TestPlayer.py (Now TestPlayer.py can be used as the API for Player class)

Sato

**2020/06/19**
  * Debuged RonWayJapan.py (Added line 57,58)
  * Modified GameManager.py so that it can judge special cases  
    一發、嶺上開花、海底撈月、河底撈魚、双倍立直、流局満貫、天和、地和、人和  
    (槍槓 is not yet implemanted since it will need to interact with other classes)

Sato

**2020/06/18**
  * Added Unit Tests to JudgeRonTest.py (Pinghe)
  * Added the results of unit tests to "JudgeRon_Test_Report.txt" (Pinghe)
  * Added the class for Calculating 符数 (HeHand)

Sato

**2020/06/07**
  * Finish writing Unit Tests to JudgeRonTest.py (Tests is completed for existing function for now)
  * Finish writing results of unit tests to "JudgeRon_Test_Report.txt" (again this is completed for existing function for now)

Sato

**2020/06/06**
  * Added Unit Tests to JudgeRonTest.py (Tests is not yet completed)
  * Added the results of unit tests to "JudgeRon_Test_Report.txt" (again this is not yet completed)

Sato

**2020/06/05**
  * Finish writing Unit Tests to JudgeRonTest.py (Tests is completed for existing function for now)
  * Finish writing results of unit tests to "JudgeRon_Test_Report.txt" (again this is completed for existing function for now)

Sato

**2020/06/04**
  * Added Unit Tests to JudgeRonTest.py (Tests is not yet completed)
  * Added the results of unit tests to "JudgeRon_Test_Report.txt" (again this is not yet completed)

Sato

**2020/06/03**
  * Added Unit Tests to JudgeRonTest.py (Tests is not yet completed)
  * Added the results of unit tests to "JudgeRon_Test_Report.txt" (again this is not yet completed)

Sato

**2020/06/02**
  * Added JudgeRonTest.py which is Unit Tests for functions in JudgeRon (Tests is not yet completed)
  * Added the results of unit tests as "JudgeRon_Test_Report.txt" (again this is not yet completed)

Sato

**2020/05/19**
 * modified GameManager class for player's wind(風) and Riichi（立直）
 * added score calculation table in Data with npy and csv version
 
Sato

**2020/05/18**
 * the function in Pai, showHand modified for GameManager class. It will return str instead of list
 * TestPlayer class added. 
 * Gamemanager class works with TestPlayer
 
Sato

**2020/05/16**
 * modified GameManager as Finite State Machine
 
Sato

**2020/05/13**
 * Modefied class for Pai. numPai and charPai become one general class Pai
 * Added invrse function of "hand2Array", "array2Hand" to Pai.py.
   * *hand2Array: [Pai] -> np.array (4x34)*
   * *array2Hand: np.array (4x34) -> [Pai]*

Sato

**2020/05/13**
  * Added "hand2Array" function to Pai.py for representing hand with 4x34 array list
  * Added GameManager class

Sato

**2020/02/19 20:11**
  * Added function to judge Ron, which is in judgeRon.py

Sato

**2020/02/18 00:24**
  * added neural network for calcurating expectation of the hand in Mahjong, but since
    Mahjong Pai is discrete data it will not work without proper pre processing of the 
    data. 但如果得到了Data的话可以试一试。

Sato

**2020/02/15 05:00**
  * random 切牌function decideCut()　is added. Simulation canbe done from 
    Game_Simulation.py

Sato