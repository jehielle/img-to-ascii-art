# Image to ASCII Art
![image](https://img.shields.io/badge/Python-FFD43B?style=for-the-badge&logo=python&logoColor=blue)

     _                              _                         _ _
    (_)_ __ ___   __ _  __ _  ___  | |_ ___     __ _ ___  ___(_|_)
    | | '_ ` _ \ / _` |/ _` |/ _ \ | __/ _ \   / _` / __|/ __| | |
    | | | | | | | (_| | (_| |  __/ | || (_) | | (_| \__ \ (__| | |
    |_|_| |_| |_|\__,_|\__, |\___|  \__\___/   \__,_|___/\___|_|_|
    __ _  ___ _ __   |___/ __ __ _| |_ ___  _ __                
    / _` |/ _ \ '_ \ / _ \ '__/ _` | __/ _ \| '__|               
    | (_| |  __/ | | |  __/ | | (_| | || (_) | |                  
    \__, |\___|_| |_|\___|_|  \__,_|\__\___/|_|  
     |___/         
## Tools used:
* Pillow/PIL
* Python
## Steps taken:
* User uploads image by entering file path after being prompted
* Image resized, grayscaled, and translated pixels->characters based on grayscale values
* Image outputs as ASCII art
## Learned:
* File I/O
* Using built-in functions within PIL for image manipulation

## Output Examples:
### Dog
```
####@@@@@@@@#;^..,;/x8#@@@@@@@@@#81188#####81x//x888111xxxx/////////////////////////////x///////////
@@##@@@@@@@8;^.,,/x8###@@@@@@@@#88111188881xx///x888111xxxxx///////////////////////////xx///////////
@@@@@@@###1,^.,,;x#@##@@@@@@@@#88811111111xxxxx/x188111xxxxxxx/////////////////////////xx///////////
@@@@@@@##1.^.,,;x#@@##@@@@@@@#88881111111xxxxxxx/x18111xxxxxxxx////////////////////////xx///////////
@@@@@@@@8,^..,;/8@@@##@@####818888811111xxxxxxxxxxx181111xxxxxxxx//////////////////////xx///////////
@@@@@@@8,^..,;/x##81xxx/////;;;/xx18###88811x//;;;;/x///;;//////xx/////////////////////xx///////////
@####@#;^..,;;;/////xx11111xxx////;;;;;;;;;,...,,,,,;;,.^^^.,,,,;;/////////////////////xx///////////
///////;;;;////xx111111111111111x;,.....^^^^..,,,,;;;;;.^^.......,;;;//;;;;;;;;;;;;;;//xx///////////
//////;;//x1111188888888111xxxxx;............,,,;;;;;;;.^^^........,;;//xx//xx111xxx////////////////
///;;;/x11888#############81xxx;,......,,,,.,,,;;;;;;;,..^^..^^...,,;////xxxx1######8881xx//////////
;;;;/xxx118888####8888##881xx//,.....,,,;;;;,,,;;;;;;;;......^..,;;x1xx/////xx1##########81xx///;;;;
,;/;,.,/xx1118888888888888811/,....,/xxx/;;,,,,;;,;;;;;,......,,;;/x11xxxx///xx1###@@#####81xx///;;;
;;.^^^.,;xx11111118888888888x,...,1##@@##1x/;;;;;,,;;;;,...,,;;;;/x8#@@@@@#81xxx8#@@###88111xxxx///;
..^^^.^^.;/xx111111888881/;;,,,,,8##88@###81x/;;,,,;;;;,..,,;;;;x18#@@#@@@#@@1xxx118#88881111111xxx/
...^^^^^^.,/xxx111111111x;;;,,,,1#x8#####881x/;;,,,,,,,,..,;////x18#@@@@@@#@@#1xxxx188888881111181xx
...^^^^^^^,/x1xxxxxxxxx/;;/;,;;;xx118#8881///;,,,,,,,,,,,,,;//xxxx118##@@@@###11xxxxx111x1xx//11811x
.....^^^^^^;xx/;///////////;,;;,,;;;///;;;;;,,,.......,,,,,,;///xxxx1111888111111111xxx111xxxxx11111
,....^^^^^^^,;,;;;///x/x//x;,,,.,;;,,,;,,,,,,,.^^^^.,,,,,...,,;//xxxxx111111111111881111111111111111
,,,...^^^^^^^^...^.,,/////x;,....,;;;;,,,,,,,.^^^,/x1111xx////////xxxxx1111111xxx1#888811111xx111111
,,,...^^^^^^^^^...,,,;;;;;/;,....,;;;;,.,,..^^.;xx11888########81///xxx111111xxxx18811111111111111x1
,,,,....^^..,,;;;;;;;;;;;;/;....,,,,,,,.,..^^.x1111888########@@@#1/xxxx11111xxxx1111111111111111111
,;,,.....,;;;;;;;;;;;;;;///,.....,,...,,..^^.x#8########@###@@@@@@#8/xxxxx111xxxx1111111111111111xxx
;;;,,...;;;;;;;;;;;;;;;;///;..,,.........^^^,8##@@@@@@@@@@@@@@@@@@@#x/xxxxxxxxxxxxxxxxxxxxxxxxx11111
;;;;,.,;/;;;;;;;;;;;;;;//;,,..,,...^^^^.^^^.,x8#@@@@@##@@@@@@@@@@@@#1/xxxxxxxx1xx1xxxxxxxxxxxxxxxxxx
;;;;,,,//;;;;;;;;;;;;;;;,.^^,,.,,.....^.^^..,;1888#88##@@@@@@@@@@@#8xxxxxxxxx11x11111111111111111111
;;;;;,,//;;;;;;;;;;;;,.^^^^^.,,,,.,....^^....;x18####@@@@#@@@@@@##81x111xxx1111xxxxxxxxxx11111111111
///;;;;//;;;;;;;;;;,.^^^^^^^^.,,,,,,...^^^...,/x18##@@@@@#@###@#881111111811111111111xxxxxxxxxx11111
////;;;/;;;;;;;;;;,.^^^^^^^^^^.,,,///..^^....,/x188####@@#@###888111181188111xxxxxxxx1111111xxxxxxxx
////////;;;;;;;;,.^^^^^..^^^^^..,.,;xx,.^....,/18888#########88881111818@8x11111111xxxxxxxxxxxxx1111
xx1111/;;;;///;,.^^.....^^^^^......,,x1/...,,/x188####@@@###88##8818818#8118111111111111111111111111
188888/;;;/;/;,.^.....^^^^^^^......,,;88x/;/x11xx1#@@@@@@@@@#x1###88#8#81188111111111111111111111111
888888/;;////,......^^^^^^^^^.........,x1111xx1x///xx1888881x18#######811188111111111111111111111111
888888/;;///;......^^...^^^^^^......^...;/xxxx11xxxxx118888#########81111188111111111111111111111111
888888x;///;,...............^^.......^.....,x11111118888#########8811111118811xxxxxx1111111111111188
8888881/;//;......^..........^.............,/xxx18888#########8881xx11111881111xxxxxxxxxxxx111111111
88888881///,...........^....^............^..,;;/;/x1118181881111xxx1111188111111xxx11xxxxxxxxxx11111
888888881//,...........^.....................,//;;;//xxxxxxxxxxxxxx111188811111111x1x111111111111111
888888888x;,,,..^............................,;xx;///xxxx///x11xx11111888111111111111111111111111111
8888888888/,,,..^^..........................,,/xx/;//x///;;;/x11111111888111111111111111111111111111
88888111181;,...^..................,...,,,.,,;///;;;//xxx/;;/x1111111888811111x111111111111111111188
88888888888x,...^..................,..,,,.,,;;;,,,,;;xxxxxx/x11111111888811111x111111111111111111888
111111888881,......................,..,,,,,,,,,,,,,;;//xxxxxx11111111888811111x111111111111111188888
11111111111x.......................,,,,,,,,,,,;;,;;;;;/xxxxxx11111111888811111x111111111111111888888
11111111111/.......................,..,,,,,,,,;;///////xxx//xx1111111888111111x111111111111111111118
```
### Moon
```
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@##########@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@##8811xx///xx//////////xx18##@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@##81xxx///////////////;;;;;///////x188#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@#811xx///////////;;,,,,,;;;;,;//xx1111x/;////x18@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@81/////;;/;;;////;;;;,,,,,,,,,;;;;x11188881x///xx/;/18#@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@#1/;,;;,,,,,;;;;,;;;;;;;,,,,,,,,,,;;;/1111188881///xx////xx8#@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@8x/;;;;,,,;;;;;;;;;//;;;;;,,,,..,,,;;;;;;///x1111x;;;;;/xxx////x8@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@#8x/////;;;/xxxx/;;//////x////,,,,,,,,;/;,,....,,,,,,;;;;/xxxxx//////1#@@@@@@@@@@@@@@
@@@@@@@@@@@@@#1x///////;/x111xxxx//////xxxxx/;,,,..,,;;;;;,;;;;;;;;//xx118811xxx/;////1@@@@@@@@@@@@@
@@@@@@@@@@@@8//;/;/;////xxxxxx//x////xxxxx/;;/;;,,,;/xxx11xxxx111xxxxx188888111x;,;;////1@@@@@@@@@@@
@@@@@@@@@@#x/;;;;;;;///xxx////;///xxxxx1111xx111xx////xx11888#888x11xx111188111xx/;/////;x#@@@@@@@@@
@@@@@@@@@8x;;,,;;;;//xxxxx/;/;;;;;///xx1111888888811xxx11888##8888111xx1111111111xxx//x////8@@@@@@@@
@@@@@@@@1/;,,,,,;//xxxxx/x///;,;;;;/x1118111188888888888888#8888811881x/x1x111111xxxxx//////1@@@@@@@
@@@@@@@x;;;,,;;;xxxxxx/////;;;,,;;181118811111888888888888888888881xx/;;///xx//xx/;;xx/;;//;;1@@@@@@
@@@@@@x;;;;,;//x11x/;;,;;;;;;;;;;;x11881881881118888818##8888888811/,;;;;;;,,,,;;;;/xxx/;;,;;;1@@@@@
@@@@@1/;;;;;/xx1x////;;//////////;/x111118888881181x18#8##8888888881x;;;;;,,;;;,,,/;////;;,,;;;8@@@@
@@@@8/;;;;;/xx1x;/1xxxx1xxxxxxxxx1xx1111888888881//xx888##88888888111x///;;/xxx//;;///;,,,,,,,;/#@@@
@@@#x;;;;/xxxxx/;/xx1x1111xxxxx/xx/xx/xx18888111111x//x1188888881x//x1xxx///x1xx11x//;;,,....,;;x@@@
@@@1/;;;//xxx///111x11111111x1xxx///xx///x11111x/x11x//;//xxxxx/;,.,/xx/;;;;/xxxxx/;/;,,,,,.,,;;/#@@
@@#x;;;;/xx////x111111111111111xxxxxxx/;;/xxx11xx111x//;;;//;;;,,...,;,,..,.,;//;/;;;;;;,,,,,,;;;1@@
@@8//;;/x1x;;//x888888111111881xxx////;;;/xx11188881xx;,..,,,,,,,........^..^..,,;;,,,;,,,,,;,;;;/@@
@@1/;;/xx/;;;/x18888888811811111xxxxx1x///x11118811xx/;,...,,,,,,,,,...,......,,..,,,,,,,,,;,,;;;;#@
@@1x///xx/;;;11188888888818811x11111181///x1111x////;,;,,,,,,,,,,,,,..,,,,,,,,,,..,,,,,,;,,,,,,;;;#@
@@11x/111x;;;x1188888888881111111111x11/xx1888x///////;;,,,,,,..,,,,,,,,;;,,,;;,..,,,,,,,,,,,.,;,;8@
@@1111111/;;//x181888888888881111111xxxx111181x/;///xxx/;;;,,,..,,,,,,,,,,,,,;;,,.,,,,,;,,,,,.,;;;8@
@@11111xx1x////11811888811111111111xx//xxxx11181x11x11x//;;;;;,;;,;;,,,;,,,,,,;,,.,,,,;,,,,,,,,,;;#@
@@818111181x/xxx18111111111111x111xx//////xx18#8111x///;;;;;;;;;;;;;,,;;;,,,.,;,,..,,,,,,,,.,,,,,;@@
@@#1888118111xx111111111811111111xx///////xx111111x//;,;,,;///;;;;;,,,;;;,,..,,,,.,,,,,,,,,,,,,,,x@@
@@@88888818111111111111811xx11xxx/;;;,,;/x11111111x/;,;;;;;;;;;;;;;;;;;;;;,.,,,,,.,,,.,,,,,,,,,,,#@@
@@@@18888188111111111118111x1x////;/;.,;xxxx1111xxx//;////;;//;;;,,;;;,,,,.,.,,,..,,,,,,,,,,,,,,/@@@
@@@@88888888111xx1xx118111111x///;;;;;///x/x//xxxxxx11111xxxxxx;;;;;;;;,......,,,,,,,;;,,,,,,,,;#@@@
@@@@@88888888111///xx11111111x1xx//xx///////xxxx/////x1xx111111/////;;,,,,.,,,,..,.,,,,,,,,,,,,8@@@@
@@@@@@88888888111/;xx11xxxxx1xx11x1x/xxxxxxxx11xxxxx/xxxxx1111111x11x;,,,.......,,,,,,,,,,,,,,1@@@@@
@@@@@@@88118888811111111111xx////xxxxx1xxxxx11111111111x111118118811x/,,.......,,,.,,,,,,,,,,1@@@@@@
@@@@@@@@811188888888881111111x/;;;/11x11111x1xx18111111111111111811xx;,,...,,,,,,,.,,,,;,,,,8@@@@@@@
@@@@@@@@@811181888888888818811xxxxxx11111111x///1111x//11xxx111881x//;,,,.,,,,,,,,,,,,;,,,;#@@@@@@@@
@@@@@@@@@@#1188888888888888881881111188881111xx11111xx//xxxxxxxxx/;,,,,,,,,,,,,,,,,,,,,,,x@@@@@@@@@@
@@@@@@@@@@@@1x118888888888888888888881888188881888811xxxxx1x1xx///;,;;;,,,,,,,,,,,,,,,,/#@@@@@@@@@@@
@@@@@@@@@@@@@#1xx11188881888888888888888881111111x111x/xxxx/xxx/xx/;;;;,,,,,;,,;;,,,,;8@@@@@@@@@@@@@
@@@@@@@@@@@@@@@#1////x1118888888881881888881x///xx18888811x///xx/;;;;;;;;;;;;;;;;,,/8@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@#1/;;;;//11888888888881111xx///;x18888811xx//;/;;;;;;;;;;;;;;;,,/8@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@8x/;;;;/xxx11111111xxxxxx//;;/x1111xxx/////;;;;;;;////;;,;/1#@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@8x//;;/xx;;////////////;;;;;;;;;,,;;////;;///////;;;/1#@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@#8x/;/;;;;;;;;;;;;;;;,,,,,,,,,,;;;//////;;;;//18@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@#81x//;;;/;,,,,,.,,;;;;;;;;;;;;;////x18#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@##81xx///;;;/;////////xx188#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
```
