
# /*remove duplicate words after final construction of title*/

# /**/

synonyms = {
# /*difficult words to replace*/
'love' : ['love'],
'job' : ['job'],
'massage' : ['massage', 'body massage','erotic massage','sensual massage'],
'milk' : ['milk'],
'foot' : ['foot','feet','toe'],
'feet' : ['foot','feet','toe'],
'toe' : ['foot','feet','toe'],

'virgin' : ['virgin'], # /*['virgin','fresh','maiden','unmarried'],*/



'...' : ['-'],
'#' : ['No:'],
# /*'for' : ['4', 'for','because of'],*/

'and' : ['and','and','and','&',', as well as','along with'], # /*,'n'],*/
'n' : ['and','&', 'as well as','along with'], # /*,'n'],*/
'&' : ['and','n','&', 'as well as','along with'],

'a' : ['a','a','a','the','one'],
'an' : ['an','an','an','the'],

'the' : ['the','the','the','the same','a'],

'at' : ['at','at','at','by','in','on'],

'on' : ['on','on','on','on','against','about','at'],

'as' : ['as','as','as','as','just as',', then'],

'me' : ['me','me','me','me only','myself'],

'i' : ['I','I','I','I myself'],
'was' : ['was','is'],
'is' : ['was','is',''],
'are' : ['are','are','are','were','will be'],
"that's" : ["that is","it's","it is","this is","this"],
"its's" : ["that is","it's","it is","this is","this"],
'this' : ['this','the','that'],
'that' : ['this','the','that'],
'your' : ['your','this','the','that'],
# /*'his' : ['his','boy\'s','man\'s','guy\'s','dude\'s','husband\'s'],*/
# /*'her' : ['her','girl\'s','woman\'s','girlfriend\'s','chick\'s','wife\'s'],*/
'his' : ['his','his','the','his own',''], # /*some time remove it*/
'her' : ['her','her','the','her own',''], # /*some time remove it*/

'has' : ['has','has','had','having'],

'ur' : ['your',''],

'by' : ['by','by the'],

'she' : ['she','she','she','she','the girl','the woman','the girlfriend','the chick','the wife'],
'he' : ['he','he','he','he','the boy','the man','the boyfriend','the guy','the dude'],
'him' : ['him','him','him','him','the boy','the man','the boyfriend','the guy','the dude'],

'my' : ['my','my','my','my','my own', 'the', 'my dear', ''],# /*'' meaning remove it.*/
'but' : [', yet',', but',', although',', however',', though',', still'],

'while' : ['while','during','during the time','however','at the same time','whilst'],
'during' : ['during','while','amid','in the middle of','in the time of','in the course of'],
'amid' : ['during','while','amid','in the middle of','in the time of','in the course of'],

'off' : ['off','off','off','out','down'],

# /*sexy = hot, seductive, sensual, arousing, racy, spicy, hotty, naughty, steamy, tempting, captivating*/
'sexy' : ['sexy','hot','seductive','sensual','arousing','spicy','hotty','naughty','steamy','tempting','captivating','erotic'],
'sexual' : ['sexy','hot','seductive','sensual','arousing','intimate','erotic'],

'hot' : ['sexy','hot','seductive','sensual','arousing','spicy','hotty','naughty','steamy','tempting','captivating','erotic'],

'seductive' : ['sexy','hot','seductive','sensual','arousing','attractive','spicy','hotty','naughty','charming','tempting','captivating','ravishing','desirable'],

'sensual' : ['sexy','hot','seductive','sensual','arousing','racy','spicy','hotty','naughty','steamy','tempting','captivating','erotic'],
'arousing' : ['sexy','hot','seductive','sensual','arousing','racy','spicy','hotty','naughty','steamy','tempting','captivating','erotic'],
'racy' : ['sexy','hot','seductive','sensual','arousing','racy','spicy','hotty','naughty','steamy','tempting','captivating','erotic'],
'spicy' : ['sexy','hot','seductive','sensual','arousing','racy','spicy','hotty','naughty','steamy','tempting','captivating','erotic'],
'hotty' : ['sexy','super hot','seductive','sensual','arousing','racy','spicy','hotty','naughty','steamy','tempting','captivating','erotic'],
'hottie' : ['sexy','super hot','seductive','sensual','arousing','racy','spicy','hotty','naughty','steamy','tempting','captivating','erotic'],
'naughty' : ['sexy','hot','seductive','sensual','arousing','racy','spicy','hotty','naughty','steamy','tempting','captivating','erotic'],
'steamy' : ['sexy','hot','seductive','sensual','arousing','racy','spicy','hotty','naughty','steamy','tempting','captivating','erotic'],
'tempting' : ['sexy','hot','seductive','sensual','arousing','racy','spicy','hotty','naughty','steamy','tempting','captivating','erotic'],
'captivating' : ['sexy','hot','seductive','sensual','arousing','racy','spicy','hotty','naughty','steamy','tempting','captivating','erotic'],
'erotic' : ['sexy','hot','seductive','sensual','arousing','racy','spicy','hotty','naughty','steamy','tempting','captivating','erotic'],

# /*horny = aroused, excited, turned on, hot, heated, lustful, randy, passionate, desiring, sensual, slutry*/
'horny' : ['horny', 'aroused', 'excited', 'turned on', 'hot', 'heated', 'lustful', 'randy', 'passionate', 'desiring', 'sensual', 'slutry'],
'aroused' : ['horny', 'aroused', 'excited', 'turned on', 'hot', 'heated', 'lustful', 'randy', 'passionate', 'desiring', 'sensual', 'slutry'],
'excited' : ['horny', 'aroused', 'excited', 'turned on', 'hot', 'heated', 'lustful', 'randy', 'passionate', 'desiring', 'sensual', 'slutry'],
'lustful' : ['horny', 'aroused', 'excited', 'turned on', 'hot', 'heated', 'lustful', 'randy', 'passionate', 'desiring', 'sensual', 'slutry'],
'lusty' : ['horny', 'aroused', 'excited', 'turned on', 'hot', 'heated', 'lustful', 'randy', 'passionate', 'desiring', 'sensual', 'slutry'],
'randy' : ['horny', 'aroused', 'excited', 'turned on', 'hot', 'heated', 'lustful', 'randy', 'passionate', 'desiring', 'sensual', 'slutry'],
'passionate' : ['horny', 'aroused', 'excited', 'turned on', 'hot', 'heated', 'lustful', 'randy', 'passionate', 'desiring', 'sensual', 'slutry'],
'desiring' : ['horny', 'aroused', 'excited', 'turned on', 'hot', 'heated', 'lustful', 'randy', 'passionate', 'desiring', 'sensual', 'slutry'],
'slutry' : ['horny', 'aroused', 'excited', 'turned on', 'hot', 'heated', 'lustful', 'randy', 'passionate', 'desiring', 'sensual', 'slutry'],

'crazy' : ['wild', 'horny', 'aroused', 'excited', 'hot', 'heated', 'lustful', 'randy', 'passionate', 'desiring', 'sensual', 'slutry'],

# /*fuck*/
# /*'sex' : ['sex','fuck', 'fun'],*/
'sex' : ['sex','sex','sex','fuck', 'fun'], # /*60/40*/

# /*'fuck' : ['fuck','sex','bang'],# /*,'screw','nail','pound','drill'],*/
'fuck' : ['fuck','fuck','sex','bang'], # /*50/50*/

# /*'fucks' : ['fucks','pounds','bangs','drills','screws','ramms','nails'],*/
'fucks' : ['fucks','fucks','fucks','pounds','pounds','bangs','bangs','scores','drills','screws','screws','ramms','nails'],

# /*'fucked' : ['fucked','pounded','banged','drilled','screwed','rammed','boned','nailed','hammered'],*/
'fucked' : ['fucked','fucked','fucked','pounded','pounded','banged','banged','drilled','screwed','screwed','rammed','boned','nailed','hammered'],

# /*'fucking' : ['fucking','ramming','pounding','banging','stroking','hammering','dicking'],*/
'fucking' : ['fucking','fucking','fucking','pounding','pounding','banging','banging','screwing','ramming','stroking','hammering','dicking'],

'pound' : ['fuck','pound','bang','drill','screw','nail'],
'pounds' : ['pounds','fucks','pounds','bangs','drills','screws','ramms','nails'],
'pounded' : ['pounded','fucked','banged','drilled','screwed','rammed','boned','nailed','hammered'],
'pounding' : ['pounding','fucking','ramming','banging','drilling','screwing','stroking','nailing','dicking','hammering'],
'rammed' : ['rammed','fucked','banged','drilled','screwed','pounded','boned','nailed'],
'ramming' : ['ramming','fucking','pounding','banging','drilling','screwing','stroking','nailing','hammering'],
'bang' : ['bang','pound','fuck','drill','screw','nail'],
'banged' : ['banged','pounded','fucked','drilled','screwed','rammed','boned','nailed','hammered'],
'bangs' : ['bangs','pounds','fucks','drills','screws','ramms','nails','scores'],
'banging' : ['banging','ramming','pounding','fucking','drilling','screwing','stroking','nailing','hammering','dicking'],
'drill' : ['drill','pound','bang','fuck','screw','nail'],
'drills' : ['drills','pounds','bangs','fucks','screws','ramms','nails','scores'],
'drilled' : ['drilled','pounded','banged','fucked','screwed','rammed','boned','nailed','hammered'],
'drilling' : ['drilling','ramming','pounding','banging','fucking','screwing','stroking','nailing','hammering','dicking'],
'screw' : ['screw','pound','bang','drill','fuck','nail'],
'screws' : ['screws','pounds','bangs','drills','fucks','ramms','nails'],
'screwed' : ['screwed','pounded','banged','drilled','fucked','rammed','boned','nailed','hammered'],
'screwing' : ['screwing','ramming','pounding','banging','drilling','fucking','stroking','nailing','hammering','dicking'],
'nail' : ['nail','pound','bang','drill','screw','fuck'],
'nails' : ['nails','pounds','bangs','drills','screws','ramms','fucks'],
'nailed' : ['nailed','pounded','banged','drilled','screwed','rammed','boned','fucked','hammered'],
'nailing' : ['nailing','ramming','pounding','banging','drilling','screwing','stroking','fucking','hammering'],
'hammering' : ['ramming','pounding','banging','drilling','screwing','stroking','fucking','hammering','dicking'],
'hammered' : ['pounded','banged','drilled','screwed','rammed','boned','fucked','hammered'],
'hammers' : ['hammers','fucks','pounds','bangs','drills','screws','ramms','nails'],
'dicking' : ['dicking','ramming','pounding','banging','drilling','screwing','stroking','fucking','hammering'],
'dicked' : ['dicked','pounded','banged','drilled','screwed','rammed','boned','nailed','hammered'],
'scores' : ['scores','fucks','pounds','bangs','drills','screws','ramms','nails'],

# /*fuck end*/



# /*most popular keywords*/

# /*beautiful*/
'beautiful' :  [ 'beautiful','sexy', 'cute', 'cutie', 'pretty',  
				'sweet', 'breathtaking', 'adorable','spectacular','dashing','incredible',
				'hot','cool','terrific','amazing','marvelous','enchanting','fabulous','appealing',
				'lovely', 'stunning','nice-looking','fantastic','splendid',
				'magnificent', 'glorious', 'exquisite', 'pleasant', 'nice', 'awesome', 'excellent', 
				'superb', 'marvellous', 'charming', 'attractive', 'delightful', 'wonderful', 
				'glowing','shining','graceful','shiny','tempting','lovable','gracious',
				'romantic','ravishing','sensational','phenomenal','astonishing','tremendous',
				'exceptional','impressive','magical','stupendous','fascinating','dazzling','captivating',
				'alluring','elegant','exciting','entrancing','compelling','enticing','stylish',
				'staggering','striking','sparkling','radiant','gorgeous','sensual','exotic','classy','glamorous'],



'cute' :  ['beautiful','sexy','cute','cutie','pretty','sweet','breathtaking','adorable','spectacular','dashing','incredible','hot','cool','terrific','amazing','marvelous','enchanting','fabulous','appealing','lovely', 'stunning','nice-looking','fantastic','splendid','magnificent','glorious','exquisite','pleasant','nice','awesome','excellent','superb','marvellous','charming','attractive','delightful','wonderful','glowing','shining','graceful','shiny','tempting','lovable','gracious','romantic','ravishing','sensational','phenomenal','astonishing','tremendous','exceptional','impressive','magical','stupendous','fascinating','dazzling','captivating','alluring','elegant','exciting','entrancing','compelling','enticing','stylish','staggering','striking','sparkling','radiant','gorgeous','sensual','exotic','classy','glamorous'],
'cutie' :  ['beautiful','sexy','cute','cutie','pretty','sweet','breathtaking','adorable','spectacular','dashing','incredible','hot','cool','terrific','amazing','marvelous','enchanting','fabulous','appealing','lovely', 'stunning','nice-looking','fantastic','splendid','magnificent','glorious','exquisite','pleasant','nice','awesome','excellent','superb','marvellous','charming','attractive','delightful','wonderful','glowing','shining','graceful','shiny','tempting','lovable','gracious','romantic','ravishing','sensational','phenomenal','astonishing','tremendous','exceptional','impressive','magical','stupendous','fascinating','dazzling','captivating','alluring','elegant','exciting','entrancing','compelling','enticing','stylish','staggering','striking','sparkling','radiant','gorgeous','sensual','exotic','classy','glamorous'],
'pretty' :  ['beautiful','sexy','cute','cutie','pretty','sweet','breathtaking','adorable','spectacular','dashing','incredible','hot','cool','terrific','amazing','marvelous','enchanting','fabulous','appealing','lovely', 'stunning','nice-looking','fantastic','splendid','magnificent','glorious','exquisite','pleasant','nice','awesome','excellent','superb','marvellous','charming','attractive','delightful','wonderful','glowing','shining','graceful','shiny','tempting','lovable','gracious','romantic','ravishing','sensational','phenomenal','astonishing','tremendous','exceptional','impressive','magical','stupendous','fascinating','dazzling','captivating','alluring','elegant','exciting','entrancing','compelling','enticing','stylish','staggering','striking','sparkling','radiant','gorgeous','sensual','exotic','classy','glamorous'],
'sweet' :  ['beautiful','sexy','cute','cutie','pretty','sweet','breathtaking','adorable','spectacular','dashing','incredible','hot','cool','terrific','amazing','marvelous','enchanting','fabulous','appealing','lovely', 'stunning','nice-looking','fantastic','splendid','magnificent','glorious','exquisite','pleasant','nice','awesome','excellent','superb','marvellous','charming','attractive','delightful','wonderful','glowing','shining','graceful','shiny','tempting','lovable','gracious','romantic','ravishing','sensational','phenomenal','astonishing','tremendous','exceptional','impressive','magical','stupendous','fascinating','dazzling','captivating','alluring','elegant','exciting','entrancing','compelling','enticing','stylish','staggering','striking','sparkling','radiant','gorgeous','sensual','exotic','classy','glamorous'],
'breathtaking' :  ['beautiful','sexy','cute','cutie','pretty','sweet','breathtaking','adorable','spectacular','dashing','incredible','hot','cool','terrific','amazing','marvelous','enchanting','fabulous','appealing','lovely', 'stunning','nice-looking','fantastic','splendid','magnificent','glorious','exquisite','pleasant','nice','awesome','excellent','superb','marvellous','charming','attractive','delightful','wonderful','glowing','shining','graceful','shiny','tempting','lovable','gracious','romantic','ravishing','sensational','phenomenal','astonishing','tremendous','exceptional','impressive','magical','stupendous','fascinating','dazzling','captivating','alluring','elegant','exciting','entrancing','compelling','enticing','stylish','staggering','striking','sparkling','radiant','gorgeous','sensual','exotic','classy','glamorous'],
'spectacular' :  ['beautiful','sexy','cute','cutie','pretty','sweet','breathtaking','adorable','spectacular','dashing','incredible','hot','cool','terrific','amazing','marvelous','enchanting','fabulous','appealing','lovely', 'stunning','nice-looking','fantastic','splendid','magnificent','glorious','exquisite','pleasant','nice','awesome','excellent','superb','marvellous','charming','attractive','delightful','wonderful','glowing','shining','graceful','shiny','tempting','lovable','gracious','romantic','ravishing','sensational','phenomenal','astonishing','tremendous','exceptional','impressive','magical','stupendous','fascinating','dazzling','captivating','alluring','elegant','exciting','entrancing','compelling','enticing','stylish','staggering','striking','sparkling','radiant','gorgeous','sensual','exotic','classy','glamorous'],
'dashing' :  ['beautiful','sexy','cute','cutie','pretty','sweet','breathtaking','adorable','spectacular','dashing','incredible','hot','cool','terrific','amazing','marvelous','enchanting','fabulous','appealing','lovely', 'stunning','nice-looking','fantastic','splendid','magnificent','glorious','exquisite','pleasant','nice','awesome','excellent','superb','marvellous','charming','attractive','delightful','wonderful','glowing','shining','graceful','shiny','tempting','lovable','gracious','romantic','ravishing','sensational','phenomenal','astonishing','tremendous','exceptional','impressive','magical','stupendous','fascinating','dazzling','captivating','alluring','elegant','exciting','entrancing','compelling','enticing','stylish','staggering','striking','sparkling','radiant','gorgeous','sensual','exotic','classy','glamorous'],
'incredible' :  ['beautiful','sexy','cute','cutie','pretty','sweet','breathtaking','adorable','spectacular','dashing','incredible','hot','cool','terrific','amazing','marvelous','enchanting','fabulous','appealing','lovely', 'stunning','nice-looking','fantastic','splendid','magnificent','glorious','exquisite','pleasant','nice','awesome','excellent','superb','marvellous','charming','attractive','delightful','wonderful','glowing','shining','graceful','shiny','tempting','lovable','gracious','romantic','ravishing','sensational','phenomenal','astonishing','tremendous','exceptional','impressive','magical','stupendous','fascinating','dazzling','captivating','alluring','elegant','exciting','entrancing','compelling','enticing','stylish','staggering','striking','sparkling','radiant','gorgeous','sensual','exotic','classy','glamorous'],
'terrific' :  ['beautiful','sexy','cute','cutie','pretty','sweet','breathtaking','adorable','spectacular','dashing','incredible','hot','cool','terrific','amazing','marvelous','enchanting','fabulous','appealing','lovely', 'stunning','nice-looking','fantastic','splendid','magnificent','glorious','exquisite','pleasant','nice','awesome','excellent','superb','marvellous','charming','attractive','delightful','wonderful','glowing','shining','graceful','shiny','tempting','lovable','gracious','romantic','ravishing','sensational','phenomenal','astonishing','tremendous','exceptional','impressive','magical','stupendous','fascinating','dazzling','captivating','alluring','elegant','exciting','entrancing','compelling','enticing','stylish','staggering','striking','sparkling','radiant','gorgeous','sensual','exotic','classy','glamorous'],
'amazing' :  ['beautiful','sexy','cute','cutie','pretty','sweet','breathtaking','adorable','spectacular','dashing','incredible','hot','cool','terrific','amazing','marvelous','enchanting','fabulous','appealing','lovely', 'stunning','nice-looking','fantastic','splendid','magnificent','glorious','exquisite','pleasant','nice','awesome','excellent','superb','marvellous','charming','attractive','delightful','wonderful','glowing','shining','graceful','shiny','tempting','lovable','gracious','romantic','ravishing','sensational','phenomenal','astonishing','tremendous','exceptional','impressive','magical','stupendous','fascinating','dazzling','captivating','alluring','elegant','exciting','entrancing','compelling','enticing','stylish','staggering','striking','sparkling','radiant','gorgeous','sensual','exotic','classy','glamorous'],
'marvelous' :  ['beautiful','sexy','cute','cutie','pretty','sweet','breathtaking','adorable','spectacular','dashing','incredible','hot','cool','terrific','amazing','marvelous','enchanting','fabulous','appealing','lovely', 'stunning','nice-looking','fantastic','splendid','magnificent','glorious','exquisite','pleasant','nice','awesome','excellent','superb','marvellous','charming','attractive','delightful','wonderful','glowing','shining','graceful','shiny','tempting','lovable','gracious','romantic','ravishing','sensational','phenomenal','astonishing','tremendous','exceptional','impressive','magical','stupendous','fascinating','dazzling','captivating','alluring','elegant','exciting','entrancing','compelling','enticing','stylish','staggering','striking','sparkling','radiant','gorgeous','sensual','exotic','classy','glamorous'],
'enchanting' :  ['beautiful','sexy','cute','cutie','pretty','sweet','breathtaking','adorable','spectacular','dashing','incredible','hot','cool','terrific','amazing','marvelous','enchanting','fabulous','appealing','lovely', 'stunning','nice-looking','fantastic','splendid','magnificent','glorious','exquisite','pleasant','nice','awesome','excellent','superb','marvellous','charming','attractive','delightful','wonderful','glowing','shining','graceful','shiny','tempting','lovable','gracious','romantic','ravishing','sensational','phenomenal','astonishing','tremendous','exceptional','impressive','magical','stupendous','fascinating','dazzling','captivating','alluring','elegant','exciting','entrancing','compelling','enticing','stylish','staggering','striking','sparkling','radiant','gorgeous','sensual','exotic','classy','glamorous'],
'fabulous' :  ['beautiful','sexy','cute','cutie','pretty','sweet','breathtaking','adorable','spectacular','dashing','incredible','hot','cool','terrific','amazing','marvelous','enchanting','fabulous','appealing','lovely', 'stunning','nice-looking','fantastic','splendid','magnificent','glorious','exquisite','pleasant','nice','awesome','excellent','superb','marvellous','charming','attractive','delightful','wonderful','glowing','shining','graceful','shiny','tempting','lovable','gracious','romantic','ravishing','sensational','phenomenal','astonishing','tremendous','exceptional','impressive','magical','stupendous','fascinating','dazzling','captivating','alluring','elegant','exciting','entrancing','compelling','enticing','stylish','staggering','striking','sparkling','radiant','gorgeous','sensual','exotic','classy','glamorous'],
'appealing' :  ['beautiful','sexy','cute','cutie','pretty','sweet','breathtaking','adorable','spectacular','dashing','incredible','hot','cool','terrific','amazing','marvelous','enchanting','fabulous','appealing','lovely', 'stunning','nice-looking','fantastic','splendid','magnificent','glorious','exquisite','pleasant','nice','awesome','excellent','superb','marvellous','charming','attractive','delightful','wonderful','glowing','shining','graceful','shiny','tempting','lovable','gracious','romantic','ravishing','sensational','phenomenal','astonishing','tremendous','exceptional','impressive','magical','stupendous','fascinating','dazzling','captivating','alluring','elegant','exciting','entrancing','compelling','enticing','stylish','staggering','striking','sparkling','radiant','gorgeous','sensual','exotic','classy','glamorous'],
'lovely' :  ['beautiful','sexy','cute','cutie','pretty','sweet','breathtaking','adorable','spectacular','dashing','incredible','hot','cool','terrific','amazing','marvelous','enchanting','fabulous','appealing','lovely', 'stunning','nice-looking','fantastic','splendid','magnificent','glorious','exquisite','pleasant','nice','awesome','excellent','superb','marvellous','charming','attractive','delightful','wonderful','glowing','shining','graceful','shiny','tempting','lovable','gracious','romantic','ravishing','sensational','phenomenal','astonishing','tremendous','exceptional','impressive','magical','stupendous','fascinating','dazzling','captivating','alluring','elegant','exciting','entrancing','compelling','enticing','stylish','staggering','striking','sparkling','radiant','gorgeous','sensual','exotic','classy','glamorous'],
'stunning' :  ['beautiful','sexy','cute','cutie','pretty','sweet','breathtaking','adorable','spectacular','dashing','incredible','hot','cool','terrific','amazing','marvelous','enchanting','fabulous','appealing','lovely', 'stunning','nice-looking','fantastic','splendid','magnificent','glorious','exquisite','pleasant','nice','awesome','excellent','superb','marvellous','charming','attractive','delightful','wonderful','glowing','shining','graceful','shiny','tempting','lovable','gracious','romantic','ravishing','sensational','phenomenal','astonishing','tremendous','exceptional','impressive','magical','stupendous','fascinating','dazzling','captivating','alluring','elegant','exciting','entrancing','compelling','enticing','stylish','staggering','striking','sparkling','radiant','gorgeous','sensual','exotic','classy','glamorous'],
'fantastic' :  ['beautiful','sexy','cute','cutie','pretty','sweet','breathtaking','adorable','spectacular','dashing','incredible','hot','cool','terrific','amazing','marvelous','enchanting','fabulous','appealing','lovely', 'stunning','nice-looking','fantastic','splendid','magnificent','glorious','exquisite','pleasant','nice','awesome','excellent','superb','marvellous','charming','attractive','delightful','wonderful','glowing','shining','graceful','shiny','tempting','lovable','gracious','romantic','ravishing','sensational','phenomenal','astonishing','tremendous','exceptional','impressive','magical','stupendous','fascinating','dazzling','captivating','alluring','elegant','exciting','entrancing','compelling','enticing','stylish','staggering','striking','sparkling','radiant','gorgeous','sensual','exotic','classy','glamorous'],
'splendid' :  ['beautiful','sexy','cute','cutie','pretty','sweet','breathtaking','adorable','spectacular','dashing','incredible','hot','cool','terrific','amazing','marvelous','enchanting','fabulous','appealing','lovely', 'stunning','nice-looking','fantastic','splendid','magnificent','glorious','exquisite','pleasant','nice','awesome','excellent','superb','marvellous','charming','attractive','delightful','wonderful','glowing','shining','graceful','shiny','tempting','lovable','gracious','romantic','ravishing','sensational','phenomenal','astonishing','tremendous','exceptional','impressive','magical','stupendous','fascinating','dazzling','captivating','alluring','elegant','exciting','entrancing','compelling','enticing','stylish','staggering','striking','sparkling','radiant','gorgeous','sensual','exotic','classy','glamorous'],
'magnificent' :  ['beautiful','sexy','cute','cutie','pretty','sweet','breathtaking','adorable','spectacular','dashing','incredible','hot','cool','terrific','amazing','marvelous','enchanting','fabulous','appealing','lovely', 'stunning','nice-looking','fantastic','splendid','magnificent','glorious','exquisite','pleasant','nice','awesome','excellent','superb','marvellous','charming','attractive','delightful','wonderful','glowing','shining','graceful','shiny','tempting','lovable','gracious','romantic','ravishing','sensational','phenomenal','astonishing','tremendous','exceptional','impressive','magical','stupendous','fascinating','dazzling','captivating','alluring','elegant','exciting','entrancing','compelling','enticing','stylish','staggering','striking','sparkling','radiant','gorgeous','sensual','exotic','classy','glamorous'],
'glorious' :  ['beautiful','sexy','cute','cutie','pretty','sweet','breathtaking','adorable','spectacular','dashing','incredible','hot','cool','terrific','amazing','marvelous','enchanting','fabulous','appealing','lovely', 'stunning','nice-looking','fantastic','splendid','magnificent','glorious','exquisite','pleasant','nice','awesome','excellent','superb','marvellous','charming','attractive','delightful','wonderful','glowing','shining','graceful','shiny','tempting','lovable','gracious','romantic','ravishing','sensational','phenomenal','astonishing','tremendous','exceptional','impressive','magical','stupendous','fascinating','dazzling','captivating','alluring','elegant','exciting','entrancing','compelling','enticing','stylish','staggering','striking','sparkling','radiant','gorgeous','sensual','exotic','classy','glamorous'],
'exquisite' :  ['beautiful','sexy','cute','cutie','pretty','sweet','breathtaking','adorable','spectacular','dashing','incredible','hot','cool','terrific','amazing','marvelous','enchanting','fabulous','appealing','lovely', 'stunning','nice-looking','fantastic','splendid','magnificent','glorious','exquisite','pleasant','nice','awesome','excellent','superb','marvellous','charming','attractive','delightful','wonderful','glowing','shining','graceful','shiny','tempting','lovable','gracious','romantic','ravishing','sensational','phenomenal','astonishing','tremendous','exceptional','impressive','magical','stupendous','fascinating','dazzling','captivating','alluring','elegant','exciting','entrancing','compelling','enticing','stylish','staggering','striking','sparkling','radiant','gorgeous','sensual','exotic','classy','glamorous'],
'pleasant' :  ['beautiful','sexy','cute','cutie','pretty','sweet','breathtaking','adorable','spectacular','dashing','incredible','hot','cool','terrific','amazing','marvelous','enchanting','fabulous','appealing','lovely', 'stunning','nice-looking','fantastic','splendid','magnificent','glorious','exquisite','pleasant','nice','awesome','excellent','superb','marvellous','charming','attractive','delightful','wonderful','glowing','shining','graceful','shiny','tempting','lovable','gracious','romantic','ravishing','sensational','phenomenal','astonishing','tremendous','exceptional','impressive','magical','stupendous','fascinating','dazzling','captivating','alluring','elegant','exciting','entrancing','compelling','enticing','stylish','staggering','striking','sparkling','radiant','gorgeous','sensual','exotic','classy','glamorous'],
'nice' :  ['beautiful','sexy','cute','cutie','pretty','sweet','breathtaking','adorable','spectacular','dashing','incredible','hot','cool','terrific','amazing','marvelous','enchanting','fabulous','appealing','lovely', 'stunning','nice-looking','fantastic','splendid','magnificent','glorious','exquisite','pleasant','nice','awesome','excellent','superb','marvellous','charming','attractive','delightful','wonderful','glowing','shining','graceful','shiny','tempting','lovable','gracious','romantic','ravishing','sensational','phenomenal','astonishing','tremendous','exceptional','impressive','magical','stupendous','fascinating','dazzling','captivating','alluring','elegant','exciting','entrancing','compelling','enticing','stylish','staggering','striking','sparkling','radiant','gorgeous','sensual','exotic','classy','glamorous'],
'awesome' :  ['beautiful','sexy','cute','cutie','pretty','sweet','breathtaking','adorable','spectacular','dashing','incredible','hot','cool','terrific','amazing','marvelous','enchanting','fabulous','appealing','lovely', 'stunning','nice-looking','fantastic','splendid','magnificent','glorious','exquisite','pleasant','nice','awesome','excellent','superb','marvellous','charming','attractive','delightful','wonderful','glowing','shining','graceful','shiny','tempting','lovable','gracious','romantic','ravishing','sensational','phenomenal','astonishing','tremendous','exceptional','impressive','magical','stupendous','fascinating','dazzling','captivating','alluring','elegant','exciting','entrancing','compelling','enticing','stylish','staggering','striking','sparkling','radiant','gorgeous','sensual','exotic','classy','glamorous'],
'excellent' :  ['beautiful','sexy','cute','cutie','pretty','sweet','breathtaking','adorable','spectacular','dashing','incredible','hot','cool','terrific','amazing','marvelous','enchanting','fabulous','appealing','lovely', 'stunning','nice-looking','fantastic','splendid','magnificent','glorious','exquisite','pleasant','nice','awesome','excellent','superb','marvellous','charming','attractive','delightful','wonderful','glowing','shining','graceful','shiny','tempting','lovable','gracious','romantic','ravishing','sensational','phenomenal','astonishing','tremendous','exceptional','impressive','magical','stupendous','fascinating','dazzling','captivating','alluring','elegant','exciting','entrancing','compelling','enticing','stylish','staggering','striking','sparkling','radiant','gorgeous','sensual','exotic','classy','glamorous'],
'superb' :  ['beautiful','sexy','cute','cutie','pretty','sweet','breathtaking','adorable','spectacular','dashing','incredible','hot','cool','terrific','amazing','marvelous','enchanting','fabulous','appealing','lovely', 'stunning','nice-looking','fantastic','splendid','magnificent','glorious','exquisite','pleasant','nice','awesome','excellent','superb','marvellous','charming','attractive','delightful','wonderful','glowing','shining','graceful','shiny','tempting','lovable','gracious','romantic','ravishing','sensational','phenomenal','astonishing','tremendous','exceptional','impressive','magical','stupendous','fascinating','dazzling','captivating','alluring','elegant','exciting','entrancing','compelling','enticing','stylish','staggering','striking','sparkling','radiant','gorgeous','sensual','exotic','classy','glamorous'],
'marvellous' :  ['beautiful','sexy','cute','cutie','pretty','sweet','breathtaking','adorable','spectacular','dashing','incredible','hot','cool','terrific','amazing','marvelous','enchanting','fabulous','appealing','lovely', 'stunning','nice-looking','fantastic','splendid','magnificent','glorious','exquisite','pleasant','nice','awesome','excellent','superb','marvellous','charming','attractive','delightful','wonderful','glowing','shining','graceful','shiny','tempting','lovable','gracious','romantic','ravishing','sensational','phenomenal','astonishing','tremendous','exceptional','impressive','magical','stupendous','fascinating','dazzling','captivating','alluring','elegant','exciting','entrancing','compelling','enticing','stylish','staggering','striking','sparkling','radiant','gorgeous','sensual','exotic','classy','glamorous'],
'charming' :  ['beautiful','sexy','cute','cutie','pretty','sweet','breathtaking','adorable','spectacular','dashing','incredible','hot','cool','terrific','amazing','marvelous','enchanting','fabulous','appealing','lovely', 'stunning','nice-looking','fantastic','splendid','magnificent','glorious','exquisite','pleasant','nice','awesome','excellent','superb','marvellous','charming','attractive','delightful','wonderful','glowing','shining','graceful','shiny','tempting','lovable','gracious','romantic','ravishing','sensational','phenomenal','astonishing','tremendous','exceptional','impressive','magical','stupendous','fascinating','dazzling','captivating','alluring','elegant','exciting','entrancing','compelling','enticing','stylish','staggering','striking','sparkling','radiant','gorgeous','sensual','exotic','classy','glamorous'],

'attractive' :  ['beautiful','sexy','cute','cutie','pretty','sweet','breathtaking','adorable','spectacular','dashing','incredible','hot','cool','terrific','amazing','marvelous','enchanting','fabulous','appealing','lovely', 'stunning','nice-looking','fantastic','splendid','magnificent','glorious','exquisite','pleasant','nice','awesome','excellent','superb','marvellous','charming','attractive','delightful','wonderful','glowing','shining','graceful','shiny','tempting','lovable','gracious','romantic','ravishing','sensational','phenomenal','astonishing','tremendous','exceptional','impressive','magical','stupendous','fascinating','dazzling','captivating','alluring','elegant','exciting','entrancing','compelling','enticing','stylish','staggering','striking','sparkling','radiant','gorgeous','sensual','exotic','classy','glamorous'],
'delightful' :  ['beautiful','sexy','cute','cutie','pretty','sweet','breathtaking','adorable','spectacular','dashing','incredible','hot','cool','terrific','amazing','marvelous','enchanting','fabulous','appealing','lovely', 'stunning','nice-looking','fantastic','splendid','magnificent','glorious','exquisite','pleasant','nice','awesome','excellent','superb','marvellous','charming','attractive','delightful','wonderful','glowing','shining','graceful','shiny','tempting','lovable','gracious','romantic','ravishing','sensational','phenomenal','astonishing','tremendous','exceptional','impressive','magical','stupendous','fascinating','dazzling','captivating','alluring','elegant','exciting','entrancing','compelling','enticing','stylish','staggering','striking','sparkling','radiant','gorgeous','sensual','exotic','classy','glamorous'],
'wonderful' :  ['beautiful','sexy','cute','cutie','pretty','sweet','breathtaking','adorable','spectacular','dashing','incredible','hot','cool','terrific','amazing','marvelous','enchanting','fabulous','appealing','lovely', 'stunning','nice-looking','fantastic','splendid','magnificent','glorious','exquisite','pleasant','nice','awesome','excellent','superb','marvellous','charming','attractive','delightful','wonderful','glowing','shining','graceful','shiny','tempting','lovable','gracious','romantic','ravishing','sensational','phenomenal','astonishing','tremendous','exceptional','impressive','magical','stupendous','fascinating','dazzling','captivating','alluring','elegant','exciting','entrancing','compelling','enticing','stylish','staggering','striking','sparkling','radiant','gorgeous','sensual','exotic','classy','glamorous'],
'glowing' :  ['beautiful','sexy','cute','cutie','pretty','sweet','breathtaking','adorable','spectacular','dashing','incredible','hot','cool','terrific','amazing','marvelous','enchanting','fabulous','appealing','lovely', 'stunning','nice-looking','fantastic','splendid','magnificent','glorious','exquisite','pleasant','nice','awesome','excellent','superb','marvellous','charming','attractive','delightful','wonderful','glowing','shining','graceful','shiny','tempting','lovable','gracious','romantic','ravishing','sensational','phenomenal','astonishing','tremendous','exceptional','impressive','magical','stupendous','fascinating','dazzling','captivating','alluring','elegant','exciting','entrancing','compelling','enticing','stylish','staggering','striking','sparkling','radiant','gorgeous','sensual','exotic','classy','glamorous'],
'shining' :  ['beautiful','sexy','cute','cutie','pretty','sweet','breathtaking','adorable','spectacular','dashing','incredible','hot','cool','terrific','amazing','marvelous','enchanting','fabulous','appealing','lovely', 'stunning','nice-looking','fantastic','splendid','magnificent','glorious','exquisite','pleasant','nice','awesome','excellent','superb','marvellous','charming','attractive','delightful','wonderful','glowing','shining','graceful','shiny','tempting','lovable','gracious','romantic','ravishing','sensational','phenomenal','astonishing','tremendous','exceptional','impressive','magical','stupendous','fascinating','dazzling','captivating','alluring','elegant','exciting','entrancing','compelling','enticing','stylish','staggering','striking','sparkling','radiant','gorgeous','sensual','exotic','classy','glamorous'],
'graceful' :  ['beautiful','sexy','cute','cutie','pretty','sweet','breathtaking','adorable','spectacular','dashing','incredible','hot','cool','terrific','amazing','marvelous','enchanting','fabulous','appealing','lovely', 'stunning','nice-looking','fantastic','splendid','magnificent','glorious','exquisite','pleasant','nice','awesome','excellent','superb','marvellous','charming','attractive','delightful','wonderful','glowing','shining','graceful','shiny','tempting','lovable','gracious','romantic','ravishing','sensational','phenomenal','astonishing','tremendous','exceptional','impressive','magical','stupendous','fascinating','dazzling','captivating','alluring','elegant','exciting','entrancing','compelling','enticing','stylish','staggering','striking','sparkling','radiant','gorgeous','sensual','exotic','classy','glamorous'],
'tempting' :  ['beautiful','sexy','cute','cutie','pretty','sweet','breathtaking','adorable','spectacular','dashing','incredible','hot','cool','terrific','amazing','marvelous','enchanting','fabulous','appealing','lovely', 'stunning','nice-looking','fantastic','splendid','magnificent','glorious','exquisite','pleasant','nice','awesome','excellent','superb','marvellous','charming','attractive','delightful','wonderful','glowing','shining','graceful','shiny','tempting','lovable','gracious','romantic','ravishing','sensational','phenomenal','astonishing','tremendous','exceptional','impressive','magical','stupendous','fascinating','dazzling','captivating','alluring','elegant','exciting','entrancing','compelling','enticing','stylish','staggering','striking','sparkling','radiant','gorgeous','sensual','exotic','classy','glamorous'],
'lovable' :  ['beautiful','sexy','cute','cutie','pretty','sweet','breathtaking','adorable','spectacular','dashing','incredible','hot','cool','terrific','amazing','marvelous','enchanting','fabulous','appealing','lovely', 'stunning','nice-looking','fantastic','splendid','magnificent','glorious','exquisite','pleasant','nice','awesome','excellent','superb','marvellous','charming','attractive','delightful','wonderful','glowing','shining','graceful','shiny','tempting','lovable','gracious','romantic','ravishing','sensational','phenomenal','astonishing','tremendous','exceptional','impressive','magical','stupendous','fascinating','dazzling','captivating','alluring','elegant','exciting','entrancing','compelling','enticing','stylish','staggering','striking','sparkling','radiant','gorgeous','sensual','exotic','classy','glamorous'],
'graciouss' :  ['beautiful','sexy','cute','cutie','pretty','sweet','breathtaking','adorable','spectacular','dashing','incredible','hot','cool','terrific','amazing','marvelous','enchanting','fabulous','appealing','lovely', 'stunning','nice-looking','fantastic','splendid','magnificent','glorious','exquisite','pleasant','nice','awesome','excellent','superb','marvellous','charming','attractive','delightful','wonderful','glowing','shining','graceful','shiny','tempting','lovable','gracious','romantic','ravishing','sensational','phenomenal','astonishing','tremendous','exceptional','impressive','magical','stupendous','fascinating','dazzling','captivating','alluring','elegant','exciting','entrancing','compelling','enticing','stylish','staggering','striking','sparkling','radiant','gorgeous','sensual','exotic','classy','glamorous'],
'ravishing' :  ['beautiful','sexy','cute','cutie','pretty','sweet','breathtaking','adorable','spectacular','dashing','incredible','hot','cool','terrific','amazing','marvelous','enchanting','fabulous','appealing','lovely', 'stunning','nice-looking','fantastic','splendid','magnificent','glorious','exquisite','pleasant','nice','awesome','excellent','superb','marvellous','charming','attractive','delightful','wonderful','glowing','shining','graceful','shiny','tempting','lovable','gracious','romantic','ravishing','sensational','phenomenal','astonishing','tremendous','exceptional','impressive','magical','stupendous','fascinating','dazzling','captivating','alluring','elegant','exciting','entrancing','compelling','enticing','stylish','staggering','striking','sparkling','radiant','gorgeous','sensual','exotic','classy','glamorous'],
'sensational' :  ['beautiful','sexy','cute','cutie','pretty','sweet','breathtaking','adorable','spectacular','dashing','incredible','hot','cool','terrific','amazing','marvelous','enchanting','fabulous','appealing','lovely', 'stunning','nice-looking','fantastic','splendid','magnificent','glorious','exquisite','pleasant','nice','awesome','excellent','superb','marvellous','charming','attractive','delightful','wonderful','glowing','shining','graceful','shiny','tempting','lovable','gracious','romantic','ravishing','sensational','phenomenal','astonishing','tremendous','exceptional','impressive','magical','stupendous','fascinating','dazzling','captivating','alluring','elegant','exciting','entrancing','compelling','enticing','stylish','staggering','striking','sparkling','radiant','gorgeous','sensual','exotic','classy','glamorous'],
'phenomenal' :  ['beautiful','sexy','cute','cutie','pretty','sweet','breathtaking','adorable','spectacular','dashing','incredible','hot','cool','terrific','amazing','marvelous','enchanting','fabulous','appealing','lovely', 'stunning','nice-looking','fantastic','splendid','magnificent','glorious','exquisite','pleasant','nice','awesome','excellent','superb','marvellous','charming','attractive','delightful','wonderful','glowing','shining','graceful','shiny','tempting','lovable','gracious','romantic','ravishing','sensational','phenomenal','astonishing','tremendous','exceptional','impressive','magical','stupendous','fascinating','dazzling','captivating','alluring','elegant','exciting','entrancing','compelling','enticing','stylish','staggering','striking','sparkling','radiant','gorgeous','sensual','exotic','classy','glamorous'],
'astonishing' :  ['beautiful','sexy','cute','cutie','pretty','sweet','breathtaking','adorable','spectacular','dashing','incredible','hot','cool','terrific','amazing','marvelous','enchanting','fabulous','appealing','lovely', 'stunning','nice-looking','fantastic','splendid','magnificent','glorious','exquisite','pleasant','nice','awesome','excellent','superb','marvellous','charming','attractive','delightful','wonderful','glowing','shining','graceful','shiny','tempting','lovable','gracious','romantic','ravishing','sensational','phenomenal','astonishing','tremendous','exceptional','impressive','magical','stupendous','fascinating','dazzling','captivating','alluring','elegant','exciting','entrancing','compelling','enticing','stylish','staggering','striking','sparkling','radiant','gorgeous','sensual','exotic','classy','glamorous'],
'tremendous' :  ['beautiful','sexy','cute','cutie','pretty','sweet','breathtaking','adorable','spectacular','dashing','incredible','hot','cool','terrific','amazing','marvelous','enchanting','fabulous','appealing','lovely', 'stunning','nice-looking','fantastic','splendid','magnificent','glorious','exquisite','pleasant','nice','awesome','excellent','superb','marvellous','charming','attractive','delightful','wonderful','glowing','shining','graceful','shiny','tempting','lovable','gracious','romantic','ravishing','sensational','phenomenal','astonishing','tremendous','exceptional','impressive','magical','stupendous','fascinating','dazzling','captivating','alluring','elegant','exciting','entrancing','compelling','enticing','stylish','staggering','striking','sparkling','radiant','gorgeous','sensual','exotic','classy','glamorous'],
'exceptional' :  ['beautiful','sexy','cute','cutie','pretty','sweet','breathtaking','adorable','spectacular','dashing','incredible','hot','cool','terrific','amazing','marvelous','enchanting','fabulous','appealing','lovely', 'stunning','nice-looking','fantastic','splendid','magnificent','glorious','exquisite','pleasant','nice','awesome','excellent','superb','marvellous','charming','attractive','delightful','wonderful','glowing','shining','graceful','shiny','tempting','lovable','gracious','romantic','ravishing','sensational','phenomenal','astonishing','tremendous','exceptional','impressive','magical','stupendous','fascinating','dazzling','captivating','alluring','elegant','exciting','entrancing','compelling','enticing','stylish','staggering','striking','sparkling','radiant','gorgeous','sensual','exotic','classy','glamorous'],
'impressive' :  ['beautiful','sexy','cute','cutie','pretty','sweet','breathtaking','adorable','spectacular','dashing','incredible','hot','cool','terrific','amazing','marvelous','enchanting','fabulous','appealing','lovely', 'stunning','nice-looking','fantastic','splendid','magnificent','glorious','exquisite','pleasant','nice','awesome','excellent','superb','marvellous','charming','attractive','delightful','wonderful','glowing','shining','graceful','shiny','tempting','lovable','gracious','romantic','ravishing','sensational','phenomenal','astonishing','tremendous','exceptional','impressive','magical','stupendous','fascinating','dazzling','captivating','alluring','elegant','exciting','entrancing','compelling','enticing','stylish','staggering','striking','sparkling','radiant','gorgeous','sensual','exotic','classy','glamorous'],
'magical' :  ['beautiful','sexy','cute','cutie','pretty','sweet','breathtaking','adorable','spectacular','dashing','incredible','hot','cool','terrific','amazing','marvelous','enchanting','fabulous','appealing','lovely', 'stunning','nice-looking','fantastic','splendid','magnificent','glorious','exquisite','pleasant','nice','awesome','excellent','superb','marvellous','charming','attractive','delightful','wonderful','glowing','shining','graceful','shiny','tempting','lovable','gracious','romantic','ravishing','sensational','phenomenal','astonishing','tremendous','exceptional','impressive','magical','stupendous','fascinating','dazzling','captivating','alluring','elegant','exciting','entrancing','compelling','enticing','stylish','staggering','striking','sparkling','radiant','gorgeous','sensual','exotic','classy','glamorous'],
'stupendous' :  ['beautiful','sexy','cute','cutie','pretty','sweet','breathtaking','adorable','spectacular','dashing','incredible','hot','cool','terrific','amazing','marvelous','enchanting','fabulous','appealing','lovely', 'stunning','nice-looking','fantastic','splendid','magnificent','glorious','exquisite','pleasant','nice','awesome','excellent','superb','marvellous','charming','attractive','delightful','wonderful','glowing','shining','graceful','shiny','tempting','lovable','gracious','romantic','ravishing','sensational','phenomenal','astonishing','tremendous','exceptional','impressive','magical','stupendous','fascinating','dazzling','captivating','alluring','elegant','exciting','entrancing','compelling','enticing','stylish','staggering','striking','sparkling','radiant','gorgeous','sensual','exotic','classy','glamorous'],
'fascinating' :  ['beautiful','sexy','cute','cutie','pretty','sweet','breathtaking','adorable','spectacular','dashing','incredible','hot','cool','terrific','amazing','marvelous','enchanting','fabulous','appealing','lovely', 'stunning','nice-looking','fantastic','splendid','magnificent','glorious','exquisite','pleasant','nice','awesome','excellent','superb','marvellous','charming','attractive','delightful','wonderful','glowing','shining','graceful','shiny','tempting','lovable','gracious','romantic','ravishing','sensational','phenomenal','astonishing','tremendous','exceptional','impressive','magical','stupendous','fascinating','dazzling','captivating','alluring','elegant','exciting','entrancing','compelling','enticing','stylish','staggering','striking','sparkling','radiant','gorgeous','sensual','exotic','classy','glamorous'],
'dazzling' :  ['beautiful','sexy','cute','cutie','pretty','sweet','breathtaking','adorable','spectacular','dashing','incredible','hot','cool','terrific','amazing','marvelous','enchanting','fabulous','appealing','lovely', 'stunning','nice-looking','fantastic','splendid','magnificent','glorious','exquisite','pleasant','nice','awesome','excellent','superb','marvellous','charming','attractive','delightful','wonderful','glowing','shining','graceful','shiny','tempting','lovable','gracious','romantic','ravishing','sensational','phenomenal','astonishing','tremendous','exceptional','impressive','magical','stupendous','fascinating','dazzling','captivating','alluring','elegant','exciting','entrancing','compelling','enticing','stylish','staggering','striking','sparkling','radiant','gorgeous','sensual','exotic','classy','glamorous'],
'alluring' :  ['beautiful','sexy','cute','cutie','pretty','sweet','breathtaking','adorable','spectacular','dashing','incredible','hot','cool','terrific','amazing','marvelous','enchanting','fabulous','appealing','lovely', 'stunning','nice-looking','fantastic','splendid','magnificent','glorious','exquisite','pleasant','nice','awesome','excellent','superb','marvellous','charming','attractive','delightful','wonderful','glowing','shining','graceful','shiny','tempting','lovable','gracious','romantic','ravishing','sensational','phenomenal','astonishing','tremendous','exceptional','impressive','magical','stupendous','fascinating','dazzling','captivating','alluring','elegant','exciting','entrancing','compelling','enticing','stylish','staggering','striking','sparkling','radiant','gorgeous','sensual','exotic','classy','glamorous'],
'elegant' :  ['beautiful','sexy','cute','cutie','pretty','sweet','breathtaking','adorable','spectacular','dashing','incredible','hot','cool','terrific','amazing','marvelous','enchanting','fabulous','appealing','lovely', 'stunning','nice-looking','fantastic','splendid','magnificent','glorious','exquisite','pleasant','nice','awesome','excellent','superb','marvellous','charming','attractive','delightful','wonderful','glowing','shining','graceful','shiny','tempting','lovable','gracious','romantic','ravishing','sensational','phenomenal','astonishing','tremendous','exceptional','impressive','magical','stupendous','fascinating','dazzling','captivating','alluring','elegant','exciting','entrancing','compelling','enticing','stylish','staggering','striking','sparkling','radiant','gorgeous','sensual','exotic','classy','glamorous'],
'exciting' :  ['beautiful','sexy','cute','cutie','pretty','sweet','breathtaking','adorable','spectacular','dashing','incredible','hot','cool','terrific','amazing','marvelous','enchanting','fabulous','appealing','lovely', 'stunning','nice-looking','fantastic','splendid','magnificent','glorious','exquisite','pleasant','nice','awesome','excellent','superb','marvellous','charming','attractive','delightful','wonderful','glowing','shining','graceful','shiny','tempting','lovable','gracious','romantic','ravishing','sensational','phenomenal','astonishing','tremendous','exceptional','impressive','magical','stupendous','fascinating','dazzling','captivating','alluring','elegant','exciting','entrancing','compelling','enticing','stylish','staggering','striking','sparkling','radiant','gorgeous','sensual','exotic','classy','glamorous'],
'entrancing' :  ['beautiful','sexy','cute','cutie','pretty','sweet','breathtaking','adorable','spectacular','dashing','incredible','hot','cool','terrific','amazing','marvelous','enchanting','fabulous','appealing','lovely', 'stunning','nice-looking','fantastic','splendid','magnificent','glorious','exquisite','pleasant','nice','awesome','excellent','superb','marvellous','charming','attractive','delightful','wonderful','glowing','shining','graceful','shiny','tempting','lovable','gracious','romantic','ravishing','sensational','phenomenal','astonishing','tremendous','exceptional','impressive','magical','stupendous','fascinating','dazzling','captivating','alluring','elegant','exciting','entrancing','compelling','enticing','stylish','staggering','striking','sparkling','radiant','gorgeous','sensual','exotic','classy','glamorous'],
'compelling' :  ['beautiful','sexy','cute','cutie','pretty','sweet','breathtaking','adorable','spectacular','dashing','incredible','hot','cool','terrific','amazing','marvelous','enchanting','fabulous','appealing','lovely', 'stunning','nice-looking','fantastic','splendid','magnificent','glorious','exquisite','pleasant','nice','awesome','excellent','superb','marvellous','charming','attractive','delightful','wonderful','glowing','shining','graceful','shiny','tempting','lovable','gracious','romantic','ravishing','sensational','phenomenal','astonishing','tremendous','exceptional','impressive','magical','stupendous','fascinating','dazzling','captivating','alluring','elegant','exciting','entrancing','compelling','enticing','stylish','staggering','striking','sparkling','radiant','gorgeous','sensual','exotic','classy','glamorous'],
'enticing' :  ['beautiful','sexy','cute','cutie','pretty','sweet','breathtaking','adorable','spectacular','dashing','incredible','hot','cool','terrific','amazing','marvelous','enchanting','fabulous','appealing','lovely', 'stunning','nice-looking','fantastic','splendid','magnificent','glorious','exquisite','pleasant','nice','awesome','excellent','superb','marvellous','charming','attractive','delightful','wonderful','glowing','shining','graceful','shiny','tempting','lovable','gracious','romantic','ravishing','sensational','phenomenal','astonishing','tremendous','exceptional','impressive','magical','stupendous','fascinating','dazzling','captivating','alluring','elegant','exciting','entrancing','compelling','enticing','stylish','staggering','striking','sparkling','radiant','gorgeous','sensual','exotic','classy','glamorous'],
'stylish' :  ['beautiful','sexy','cute','cutie','pretty','sweet','breathtaking','adorable','spectacular','dashing','incredible','hot','cool','terrific','amazing','marvelous','enchanting','fabulous','appealing','lovely', 'stunning','nice-looking','fantastic','splendid','magnificent','glorious','exquisite','pleasant','nice','awesome','excellent','superb','marvellous','charming','attractive','delightful','wonderful','glowing','shining','graceful','shiny','tempting','lovable','gracious','romantic','ravishing','sensational','phenomenal','astonishing','tremendous','exceptional','impressive','magical','stupendous','fascinating','dazzling','captivating','alluring','elegant','exciting','entrancing','compelling','enticing','stylish','staggering','striking','sparkling','radiant','gorgeous','sensual','exotic','classy','glamorous'],
'staggering' :  ['beautiful','sexy','cute','cutie','pretty','sweet','breathtaking','adorable','spectacular','dashing','incredible','hot','cool','terrific','amazing','marvelous','enchanting','fabulous','appealing','lovely', 'stunning','nice-looking','fantastic','splendid','magnificent','glorious','exquisite','pleasant','nice','awesome','excellent','superb','marvellous','charming','attractive','delightful','wonderful','glowing','shining','graceful','shiny','tempting','lovable','gracious','romantic','ravishing','sensational','phenomenal','astonishing','tremendous','exceptional','impressive','magical','stupendous','fascinating','dazzling','captivating','alluring','elegant','exciting','entrancing','compelling','enticing','stylish','staggering','striking','sparkling','radiant','gorgeous','sensual','exotic','classy','glamorous'],
'striking' :  ['beautiful','sexy','cute','cutie','pretty','sweet','breathtaking','adorable','spectacular','dashing','incredible','hot','cool','terrific','amazing','marvelous','enchanting','fabulous','appealing','lovely', 'stunning','nice-looking','fantastic','splendid','magnificent','glorious','exquisite','pleasant','nice','awesome','excellent','superb','marvellous','charming','attractive','delightful','wonderful','glowing','shining','graceful','shiny','tempting','lovable','gracious','romantic','ravishing','sensational','phenomenal','astonishing','tremendous','exceptional','impressive','magical','stupendous','fascinating','dazzling','captivating','alluring','elegant','exciting','entrancing','compelling','enticing','stylish','staggering','striking','sparkling','radiant','gorgeous','sensual','exotic','classy','glamorous'],

'sparkling' :  ['beautiful','sexy','cute','cutie','pretty','sweet','breathtaking','adorable','spectacular','dashing','incredible','hot','cool','terrific','amazing','marvelous','enchanting','fabulous','appealing','lovely', 'stunning','nice-looking','fantastic','splendid','magnificent','glorious','exquisite','pleasant','nice','awesome','excellent','superb','marvellous','charming','attractive','delightful','wonderful','glowing','shining','graceful','shiny','tempting','lovable','gracious','romantic','ravishing','sensational','phenomenal','astonishing','tremendous','exceptional','impressive','magical','stupendous','fascinating','dazzling','captivating','alluring','elegant','exciting','entrancing','compelling','enticing','stylish','staggering','striking','sparkling','radiant','gorgeous','sensual','exotic','classy','glamorous'],
'blistering' :  ['beautiful','sexy','cute','cutie','pretty','sweet','breathtaking','adorable','spectacular','dashing','incredible','hot','cool','terrific','amazing','marvelous','enchanting','fabulous','appealing','lovely', 'stunning','nice-looking','fantastic','splendid','magnificent','glorious','exquisite','pleasant','nice','awesome','excellent','superb','marvellous','charming','attractive','delightful','wonderful','glowing','shining','graceful','shiny','tempting','lovable','gracious','romantic','ravishing','sensational','phenomenal','astonishing','tremendous','exceptional','impressive','magical','stupendous','fascinating','dazzling','captivating','alluring','elegant','exciting','entrancing','compelling','enticing','stylish','staggering','striking','sparkling','radiant','gorgeous','sensual','exotic','classy','glamorous'],
'radiant' :  ['beautiful','sexy','cute','cutie','pretty','sweet','breathtaking','adorable','spectacular','dashing','incredible','hot','cool','terrific','amazing','marvelous','enchanting','fabulous','appealing','lovely', 'stunning','nice-looking','fantastic','splendid','magnificent','glorious','exquisite','pleasant','nice','awesome','excellent','superb','marvellous','charming','attractive','delightful','wonderful','glowing','shining','graceful','shiny','tempting','lovable','gracious','romantic','ravishing','sensational','phenomenal','astonishing','tremendous','exceptional','impressive','magical','stupendous','fascinating','dazzling','captivating','alluring','elegant','exciting','entrancing','compelling','enticing','stylish','staggering','striking','sparkling','radiant','gorgeous','sensual','exotic','classy','glamorous'],
'gorgeous' :  ['beautiful','sexy','cute','cutie','pretty','sweet','breathtaking','adorable','spectacular','dashing','incredible','hot','cool','terrific','amazing','marvelous','enchanting','fabulous','appealing','lovely', 'stunning','nice-looking','fantastic','splendid','magnificent','glorious','exquisite','pleasant','nice','awesome','excellent','superb','marvellous','charming','attractive','delightful','wonderful','glowing','shining','graceful','shiny','tempting','lovable','gracious','romantic','ravishing','sensational','phenomenal','astonishing','tremendous','exceptional','impressive','magical','stupendous','fascinating','dazzling','captivating','alluring','elegant','exciting','entrancing','compelling','enticing','stylish','staggering','striking','sparkling','radiant','gorgeous','sensual','exotic','classy','glamorous'],
'sensual' :  ['beautiful','sexy','cute','cutie','pretty','sweet','breathtaking','adorable','spectacular','dashing','incredible','hot','cool','terrific','amazing','marvelous','enchanting','fabulous','appealing','lovely', 'stunning','nice-looking','fantastic','splendid','magnificent','glorious','exquisite','pleasant','nice','awesome','excellent','superb','marvellous','charming','attractive','delightful','wonderful','glowing','shining','graceful','shiny','tempting','lovable','gracious','romantic','ravishing','sensational','phenomenal','astonishing','tremendous','exceptional','impressive','magical','stupendous','fascinating','dazzling','captivating','alluring','elegant','exciting','entrancing','compelling','enticing','stylish','staggering','striking','sparkling','radiant','gorgeous','sensual','exotic','classy','glamorous'],
'sensuous' :  ['beautiful','sexy','cute','cutie','pretty','sweet','breathtaking','adorable','spectacular','dashing','incredible','hot','cool','terrific','amazing','marvelous','enchanting','fabulous','appealing','lovely', 'stunning','nice-looking','fantastic','splendid','magnificent','glorious','exquisite','pleasant','nice','awesome','excellent','superb','marvellous','charming','attractive','delightful','wonderful','glowing','shining','graceful','shiny','tempting','lovable','gracious','romantic','ravishing','sensational','phenomenal','astonishing','tremendous','exceptional','impressive','magical','stupendous','fascinating','dazzling','captivating','alluring','elegant','exciting','entrancing','compelling','enticing','stylish','staggering','striking','sparkling','radiant','gorgeous','sensual','exotic','classy','glamorous'],
'exotic' :  ['beautiful','sexy','cute','cutie','pretty','sweet','breathtaking','adorable','spectacular','dashing','incredible','hot','cool','terrific','amazing','marvelous','enchanting','fabulous','appealing','lovely', 'stunning','nice-looking','fantastic','splendid','magnificent','glorious','exquisite','pleasant','nice','awesome','excellent','superb','marvellous','charming','attractive','delightful','wonderful','glowing','shining','graceful','shiny','tempting','lovable','gracious','romantic','ravishing','sensational','phenomenal','astonishing','tremendous','exceptional','impressive','magical','stupendous','fascinating','dazzling','captivating','alluring','elegant','exciting','entrancing','compelling','enticing','stylish','staggering','striking','sparkling','radiant','gorgeous','sensual','exotic','classy','glamorous'],
'classy' :  ['beautiful','sexy','cute','cutie','pretty','sweet','breathtaking','adorable','spectacular','dashing','incredible','hot','cool','terrific','amazing','marvelous','enchanting','fabulous','appealing','lovely', 'stunning','nice-looking','fantastic','splendid','magnificent','glorious','exquisite','pleasant','nice','awesome','excellent','superb','marvellous','charming','attractive','delightful','wonderful','glowing','shining','graceful','shiny','tempting','lovable','gracious','romantic','ravishing','sensational','phenomenal','astonishing','tremendous','exceptional','impressive','magical','stupendous','fascinating','dazzling','captivating','alluring','elegant','exciting','entrancing','compelling','enticing','stylish','staggering','striking','sparkling','radiant','gorgeous','sensual','exotic','classy','glamorous'],
'glamorous' :  ['beautiful','sexy','cute','cutie','pretty','sweet','breathtaking','adorable','spectacular','dashing','incredible','hot','cool','terrific','amazing','marvelous','enchanting','fabulous','appealing','lovely', 'stunning','nice-looking','fantastic','splendid','magnificent','glorious','exquisite','pleasant','nice','awesome','excellent','superb','marvellous','charming','attractive','delightful','wonderful','glowing','shining','graceful','shiny','tempting','lovable','gracious','romantic','ravishing','sensational','phenomenal','astonishing','tremendous','exceptional','impressive','magical','stupendous','fascinating','dazzling','captivating','alluring','elegant','exciting','entrancing','compelling','enticing','stylish','staggering','striking','sparkling','radiant','gorgeous','sensual','exotic','classy','glamorous'],
'glamor' :  ['beautiful','sexy','cute','cutie','pretty','sweet','breathtaking','adorable','spectacular','dashing','incredible','hot','cool','terrific','amazing','marvelous','enchanting','fabulous','appealing','lovely', 'stunning','nice-looking','fantastic','splendid','magnificent','glorious','exquisite','pleasant','nice','awesome','excellent','superb','marvellous','charming','attractive','delightful','wonderful','glowing','shining','graceful','shiny','tempting','lovable','gracious','romantic','ravishing','sensational','phenomenal','astonishing','tremendous','exceptional','impressive','magical','stupendous','fascinating','dazzling','captivating','alluring','elegant','exciting','entrancing','compelling','enticing','stylish','staggering','striking','sparkling','radiant','gorgeous','sensual','exotic','classy','glamorous'],
'glamour' :  ['beautiful','sexy','cute','cutie','pretty','sweet','breathtaking','adorable','spectacular','dashing','incredible','hot','cool','terrific','amazing','marvelous','enchanting','fabulous','appealing','lovely', 'stunning','nice-looking','fantastic','splendid','magnificent','glorious','exquisite','pleasant','nice','awesome','excellent','superb','marvellous','charming','attractive','delightful','wonderful','glowing','shining','graceful','shiny','tempting','lovable','gracious','romantic','ravishing','sensational','phenomenal','astonishing','tremendous','exceptional','impressive','magical','stupendous','fascinating','dazzling','captivating','alluring','elegant','exciting','entrancing','compelling','enticing','stylish','staggering','striking','sparkling','radiant','gorgeous','sensual','exotic','classy','glamorous'],
'glam' :  ['beautiful','sexy','cute','cutie','pretty','sweet','breathtaking','adorable','spectacular','dashing','incredible','hot','cool','terrific','amazing','marvelous','enchanting','fabulous','appealing','lovely', 'stunning','nice-looking','fantastic','splendid','magnificent','glorious','exquisite','pleasant','nice','awesome','excellent','superb','marvellous','charming','attractive','delightful','wonderful','glowing','shining','graceful','shiny','tempting','lovable','gracious','romantic','ravishing','sensational','phenomenal','astonishing','tremendous','exceptional','impressive','magical','stupendous','fascinating','dazzling','captivating','alluring','elegant','exciting','entrancing','compelling','enticing','stylish','staggering','striking','sparkling','radiant','gorgeous','sensual','exotic','classy','glamorous'],
'betty' :  ['beautiful','sexy','cute','cutie','pretty','sweet','breathtaking','adorable','spectacular','dashing','incredible','hot','cool','terrific','amazing','marvelous','enchanting','fabulous','appealing','lovely', 'stunning','nice-looking','fantastic','splendid','magnificent','glorious','exquisite','pleasant','nice','awesome','excellent','superb','marvellous','charming','attractive','delightful','wonderful','glowing','shining','graceful','shiny','tempting','lovable','gracious','romantic','ravishing','sensational','phenomenal','astonishing','tremendous','exceptional','impressive','magical','stupendous','fascinating','dazzling','captivating','alluring','elegant','exciting','entrancing','compelling','enticing','stylish','staggering','striking','sparkling','radiant','gorgeous','sensual','exotic','classy','glamorous'],
'stunner' :  ['stunner','beautiful','sexy','cute','cutie','pretty','sweet','breathtaking','adorable','spectacular','dashing','incredible','hot','cool','terrific','amazing','marvelous','enchanting','fabulous','appealing','lovely', 'stunning','nice-looking','fantastic','splendid','magnificent','glorious','exquisite','pleasant','nice','awesome','excellent','superb','marvellous','charming','attractive','delightful','wonderful','glowing','shining','graceful','shiny','tempting','lovable','gracious','romantic','ravishing','sensational','phenomenal','astonishing','tremendous','exceptional','impressive','magical','stupendous','fascinating','dazzling','captivating','alluring','elegant','exciting','entrancing','compelling','enticing','stylish','staggering','striking','sparkling','radiant','gorgeous','sensual','exotic','classy','glamorous'],

'sublime' :  ['sublime','beautiful','sexy','cute','cutie','pretty','sweet','breathtaking','adorable','spectacular','dashing','incredible','hot','cool','terrific','amazing','marvelous','enchanting','fabulous','appealing','lovely', 'stunning','nice-looking','fantastic','splendid','magnificent','glorious','exquisite','pleasant','nice','awesome','excellent','superb','marvellous','charming','attractive','delightful','wonderful','glowing','shining','graceful','shiny','tempting','lovable','gracious','romantic','ravishing','sensational','phenomenal','astonishing','tremendous','exceptional','impressive','magical','stupendous','fascinating','dazzling','captivating','alluring','elegant','exciting','entrancing','compelling','enticing','stylish','staggering','striking','sparkling','radiant','gorgeous','sensual','exotic','classy','glamorous'],

# /*anal*/
'anal' : ['analized', 'anal', 'anal sex', 'anal fuck', 'assfuck', 'assfucking', 'assfucked', 'assrailed', 'assdrilled', 'analplay', 'anally fucked', 'buttfuck', 'butt pound'],
'analsex' : ['analized', 'anal', 'anal sex', 'anal fuck', 'assfuck', 'assfucking', 'assfucked', 'assrailed', 'assdrilled', 'analplay', 'anally fucked', 'buttfuck', 'butt pound'],
'assfuck' : ['analized', 'anal', 'anal sex', 'anal fuck', 'assfuck', 'assfucking', 'assfucked', 'assrailed', 'assdrilled', 'analplay', 'anally fucked', 'buttfuck', 'butt pound'],
'assfucking' : ['anal', 'anal sex', 'anal fuck', 'assfuck', 'assfucking', 'assfucked', 'assrailed', 'assdrilled', 'analplay', 'anally fucked', 'buttfuck', 'butt pound'],
'assfucked' : ['analized', 'anal', 'anal sex', 'anal fuck', 'assfuck', 'assfucking', 'assfucked', 'assrailed', 'assdrilled', 'analplay', 'anally fucked', 'buttfuck', 'butt pound'],
'assrailed' : ['analized', 'anal', 'anal sex', 'anal fuck', 'assfuck', 'assfucking', 'assfucked', 'assrailed', 'assdrilled', 'analplay', 'anally fucked', 'buttfuck', 'butt pound'],
'analized' : ['analized', 'anal', 'anal sex', 'anal fuck', 'assfuck', 'assfucking', 'assfucked', 'assrailed', 'assdrilled', 'analplay', 'anally fucked', 'buttfuck', 'butt pound'],
'buttfuck' : ['analized','anal', 'anal sex', 'anal fuck', 'assfuck', 'assfucking', 'assfucked', 'assrailed', 'assdrilled', 'analplay', 'anally fucked', 'buttfuck', 'butt pound'],

'backdoor' : ['backdoor','anal','butt','assfuck','anal sex','buttfuck'],

# /*teen*/
'teen' :  ['teen', 'teenage', 'teenager',
          'young', 'younger', 'young girl',
		 '18 years old','18y','18yo',
		 '19 years old', '19y', '19yo',
		 '20 years old', '20y', '20yo',
		 '21 years old', '21y', '21yo',
		 'barely legal','skinny girl','small girl','petite',
		 'sister','step sister','stepsister','sis','sissy','sister in-law',
	     'small tits',
		 'schoolgirl','school girl',
		 'daughter','step-daughter','step daughter',
		 'innocent','student','niece','virgin'],

'teens' :  ['teen', 'teenage', 'teenager','young girl',
		 '18 years old','18y','18yo',
		 '19 years old', '19y', '19yo',
		 '20 years old', '20y', '20yo',
		 '21 years old', '21y', '21yo',
		 'barely legal','skinny girl','small girl','petite',
		 'sister','step sister','stepsister','sis','sissy','sister in-law',
	     'small tits',
		 'schoolgirl','school girl',
		 'daughter','step-daughter','step daughter',
		 'innocent','student','niece','virgin'],
		 
# /*young*/
'young' :  ['teen', 'teenage', 'teenager','young',
		 '18 years old','18y','18yo',
		 '19 years old', '19y', '19yo',
		 '20 years old', '20y', '20yo',
		 '21 years old', '21y', '21yo',
		 'barely legal','youthful','petite','youngish',
		 'innocent','tender','younger'],

'teenage' :  ['teen', 'teenage', 'teenager','young', 'younger',
		 '18 years old','18y','18yo',
		 '19 years old', '19y', '19yo',
		 '20 years old', '20y', '20yo',
		 '21 years old', '21y', '21yo',
		 'barely legal','skinny','petite','school going',
		 'innocent','student','virgin'],
'teenager' :  ['teen', 'teenage', 'teenager','young', 'younger',
		 '18 years old','18y','18yo',
		 '19 years old', '19y', '19yo',
		 '20 years old', '20y', '20yo',
		 '21 years old', '21y', '21yo',
		 'barely legal','skinny','petite','school going',
		 'innocent','student','virgin'],	

'petite' :  ['teen', 'teenage', 'teenager','young', 'younger',
		 '18 years old','18y','18yo',
		 '19 years old', '19y', '19yo',
		 '20 years old', '20y', '20yo',
		 '21 years old', '21y', '21yo',
		 'barely legal','skinny','petite','school going',
		 'innocent','little','virgin','small',],

# /*sister, sis, sissy, sister in-law*/
'sister' : ['sister','sis','sissy','sister in-law','not sister'], 
'sisters' : ['sisters','sis','sissy','sister in-law','not sisters'], 
'sis' : ['sister','sis','sissy','sister in-law','not sister'],	 
'sissy' : ['sister','sis','sissy','sister in-law','not sister'],	
'stepsis' : ['step sister','step sis','step sissy','sister in-law','stepsister','not his sister'],	
'stepsister' : ['step sister','step sis','step sissy','sister in-law','stepsis','not his sisters'],
	
 
# /*titted, boobed, breasted, chested, tits,titties, tit, titty, tity, Breasts, boob, boobs, boobies melon*/
'tit' : ['tit','boob','breast','chest','bosom','melon','rack'],
'boob' : ['tit','boob','breast','chest','bosom','melon','rack'],
'breast' : ['tit','boob','breast','chest','bosom','melon','rack'],
'chest' : ['tit','boob','breast','chest','bosom','melon','rack'],
'bosom' : ['tit','boob','breast','chest','bosom','melon','rack'],
'melon' : ['tit','boob','breast','chest','bosom','melon','rack'],
'rack' : ['tit','boob','breast','chest','bosom','melon','rack'],
'jugg' : ['tit','boob','breast','chest','bosom','melon','rack'],

'tits' : ['tits','titty', 'titties', 'tity', 'boobs','breasts','chests','bosoms','boobies','melons','racks'],
'titty' : ['tits','titty', 'tity', 'boobs','breasts','chests','bosoms','boobies','melons','racks','booby'],
'tity' : ['tits','titty', 'tity', 'boobs','breasts','chests','bosoms','boobies','melons','racks','booby'],
'booby' : ['tits','titty', 'tity', 'boobs','breasts','chests','bosoms','boobies','melons','racks','booby'],
'boobs' : ['tits','titty',  'titties', 'tity', 'boobs','breasts','chests','bosoms','boobies','melons','racks'],
'breasts' : ['tits','titty',  'titties', 'tity', 'boobs','breasts','chests','bosoms','boobies','melons','racks'],
'chests' : ['tits','titty',  'titties', 'tity', 'boobs','breasts','chests','bosoms','boobies','melons','racks'],
'bosoms' : ['tits','titty',  'titties', 'tity', 'boobs','breasts','chests','bosoms','boobies','melons','racks'],
'boobies' : ['tits','titty',  'titties', 'tity', 'boobs','breasts','chests','bosoms','boobies','melons','racks','booby'],
'melons' : ['tits','titty',  'titties', 'tity', 'boobs','breasts','chests','bosoms','boobies','melons','racks'],
'racks' : ['tits','titty',  'titties', 'tity', 'boobs','breasts','chests','bosoms','boobies','melons','racks'],
'juggs' : ['tits','titty',  'titties', 'tity', 'boobs','breasts','chests','bosoms','boobies','melons','racks'],

'titted' : ['titted','boobed','breasted','chested'],
'boobed' : ['titted','boobed','breasted','chested'],
'breasted' : ['titted','boobed','breasted','chested'],
'chested' : ['titted','boobed','breasted','chested'],
'jugged' : ['titted','boobed','breasted','chested','jugged'],

# /*'threesome','threesom', 'three some','3some',threeway*/
'threesome' : ['threesome','three some','3some','threesom','trio'],
'threesom' : ['threesome','three some','3some','threesom','trio'],
'3som' : ['3som','threesome','three some','3some','threesom','trio'],
'3some' : ['threesome','three some','3some','threesom','trio'],
'trio' : ['trio','threesome','three some','3some','threesom'],
'threeway' : ['threeway','threesome','three some','3some','threesom'],



# /*'gangbang','foursome','four some','4some', 'orgy','party','family','group','swingers'*/
'gangbang' : ['gangbang','gangbanged','orgy','party','group sex','swingers party','fuckfest'],
'gangbanged' : ['gangbang','gangbanged', 'group fucked', 'orgy','party fucked','group sex','swingers','fuckfest'],

'foursome' : ['gangbang','gangbanged', 'foursome','four some','4some', 'orgy','party sex','family sex','group sex','swingers','fuckfest'],
'4some' : ['gangbang','gangbanged','foursome','four some','4some', 'orgy','party sex','family sex','group sex','swingers','fuckfest'],
'orgy' : ['gangbang','gangbanged','foursome','four some','4some', 'orgy','party sex','family sex','group sex','swingers','fuckfest'],
'party' : ['gangbang','gangbanged','foursome','four some','4some', 'orgy','party','family sex','group sex','swingers','fuckfest','celebration'],
'fuckfest' : ['gangbang','gangbanged','foursome','four some','4some', 'orgy','party','family sex','group sex','swingers','fuckfest'],

'swingers' : ['gangfuck','swappers','foursome','four some','4some', 'orgy','party','group sex','swingers','fuckfest'],
'swinger' : ['gangfuck','swapper','foursome','four some','4some', 'orgy','party','group sex','swingers','fuckfest'],

# /*share shares sharing shared*/
'share' : ['share','divide','use','taste','experience'],
'shares' : ['shares','enjoys together','uses','tastes','experiences'],
'sharing' : ['sharing','enjoying together','using','tasting','experiencing'],
'shared' : ['shared','enjoyed together','used','tasted','experienced'],
 

# /*'bukkake'*/
'bukkake' : ['gangbang','blowbangs','blowbang','blowfest','bukkake facial','facial cum cover','face cum cover','bukkake'],

# /*'asian','asia','china','chinese','korea','korean','Japanese','japan','thai','jav','uncensored','censored','filipina','vietnamese','indonesian','indonesia','jp','jpn'*/
'asian' : ['asian','chinese','korean','Japanese','thai','filipina','vietnamese','indonesian'],
'chinese' : ['asian','chinese','korean','Japanese','thai','filipina','vietnamese','indonesian'],
'korean' : ['asian','chinese','korean','Japanese','thai','filipina','vietnamese','indonesian'],
'japanese' : ['asian','chinese','korean','Japanese','thai','filipina','vietnamese','indonesian'],
'thai' : ['asian','chinese','korean','Japanese','thai','filipina','vietnamese','indonesian'],
'vietnamese' : ['asian','chinese','korean','Japanese','thai','filipina','vietnamese','indonesian'],
'indonesian' : ['asian','chinese','korean','Japanese','thai','filipina','vietnamese','indonesian'],
'filipina' : ['asian','chinese','korean','Japanese','thai','filipina','vietnamese','indonesian'],
'filipino' : ['asian','chinese','korean','Japanese','thai','filipina','vietnamese','indonesian'],

'asia' : ['asia','china','korea','japan','thailand','filipines','vietnam','indonesia','jp','jpn'],
'china' : ['asia','china','korea','japan','thailand','filipines','vietnam','indonesia','jp','jpn'],
'korea' : ['asia','china','korea','japan','thailand','filipines','vietnam','indonesia','jp','jpn'],
'japan' : ['asia','china','korea','japan','thailand','filipines','vietnam','indonesia','jp','jpn'],
'indonesia' : ['asia','china','korea','japan','thailand','filipines','vietnam','indonesia','jp','jpn'],
'jp' : ['asia','china','korea','japan','thailand','filipines','vietnam','indonesia','jp','jpn'],
'jpn' : ['asia','china','korea','japan','thailand','filipines','vietnam','indonesia','jp','jpn'],


'uncensored' : ['asian','asia','china','chinese','korea','korean','Japanese','japan','thai','jav','uncensored','censored','filipina','vietnamese','indonesian','indonesia','jp','jpn'],
'censored' : ['asian','asia','china','chinese','korea','korean','Japanese','japan','thai','jav','uncensored','censored','filipina','vietnamese','indonesian','indonesia','jp','jpn'],
'jav' : ['asian','asia','china','chinese','korea','korean','Japanese','japan','thai','jav','uncensored','censored','filipina','vietnamese','indonesian','indonesia','jp','jpn'],
'javhd' : ['asian','asia','china','chinese','korea','korean','Japanese','japan','thai','jav','uncensored','censored','filipina','vietnamese','indonesian','indonesia','jp','jpn'],

# /*bbcbiggest = huge, long, enormous, immense, massive, gigantic, mammoth, monster, thick, fat*/
'bbc' : ['BBC',
        'big dick', 'huge dick','long dick','enormous dick','immense dick','massive dick','gigantic dick','mammoth dick','monster dick','thick dick','fat dick',
        'big cock', 'huge cock','long cock','enormous cock','immense cock','massive cock','gigantic cock','mammoth cock','monster cock','thick cock','fat cock',
        
		'big black dick', 'huge black dick','long black dick','enormous black dick','immense black dick','massive black dick','gigantic black dick','mammoth black dick','monster black dick','thick black dick','fat black dick',
        'big black cock', 'huge black cock','long black cock','enormous black cock','immense black cock','massive black cock','gigantic black cock','mammoth black cock','monster black cock','thick black cock','fat black cock',
			        
		'big balls',
		'bull dick', 'big bull dick'],

'bbcs' : ['BBCs',
        'big dicks', 'huge dicks','long dicks','enormous dicks','immense dicks','massive dicks','gigantic dicks','mammoth dicks','monster dicks','thick dicks','fat dicks',
        'big cocks', 'huge cocks','long cocks','enormous cocks','immense cocks','massive cocks','gigantic cocks','mammoth cocks','monster cocks','thick cocks','fat cocks',
        
		'big black dicks', 'huge black dicks','long black dicks','enormous black dicks','immense black dicks','massive black dicks','gigantic black dicks','mammoth black dicks','monster black dicks','thick black dicks','fat black dicks',
        'big black cocks', 'huge black cocks','long black cocks','enormous black cocks','immense black cocks','massive black cocks','gigantic black cocks','mammoth black cocks','monster black cocks','thick black cocks','fat black cocks',
			        
		'big balls',
		'bull dicks', 'big bull dicks'],
# /*bwc*/
'bwc' : ['bwc',
        'big dick', 'huge dick','long dick','enormous dick','immense dick','massive dick','gigantic dick','mammoth dick','monster dick','thick dick','fat dick',
        'big cock', 'huge cock','long cock','enormous cock','immense cock','massive cock','gigantic cock','mammoth cock','monster cock','thick cock','fat cock',
        
		'big white dick', 'huge white dick','long white dick','enormous white dick','immense white dick','massive white dick','gigantic white dick','mammoth white dick','monster white dick','thick white dick','fat white dick',
        'big white cock', 'huge white cock','long white cock','enormous white cock','immense white cock','massive white cock','gigantic white cock','mammoth white cock','monster white cock','thick white cock','fat white cock',
			        
		'big balls',
		'white bull dick', 'big cow dick'],
		
# /*big biggest, huge, enormous, immense, massive, gigantic, mammoth, monster, */
'big' : ['big', 'huge', 'fat', 'massive', 'large'],
'biggest' : ['biggest', 'huge', 'enormous', 'immense', 'massive', 'gigantic', 'mammoth', 'monster'],
'huge' : ['huge', 'enormous', 'immense', 'massive', 'gigantic', 'mammoth', 'monster','giant'],
'giant' : ['huge', 'enormous', 'immense', 'massive', 'gigantic', 'mammoth', 'monster','giant'],
'enormous' : ['biggest', 'huge', 'enormous', 'immense', 'massive', 'gigantic', 'mammoth', 'monster','giant'],
'immense' : ['biggest', 'huge', 'enormous', 'immense', 'massive', 'gigantic', 'mammoth', 'monster','giant'],
'massive' : ['biggest', 'huge', 'enormous', 'immense', 'massive', 'gigantic', 'mammoth', 'monster','giant'],
'gigantic' : ['biggest', 'huge', 'enormous', 'immense', 'massive', 'gigantic', 'mammoth', 'monster','giant'],
'mammoth' : ['biggest', 'huge', 'enormous', 'immense', 'massive', 'gigantic', 'mammoth', 'monster','giant'],
'monster' : ['biggest', 'huge', 'enormous', 'immense', 'massive', 'gigantic', 'mammoth', 'monster','giant'],

'large' : ['big', 'huge', 'fat', 'massive', 'large'],

# /*ass*/
'ass' : ['ass','ass','ass','butt','arse','backdoor','bum', 'buttock', 'backside','anus'], # /*'rear end'*/
'butt' : ['ass','butt','arse','backdoor','bum', 'buttock', 'backside','anus'],
'arse' : ['ass','butt','arse','backdoor','bum', 'buttock', 'backside','anus'],
'anus' : ['ass','butt','arse','backdoor','bum', 'buttock', 'backside','anus'],

'booty' : ['brazilian butt','bubble butt','round ass','apple booty','bootylicious'],
'bootylicious' : ['brazilian butt','bubble butt','round ass','apple booty','bootylicious'],

'brazilian' : ['brazilian','brazilian butt','bubble butt','round ass','apple booty'],
'bubble' : ['bubble', 'round','apple'],
'round' : ['bubble', 'round','apple'],

# /*asshole*/
'asshole' : ['ass','anus','asshole','ass hole','butt hole','butthole','arsehole','arse hole','rear hole','backdoor','shit hole','crap hole'],
'butthole' : ['ass','anus','asshole','ass hole','butt hole','butthole','arsehole','arse hole','rear hole','backdoor','shit hole','crap hole'],
'arsehole' : ['ass','anus','asshole','ass hole','butt hole','butthole','arsehole','arse hole','rear hole','backdoor','shit hole','crap hole'],

'bootyhole' : ['brazilian butt hole','bubble butt hole','round ass hole','apple booty hole','booty hole','bootyhole'],

# /*dick, boner,penis,cock,*/
'dick' : ['dick','dick','dick', 'cock','cock', 'boner',  'hot rod', 'strong shaft', 'wood shaft', 'willy','weapon'],
'dicks' : ['dicks', 'boners', 'cocks'],
'boner' : ['dick', 'boner', 'cock', 'hot rod', 'hard shaft', 'wood shaft', 'willy','weapon'],
'penis' : ['dick', 'boner','penis', 'cock'],
'cock' : ['cock', 'cock', 'cock', 'dick', 'dick', 'boner', 'hot rod', 'hard shaft', 'wood shaft', 'willy','weapon'],
'shaft' : ['cock', 'cock', 'cock', 'dick', 'dick', 'boner', 'hot rod', 'hard shaft', 'wood shaft', 'willy','weapon'],
'cocks' : ['dicks', 'boners', 'cocks'],
'rod' : ['dick', 'boner', 'cock','hot rod', 'hot shaft', 'wood shaft', 'willy','weapon'],
'tool' : ['dick','dick','dick', 'cock','cock', 'boner',  'hot rod', 'strong shaft', 'wood shaft', 'willy','weapon'],

'snake' : ['penis','snake','dick', 'boner', 'cock','rod'],

# /*old = ol' aged, olden, oldie, oldish, gray-haired, elderly, mature, matured, senior, veteran, experienced, */
'old' : ['old', "ol'", 'aged', 'olden', 'oldie', 'oldish', 'gray-haired', 'elderly', 'mature', 'matured', 'senior', 'veteran', 'experienced'],
'older' : ['old', "ol'", 'aged', 'olden', 'oldie', 'oldish', 'gray-haired', 'elderly', 'mature', 'matured', 'senior', 'veteran', 'experienced'],
'aged' : ['old', "ol'", 'aged', 'olden', 'oldie', 'oldish', 'gray-haired', 'elderly', 'mature', 'matured', 'senior', 'veteran', 'experienced'],
'elderly' : ['old', "ol'", 'aged', 'olden', 'oldie', 'oldish', 'gray-haired', 'elderly', 'mature', 'matured', 'senior', 'veteran', 'experienced'],
'senior' : ['old', "ol'", 'aged', 'olden', 'oldie', 'oldish', 'gray-haired', 'elderly', 'mature', 'matured', 'senior', 'veteran', 'experienced'],
'veteran' : ['old', "ol'", 'aged', 'olden', 'oldie', 'oldish', 'gray-haired', 'elderly', 'mature', 'matured', 'senior', 'veteran', 'experienced'],
'experienced' : ['old', "ol'", 'aged', 'olden', 'oldie', 'oldish', 'gray-haired', 'elderly', 'mature', 'matured', 'senior', 'veteran', 'experienced'],

# /*Little, mini, tiny, teeny, small,*/
'small' : ['little', 'mini', 'tiny', 'teeny', 'small'],
'tiny' : ['little', 'mini', 'tiny', 'teeny', 'small','short'],
'little' : ['little', 'mini', 'tiny', 'teeny', 'small','short'],
'lil' : ['little', 'mini', 'tiny', 'teeny', 'small','short'],
'mini' : ['little', 'mini', 'tiny', 'teeny', 'small','short'],

# /*long = lengthy, prolonged*/
'long' : ['long', 'lengthy', 'prolonged'],


# /*blowjob*/
'blowjob' : ['blowjob', 'blow', 'blow job', 'bj', 'oral','suck','sucking'],
'bj' : ['blowjob', 'blow', 'blow job', 'bj', 'oral','suck','sucking'],
'blow' : ['blowjob', 'blow job', 'bj', 'oral','suck','sucking'],
'blows' : ['gives blowjob', 'gives blow job', 'gives bj', 'bjs', 'gives oral','sucks','blows'],
'blowing' : ['giving blowjob to', 'giving blow job to', 'giving bj to', 'giving oral to', 'blowing','edging'],
'sucking' : ['giving blowjob to', 'giving blow job to', 'giving bj to', 'giving oral to', 'blowing','edging'],
'edging' : ['blowjob', 'blow job', 'bj', 'oral', 'blowing','edging'],
'suck' : ['blowjob', 'blow job', 'bj', 'oral','suck','blow'],
'sucks' : ['gives blowjob', 'gives blow job', 'gives bj', 'bjs', 'gives oral','sucks','blows'],
'sucked' : ['blowjobbed', 'blow jobbed', 'bj', 'oraled','sucked','blowed'],
'oral' : ['blowjob', 'blow job', 'bj', 'oral','suck','blow','fellatio'],
'fellatio' : ['blowjob', 'blow job', 'bj', 'oral','suck','blow','fellatio'],


# /*porn, porno, Xxx, erotic, nsfw*/
'porn' : ['porn','porno','Xxx','erotic video','nsfw video'],
'porno' : ['porn','porno','Xxx','erotic video','nsfw video'],
'xxx' : ['porn','porno','Xxx','erotic','nsfw'],
'nsfw' : ['porn','porno','Xxx','erotic','nsfw'],

# /*college = college girl, college student, highschool, highschool girl, highschool student*/
'college' : ['college','academy','highschool','high school','junior high school','university'],
'coed' : ['college','academy','highschool','high school','junior high school','university'],


# /*car*/
'car' : ['car','automobile','motor car','vehicle','van','the ride','wheels','transport'],
'transport' : ['car','automobile','motor car','vehicle','van','the ride','wheels','transport'],
'bus' : ['bus','truck','van','wagon','car','wheels','transport'],
'van' : ['bus','truck','van','wagon','car','wheels','transport'],
'truck' : ['bus','truck','van','wagon','car','wheels','transport'],

'taxi' : ['taxi','cab','van','taxicab','car','tourist car'],

# /*bitch, slut, whore, tart, vixen*/
'bitch' : ['bitch','slut','whore','tart','vixen'],
'bitches' : ['bitches','sluts','whores','tarts','vixens'],
'slut' : ['bitch','slut','whore','tart','vixen'],
'sluts' : ['bitches','sluts','whores','tarts','vixens'],
'whore' : ['bitch','slut','whore','tart','vixen'],
'whores' : ['bitches','sluts','whores','tarts','vixens'],
'tart' : ['bitch','slut','whore','tart','vixen'],
'tarts' : ['bitches','sluts','whores','tarts','vixens'],
'vixen' : ['bitch','slut','whore','tart','vixen'],
'vixens' : ['bitches','sluts','whores','tarts','vixens'],

'fox' : ['fox','bitch','slut','whore','tart','vixen'],
# /*slutty*/
'slutty' : ['slutty','slut','sluttish','bitchy','bitch','whore','vixen','sultry'],
'sultry' : ['sultry','slutty','slut','sluttish','bitchy','bitch','whore','vixen'],
'bitchy' : ['sultry','slutty','slut','sluttish','bitchy','bitch','whore','vixen'],
'sluttish' : ['sultry','slutty','slut','sluttish','bitchy','bitch','whore','vixen'],

# /*fisting, inserting, stuffing*/
'fist' : ['fisting','inserting','stuffing','fisted','inserted','stuffed'],
'fisting' : ['fisting','inserting','stuffing'],
'inserting' : ['fisting','inserting','stuffing'],
'stuffing' : ['fisting','inserting','stuffing'],

'stuffed' : ['fisted','inserted','stuffed'],
'fisted' : ['fisted','inserted','stuffed'],
'inserted' : ['fisted','inserted','stuffed'],

	                
# /*'pussy','vagina','vulva','cunt','clit','clitoris','labia','twat'*/
'pussy' : ['pussy','vagina','vulva','cunt','pussy lips','pussy cheeks','twat','hole'],
'vagina' : ['pussy','vagina','vulva','cunt','pussy lips','pussy cheeks','twat','hole'],
'vulva' : ['pussy','vagina','vulva','cunt','pussy lips','pussy cheeks','twat','hole'],
'cunt' : ['pussy','vagina','vulva','cunt','pussy lips','pussy cheeks','twat','hole'],
'twat' : ['pussy','vagina','vulva','cunt','pussy lips','pussy cheeks','twat','hole'],

# /*clit*/
'clit' : ['clit','clitoris','clt','labia'],
'clitoris' : ['clit','clitoris','clt','labia'],
'clt' : ['clit','clitoris','clt','labia'],
'labia' : ['clit','clitoris','clt','labia'],

# /*puffy*/
'puffy' : ['big','large','bloated','swollen'],
'swollen' : ['big','large','bloated','swollen'],



# /*juicy*/
'juicy' : ['juicy','lush','yummy','luscious','pulpy','dripping'],

# /*wet*/
'wet' : ['wet','juicy','lush','luscious','pulpy','yummy','dripping','moist','watery','humid'],
'lush' : ['wet','juicy','lush','luscious','pulpy','yummy','dripping','moist','watery','humid'],
'luscious' : ['wet','juicy','lush','luscious','pulpy','yummy','dripping','moist','watery','humid'],
'pulpy' : ['wet','juicy','lush','luscious','pulpy','yummy','dripping','moist','watery','humid'],
'yummy' : ['wet','juicy','lush','luscious','pulpy','yummy','dripping','moist','watery','humid'],
'moist' : ['wet','juicy','lush','luscious','pulpy','yummy','dripping','moist','watery','humid'],
'watery' : ['wet','juicy','lush','luscious','pulpy','yummy','dripping','moist','watery','humid'],
'humid' : ['wet','juicy','lush','luscious','pulpy','yummy','dripping','moist','watery','humid'],




# /*lesbian    lesbians, girl-girl, girl on girl, lesbo, les, lez, gay woman, female homosexual, homosexual woman,*/
'lesbian' : ['lesbian','lesbians', 'lesbo','les','lez','gay woman','female homosexual','homosexual woman','homosexual','girl-girl','girl on girl','tribbing'],
'lesbo' : ['lesbian','lesbians','lesbo','les','lez','gay woman','female homosexual','homosexual woman','homosexual','girl-girl','girl on girl','tribbing'],
'les' : ['lesbian','lesbians','lesbo','les','lez','gay woman','female homosexual','homosexual woman','homosexual','girl-girl','girl on girl','tribbing'],
'lez' : ['lesbian','lesbians','lesbo','les','lez','gay woman','female homosexual','homosexual woman','homosexual','girl-girl','girl on girl','tribbing'],
'tribbing' : ['lesbian','lesbians','lesbo','les','lez','gay woman','female homosexual','homosexual woman','homosexual','girl-girl','girl on girl','tribbing'],

# /*lesbians*/
'lesbians' : ['lesbians', 'lesbian','lesbos','les','lez','gay women','female homosexuals','homosexual women','homosexuals','girl-girl','girl on girl'],
'lesbos' : ['lesbians', 'lesbian','lesbos','les','lez','gay women','female homosexuals','homosexual women','homosexuals','girl-girl','girl on girl'],


# /*man = 'husband', 'hubby', 'guy', 'fellow', 'dude', 'buddy', 'gentalman', 'person', 'pal', 'old lad', 'mate', 'partner', 'friend', 'old boy', 'boyfriend', 'stud'*/
'man' : ['man','husband', 'hubby', 'guy', 'fellow', 'dude', 'buddy', 'gentalman', 'person', 'pal', 'old lad', 'mate', 'partner', 'friend', 'old boy', 'boyfriend', 'stud','boy','bf'],
'male' : ['man','husband', 'hubby', 'guy', 'fellow', 'dude', 'buddy', 'gentalman', 'person', 'pal', 'old lad', 'mate', 'partner', 'friend', 'old boy', 'boyfriend', 'stud','boy','bf'],
'gentalman' : ['man','husband', 'hubby', 'guy', 'fellow', 'dude', 'buddy', 'gentalman', 'person', 'pal', 'old lad', 'mate', 'partner', 'friend', 'old boy', 'boyfriend', 'stud','boy','bf'],

'boyfriend' : ['man','husband', 'hubby', 'guy', 'dude', 'buddy', 'partner', 'friend', 'boyfriend', 'bf'],
'bf' : ['man','husband', 'hubby', 'guy', 'dude', 'buddy', 'partner', 'friend', 'boyfriend', 'bf'],

'boyfriends' : ['men','guys', 'guies', 'boys',  'friends', 'buddies', 'dudes', 'boyfriends'],
'bfs' : ['men','guys', 'guies', 'boys',  'friends', 'buddies', 'dudes', 'boyfriends'],

'boy' : ['young man', 'guy', 'fellow', 'dude', 'buddy', 'gentalman', 'person', 'pal', 'lad', 'mate', 'partner', 'friend', 'boy', 'boyfriend','bf'],

'guy' : ['guy', 'fellow', 'dude', 'buddy', 'person', 'pal', 'mate', 'partner', 'friend', 'companion'],
'fellow' : ['guy', 'fellow', 'dude', 'buddy', 'person', 'pal', 'mate', 'partner', 'friend', 'companion'],
'dude' : ['guy', 'fellow', 'dude', 'buddy', 'doods', 'pal', 'mate', 'partner', 'friend', 'companion'],
'buddy' : ['guy', 'fellow', 'dude', 'buddy', 'person', 'pal', 'mate', 'partner', 'friend', 'companion'],
'person' : ['guy', 'fellow', 'dude', 'buddy', 'person', 'pal', 'mate', 'partner', 'friend', 'companion'],
'pal' : ['guy', 'fellow', 'dude', 'buddy', 'person', 'pal', 'mate', 'partner', 'friend', 'companion'],
'mate' : ['guy', 'fellow', 'dude', 'buddy', 'person', 'pal', 'mate', 'partner', 'friend', 'companion'],
'partner' : ['guy', 'fellow', 'dude', 'buddy', 'person', 'pal', 'mate', 'partner', 'friend', 'companion'],
'friend' : ['guy', 'fellow', 'dude', 'buddy', 'person', 'pal', 'mate', 'partner', 'friend', 'companion'],
'companion' : ['guy', 'fellow', 'dude', 'buddy', 'person', 'pal', 'mate', 'partner', 'friend', 'companion'],


'husband' : ['man','husband', 'hubby', 'guy', 'dude', 'buddy',  'companion', 'partner', 'friend', 'spouse', 'boyfriend','bf'],
'hubby' : ['man','husband', 'hubby', 'guy', 'dude', 'buddy', 'companion', 'partner', 'friend', 'spouse', 'boyfriend', 'bf'],


'stud' : ['stud','heman','macho','macho-man','machoman','masculine','hunk','hunky','handsome'],
'studs' : ['studs','hemen','machos','macho-men','machomen','masculines','hunks','hunkies','handsomes'],

'hunk' : ['stud','heman','macho','macho-man','machoman','masculine','hunk','hunky','handsome'],
'hunks' : ['studs','hemen','machos','macho-men','machomen','masculines','hunks','hunkies','handsomes'],
'hunky' : ['stud','heman','macho','macho-man','machoman','masculine','hunk','hunky','handsome'],
'macho' : ['stud','heman','macho','macho-man','machoman','masculine','hunk','hunky','handsome'],
'handsome' : ['stud','heman','macho','macho-man','machoman','masculine','hunk','hunky','handsome'],

# /*men = 'guys', 'guies', 'boys', 'persons', 'friends', 'buddies', 'dudes', 'boyfriends', 'studs'*/
'men' : ['men','guys', 'guies', 'boys', 'persons', 'friends', 'buddies', 'dudes', 'boyfriends'],
'guys' : ['men','guys', 'guies', 'boys', 'persons', 'friends', 'buddies', 'dudes', 'boyfriends'],
'guies' : ['men','guys', 'guies', 'boys', 'persons', 'friends', 'buddies', 'dudes', 'boyfriends'],
'boys' : ['men','guys', 'guies', 'boys', 'persons', 'friends', 'buddies', 'dudes', 'boyfriends'],
'persons' : ['men','guys', 'guies', 'boys', 'persons', 'friends', 'buddies', 'dudes'],
'friends' : ['men','guys', 'guies', 'boys', 'persons', 'friends', 'buddies', 'dudes'],
'buddies' : ['men','guys', 'guies', 'boys', 'persons', 'friends', 'buddies', 'dudes'],
'dudes' : ['men','guys', 'guies', 'boys', 'persons', 'friends', 'buddies', 'dudes'],




# /*skinny slim = thin, fit, lean, bony, poor*/
'skinny' : ['skinny','slim','thin','fit','lean','poor'],
'slim' : ['slim','thin','fit','lean'],
'thin' : ['slim','thin','fit','lean'],
'lean' : ['slim','thin','fit','lean'],

# /*dildo, vibrator plug toy*/
'dildo' : ['dildo','vibrator','plug','toy'],
'dildos' : ['dildo','vibrator','plug','toy'],
'vibrator' : ['dildo','vibrator','plug','toy'],
'vibrators' : ['dildos','vibrators','plugs','toys'],
'plug' : ['dildo','vibrator','plug','toy'],
'plugs' : ['dildos','vibrators','plugs','toys'],
'toy' : ['dildo','vibrator','plug','toy'],
'toys' : ['dildos','vibrators','plugs','toys'],

# /*dad, daddy, stepdad, step dad,father dads, daddies */
'dad' : ['dad','daddy','stepdad','step dad','father','step father','not her dad'],
'dads' : ['dads','daddies','stepdads','step dads','fathers','step fathers','not her dads'],
'daddy' : ['dad','daddy','stepdad','step dad','father','step father','not her dad'],
'daddies' : ['dads','daddies','stepdads','step dads','fathers','step fathers','not her dads'],
'stepdad' : ['dad','daddy','stepdad','step dad','father','step father','not her dad'],
'stepdads' : ['dads','daddies','stepdads','step dads','fathers','step fathers','not her dads'],
'father' : ['dad','daddy','stepdad','step dad','father','step father','not her dad'],
'fathers' : ['dads','daddies','stepdads','step dads','fathers','step fathers','not her dads'],

# /*mom, mum, mamma, mommy, mummy momma mother*/
'mom' : ['mom','mum','mamma','mommy','mummy','momma','mother','stepmom','step-mom','stepmother','not his mom'],
'moms' : ['moms','mums','mammas','mommies','mummies','mommas','mothers','stepmoms','step-moms','stepmothers','not his moms'],
'mum' : ['mom','mum','mamma','mommy','mummy','momma','mother','stepmom','step-mom','stepmother','not his mom'],
'mamma' : ['mom','mum','mamma','mommy','mummy','momma','mother','stepmom','step-mom','stepmother','not his mom'],
'mommy' : ['mom','mum','mamma','mommy','mummy','momma','mother','stepmom','step-mom','stepmother','not his mom'],
'mummy' : ['mom','mum','mamma','mommy','mummy','momma','mother','stepmom','step-mom','stepmother','not his mom'],
'momma' : ['mom','mum','mamma','mommy','mummy','momma','mother','stepmom','step-mom','stepmother','not his mom'],
'mother' : ['mom','mum','mamma','mommy','mummy','momma','mother','stepmom','step-mom','stepmother','not his mom'],
'mothers' : ['moms','mums','mammas','mommies','mummies','mommas','mothers','stepmoms','step-moms','stepmothers','not his moms'],
'stepmom' : ['mom','mum','mamma','mommy','mummy','momma','mother','stepmom','step-mom','stepmother','not his mom'],
'stepmoms' : ['moms','mums','mammas','mommies','mummies','mommas','mothers','stepmoms','step-moms','stepmothers','not his moms'],
'step-mom' : ['mom','mum','mamma','mommy','mummy','momma','mother','stepmom','step-mom','stepmother','not his mom'],
'stepmother' : ['mom','mum','mamma','mommy','mummy','momma','mother','stepmom','step-mom','stepmother','not his mom'],

 
# /*'gilf', 'granny','grandma','grand mother','grandmother'*/
'gilf' : ['gilf', 'granny','grandma','grand mother','grandmother','70 years old','wrinkled woman'],
'granny' : ['gilf', 'granny','grandma','grand mother','grandmother','70 years old','wrinkled woman'],
'grandma' : ['gilf', 'granny','grandma','grand mother','grandmother','70 years old','wrinkled woman'],
'grandmother' : ['gilf', 'granny','grandma','grand mother','grandmother','70 years old','wrinkled woman'],

'grannies' : ['gilfs', 'grannies','grandmas','grand mothers','grandmothers'],


# /*'black','ebony','african','south african','afro','nigerian', 'caribbean','chocolate'*/
'black' : ['black','ebony','african','afro', 'caribbean','chocolate'],
'ebony' : ['black','ebony','african','afro', 'caribbean','chocolate'],
'bull' : ['black','bull','african','afro', 'caribbean'],
'african' : ['black','ebony','african','afro','south african','nigerian', 'caribbean','chocolate'],
'afro' : ['black','ebony','african','afro','nigerian', 'caribbean','chocolate'],
'nigerian' : ['black','ebony','african','south african','afro','nigerian', 'caribbean','chocolate'],
'caribbean' : ['black','ebony','african','south african','afro','nigerian', 'caribbean','chocolate'],
'negro' : ['black','ebony','african','south african','afro','nigerian', 'caribbean','chocolate'],
'chocolate' : ['black','ebony','african','afro','nigerian', 'caribbean','chocolate'],

# /*blonde,blondie ,'blond' golden haired, yellow haired, straw haired, bleached haired, sandy, sandy haired,*/
'blonde' : ['blonde','blondie','blond','golden-haired','yellow-haired','straw-haired','bleached-haired','bleached','sandy-haired'],
'blond' : ['blonde','blondie','blond','golden-haired','yellow-haired','straw-haired','bleached-haired','bleached','sandy-haired'],
'blondie' : ['blonde','blondie','blond','golden-haired','yellow-haired','straw-haired','bleached-haired','bleached','sandy-haired'],
'bleached' : ['blonde','blondie','blond','golden-haired','yellow-haired','straw-haired','bleached-haired','bleached','sandy-haired'],

# /*'bunette','brunet', 'brown hair','black hair' dark haired' dark brown haired, dusky haired*/
'brunette' : ['brunette','brown hair','black hair','dark haired','dark brown haired','dusky haired','Brunette with long hair','long haired Brunette'],
'brunet' : ['brunette','brunet','brown hair','black hair','dark haired','dark brown haired','dusky haired','Brunette with long hair','long haired Brunette'],

# /*tight*/
'tight' : ['tight','young','tight-fitting','tightfitting','compact','sturdy','contracted','narrow'],

# /*taboo = taboo family, forbidden, immoral */
'taboo' : ['taboo','forbidden','immoral','taboo family','forbidden family', 'forbidden sex', 'immoral family', 'immoral sex', 'family','prohibited', 'prohibited sex','prohibited family'],
'forbidden' : ['taboo','forbidden','immoral','taboo family','forbidden family', 'forbidden sex', 'immoral family', 'immoral sex', 'family','prohibited', 'prohibited sex','prohibited family'],
'immoral' : ['taboo','forbidden','immoral','taboo family','forbidden family', 'forbidden sex', 'immoral family', 'immoral sex', 'family','prohibited', 'prohibited sex','prohibited family'],


# /*pov,close-up,'point of view','close up','eye contact'*/
'pov' : ['pov','close-up','close up','point of view','eye contact','pov style'],
'closeup' : ['pov','close-up','close up','point of view','eye contact','pov style'],

# /*mistress = whore, hooker, prostitute, kept woman, ladylove, girldfriend, sugar girl, extramarital woman, other woman*/
'mistress' : ['mistress','whore','hooker','prostitute','kept woman','ladylove','girldfriend','sugar girl','extramarital woman','other woman','sweetheart','dream girl'],

# /*slave, servent, sub, submissive*/
'slave' : ['slave','servent','sub','submissive'],
'slaves' : ['slaves','servents','subs','submissives'],
'servent' : ['slave','servent','sub','submissive'],
'sub' : ['slave','servent','sub','submissive'],
'subs' : ['slaves','servents','subs','submissives'],
'submissive' : ['slave','servent','sub','submissive'],

# /*orgasmic, orgasm, orgasmes*/
'orgasmic' : ['orgasmic', 'exceptionally exciting', 'ecstatic',  'orgastic', 'intoxicated', 'euphoric', 'explosive'],
'orgasm' : ['orgasm', 'climax', 'ejaculation', 'cum'], 
'orgasms' : ['multiple orgasm', 'climaxes', 'ejaculations', 'cums'],

'climax' : ['orgasm', 'climax', 'ejaculation', 'cum'], 
'ejaculation' : ['orgasm', 'climax', 'ejaculation', 'cum'], 

# /*boss, Officer office boss, employer, supervisor, director, top dog, office head, office chief, manager, office manager, CEO, executive*/
'boss' : ['boss','officer', 'office boss','employer','supervisor','director','top dog','office head','office chief','manager','office manager','CEO','executive'],
'officer' : ['boss','officer', 'office boss','employer','supervisor','director','top dog','office head','office chief','manager','office manager','CEO','executive'],
'manager' : ['boss','officer', 'office boss','employer','supervisor','director','top dog','office head','office chief','manager','office manager','CEO','executive'],
'employer' : ['boss','officer', 'office boss','employer','supervisor','director','top dog','office head','office chief','manager','office manager','CEO','executive'],
'executive' : ['boss','officer', 'office boss','employer','supervisor','director','top dog','office head','office chief','manager','office manager','CEO','executive'],
'supervisor' : ['boss','officer', 'office boss','employer','supervisor','director','top dog','office head','office chief','manager','office manager','CEO','executive'],
'director' : ['boss','officer', 'office boss','employer','supervisor','director','top dog','office head','office chief','manager','office manager','CEO','executive'],

# /*office = office, company office, organization office, corporation office, corporate office, agency office*/
'office' : ['office','workplace', 'company office','organization office','corporation office','corporate office','agency office'],
'workplace' : ['office','workplace', 'company office','organization office','corporation office','corporate office','agency office'],

# /*saggy = flabby, floppy, sagging, limp, dropping, baggy, loose, sloppy, loose-fitting, hanging, */
'saggy' : ['saggy','flabby','floppy','sagging','limp','dropping','baggy','loose','sloppy','loose-fitting','hanging'],

# /*couple, duo, lovers, mates, intimate couple, real couple, spouses, romantic duo, romantic couple, bf gf, boyfriend girlfriend, married couple, pair, husband and wife,*/
'couple' : ['couple','duo','lovers','mates','intimate couple','real couple','spouses','romantic duo','romantic couple','bf gf','boyfriend girlfriend','married couple','pair','romantic pair','intimate pair','husband and wife' ],
'cpl' : ['couple','duo','lovers','mates','intimate couple','real couple','spouses','romantic duo','romantic couple','bf gf','boyfriend girlfriend','married couple','pair','romantic pair','intimate pair','husband and wife' ],
'couples' : ['couple','duo','lovers','mates','intimate couple','real couple','spouses','romantic duo','romantic couple','bf gf','boyfriend girlfriend','married couple','pair','romantic pair','intimate pair','husband and wife' ],

# /*intimate romantic loving, friendly, affectionate, devoted, private, personal, deep, secret, */
'intimate' : ['intimate','romantic','loving','friendly','affectionate','devoted','private','personal','deep','secret'],
'romantic' : ['intimate','romantic','loving','friendly','affectionate','devoted','private','personal','deep','secret'],
'affectionate' : ['intimate','romantic','loving','friendly','affectionate','devoted','private','personal','deep','secret'],
'devoted' : ['intimate','romantic','loving','friendly','affectionate','devoted','private','personal','deep','secret'],
'private' : ['intimate','romantic','loving','friendly','affectionate','devoted','private','personal','deep','secret'],
'personal' : ['intimate','romantic','loving','friendly','affectionate','devoted','private','personal','deep','secret'],

# /*loving*/
'loving' : ['intimate','romantic','loving','friendly','affectionate','devoted','private','personal','deep','secret'],


# /*masturbate, masturbate, wank, rub, stimulation*/
'masturbating' : ['masturbating','wanking','rubbing','stimulating'],
'masturbation' : ['masturbation', 'masturbating','wanking','rubbing','stimulating'],
'wanking' : ['masturbation', 'masturbating','wanking','rubbing','stimulating'],
'rubbing' : ['masturbation', 'masturbating','wanking','rubbing','stimulating'],
'stimulating' : ['masturbation', 'masturbating','wanking','rubbing','stimulating'],

'masturbates' : ['masturbates','wanks','rubs','stimulates'],
'wanks' : ['masturbates','wanks','rubs','stimulates'],
'rubs' : ['masturbates','wanks','rubs','stimulates'],
'stimulates' : ['masturbates','wanks','rubs','stimulates'],

'masturbate' : ['masturbate','wank','rub','stimulate'],
'wank' : ['masturbate','wank','rub','stimulate'],
'rub' : ['masturbate','wank','rub','stimulate'],
'stimulate' : ['masturbate','wank','rub','stimulate'],

'masturbated' : ['masturbated','wanked','rubbed','stimulated'],
'wanked' : ['masturbated','wanked','rubbed','stimulated'],
'rubbed' : ['masturbated','wanked','rubbed','stimulated'],
'stimulated' : ['masturbated','wanked','rubbed','stimulated'],

'fap' : ['fap','masturbate','jerk','wank','stroke'],

# /*doggy, doggystyle, bareback*/
'doggy' : ['doggy', 'doggie', 'doggystyle', 'doggy-style', 'doggy-fucks',  'reverse cowgirl', 'from behind', 'bending over'],
'doggie' : ['doggy', 'doggie', 'doggystyle', 'doggy-style', 'doggy-fucks',  'reverse cowgirl', 'from behind', 'bending over'],
'doggystyle' : ['doggy', 'doggystyle','doggy-style', 'doggy-fucks',  'reverse cowgirl', 'from behind', 'bending over'],

# /* , , Take off Condom, Cumming Inside My Wife, ,*/
'bareback' : ['bareback', 'without condom fuck', 'Risky Creampie sex', 'Removed Condom sex', 'condomless fuck'],
'barebacks' : ['barebacks', 'without condom fuck', 'Risky Creampie fuck', 'Removed Condom fuck', 'condomless sex'],
'barebacking' : ['barebacking', 'fucking without condom', 'Risky Creampie fucking', 'Removed Condom fucking', 'condomless fucking'],

# /*czech */
'czech' : ['czech', 'Czech Streets', 'Czech Casting', 'Czech Amateur', 'Czech MILF', 'Czech Amateur Casting', 'Czech Street Casting'],

# /*yoga */
'yoga' : ['Yoga Teacher Fuck', 'Yoga Pants', 'Nude Yoga', 'Naked Yoga', 'Yoga Class', 'Yoga Pussy', 'Yoga Fuck'],

# /*cum, cumming*/
'cum' : ['cum',  'cumming', 'cummings', 'ejaculate', 'ejaculated', 'ejaculating', 'sperm', 'load', 'shemen','jizz','spunk'],
'cumming' : ['cum',  'cumming', 'cummings', 'ejaculate', 'ejaculating', 'sperm', 'load', 'shemen','jizz','spunking'],
'cummings' : ['cum',  'cumming', 'cummings', 'ejaculate', 'ejaculated', 'ejaculating', 'sperm', 'load', 'shemen','jizz'],
'ejaculate' : ['cum',  'cumming', 'cummings', 'ejaculate', 'ejaculated', 'ejaculating', 'sperm', 'load', 'shemen','jizz'],
'ejaculated' : ['cum',  'cumming', 'cummings', 'ejaculate', 'ejaculated', 'ejaculating', 'spermrd', 'loaded', 'shemen','jizzed','spunked'],
'ejaculating' : ['cum',  'cumming', 'cummings', 'ejaculate', 'ejaculated', 'ejaculating', 'sperm', 'load', 'shemen','jizz'],
'sperm' : ['cum',  'cumming', 'cummings', 'ejaculate', 'ejaculated', 'ejaculating', 'sperm', 'load', 'shemen','jizz'],
'shemen' : ['cum',  'cumming', 'cummings', 'ejaculate', 'ejaculated', 'ejaculating', 'sperm', 'load', 'shemen','jizz'],
'jizz' : ['cum',  'cumming', 'cummings', 'ejaculate', 'ejaculated', 'ejaculating', 'sperm', 'load', 'shemen','jizz'],
'spunked' : ['cum',  'cumming', 'cummings', 'ejaculate', 'ejaculated', 'ejaculating', 'spermrd', 'loaded', 'shemen','jizzed','spunked'],



# /*facial facialized , jizzed, cumshot, tribute, spraying*/
'facial' : ['facial','facialized','jizzed','cumshot','cum tribute','spraying'],
'facials' : ['facials','facialized','jizzed','cumshots','cum tributes','sprayings'],
'facialized' : ['facial','facialized','jizzed','cumshot','cum tribute','spraying'],
'jizzed' : ['facial','facialized','jizzed','cumshot','cum tribute','spraying'],
'cumshot' : ['facial','facialized','jizzed','cumshot','cum tribute','spraying'],
'cumshots' : ['facials','facialized','jizzed','cumshots','cum tributes','sprayings'],
'tribute' : ['facial','facialized','jizzed','cumshot','cum tribute','spraying'],
'spraying' : ['facial','facialized','jizzed','cumshot','cum tribute','spraying'],
'burst' : ['facial','facialized','jizzed','cumshot','cum tribute','spraying'],
'explosion' : ['facial','facialized','jizzed','cumshot','cum tribute','spraying'],


 
# /*'bdsm','slave','training','torture','bondage','domination','humiliation','submission','submissive','dogging','punishment','dominating'*/
'bdsm' : ['bdsm','slave','training','torture','bondage','domination','humiliation','submission','submissive','punishment','dominating'],
'training' : ['bdsm','slave','training','torture','bondage','domination','humiliation','submission','submissive','dogging','punishment','dominating'],
'torture' : ['bdsm','slave','training','torture','bondage','domination','humiliation','submission','submissive','dogging','punishment','dominating'],
'tortured' : ['bdsm','slaved','trained','tortured','bondaged','dominated','humiliated','submission','submissive','dogged','punished'],
'bondage' : ['bdsm','slave','training','torture','bondage','domination','humiliation','submission','submissive','dogging','punishment','dominating'],
'domination' : ['bdsm','slave','training','torture','bondage','domination','humiliation','submission','submissive','dogging','punishment','dominating'],
'dominating' : ['bdsm','slave','training','torture','bondage','domination','humiliation','submission','submissive','dogging','punishment','dominating'],
'dominated' : ['bdsm','slaved','trained','tortured','bondaged','dominated','humiliated','submission','submissive','dogged','punished'],
'dominates' : ['bdsm','slaved','trained','tortured','bondaged','dominated','humiliated','submission','submissive','dogged','punished'],
'humiliating' : ['bdsm','slave','training','torture','bondage','domination','humiliation','submission','submissive','dogging','punishment','dominating'],
'humiliation' : ['bdsm','slave','training','torture','bondage','domination','humiliation','submission','submissive','dogging','punishment','dominating'],
'humiliated' : ['bdsm','slaved','trained','tortured','bondaged','dominated','humiliated','submission','submissive','dogged','punished'],
'submission' : ['bdsm','slave','training','torture','bondage','domination','humiliation','submission','submissive','dogging','punishment','dominating'],
'dogging' : ['bdsm','slave','training','torture','bondage','domination','humiliation','submission','submissive','dogging','punishment','dominating'],
'punishment' : ['bdsm','slave','training','torture','bondage','domination','humiliation','submission','submissive','dogging','punishment','dominating'],
'punished' : ['bdsm','slaved','trained','tortured','bondaged','dominated','humiliated','submission','submissive','dogged','punished'],


# /*handjob, hj, Handjobs , 'happy ending'*/
'handjob' : ['handjob','hj','happy ending','hand job'],
'Handjobs' : ['handjob','hj','happy ending','hand job'],

# /*interracial, ir, BLACKED, racial,*/
'interracial' : ['interracial','IR','BLACKED','racial'],
'ir' : ['interracial','IR','BLACKED','racial'],
'blacked' : ['interracial','IR','BLACKED','racial'],
'blackedraw' : ['BLACKEDRAW','interracial','IR','BLACKED','racial'],

# /*teacher, educator, schoolteacher, coach trainer private tutor, mentor, instructor*/
'teacher' : ['teacher','educator','schoolteacher','tutor','private tutor','mentor','professor','guru'],
'teachers' : ['teachers','educators','schoolteachers','tutors','private tutors','mentors','professors','gurus'],
'tutor' : ['teacher','educator','schoolteacher','tutor','private tutor','mentor','professor','guru'],
'mentor' : ['teacher','educator','schoolteacher','tutor','private tutor','mentor','professor','guru'],
'professor' : ['teacher','educator','schoolteacher','tutor','private tutor','mentor','professor','guru'],

'coach' : ['coach','trainer','instructor'],
'trainer' : ['coach','trainer','instructor'],
'instructor' : ['coach','trainer','instructor'],

# /*babysitter = nanny, clid-caretaker, caretaker, housekeeper, domestic servent, maid,*/
'babysitter' : ['babysitter','nanny','clid-caretaker','caretaker','housekeeper','domestic servent','maid','nursemaid','governess'],
'nanny' : ['babysitter','nanny','clid-caretaker','caretaker','housekeeper','domestic servent','maid','nursemaid','governess'],
'nursemaid' : ['babysitter','nanny','clid-caretaker','caretaker','housekeeper','domestic servent','maid','nursemaid','governess'],
'governess' : ['babysitter','nanny','clid-caretaker','caretaker','housekeeper','domestic servent','maid','nursemaid','governess'],

# /*maid = domestic servent, housekeeper, domestic help, caretaker, nanny, nursemaid,*/
'maid' : ['maid','domestic servent','housekeeper','domestic help','caretaker','nanny','nursemaid','governess'],
'housekeeper' : ['maid','domestic servent','housekeeper','domestic help','caretaker','nanny','nursemaid','governess'],
'caretaker' : ['maid','domestic servent','housekeeper','domestic help','caretaker','nanny','nursemaid','governess'],

# /**/
'' : ['','','','',''],
# /**/
'' : ['','','','',''],
# /**/
'' : ['','','','',''],
# /*most popular keywords end*/


# /*few replacement*/
'' : ['','','','',''],
'' : ['','','','',''],
'' : ['','','','',''],


'penetration' : ['penetration','penetration','penetration','insertion','entry','invasion'],

'pee' : ['pee','urine','urinate','piss'],
'piss' : ['pee','urine','urinate','piss'],


'session' : ['session','mission','showdown','event','affair'],

'therapy' : ['therapy','healing','healing treatment','remidial therapy','healing therapy'],

'night' : ['night','evening','nighttime'],
'evening' : ['night','evening','nighttime'],
'nighttime' : ['night','evening','nighttime'],

'chair' : ['chair','seat','bench','armchair','rocker'],

'spank' : ['spank','butt slap','butt spank','ass slap','ass spank'],
'spanks' : ['spanks','butt slaps','butt spanks','ass slaps','ass spanks'],
'spanked' : ['spanked','butt slapped','butt spanked','ass slapped','ass spanked'],
'spanking' : ['spanking','butt slapping','butt spanking','ass slapping','ass spanking'],


'soft' : ['soft','smooth','cozy','comfy','comfortable'],

'studying' : ['studying','learning','reading','taking lesson','attending class'],

'study' : ['study','learning','reading','comprehending'],

'hand' : ['hand','hand','hand','hand grip','palm','hand fist','hand grasp'],


'call' : ['call','call','call','on demand'],

'preview' : ['preview','sneak peek','clip','trailer','teaser','promo'],
'trailer' : ['preview','sneak peek','clip','trailer','teaser','promo'],
'teaser' : ['preview','sneak peek','clip','trailer','teaser','promo'],
'promo' : ['preview','sneak peek','clip','trailer','teaser','promo'],

'repair' : ['repair','service','plumber','handyman'],

'fix' : ['repair','correct','fix','restore','adjust'],

'service' : ['service','satisfaction','amusement','pleasure','enjoyment'],
'services' : ['services','satisfies','amuses','pleases'],
'serviced' : ['serviced','satisfied','amused','pleased'],
'servicing' : ['servicing','satisfing','amusing','pleasing'],

'delivery' : ['percel delivery','percel distribution','percel dispatch','percel shipment','percel mailing','postman','ecommerce'],
'distribution' : ['percel delivery','percel distribution','percel dispatch','percel shipment','percel mailing','postman','ecommerce'],
'shipment' : ['percel delivery','percel distribution','percel dispatch','percel shipment','percel mailing','postman','ecommerce'],
'mailing' : ['percel delivery','percel distribution','percel dispatch','percel shipment','percel mailing','postman','ecommerce'],
'postman' : ['percel delivery','percel distribution','percel dispatch','percel shipment','percel mailing','postman','ecommerce'],
'ecommerce' : ['percel delivery','percel distribution','percel dispatch','percel shipment','percel mailing','postman','ecommerce'],

'club' : ['club','hangout','nightclub','disco'],

'slamming' : ['slamming','banging','slapping','fucking','ramming'],
'slammed' : ['slammed','banged','slaped','fucked','rammed'],
'slam' : ['slam','bang','slap','fucked','rammed'],

'hottest' : ['hottest','very best','most beautiful','most sexy','sizzling hot','blazing hot','scorching hot'],

'getting' : ['getting','is getting','being','having',''],

'taking' : ['getting','is getting','being','having','taking'],

'motion' : ['action','motion','move','movement','gesture','speed'],
'speed' : ['action','motion','move','movement','gesture','speed'],
'movement' : ['action','motion','move','movement','gesture','speed'],

'slow' : ['slow','lazy','calm','lazy bum','relaxed','reluctant'],
'lazy' : ['slow','lazy','calm','lazy bum','relaxed','reluctant'],
'calm' : ['slow','lazy','calm','lazy bum','relaxed','reluctant'],
'slow' : ['slow','lazy','calm','lazy bum','relaxed','reluctant'],
'relaxed' : ['slow','lazy','calm','lazy bum','relaxed','reluctant'],
'reluctant' : ['slow','lazy','calm','lazy bum','relaxed','reluctant'],


'pati' : ['pati','devar','bhai','dost','bhaiya','yaar','sainya'],
'devar' : ['pati','devar','bhai','dost','bhaiya','yaar','sainya'],
'bhai' : ['pati','devar','bhai','dost','bhaiya','yaar','sainya'],
'dost' : ['pati','devar','bhai','dost','bhaiya','yaar','sainya'],
'bhaiya' : ['pati','devar','bhai','dost','bhaiya','yaar','sainya'],
'sainya' : ['pati','devar','bhai','dost','bhaiya','yaar','sainya'],

'chudai' : ['chudai','chodna','chod dena','thukai','gaand marna','chut fadna'],

# /*German Goo Girls = GGG*/
'goo' : ['GGG','tripple G','orgasmic','ejaculatating','bukkake','cum hungry'],
'' : ['','','','',''],
'nuru' : ['nuru','slippery','smooth','Kawasaki massage','erotic massage','japanese nuru massage'],

'mff' : ['mff','ffm','one man with two woman','guy with two girls','single guy, double girls','two woman with one man','couple of babes with one guy','hotties with a guy','threesome'],
'ffm' : ['mff','ffm','one man with two woman','guy with two girls','single guy, double girls','two woman with one man','couple of babes with one guy','hotties with a guy','threesome'],

# /*'m27' : ['','','','',''],*/
'n15' : ['vintage','retro','adult story','adult movie','uncut story',''],# /*some time remove*/
'f70' : ['f70','adult story','adult movie','family sex','taboo family','vintage orgy','uncut story','parody',''],# /*some time remove*/

'omg' : ['OMG!','fuck!','F*ck!','Shit!','Wow!','Oh God!'],
'wow' : ['OMG!','fuck!','F*ck!','Shit!','Wow!','Oh God!'],
'shit' : ['OMG!','fuck!','F*ck!','Shit!','Wow!','Oh God!'],
'oh' : ['OMG!','fuck!','F*ck!','Shit!','Wow!','Oh God!'],
'god' : ['god','lord','dear','dear god','dear lord'],

'tv' : ['television','telly','tube','netfilx','adult-tube'],

# /*'class' : ['class','class room','education','course','lesson'],*/

'education' : ['education','course','lesson'],
'course' : ['education','course','lesson'],


'quicky' : ['quicky','quickie','Quick Fuck','Quickie Sex'],
'quickie' : ['quicky','quickie','Quick Fuck','Quickie Sex'],

'fake' : ['fake','artificial','not real'],

'perky' : ['perky','happy','bubbly','playful','buoyant','cheerful'],
'happy' : ['perky','happy','bubbly','playful','buoyant','cheerful'],
'bubbly' : ['perky','happy','bubbly','playful','buoyant','cheerful'],
'buoyant' : ['perky','happy','bubbly','playful','buoyant','cheerful'],
'cheerful' : ['perky','happy','bubbly','playful','buoyant','cheerful'],

'park' : ['park','garden','outdoor','public','green'],

# /*'lets' : ['let us','lets','let\'s', 'we will'],*/

'anything' : ['anything','everything','whatever'],
'everything' : ['anything','everything','whatever'],

'll' : ['ll','will'], # /*i'll, we'll etc*/

'will' : ['\'ll','will','will', 'would'], 

'we' : ['we are','we ware','we', 'we'], 

'find' : ['find','uncover','discover', 'reveal'], 
'finds' : ['finds','uncovers','discovers', 'reveals'], 

'today' : ['today','now','tonight', 'nowadays','next','soon','these days','at present','this day','this afternoon','this evening','this morning','at the moment','right now','this time', 'just now'], 
'now' : ['today','now','tonight', 'nowadays','next','soon','these days','at present','this day','this afternoon','this evening','this morning','at the moment','right now','this time', 'just now'], 
'tonight' : ['today','now','tonight', 'nowadays','next','soon','these days','at present','this day','this afternoon','this evening','this morning','at the moment','right now','this time', 'just now'], 
'nowadays' : ['today','now','tonight', 'nowadays','next','soon','these days','at present','this day','this afternoon','this evening','this morning','at the moment','right now','this time', 'just now'], 
'next' : ['today','now','tonight', 'nowadays','next','soon','these days','at present','this day','this afternoon','this evening','this morning','at the moment','right now','this time', 'just now'], 
'soon' : ['today','now','tonight', 'nowadays','next','soon','these days','at present','this day','this afternoon','this evening','this morning','at the moment','right now','this time', 'just now'], 


'bro' : ['stepbro','stepbrother','step-brother','step brother','not her brother'],
'brother' : ['stepbro','stepbrother','step-brother','step brother','not her brother'],
'stepbro' : ['stepbro','stepbrother','step-brother','step brother','not her brother'],
'stepbrother' : ['stepbro','stepbrother','step-brother','step brother','not her brother'],
'step-brother' : ['stepbro','stepbrother','step-brother','step brother','not her brother'],


'full' : ['full','packed','loaded','stuffed','filled'],
'packed' : ['full','packed','loaded','stuffed','filled'],
'loaded' : ['full','packed','loaded','stuffed','filled'],

'oozing' : ['oozing','dripping','exuding','discharging','seeping'],
'dripping' : ['oozing','dripping','exuding','discharging','seeping'],
'exuding' : ['oozing','dripping','exuding','discharging','seeping'],
'discharging' : ['oozing','dripping','exuding','discharging','seeping'],
'seeping' : ['oozing','dripping','exuding','discharging','seeping'],


'shocked' : ['shocked','stunned','astonished','amazed','startled'],
'stunned' : ['shocked','stunned','astonished','amazed','startled'],
'astonished' : ['shocked','stunned','astonished','amazed','startled'],
'amazed' : ['shocked','stunned','astonished','amazed','startled'],
'startled' : ['shocked','stunned','astonished','amazed','startled'],


'photoshoot' : ['photoshoot','photo session','photosession'],
'photographer' : ['photographer','camera man','paparazzo','photo snapper'],

'caught' : ['caught','busted','exposed'],
'busted' : ['caught','busted','exposed'],
'exposed' : ['caught','busted','exposed'],

'skills' : ['talent','art','ability','artistry','technique'],

'ugly' : ['ugly','fugly','unattractive','awful','awkward'],
'fugly' : ['ugly','fugly','unattractive','awful','awkward'],
'unattractive' : ['ugly','fugly','unattractive','awful','awkward'],
'awful' : ['ugly','fugly','unattractive','awful','awkward'],
'awkward' : ['ugly','fugly','unattractive','awful','awkward'],

'fan' : ['fan','lover','follower','devotee','admirer'], 
'follower' : ['fan','lover','follower','devotee','admirer'], 
'devotee' : ['fan','lover','follower','devotee','admirer'], 
'admirer' : ['fan','lover','follower','devotee','admirer'], 
 

'neighbour' : ['neighbour','neighbor','nextdoor','next-door','friend'],
'neighbor' : ['neighbour','neighbor','nextdoor','next-door','friend'],
'nextdoor' : ['neighbour','neighbor','nextdoor','next-door','friend'],
'next-door' : ['neighbour','neighbor','nextdoor','next-door','friend'],

'masseur' : ['masseur','male massager','massager boy','massager man','massager guy'],

'masseuse' : ['masseuse','female massager','girl massager','massager girl'],

'upskirt' : ['upskirt','upskirting','upskirts','pantyless','pantiless'],
'upskirting' : ['upskirt','upskirting','upskirts','pantyless','pantiless'],
'upskirts' : ['upskirt','upskirting','upskirts','pantyless','pantiless'],

'bedtime' : ['sleeping','bedtime','sleepy','dreamy'],

'pantyless' : ['pantyless','without panty','underwear less'],

'cheater' : ['cheater','cheating','cheat','unfaithful'],

'cheating' : ['cheating','ditching'],
'cheat' : ['cheat','ditch'],
'cheats' : ['cheats','ditchs'],

'flash' : ['flash','outdoor display ','outdoor exhibition','public display ','public exhibition'],
'flashes' : ['flashes','displayes outdoor','exhibits outdoor'],
'flashing' : ['flashing','outdoor displaying','outdoor exhibiting', 'public displaying','public exhibiting'],

'show' : ['show','display','exhibit'],
'shows' : ['shows','displayes','exhibits'],
'showing' : ['showing','displaying','exhibiting'],

'display' : ['show','display','exhibit'],
'displayes' : ['shows','displayes','exhibits'],
'displaying' : ['showing','displaying','exhibiting'],

'exhibit' : ['show','display','exhibit'],
'exhibits' : ['shows','displayes','exhibits'],
'exhibiting' : ['showing','displaying','exhibiting'],


'kiss' : ['kiss','smooch'],
'smooch' : ['kiss','smooch'],
'kissing' : ['kissing','smooching'],
'smooching' : ['kissing','smooching'],

'schoolgirl' : ['schoolgirl', 'preppy','School girl','schoolgirl (roleplay)','schoolgirl dress','schoolgirl (cosplay)','schoolgirl (parody)'],

'preppy' : ['schoolgirl', 'preppy','youthful','teen','18yo'],

'delicious' : ['delicious','yummy','tasty'],
'yummy' : ['delicious','yummy','tasty'],
'tasty' : ['delicious','yummy','tasty'],
'good' : ['good','delicious','yummy','tasty'],

'w' : ['w','with','with','with','accompanying with'],
'with' : ['w','with','with','with','accompanying with'],

'latex' : ['latex','rubber','pvc'], 
'rubber' : ['latex','rubber','pvc'], 
'pvc' : ['latex','rubber','pvc'], 

'sodomize' : ['sodomize','sodomizes','sodomized','anal practise','anal insert'],
'sodomizes' : ['sodomize','sodomizes','sodomized','anal practise','anal insert'],
'sodomized' : ['sodomize','sodomizes','sodomized','anal practised','anal inserted'],

'gothic' : ['gothic','mediecal','mediaeval'],  

'strapon' : ['strapon','strapping','strap-on','strapon dildo','Role Reversal strapon'],
'strapons' : ['strapon','strapping','strap-on','strapon dildo','Role Reversal strapon'],

'strap' : ['strap','strapping'],

'sporty' : ['sporty','flamboyant','playful','flaunting'],
'flamboyant' : ['sporty','flamboyant','playful','flaunting'],
'playful' : ['sporty','flamboyant','playful','flaunting'],
'flaunting' : ['sporty','flamboyant','playful','flaunting'],

'cameltoe' : ['cameltoe', 'camel toe', 'bikini cameltoe', 'cameltoe bikini', 'cameltoe leggings', 'leggings cameltoe','spandex cameltoe','cameltoe pussy'],     

'glasses' : ['glasses','eyeglasses','spectacles'],
'eyeglasses' : ['glasses','eyeglasses','spectacles'],
'spectacles' : ['glasses','eyeglasses','spectacles'],

'oil' : ['oil','oils','oiled','oily','oiled up','lubed'],
'oils' : ['oil','oils','oiled','oily','oiled up','lubed'],
'oiled' : ['oil','oils','oiled','oily','oiled up','lubed'],
'lubed' : ['oil','oils','oiled','oily','oiled up','lubed'],
'oily' : ['oil','oils', 'oiled','oily','oiled up','lubed'],

'bedroom' : ['chamber','bedroom','sleeping room','bunk room'],


'military' : ['military','army','soldier','trooper'],
'soldier' : ['military','army','soldier','trooper'],
'army' : ['military','army','soldier','trooper'],


'body' : ['body','physique','figure'],
'figure' : ['body','physique','figure'],
'physique' : ['body','physique','figure'],

'tryouts' : ['tryouts','test','examination','trial'],
'trial' : ['tryouts','test','examination','trial'],


'x' : ['with','against','vs','and','&'],

'topless' : ['topless','bare-breasted','bare-chested','braless','nude','unclothed'],

'mouth' : ['mouth','tongue'],
'tongue' : ['mouth','tongue'],

'action' : ['action','play','fun','job','process'],

'freaky' : ['bizarre','freaky','perverted','prev','crazy','strange','peculiar','weird'],
'crazy' : ['bizarre','freaky','perverted','prev','crazy','strange','peculiar','weird'],
'weird' : ['bizarre','freaky','perverted','prev','crazy','strange','peculiar','weird'],




# /*'s' : ['\'s'], to retrive back  's  after tokenization*/

'student' : ['student','learner'],
 
'rim' : ['rim','rims','rimming','rimjob','rimmed','analingus','anilingus','ass licking'],
'rims' : ['rim','rims','rimming','rimjob','rimmed','analingus','anilingus','ass licking'],
'rimming' : ['rim','rims','rimming','rimjob','rimmed','analingus','anilingus','ass licking'],
'rimjob' : ['rim','rims','rimming','rimjob','rimmed','analingus','anilingus','ass licking'],
'rimmed' : ['rim','rims','rimming','rimjob','rimmed','analingus','anilingus','ass licking'],
'analingus' : ['rim','rims','rimming','rimjob','rimmed','analingus','anilingus','ass licking'],
'anilingus' : ['rim','rims','rimming','rimjob','rimmed','analingus','anilingus','ass licking'],




'end' : ['end','finish','windup','wrap-up'], 
'ends' : ['ends','finishes','windups','wraps up'],

'bi' : ['bi','bisexual','hermaphrodites','hermaphrodditic','intersexual'],    
'bisex' : ['bi','bisexual','hermaphrodites','hermaphrodditic','intersexual'],    
'bisexual' : ['bi','bisexual','hermaphrodites','hermaphrodditic','intersexual'],    
'hermaphrodites' : ['bi','bisexual','hermaphrodites','hermaphrodditic','intersexual'],    
'hermaphrodite' : ['bi','bisexual','hermaphrodites','hermaphrodditic','intersexual'],    
'hermaphrodditic' : ['bi','bisexual','hermaphrodites','hermaphrodditic','intersexual'],   
'intersexual' : ['bi','bisexual','hermaphrodites','hermaphrodditic','intersexual'],   
 

'affair' : ['affair','illigal relation','extramarital relation'],
'affairs' : ['affairs','illigal relations','extramarital relations'],

'worship' : ['worship','worshipping','fetish','adoration','devotion'],
'worshipping' : ['worship','worshipping','fetish','adoration','devotion'],
'worshiped' : ['worship','worshipping','fetish','adoration','devotion'],
'worshipped' : ['worship','worshipping','fetish','adoration','devotion'],

'jock' : ['jock','athlete','sportsman'],
'jocks' : ['jocks','athletes','sportsmen'],



'cd' : ['crossdresser','crossdress'],
'cd' : ['crossdresser'],
'crossdresser' : ['crossdresser','crossdress','Crossed','crossdressing','male to female dressing','mtf dresser'],
'crossdress' : ['crossdresser','crossdress','Crossed','crossdressing','male to female dressing','mtf dresser'],
'Crossed' : ['crossdresser','crossdress','Crossed','crossdressing','male to female dressing','mtf dresser'],
'crossdressing' : ['crossdresser','crossdress','Crossed','crossdressing','male to female dressing','mtf dresser'],
'mtf' : ['crossdresser','crossdress','Crossed','crossdressing','male to female dressing','mtf dresser'],

'billy' : ['billy','willy','little penis','small dick'],
'willy' : ['billy','willy','little penis','small dick'],

'roommate' : ['roommate','buddy','homie','pal','companion'],  
'companion' : ['roommate','buddy','homie','pal','companion'],  
'homie' : ['roommate','buddy','homie','pal','companion'],  
'homies' : ['roommate','buddy','friend','pal','companion'], 
 
'again' : ['again','once again','once more','one more time'],

'handyman' : ['handyman','mechanic','repairman','technician','plumber', 'repair guy'],
'mechanic' : ['handyman','mechanic','repairman','technician','plumber', 'repair guy'],
'repairman' : ['handyman','mechanic','repairman','technician','plumber', 'repair guy'],
'technician' : ['handyman','mechanic','repairman','technician','plumber', 'repair guy'],
'plumber' : ['handyman','mechanic','repairman','technician','plumber', 'repair guy'],


'desk' : ['desk','table','tabletop'],

'table' : ['desk','table','tabletop','counter', 'stand', 'bar'],


'milking' : ['milking','lactating'],
'lactating' : ['milking','lactating'],

'lactation' : ['milk','lactation'],

'midget' : ['short','small','midget','lilliputian','petite'],

'dwarf' : ['short','small','midget','lilliput','petite'],

'moment' : ['moment','time','occasion'], 
'moments' : ['moments','time','occasion'], 
'time' : ['moments','time','occasion'],   
'times' : ['moments','time','occasion'],   
'occasion' : ['moments','time','occasion'],
  


'casual' : ['casual','accidental','random','spontaneous','unplanned','unforeseen','unexpected'],
'accidental' : ['casual','accidental','random','spontaneous','unplanned','unforeseen','unexpected'],
'spontaneous' : ['casual','accidental','random','spontaneous','unplanned','unforeseen','unexpected'],
'unplanned' : ['casual','accidental','random','spontaneous','unplanned','unforeseen','unexpected'],
'unforeseen' : ['casual','accidental','random','spontaneous','unplanned','unforeseen','unexpected'],
'unexpected' : ['casual','accidental','random','spontaneous','unplanned','unforeseen','unexpected'],

'neighbor' : ['neighbor','friend','acquaintance','homebudy','nextdoorbudy','bystander','guy next door'],  
'acquaintance' : ['neighbor','friend','acquaintance','homebudy','nextdoorbudy','bystander','guy next door'],  
'homebody' : ['neighbor','friend','acquaintance','homebudy','nextdoorbudy','bystander','guy next door'],  
'nextdoorbudy' : ['neighbor','friend','acquaintance','homebudy','nextdoorbudy','bystander','guy next door'], 
'nextdoorbuddies' : ['neighbors','friends','acquaintances','homebudy','nextdoorbudy','bystanders','guies next door'], 
'bystander' : ['neighbor','friend','acquaintance','homebudy','nextdoorbudy','bystander','guy next door'],  


'waitress' : ['waitress','hostess','stewardess','female attendent','female waiter','female host'],
'hostess' : ['waitress','hostess','stewardess','female attendent','female waiter','female host'],
'stewardess' : ['waitress','hostess','stewardess','female attendent','female waiter','female host'],

'outfit' : ['outfit','uniform','dress','costume','suit','clothing','apparel'],    
'outfits' : ['outfits','uniforms','dresses','costumes','suits','clothings','apparels'],    
'uniform' : ['outfit','uniform','dress','costume','suit','clothing','apparel'], 
'uniforms' : ['outfits','uniforms','dresses','costumes','suits','clothings','apparels'],   
'dress' : ['outfit','uniform','dress','costume','suit','clothing','apparel'],  
'dresses' : ['outfits','uniforms','dresses','costumes','suits','clothings','apparels'],  
'costume' : ['outfit','uniform','dress','costume','suit','clothing','apparel'],  
'costumes' : ['outfits','uniforms','dresses','costumes','suits','clothings','apparels'],  
'suit' : ['outfit','uniform','dress','costume','suit','clothing','apparel'],  
'suits' : ['outfits','uniforms','dresses','costumes','suits','clothings','apparels'],  
'clothing' : ['outfit','uniform','dress','costume','suit','clothing','apparel'],
'clothings' : ['outfits','uniforms','dresses','costumes','suits','clothings','apparels'],
'apparel' : ['outfit','uniform','dress','costume','suit','clothing','apparel'], 
'apparels' : ['outfits','uniforms','dresses','costumes','suits','clothings','apparels'],  


'jeans' : ['jeans','demins','blue jeans','levis jeans','levis pants'],

'softcore' : ['softcore','pornographic','pornigraphy','X-rated','xrated','bluefilm','erotica','erotic','vulgar'],
'pornographic' : ['softcore','pornographic','pornigraphy','X-rated','xrated','bluefilm','erotica','erotic','vulgar'],
'pornigraphy' : ['softcore','pornographic','pornigraphy','X-rated','xrated','bluefilm','erotica','erotic','vulgar'],
'xrated' : ['softcore','pornographic','pornigraphy','X-rated','xrated','bluefilm','erotica','erotic','vulgar'],
'bluefilm' : ['softcore','pornographic','pornigraphy','X-rated','xrated','bluefilm','erotica','erotic','vulgar'],
'erotica' : ['softcore','pornographic','pornigraphy','X-rated','xrated','bluefilm','erotica','erotic','vulgar'],
'vulgar' : ['softcore','pornographic','pornigraphy','X-rated','xrated','bluefilm','erotica','erotic','vulgar'],


'flexible' : ['flexible','flexi','bendable','elastic','gymnast'],    
'flexi' : ['flexible','flexi','bendable','elastic','gymnast'],    
'bendable' : ['flexible','flexi','bendable','elastic','gymnast'],    
'elastic' : ['flexible','flexi','bendable','elastic','gymnast'],    
'gymnast' : ['flexible','flexi','bendable','elastic','gymnast'],    


'nudist' : ['nudist','exhibitionist'], 
'exhibitionist' : ['nudist','exhibitionist'], 

'morning' : ['morning','breakfast','awakening'],
'breakfast' : ['morning','breakfast','awakening'],
'awakening' : ['morning','breakfast','awakening'],

'cosplay' : ['cosplay','costume play','dressing up','anime dressing','hentai dressing','manga dressing','naruto dressing'],

'roleplay' : ['sexual roleplay','roleplay','erotic roleplay','sexual fantasy play'],

'parody' : ['parody','storyline','plotline','story porn'], 



'abuse' : ['molest','ruin','spoil','waste'],
'abused' : ['molested','ruined','spoiled','wasted'],

'cheerleader' : ['cheerleader','cheer girl'],
'agent' : ['agent','broker','negotiator','handler','pimp'],


'shy' : ['quite','hesitant','afraid','nervous','humble','introvert'],
'hesitant' : ['quite','hesitant','afraid','nervous','humble','introvert'],
'afraid' : ['quite','hesitant','afraid','nervous','humble','introvert'],
'nervous' : ['quite','hesitant','afraid','nervous','humble','introvert'],
'humble' : ['quite','hesitant','afraid','nervous','humble','introvert'],
'introvert' : ['quite','hesitant','afraid','nervous','humble','introvert'],

'nipple' : ['nipple','nob','teat','nip'],
'nob' : ['nipple','nob','teat','nip'],
'nip' : ['nipple','nob','teat','nip'],
'nipples' : ['nipples','nobs','teats','nips'],
'nobs' : ['nipples','nobs','teats','nips'],
'nips' : ['nipples','nobs','teats','nips'],

'valentines' : ['lovers','valentines'],
'valentine' : ['lovers','valentines'],


'shaved' : ['shaved','hairless','smooth'],

'village' : ['village','country','native','small town','suburb'],

'town' : ['town','city','country','village'],
'city' : ['town','city','country','village'],
'country' : ['town','city','country','village'],

'sloppy' : ['sloppy','slurping','wet','watery'],
'slurping' : ['sloppy','slurping','wet','watery'],


'toilet' : ['toilet','restroom','latrine','bathroom','lavatory','commode','washroom'],
'restroom' : ['toilet','restroom','latrine','bathroom','lavatory','commode','washroom'],
'latrine' : ['toilet','restroom','latrine','bathroom','lavatory','commode','washroom'],
'lavatory' : ['toilet','restroom','latrine','bathroom','lavatory','commode','washroom'],
'commode' : ['toilet','restroom','latrine','bathroom','lavatory','commode','washroom'],
'washroom' : ['toilet','restroom','latrine','bathroom','lavatory','commode','washroom'],


'screaming' : ['screaming','crying','loud moaning'], 
'crying' : ['screaming','crying','loud moaning'], 

'quickie' : ['quickie','quick fuck','quick sex'],
'tricked' : ['tricked','seduced'],

'trickery' : ['trickery','cheating','fraud','deceit',''],
'trick' : ['trick','stunt','prank','scam'],
'tricks' : ['tricks','stunts','pranks','scams'],
'tricky' : ['trickful','crafty','artful','scammy','dodgy'],


'seduce' : ['seduce', 'tempt', 'tease', 'attract', 'captivate','lure'],
'tempt' : ['seduce', 'tempt', 'tease', 'attract', 'captivate','lure'],
'tease' : ['seduce', 'tempt', 'tease', 'attract', 'captivate','lure'],
'attract' : ['seduce', 'tempt', 'tease', 'attract', 'captivate','lure'],
'captivate' : ['seduce', 'tempt', 'tease', 'attract', 'captivate','lure'],
'lure' : ['seduce', 'tempt', 'tease', 'attract', 'captivate','lure'],


'seduces' : ['seduces', 'tempts', 'teases', 'attracts', 'captivates','lures'],
'tempts' : ['seduces', 'tempts', 'teases', 'attracts', 'captivates','lures'],
'teases' : ['seduces', 'tempts', 'teases', 'attracts', 'captivates','lures'],
'attracts' : ['seduces', 'tempts', 'teases', 'attracts', 'captivates','lures'],
'captivates' : ['seduces', 'tempts', 'teases', 'attracts', 'captivates','lures'],
'lures' : ['seduces', 'tempts', 'teases', 'attracts', 'captivates','lures'],


'seduced' : ['seduced', 'tempted', 'teased', 'attracted', 'captivated'],
'tempted' : ['seduced', 'tempted', 'teased', 'attracted', 'captivated'],
'teased' : ['seduced', 'tempted', 'teased', 'attracted', 'captivated'],
'attracted' : ['seduced', 'tempted', 'teased', 'attracted', 'captivated'],
'captivated' : ['seduced', 'tempted', 'teased', 'attracted', 'captivated'],


'seducing' : ['seducing', 'tempting', 'teasing', 'attracting', 'captivating'],
'tempting' : ['seducing', 'tempting', 'teasing', 'attracting', 'captivating'],
'teasing' : ['seducing', 'tempting', 'teasing', 'attracting', 'captivating'],
'attracting' : ['seducing', 'tempting', 'teasing', 'attracting', 'captivating'],



'bizarre' : ['bizarre','perverted','weird','strange','ridiculous','kinky'],
'weird' : ['bizarre','perverted','weird','strange','ridiculous','kinky'],
'strange' : ['bizarre','perverted','weird','strange','ridiculous','kinky'],
'ridiculous' : ['bizarre','perverted','weird','strange','ridiculous','kinky'],
'kinky' : ['bizarre','perverted','weird','strange','ridiculous','kinky'],

 
'lick' : ['lick','cunnilingu', 'tongue','taste'],
'licks' : ['licks','cunnilingu', 'tongues','tastes'],
'licked' : ['lick','cunnilingu', 'tongue','taste'],
'licking' : ['licking','cunnilingu', 'giving tongue','tasting'],
'cunnilingu' : ['lick','cunnilingu', 'tongue','taste'],
'cunnilingus' : ['lick','cunnilingus', 'tongue','taste'],

'dp' : ['double penetration','fuck both holes','double insertion', 'doublefucked'],
  
'seduction' : ['seduction','lovemaking','romance'],
'lovemaking' : ['seduction','lovemaking','romance'],
'romance' : ['seduction','lovemaking','romance'],


'ride' : ['ride','riding','cowgirl','reverse cowgirl'],
'rides' : ['rides','riding','cowgirls','does reverse cowgirl','has reverse cowgirl','reverse cowgirls'],
'riding' : ['ride','riding','cowgirl','reverse cowgirl'],
'cowgirl' : ['ride','riding','cowgirl','reverse cowgirl','fat ass'],
'cowgirls' : ['ride','riding','cowgirls','reverse cowgirls'],


'queen' : ['queen','princess'],
'queens' : ['queens','princess'],
'princess' : ['queen','princess'],


'finger' : ['finger','rub','solo play'],
'fingers' : ['fingers','rubs','solo playes'],
'fingering' : ['fingering','rubbing','solo playing'],
'fingered' : ['fingered','rubbed','solo played'],

 
'solo' : ['solo','camgirl','camster','camshow','solo masturbation','solo pleasure','solo play'],
'camgirl' : ['solo','camgirl','camster','camshow','solo masturbation','solo pleasure','solo play'],
'camster' : ['solo','camgirl','camster','camshow','solo masturbation','solo pleasure','solo play'],
 
'pool' : ['pool','swimming pool'],

'subtitled' : ['subtitled','captions','captioned','with subtitles','with captions'],
'subtitles' : ['subtitled','captions','captioned','with subtitles','with captions'],
'captions' : ['subtitled','captions','captioned','with subtitles','with captions'],
'captioned' : ['subtitled','captions','captioned','with subtitles','with captions'],



'spying' : ['spying','peeping','snooping'],

'story' : ['story','tale','saga','fabel','memoir','drama'],
'tale' : ['story','tale','saga','fabel','memoir','drama'],
'saga' : ['story','tale','saga','fabel','memoir','drama'],
'fabel' : ['story','tale','saga','fabel','memoir','drama'],
'memoir' : ['story','tale','saga','fabel','memoir','drama'],
'drama' : ['story','tale','saga','fabel','memoir','drama'],

 

'thong' : ['thong','lingerie','bikini','panties','panty','swimsuit','swimwear','bra','micro bikini'],
'lingerie' : ['thong','lingerie','bikini','panties','panty','swimsuit','swimwear','bra','micro bikini'],
'bikini' : ['thong','lingerie','bikini','panties','panty','swimsuit','swimwear','bra','micro bikini'],
'panties' : ['thong','lingerie','bikini','panties','panty','swimsuit','swimwear','bra','micro bikini'],
'panty' : ['thong','lingerie','bikini','panties','panty','swimsuit','swimwear','bra','micro bikini'],
'swimsuit' : ['thong','lingerie','bikini','panties','panty','swimsuit','swimwear','bra','micro bikini'],
'swimwear' : ['thong','lingerie','bikini','panties','panty','swimsuit','swimwear','bra','micro bikini'],
'bra' : ['thong','lingerie','bikini','panties','panty','swimsuit','swimwear','bra','micro bikini'],



'having' : ['having','enjoy','enjoying','have'],

'creamy' : ['creamy','cream filled','milky','buttery'],
'milky' : ['creamy','cream filled','milky','lactating'],


'home' : ['home','house','appartment'],
'house' : ['home','house','appartment'],
'appartment' : ['home','house','appartment'],

'natural' : ['natural','homegrown','real','homemade'],
'naturally' : ['natural','homegrown','real','homemade'],
'homegrown' : ['natural','homegrown','real','homemade'],
  
'machines' : ['machines','machine','fuck machine','fucking machine','sex machine'],
'machine' : ['machines','machine','fuck machine','fucking machine','sex machine'],

'helps' : ['helps','assists','supports'],
'assists' : ['helps','assists','supports'],
'supports' : ['helps','assists','supports'],


'phat' : ['ace','brilliant','excellent','fabulous','awesome','lush','splendid','outstanding','wicked','smoking hot'],

'pleased' : ['pleased','satisfied','contented','entertained','amused'],
'satisfied' : ['pleased','satisfied','contented','entertained','amused'],
'pleases' : ['pleases','satisfies','contents','entertains','amuses'],
 
'secretary' : ['secretary','personal assitant','office worker','office employee','employee','office co-worker','co-worker','office clerk'],
'secretaries' : ['secretaries','personal assitants','office workers','office employeess','employees','office co-workers','co-workers','office clerks'],
'employee' : ['secretary','personal assitant','office worker','office employee','employee','office co-worker','co-worker','office clerk'],
'co-worker' : ['secretary','personal assitant','office worker','office employee','employee','office co-worker','co-worker','office clerk'],
'coworker' : ['secretary','personal assitant','office worker','office employee','employee','office co-worker','co-worker','office clerk'],
'worker' : ['secretary','personal assitant','office worker','office employee','employee','office co-worker','co-worker','office clerk'],
'colleague' : ['colleague','employee','co-worker','office friends','office workers'],


'client' : ['client','customer','consumer','purchaser'],
'customer' : ['client','customer','consumer','purchaser'],
'consumer' : ['client','customer','consumer','purchaser'],


'spread' : ['spread','stretch'],
'stretch' : ['spread','stretch'],
'spreading' : ['spreading','stretching'],
'stretching' : ['spreading','stretching'],
'spreads' : ['spreads','streachs'],
'streachs' : ['spreads','streachs'],
 
'stiff' : ['hard','solid','firm','thick','strong','erect'],

'geek' : ['geek','nerd','jerk','techie'],
'geeky' : ['geeky','nerdy','jerky','techie'],
'nerd' : ['geek','nerd','jerk','techie'],
'nerdy' : ['geeky','nerdy','jerky','techie'],
# /*'jerk' : ['geek','nerd','jerk','techie'],*/ # /*mostly used for "jerk off"*/
'techie' : ['geek','nerd','jerk','techie'],



'takes' : ['takes','enjoys','gets','has'],

'nurse' : ['hospital nurse','hospital caretaker','female attendent','hospital attendent','medic','nursemaid'],
   
'chat' : ['chat','chatting','sexting'],

'vacation' : ['vacation','holiday','weekend','outing'],
'holiday' : ['vacation','holiday','weekend','outing'],
'weekend' : ['vacation','holiday','weekend','outing'],

'kitchen' : ['kitchen','kitchen sink','kitchen table'],

'filled' : ['filled','creampied','cream filled','creamed','stuffed'],
 
'enjoying' : ['enjoying','having fun','loving'],

'loves' : ['enjoys','likes','loves','adores', 'is a fan of'],
'likes' : ['enjoys','likes','loves','adores', 'is a fan of'],
   
'joi' : ['jerkoff instructions'],

'till' : ['till','until','up to','up till','before'],
'until' : ['till','until','up to','up till','before'],

'another' : ['another','yet another','one more','other','more','some other','fresh'],

'son' : ['son','step son','boy'],
'stepson' : ['son','step son','boy'],

'gf' : ['gf','girlfriend','date','girl friend','sweetheart','soul mate','fiancee','lover','true love'],
'girlfriend' : ['gf','girlfriend','date','girl friend','sweetheart','soul mate','fiancee','lover','true love'],
'girlfriends' : ['gfs','girlfriends','dates','girl-friends','sweethearts','soul-mates','lovers','true-loves'],
'date' : ['gf','girlfriend','date','girl friend','sweetheart','soul mate','fiancee','lover','true love'],



'episode' : ['episode','season','part','series'],

'property' : ['property','real estate'],



'fantasy' : ['fantasy','dream','desire','obsession'],
'adventure' : ['adventure', 'fantasy','dream','desire','obsession','experience'],
'adventures' : ['adventures', 'fantasies','dreams','desires','obsessions','experiences'],
'dream' : ['fantasy','dream','desire','wish','obsession'],
'dreams' : ['fantasies','dreams','desires','wishes'],
'desire' : ['fantasy','dream','desire','obsession','lust'],
'lust' : ['fantasy','dream','desire','obsession','lust'],
'obsession' : ['fantasy','dream','desire','obsession'],
'desires' : ['fantasies','dreams','desires'],

'experience' : ['adventure', 'fantasy','fun','enjoyment','experience'],

'first' : ['first','1st', 'first-time','maiden'],
'1st' : ['first','1st',' first-time','maiden'],
'first-time' : ['first','1st',' first-time','maiden'],
'maiden' : ['first','1st',' first-time','maiden'],

'second' : ['2nd','second'],
'2nd' : ['2nd','second'],

'new' : ['new','fresh','recent'],
'fresh' : ['new','fresh','recent'],
'recent' : ['new','fresh','recent'],

'vs' : ['with','against'],

'featuring' : ['feat','featuring','starring','Ft.'],
'feat' : ['feat','featuring','starring','Ft.'],
'ft' : ['feat','featuring','starring','Ft.'],
'starring' : ['feat','featuring','starring','Ft.'],

'cheeks' : ['lips'],
'lips' : ['cheeks'],

'forest' : ['forest','woods','jungle','outdoor'],
'woods' : ['forest','woods','jungle','outdoor'],
'jungle' : ['forest','woods','jungle','outdoor'],

'swap' : ['swap','exchange'],
'swaps' : ['swaps','exchanges'],
# /*'exchange' : ['swap'],*/
'swapping' : ['swapping','exchanging'],

'football' : ['football','soccer','nfl','rugby'],
'soccer' : ['football','soccer','nfl','rugby'],

'sauna' : ['sauna','spa','hot spring','helth club','steam room','hot tub'],
'spa' : ['sauna','spa','hot spring','helth club','steam room','hot tub'],

'herself' : ['her','herself','her body','her pussy','her soul'],

'miss' : ['miss','young','missy','young lady','young woman','young girl','unmarried woman','unmarried lady'],
'missy' : ['miss','young','missy','young lady','young woman','young girl','unmarried woman','unmarried lady'],
'mrs' : ['mrs','married woman','married lady', 'house wife'],
'ms' : ['ms','the','babe','beutiful','sexy','lovely'],

'raw' : ['rude','natural','pure','coarse','hard'],

'shes' : ['shes','she is','she\'s'],
  
'hidden' : ['hidden','secret','private','concealed'],
'spy' : ['hidden','secret','private','concealed','spy'],
'secret' : ['hidden','secret','private','concealed'],
'private' : ['hidden','secret','private','concealed'],

'twice' : ['twice', 'two times','second time','over again','once over'],
'pls' : ['please','pls','plz'],
 
'beach' : ['beach','shore','coast','seashore','seaside', 'seafront'],
'vr' : ['vr','virtual real','virtual reality'],

'emo' : ['emo','emocore','tattooed'],
'tattooed' : ['emo','emocore','tattooed'],
 
'police' : ['police','cop','policeman','lawman','police officer','officer'],
'cop' : ['police','cop','policeman','lawman','police officer','officer'],
   
'xhamster' : ['xhamster','xvideos','pornhub','xnxx'],
'xvideos' : ['xhamster','xvideos','pornhub','xnxx'],
'pornhub' : ['xhamster','xvideos','pornhub','xnxx'],
'xnxx' : ['xhamster','xvideos','pornhub','xnxx'],

'classic' : ['classic','classy','glamorous','classical','superior','superb'],
'classy' : ['classic','classy','glamorous','classical','superior','superb'],
'classical' : ['classic','classy','glamorous','classical','superior','superb'],

'driver' : ['driver','chauffeur','cabbie','cabby'],

'grandpa' : ['grandpa','grandpapa','grand father','old man','step grandpa'],

'compilation' : ['compilation','compiled collection','collection','compiled clips','compiled videos'],
'collection' : ['compilation','compiled collection','collection','compiled clips','compiled videos'],

'hairy' : ['hairy','full of hair','furry','haired','fuzzed','bushy'],

'phone' : ['phone','mobile','mobile phone','cell phone'],

'christmas' : ['christmas','xmas','x-mas','christmas day','xmas day','christmas eve', 'x-mas eve','christmas night','x-mas night','christmas party','x-mas party', 'christmas celebration','x-mas celebration' ],
'xmas' : ['christmas','xmas','x-mas','christmas day','xmas day','christmas eve', 'x-mas eve','christmas night','x-mas night','christmas party','x-mas party', 'christmas celebration','x-mas celebration' ],
'x-mas' : ['christmas','xmas','x-mas','christmas day','xmas day','christmas eve', 'x-mas eve','christmas night','x-mas night','christmas party','x-mas party', 'christmas celebration','x-mas celebration' ],
 
'muscular' : ['muscular','muscled','robust','athletic','powerful','herculean','hulky','masculine'],

'athletic' : ['muscular','muscled','robust','athletic','powerful','energetic','strong','masculine','fit'],
'energetic' : ['muscular','muscled','robust','athletic','powerful','energetic','strong','masculine','fit'],


'birthday' : ['birthday','cakeday','birthday party','birthday celebration','birthday gift', 'cakeday party', 'cakeday celebration'],
 
'spouse' : ['spouse','batter half','partner','companion','roommate','soulmate','lover'],
'lover' : ['spouse','batter half','partner','companion','roommate','soulmate','lover'],
'partner' : ['spouse','batter half','partner','companion','roommate','soulmate','lover'],
'companion' : ['spouse','batter half','partner','companion','roommate','soulmate','lover'],
'roommate' : ['spouse','batter half','partner','companion','roommate','soulmate','lover'],
'soulmate' : ['spouse','batter half','partner','companion','roommate','soulmate','lover'],
 
'bathroom' : ['bathroom','shower'],
'shower' : ['bathroom','shower','bath'],
'bath' : ['bathroom','shower','bath'],
 
'bathtub' : ['bathroom','shower','bath','bathtub','bathing tub','tub'],
'tub' : ['bathroom','shower','bath','bathtub','bathing tub','tub'],

'fisting' : ['fisting','inserting','stuffing'],
'inserting' : ['fisting','inserting','stuffing'],
'stuffing' : ['fisting','inserting','stuffing'],

'fits' : ['fits','takes'],

'stroking' : ['stroking','thumping','jerking','yanking'],
'strok' : ['stroking','thumping','jerking','yanking'],
'strokes' : ['strokes','thumps','jerkes','yanks'],
'thumping' : ['stroking','thumping','jerking','yanking'],
# /*'humping' : ['stroking','thumping','humping','jerking','yanking'],*/
'jerking' : ['stroking','thumping','jerking','yanking'],
'yanking' : ['stroking','thumping','jerking','yanking'],
 
'ruined' : ['ruined','destroyed','wrecked'],
'destroyed' : ['ruined','destroyed','wrecked'],
'destroy' : ['ruined','destroyed','wrecked'],
'destroyes' : ['ruined','destroyed','wrecked'],
'destruction' : ['ruined','destroyed','wrecked'],
'wrecked' : ['ruined','destroyed','wrecked'],

'married' : ['married','already married'],

'inches' : ['inches','inches long'],
'inch' : ['inch','inch long'],
'tricky' : ['tricky','trick full','skilled','skillful'], 
'balls' : ['balls','testicles','testis','nuts'],
'plus' : ['plus','+'],

'shiny' : ['shiny','polished','glossy','bright','glistening','glowing','shining','glittering','glistering'],
'polished' : ['shiny','polished','glossy','bright','glistening','glowing','shining','glittering','glistering'],
'glossy' : ['shiny','polished','glossy','bright','glistening','glowing','shining','glittering','glistering'],
'bright' : ['shiny','polished','glossy','bright','glistening','glowing','shining','glittering','glistering'],
'glistening' : ['shiny','polished','glossy','bright','glistening','glowing','shining','glittering','glistering'],
'glittering' : ['shiny','polished','glossy','bright','glistening','glowing','shining','glittering','glistering'],
'glistering' : ['shiny','polished','glossy','bright','glistening','glowing','shining','glittering','glistering'],

'guest' : ['guest','visitor','relative','stranger','unknown guy'],

'stranger' : ['guest','visitor','random guy','stranger','unknown guy','unknown','outsider','outlander'],

'juices' : ['juices','cums','loads'],
'cums' : ['juices','cums','loads'],
'loads' : ['juices','cums','loads'],

'sperm' : ['sperm','shemen','cum','load','juice'],
'shemen' : ['sperm','shemen','cum','load','juice'],
'load' : ['sperm','shemen','cum','load','juice'],
'juice' : ['sperm','shemen','cum','load','juice'],

'redhead' : ['redhead','red haired'],
'ex' : ['ex','previous','former','past','old'],
'gift' : ['gift','present','surprise'],

'online' : ['online','on tinder','on facebook','on internet','on social network','on dating site','on dating app'],
'credit' : ['credit','loan','mortgage'],
'loan' : ['credit','loan','mortgage'],

'daughter' : ['daughter','step-daughter','step daughter'],
'step-daughter' : ['daughter','step-daughter','step daughter'],
'stepdaughter' : ['daughter','step-daughter','step daughter'],

'casting' : ['casting','audition','interview','casting couch','interviewed'],  
'audition' : ['casting','audition','interview','casting couch','interviewed'],  
'interview' : ['casting','audition','interview','casting couch','interviewed'],
'interviewed' : ['casting','audition','interview','casting couch','interviewed'],
 
'sofa' : ['sofa','couch'],

'preggo' : ['preggo','pregnant','preggers'],
'pregnant' : ['preggo','pregnant','preggers'],

'special' : ['special','premium','exclusive','especial','best','exceptional','smashing','different'], 
'premium' : ['special','premium','exclusive','especial','best','exceptional','smashing','different'], 
'exclusive' : ['special','premium','exclusive','especial','best','exceptional','smashing','different'], 
'especial' : ['special','premium','exclusive','especial','best','exceptional','smashing','different'], 
'smashing' : ['special','premium','exclusive','especial','best','exceptional','smashing','different'], 

'pantyhose' : ['pantyhose','nylons','stockings','leggings'],
'nylons' : ['pantyhose','nylons','stockings','leggings'],
'nylon' : ['pantyhose','nylons','stockings','leggings'],
'stockings' : ['pantyhose','nylons','stockings','leggings'],
'stocking' : ['pantyhose','nylons','stockings','leggings'],
'leggings' : ['pantyhose','nylons','stockings','leggings'],
'legging' : ['pantyhose','nylons','stockings','leggings'],

'rubs' : ['rubs','pats','strokes','massages','stroking'],
'rubbing' : ['rubbing','patting','stroking','massaging','pumping','humping'],
'rubbed' : ['rubbed','patted','stroked','massaged'],
'pumping' : ['rubbing','patting','stroking','massaging','pumping'],

'humping' : ['humping','rubbing','patting','stroking','massaging','pumping'],

'hole' : ['hole','opening','crack','gap','cave','pit'],
'holes' : ['holes','openings','cracks','gaps','caves','pits'],

# /*saree, sari, satin saree, paticote, blouse, lahenga, choli, pallu, desi saree, indian saree,*/
'saree' : ['saree','sari','satin saree','paticote','blouse','lahenga','choli','pallu','desi saree','indian saree'],
 
'spandex' : ['spandex','tight pants','tight leggings'],
'free' : ['free','free of cost','free of charge','absolutely free','for free','costing tothing','costless','unpaid','gratis'],
'atm' : ['atm','ass to mouth','anal to suck','anal to blow','anal to oral'],

'best' : ['best','great','perfect','top','super','A-1'],
'perfect' : ['best','great','perfect','top','super','A-1'],
'great' : ['best','great','perfect','top','super','A-1'],



'fun' : ['fun', 'enjoyment', 'joy', 'pleasure', 'blast', 'relaxation', 'good time', 'amusement', 'play'],
'enjoyment' : ['fun', 'enjoyment', 'joy', 'pleasure', 'blast', 'relaxation', 'good time', 'amusement', 'play'],
'pleasure' : ['fun', 'enjoyment', 'joy', 'pleasure', 'blast', 'relaxation', 'good time', 'amusement', 'play'],
'relaxation' : ['fun', 'enjoyment', 'joy', 'pleasure', 'blast', 'relaxation', 'good time', 'amusement', 'play'],
'amusement' : ['fun', 'enjoyment', 'joy', 'pleasure', 'blast', 'relaxation', 'good time', 'amusement', 'play'],

'play' : ['fun', 'enjoy', 'joy', 'pleasure', 'blast', 'relaxation', 'good time', 'amusement', 'play'],
'playing' : ['having fun', 'enjoying', 'having joy', 'having pleasure', 'having blast', 'relaxing', 'having good time', 'amusing', 'playing'],
'plays' : ['has fun', 'enjoys', 'has joy', 'has pleasure', 'has blast', 'has relaxation', 'has amusement', 'plays'],


'enjoy' : ['fun', 'enjoy', 'please', 'blast', 'relax', 'amuse', 'play'],
'enjoys' : ['has fun', 'enjoys', 'has joy', 'has pleasure', 'has blast', 'has relaxation', 'has amusement', 'plays'],
'enjoyed' : ['had fun', 'enjoyed', 'had joy', 'had pleasure', 'had blast', 'had relaxation', 'had amusement', 'played'],
'enjoying' : ['having fun', 'enjoying', 'having joy', 'having pleasure', 'having blast', 'relaxing', 'having good time', 'amusing', 'playing'],

'endure' : ['endure', 'withstand', 'tolerate', 'encounter', 'suffer'],
'endures' : ['endures', 'withstands', 'tolerates', 'encounters', 'suffers'],

# /*'creampied', 'creampie' , 'cream filled', 'creamed', 'cream stuffed' , 'cum inside', 'ejaculated inside', 'cum dripping'*/
'creampied' : ['creampied', 'creampie' , 'cream filled', 'creamed', 'cream stuffed' , 'cum inside', 'ejaculated inside', 'cum dripping','spunked inside'],
'creampie' : ['creampied', 'creampie' , 'cream filling', 'creamed', 'cream stuffing' , 'cum inside', 'ejaculatating inside', 'cum dripping','spunking inside'],
'creamed' : ['creampied', 'creampie' , 'cream filled', 'creamed', 'cream stuffed' , 'cum inside', 'ejaculated inside', 'cum dripping','spunked inside'],


'style' : ['style','pose','position','posture'],
'pose' : ['style','pose','position','posture'],
'position' : ['style','pose','position','posture'],
'posture' : ['style','pose','position','posture'],

'positions' : ['positions','styles','poses','postures'],
'styles' : ['positions','styles','poses','postures'],
'poses' : ['positions','styles','poses','postures'],
'postures' : ['positions','styles','poses','postures'],




'str8' : ['straight','heterosexual','hetro'],
'hetero' : ['hetero','heterosexual','straight'],
'heterosexual' : ['hetero','heterosexual','straight'],

'fetish' : ['fetish','worshiping','fantasy','obsession'],

'footjob' : ['footjob', 'foot job','foot fetish', 'foot fuck', 'foot play', 'feet worship'],
'feetjob' : ['footjob', 'foot job','foot fetish', 'foot fuck', 'foot play', 'feet worship'],

'chef' : ['chef','cook'],
'cook' : ['chef','cook'],

'family' : ['forbidden family','taboo family','immoral family'],

'umcut' : ['full','complete','whole'],

'feels' : ['feels','tastes','seems'],

'washer' : ['washer','cleaner'],
'cleaner' : ['washer','cleaner'],

'clean' : ['clean','wash','clear'],
'wash' : ['clean','wash','clear'],
'clear' : ['clean','wash','clear'],

'pissing' : ['pissing','peeing','urinating'],
'pissed' : ['pissed', 'pissing','peeing','urinating'],
'peeing' : ['pissing','peeing','urinating'],
'urinating' : ['pissing','peeing','urinating'],

'deepthroat' : ['deepthroat','deep throat','deep-throat','throatpie','gagged','gagging','throat fuck'],
'deepthroating' : ['deepthroat','deep throat','deep-throat','throatpie','gagged','gagging','throat fuck'],
'throat' : ['deepthroat','deep throat','deep-throat','throatpie','gagged','gagging','throat fuck'],
'throatpie' : ['deepthroat','deep throat','deep-throat','throatpie','gagged','gagging','throat fuck'],
'gag' : ['deepthroat','deep throat','deep-throat','throatpie','gagged','gagging','throat fuck'],
'gags' : ['deepthroat','deep throat','deep-throat','throatpie','gagged','gagging','throat fuck'],
'gagged' : ['deepthroat','deep throat','deep-throat','throatpie','gagged','gagging','throat fuck'],
'gagging' : ['deepthroat','deep throat','deep-throat','throatpie','gagged','gagging','throat fuck'],


'gym' : ['gym','gymnasium','health club','fitnessrooms'],
'gymnasium' : ['gym','gymnasium','health club','fitnessrooms'],
'fitnessrooms' : ['gym','gymnasium','health club','fitnessrooms'],

'workout' : ['gym','exercise','gym session','workout'],

'exercise' : ['gym session','exercise','workout'],
'exercises' : ['exercises','works out'],

'innocent' : ['innocent','angel','childlike','naive'],    
'angel' : ['innocent','angel','childlike','naive'],    
'childlike' : ['innocent','angel','childlike','naive'],    
'naive' : ['innocent','angel','childlike','naive'], 
   
'younger' : ['younger','junior'],
'junior' : ['younger','junior'],

   
   
'swallow' : ['swallow','eat','gulp','slurp'],
'eat' : ['swallow','eat','gulp','slurp'],
'gulp' : ['swallow','eat','gulp','slurp'],
'slurp' : ['swallow','eat','gulp','slurp'],

'swallows' : ['swallows','eats','gulps','slurps'],
'eats' : ['swallows','eats','gulps','slurps'],
'gulps' : ['swallows','eats','gulps','slurps'],
'slurps' : ['swallows','eats','gulps','slurps'],

'swallowed' : ['swallowed','ate','gulpped','slurpped'],
'ate' : ['swallowed','ate','gulpped','slurpped'],
'gulpped' : ['swallowed','ate','gulpped','slurpped'],
'slurpped' : ['swallowed','ate','gulpped','slurpped'],

'swallowing' : ['swallowing','eating','gulping','slurping','drinking'],
'eating' : ['swallowing','eating','gulping','slurping'],
'gulping' : ['swallowing','eating','gulping','slurping','drinking'],

'drinking' : ['swallowing','gulping','slurping','drinking','consuming','imbibing'],
'drink' : ['swallow','gulp','slurp','drink','consume','imbibe'],
'drinks' : ['swallows','gulps','slurps','drinks','consumes','imbibes'],

'room' : ['room','house','place'],
'rooms' : ['rooms','house','place'],

'twink' : ['twink','boyish man','boyish young'],

'strip' : ['strip','remove clothes','remove clothes erotically','striptease','undress', 'undress erotically'],
'strips' : ['strips','removes clothes','removes clothes erotically','striptease','undresses', 'undresses erotically'],
'stripping' : ['strip','removing clothes','removing clothes erotically','striptease','undressing', 'undressing erotically'],

'stripper' : ['stripper','striptease','stripteaser','strip dancer','pole dancer'],
'striper' : ['stripper','striptease','stripteaser','strip dancer','pole dancer'],
'striptease' : ['stripper','striptease','stripteaser','strip dancer','pole dancer'],
'stripteaser' : ['stripper','striptease','stripteaser','strip dancer','pole dancer'],

'stripclub' : ['stripclub', 'stripper club','striptease club','stripteaser club','strip dancer club','pole dancer club'],


'day' : ['day','night','times','hours'],

'face' : ['face','mouth'],

'rapid' : ['rapid', 'very quick','fast', 'agile','brisk'],

'resist' : ['resist','prevent','refuse','curb','contend'],
'prevent' : ['resist','prevent','refuse','curb','contend'],
'refuse' : ['resist','prevent','refuse','curb','contend'],
'curb' : ['resist','prevent','refuse','curb','contend'],
'contend' : ['resist','prevent','refuse','curb','contend'],

'yank' : ['yank','jerk'],
'yanks' : ['yanks','jerks'],

'couch' : ['couch','sofa','lounge','love seat'],
'sofa' : ['couch','sofa','lounge','love seat'],
'lounge' : ['couch','sofa','lounge','love seat'],

'pawn' : ['pawn','pawn shop','payday loan','loan shop'],

'multiple' : ['multiple','many','numerous','various','several'],
'numerous' : ['multiple','many','numerous','various','several'],
'various' : ['multiple','many','numerous','various','several'],
'several' : ['multiple','many','numerous','various','several'],

'dorm' : ['dorm','school','college'],

'ready' : ['ready','prepared','available','waiting'],
'available' : ['ready','prepared','available','waiting'],
'waiting' : ['ready','prepared','available','waiting'],
'prepared' : ['ready','prepared','available','waiting'],

'prep' : ['ready','prepare','provide','prep','make-ready'],
'preps' : ['prepares','provides','preps'],
'prepare' : ['ready','prepare','provide','prep','make-ready'],
'prepares' : ['prepares','provides','preps'],



'shake' : ['shake','jerk','rock','wobble','swing'],
'wobble' : ['shake','jerk','rock','wobble','swing'],
'swing' : ['shake','jerk','rock','wobble','swing'],

'teach' : ['teach','instruct','educate','demonstrate','show'],
'teaches' : ['teaches','instructs','educates','demonstrates','shows'],

'instruct' : ['teach','instruct','educate','demonstrate','show'],
'instructs' : ['teaches','instructs','educate','demonstrates','shows'],

'educate' : ['teach','instruct','educate','demonstrate','show'],
'educates' : ['teaches','instructs','educates','demonstrates','shows'],

'demonstrate' : ['teach','instruct','educate','demonstrate','show'],
'demonstrates' : ['teaches','instructs','educate','demonstrates','shows'],

'red' : ['red','pink','rosey','rose', 'cherry','crimson','ruby','scarlet','maroon'],
'pink' : ['red','pink','rosey','rose', 'cherry','crimson','ruby','scarlet','maroon'],
'rosey' : ['red','pink','rosey','rose', 'cherry','crimson','ruby','scarlet','maroon'],
'rose' : ['red','pink','rosey','rose', 'cherry','crimson','ruby','scarlet','maroon'],
'cherry' : ['red','pink','rosey','rose', 'cherry','crimson','ruby','scarlet','maroon'],
'crimson' : ['red','pink','rosey','rose', 'cherry','crimson','ruby','scarlet','maroon'],
'ruby' : ['red','pink','rosey','rose', 'cherry','crimson','ruby','scarlet','maroon'],
'scarlet' : ['red','pink','rosey','rose', 'cherry','crimson','ruby','scarlet','maroon'],
'maroon' : ['red','pink','rosey','rose', 'cherry','crimson','ruby','scarlet','maroon'],



'america' : ['america','americana','american'],
'americana' : ['america','americana','american'],
'american' : ['america','americana','american'],

'jiggly' : ['jiggly','wobbly','saggy','flabby','pudgy','jumpy','dangly', 'jingly', 'huggy', 'blingly','floppy'],
'wobbly' : ['jiggly','wobbly','saggy','flabby','pudgy','jumpy','dangly', 'jingly', 'huggy', 'blingly','floppy'],
'saggy' : ['jiggly','wobbly','saggy','flabby','pudgy','jumpy','dangly', 'jingly', 'huggy', 'blingly','floppy'],
'flabby' : ['jiggly','wobbly','saggy','flabby','pudgy','jumpy','dangly', 'jingly', 'huggy', 'blingly','floppy'],
'pudgy' : ['jiggly','wobbly','saggy','flabby','pudgy','jumpy','dangly', 'jingly', 'huggy', 'blingly','floppy'],
'jumpy' : ['jiggly','wobbly','saggy','flabby','pudgy','jumpy','dangly', 'jingly', 'huggy', 'blingly','floppy'],
'dangly' : ['jiggly','wobbly','saggy','flabby','pudgy','jumpy','dangly', 'jingly', 'huggy', 'blingly','floppy'],
'jingly' : ['jiggly','wobbly','saggy','flabby','pudgy','jumpy','dangly', 'jingly', 'huggy', 'blingly','floppy'],
'huggy' : ['jiggly','wobbly','saggy','flabby','pudgy','jumpy','dangly', 'jingly', 'huggy', 'blingly','floppy'],
'blingly' : ['jiggly','wobbly','saggy','flabby','pudgy','jumpy','dangly', 'jingly', 'huggy', 'blingly','floppy'],
'floppy' : ['jiggly','wobbly','saggy','flabby','pudgy','jumpy','dangly', 'jingly', 'huggy', 'blingly','floppy'],

'nympho' : ['Nympho','nymphomaniac','nymph','sexpot','sex addict','floozy','floozie','cumslut','seductress','sexaholic','oversexed'],
'nymphomaniac' : ['Nympho','nymphomaniac','nymph','sexpot','sex addict','floozy','floozie','cumslut','seductress','sexaholic','oversexed'],
'nymph' : ['Nympho','nymphomaniac','nymph','sexpot','sex addict','floozy','floozie','cumslut','seductress','sexaholic','oversexed'],
'sexpot' : ['Nympho','nymphomaniac','nymph','sexpot','sex addict','floozy','floozie','cumslut','seductress','sexaholic','oversexed'],
'sexaholic' : ['Nympho','nymphomaniac','nymph','sexpot','sex addict','floozy','floozie','cumslut','seductress','sexaholic','oversexed'],
'oversexed' : ['Nympho','nymphomaniac','nymph','sexpot','sex addict','floozy','floozie','cumslut','seductress','sexaholic','oversexed'],
'cumslut' : ['Nympho','nymphomaniac','nymph','sexpot','sex addict','floozy','floozie','cumslut','seductress','sexaholic','oversexed'],
'floozy' : ['Nympho','nymphomaniac','nymph','sexpot','sex addict','floozy','floozie','cumslut','seductress','sexaholic','oversexed'],
'floozie' : ['Nympho','nymphomaniac','nymph','sexpot','sex addict','floozy','floozie','cumslut','seductress','sexaholic','oversexed'],
 


'spycam' : ['spycam','hidden cam','stalker','peeper','voyeur'],

'bhabhi' : ['bhabhi','bhabi','devar bhabhi','desi aunty','indian milf', 'desi mature','indian aunty'],
'bhabi' : ['bhabhi','bhabi','devar bhabhi','desi aunty','indian milf', 'desi mature','indian aunty'],

'master' : ['master','dominator'],

'park' : ['park','garden','lawn','yard','backyard','orchard','playground'],
'garden' : ['park','garden','lawn','yard','backyard','orchard','playground'],
'lawn' : ['park','garden','lawn','yard','backyard','orchard','playground'],
'yard' : ['park','garden','lawn','yard','backyard','orchard','playground'],
'backyard' : ['park','garden','lawn','yard','backyard','orchard','playground'],
'orchard' : ['park','garden','lawn','yard','backyard','orchard','playground'],
'playground' : ['park','garden','lawn','yard','backyard','orchard','playground'],

'parade' : ['parade','march','procession','carnival'],
'procession' : ['parade','march','procession','carnival'],
'carnival' : ['parade','march','procession','carnival'],


'tan' : ['tan','sunbathing','sunburn','tanning'],

'dance' : ['dance','dancing','dance move','dancing move','strip dance'],
'dancer' : ['dancer','dancing','strip dancer','striper'],

'femdom' : ['femdom','female domination','mistress domination','dominating female','dominating mistress','female humiliation','mistress humiliation'],

'nun' : ['nun','church sister', 'catholic nun','religious nun','christian nun','prostitute nun'],
'nuns' : ['nuns','church sisters', 'catholic nuns','religious nuns','christian nuns','prostitute nuns'],

'foreplay' : ['foreplay','kissing arousal','kissing stimulation','love-making','outercourse','touching/kissing/licking','touching kissing'],

'uncle' : ['uncle','relative','father\'s friend','aged man','elderly guy'],

'aka' : ['aka',', also known as','alias',', codename:',', screen name:',', street name:',', named:','nickname'],
'alias' : ['aka',', also known as', 'alias',', codename:',', screen name:',', street name:',', named:','nickname'],
'nickname' : ['aka',', also known as', 'alias',', codename:',', screen name:',', street name:',', named:','nickname'],
'codename' : ['aka',', also known as', 'alias',', codename:',', screen name:',', street name:',', named:','nickname'],



'star' : ['star','superstar','heroine','starring','sensation'],
'superstar' : ['star','superstar','heroine','starring','sensation'],
'heroine' : ['star','superstar','heroine','starring','sensation'],
'sensation' : ['star','superstar','heroine','starring','sensation'],


'craving' : ['craving','thirsting','desiring','longing','lusting','wanting','urging','wishing'],
'thirsting' : ['craving','thirsting','desiring','longing','lusting','wanting','urging','wishing'],
'desiring' : ['craving','thirsting','desiring','longing','lusting','wanting','urging','wishing'],
'longing' : ['craving','thirsting','desiring','longing','lusting','wanting','urging','wishing'],
'lusting' : ['craving','thirsting','desiring','longing','lusting','wanting','urging','wishing'],
'wanting' : ['craving','thirsting','desiring','longing','lusting','wanting','urging','wishing'],
'wishing' : ['craving','thirsting','desiring','longing','lusting','wanting','urging','wishing'],

'one' : ['one','a','the','single','lone','one special',''], # /*'' = remove*/

'who' : [', she',', the one','who'],

'treat' : ['treat','gift','delight','thrill','feast'],

'babydoll' : ['babydoll','satin nightgowns','sexy nightgowns','sexy nightdress'],

'witch' : ['fucking sexy','witch','fucking whore','horny bitch','bitch'],

'wicked' : ['wicked','evil','nasty','naughty','devil','demon'],
'demon' : ['wicked','evil','nasty','naughty','devil','demon'],
'evil' : ['wicked','evil','nasty','naughty','devil','demon'],
'devil' : ['wicked','evil','nasty','naughty','devil','demon'],
'devils' : ['wicked','evil','nasty','naughty','devil','demon'],

'angel' : ['angel','darling','sweetheart','honey','elf'],

'revenge' : ['revenge','repayment','attack','blowback','retaliation','vengeance'],
'repayment' : ['revenge','repayment','attack','blowback','retaliation','vengeance'],
'attack' : ['revenge','repayment','attack','blowback','retaliation','vengeance'],
'blowback' : ['revenge','repayment','attack','blowback','retaliation','vengeance'],
'retaliation' : ['revenge','repayment','attack','blowback','retaliation','vengeance'],
'vengeance' : ['revenge','repayment','attack','blowback','retaliation','vengeance'],

'sybian' : ['sybian','Sybian saddle','masturbation device','sybian device','sybian stimulation','vibrating sybian','sybian vibrator','sybian sex toy'],

'wedding' : ['wedding','marriage','marriage ceremony','wedding ceremony','marrying'],
'marriage' : ['wedding','marriage','marriage ceremony','wedding ceremony','marrying'],

'before' : ['before','ahead of','prior to','till','leads to','leading to','led to'],

'bride' : ['bride','fiancée','fiancé','newly-wed'],

'boat' : ['boat','vessel','yacht','sailing'],
'vessel' : ['boat','vessel','yacht','sailing'],
'yacht' : ['boat','vessel','yacht','sailing'],

'heels' : ['heels','stiletto','stiletto heels','high heeled shoes'],

'fishnet' : ['fishnet','fishnet tights','fishnet dress','fishnet hosiery'],

'tied' : ['tied','bound','knotted','fastened','strapped'],

'pain' : ['pain','agony','torture','physical suffering','distress'],
'agony' : ['pain','agony','torture','physical suffering','distress'],
'distress' : ['pain','agony','torture','physical suffering','distress'],
'ache' : ['pain','agony','torture','physical suffering','distress'],

'painful' : ['painful','distressing','uncomfortable','unpleasent','agonizing','extreme'],
'distressing' : ['painful','distressing','uncomfortable','unpleasent','agonizing','extreme'],
'uncomfortable' : ['painful','distressing','uncomfortable','unpleasent','agonizing','extreme'],
'unpleasent' : ['painful','distressing','uncomfortable','unpleasent','agonizing','extreme'],
'agonizing' : ['painful','distressing','uncomfortable','unpleasent','agonizing','extreme'],

'hospital' : ['hospital','clinic','nursing home','nursing ward','hospital ward'],

'punk' : ['punk','hoodlum','desperado','thief','bandit','robber'],
'punker' : ['punk','hoodlum','desperado','thief','bandit','robber'],
'hoodlum' : ['punk','hoodlum','desperado','thief','bandit','robber'],
'desperado' : ['punk','hoodlum','desperado','thief','bandit','robber'],
'thief' : ['punk','hoodlum','desperado','thief','bandit','robber'],
'bandit' : ['punk','hoodlum','desperado','thief','bandit','robber'],
'bandit' : ['punk','hoodlum','desperado','thief','bandit','robber'],


    
'squirt' : ['squirt','squirt','squirt','squirting','spurt','gush','spirt'],
'squirting' : ['squirt','squirting','squirting','squirting','spurt','gush','spirt'],
'spurt' : ['squirt','squirting','spurt','gush','spirt'],
'gush' : ['squirt','squirting','spurt','gush','spirt'],
'spirt' : ['squirt','squirting','spurt','gush','spirt'],

'standing' : ['standing','upright','vertical','stand-up'],
'upright' : ['standing','upright','vertical','stand-up'],
'vertical' : ['standing','upright','vertical','stand-up'],

'wanking' : ['wanking','roaming','strolling','moving around'],

'sell' : ['sell','trade','deal','exchange','offer'],
'sells' : ['sells','trades','deals','exchanges','offers'],
'selling' : ['selling','trading','dealing','exchanging','offering'],

'offer' : ['present','offer'],
'offers' : ['provides','presents','suggests','proposes','offering','offers'],
'offering' : ['providing','presenting','suggesting','proposing','offering'],

'join' : ['join','meet','unite','attend'],
'joined' : ['joined','mate','united','attended'],
'joins' : ['joins','meets','unites','attends'],
'joining' : ['joininig','meeting','uniting','attending'],

'pizza' : ['pizza','italian pizza','pizza pie','cheese pizza'],

'jail' : ['jail','prison','imprison','lock up','jailhouse'],
'prison' : ['jail','prison','imprison','lock up','jailhouse'],
'imprison' : ['jail','prison','imprison','lock up','jailhouse'],

'pimp' : ['pimp','whore master','prostitute agent','whoremonger','hustler'],
'hustler' : ['pimp','whore master','prostitute agent','whoremonger','hustler'],

'hug' : ['hug','embrace','cuddling'],
'embrace' : ['hug','embrace','cuddling'],
'cuddling' : ['hug','embrace','cuddling'],

'behind' : ['behind', 'doggy-fucks','doggy-style','doggystyle','backside','rear end','the back side','the back'],

'flat' : ['flat','leveled','bland','plane','stale'],

'tall' : ['tall','lofty','tall figured','lofy figured',''],

'' : ['','','','',''],
'' : ['','','','',''],
'' : ['','','','',''],
'' : ['','','','',''],
'' : ['','','','',''],
# /*few replacement end*/
'some' : ['some','few','a few',' a little'],

'nasty' : ['nasty','dirty','filthy'],
'dirty' : ['nasty','dirty','filthy'],
'filthy' : ['nasty','dirty','filthy'],
'white' : ['white','pale','white skinned','english','euro','american'],
'pale' : ['white','pale','white skinned','english','euro','american'],
'two' : ['two','a pair of','a couple of'],
'2' : ['II','two'],
'ii' : ['2','two'],
'iii' : ['3','three'],
'3' : ['three'],
'three' : ['3'],
'4' : ['iv','four'],

'part' : ['scene','video','clip','vid','part'], 
'pt' : ['part','scene','video','clip', 'vol', 'Ep'], 
'ep' : ['part','scene','video','clip', 'vol', 'Ep'], 
'vol' : ['part','scene','video','clip', 'pt', 'Ep','disk'], 
'disk' : ['part','scene','video','clip', 'pt', 'Ep','disk','vol','volume','CD'], 
# /*'cd' : ['part','scene','video','clip', 'pt', 'Ep','disk','vol','volume'], */
'scene' : ['video','clip','scene'],
'video' : ['scene','clip','video'],
'videos' : ['scenes','clips','videos'],
'vid' : ['video','scene','clip'],
'tape' : ['video','scene','clip','tape','recording','film'],
'flix' : ['video','scene','clip','flix'],
'clip' : ['scene','video','vid','clip'],
'clips' : ['scenes','videos','vids','clips'],
'mp4' : ['video','scene','clip','part I', 'Vol 1','vid'],
'.mp4' : ['video','scene','clip','part I', 'Vol 1','vid'],

'let' : ['allow','approve','grant','let'],
'allow' : ['allow','approve','grant','let'],
'allows' : ['allow','approve','grant','let'],
'approve' : ['allow','approve','grant','let'],
'grant' : ['allow','approve','grant','let'],

'rich' : ['successful','wealthy','prosperous','millionaire','business','businessman','lucky','affluent','fortunate'],
'business' : ['successful','wealthy','prosperous','millionaire','rich','businessman','lucky','affluent','fortunate'],
'businessman' : ['successful','wealthy','prosperous','millionaire','rich','lucky','affluent','fortunate'],
'lucky' : ['successful','wealthy','prosperous','millionaire','rich','lucky','businessman','affluent','fortunate'],
'poor' : ['unlucky','needy','broke','meager','unfortunate','stupid'],
'stupid' : ['unlucky','needy','broke','meager','unfortunate','stupid'],
'broke' : ['unlucky','needy','broke','meager','unfortunate','stupid'],

'vary' : ['super', 'true','truly','real','realy','very much', 'very very','too'],
# //'super' : ['vary', 'true','truly','real','realy','very much', 'very very'],
'super' : ['best','great','perfect','top','super','A-1','true','truly','real', 'realy', ''], #//adjective, may remove some time
'too' : ['too','very','super'],
'true' : ['real','actual','pure','genuine'],
'real' : ['true','actual','pure','genuine'],
'top' : ['best','finest','excellent','top-notch','super','#1'],
'song' : ['music video','music','video song','dance video', 'mujra song'],
'nude' : ['naked','bare','without clothes','undressed','unclothed', 'stripped','clothless'],
'naked' : ['nude','bare','without clothes','undressed','unclothed', 'stripped','clothless'],

'completely' : ['fully','absolutely','totally','entirely'],
'fully' : ['completely','absolutely','totally','entirely'],
'absolutely' : ['completely','fully','totally','entirely'],
'totally' : ['completely','fully','absolutely','entirely'],
'entirely' : ['completely','fully','totally','absolutely'],

'vintage' : ['retro'],
'retro' : ['vintage'],

'cinema' : ['full movie', 'full video'],
'movie' : ['cinema', 'full video'],

'film' : ['record', 'capture', 'shoot'],
'films' : ['records', 'captures','shoots'],
'filmed' : ['recorded', 'captured', 'shought'],
'filming' : ['recording', 'capturing', 'shooting'],
'recording' : ['recording', 'capturing', 'shooting'],
'shooting' : ['recording', 'capturing', 'shooting'],

'prostitute' : ['prostitute', 'hooker', 'sex worker', 'escort'],
'prostitutes' : ['prostitutes', 'hookers', 'sex workers', 'escorts'],
'hooker' : ['prostitute', 'hooker', 'sex worker', 'escort'],
'hookers' : ['prostitutes', 'hookers', 'sex workers', 'escorts'],
'escort' : ['prostitute', 'hooker', 'sex worker', 'escort'],
'escorts' : ['prostitutes', 'hookers', 'sex workers', 'escorts'],

'webcam' : ['cam','camera','cams','live cam','live stream','skype'],
'cam' : ['webcam','camera','cams','live cam','live stream', 'skype'],
'camera' : ['webcam','cam','cams','live cam','live stream', 'skype'],
'camshow' : ['live show','live streaming','live cam','cam show'],
'live' : ['camshow','live streaming','live cam'],
'camaster' : ['camshow','live','live streaming','live stream','tiktoker','onlyfans'],

'skype' : ['skype','whatsapp','wechat','zoom call'],
'whatsapp' : ['skype','whatsapp','wechat','zoom call'],
'wechat' : ['skype','whatsapp','wechat','zoom call'],

'hd' : ['4k','1080p','720p','high def','high definition','High Quality','HQ'],
'hq' : ['4k','1080p','720p','high def','high definition','High Quality','HQ'],
'4k' : ['HD','1080p','720p','high def','high definition','High Quality','HQ'],
'1080p' : ['4k','HD','720p','high def','high definition','High Quality','HQ'],
'720p' : ['4k','1080p','HD','high def','high definition','High Quality','HQ'],

'69' : ['69 pose'],
'legs' : ['long legs'],

'audio' : ['sound','voice','conversation'],
'sound' : ['audio','voice','conversation'],
'voice' : ['audio','sound','conversation'],
'conversation' : ['audio','voice','sound','talk'],

'bhai' : ['brother','step brother','step bro'],
'bahan' : ['sister','step sister','step sis','sisy','sissy'],
'bahen' : ['sister','step sister','step sis','sisy','sissy'],
# /*'chudai''saree','sari','Randi','raand',CHOOT,*/

# /*bbw*/
'bbw' : ['pawg','plumpers',
        'chubby woman', 'chubby girl', 'chubby milf', 'chubby wife', 'chubby housewife', 'chubby babe',
        'curvy woman', 'curvy girl', 'curvy milf', 'curvy wife', 'curvy housewife', 'curvy babe',
        'fat woman', 'fat girl', 'fat milf', 'fat wife', 'fat housewife', 'fat babe',
        'fatty woman', 'fatty girl', 'fatty milf', 'fatty wife', 'fatty housewife', 'fatty babe',
        'busty woman', 'busty girl', 'busty milf', 'busty wife', 'busty housewife', 'busty babe',
        'plumper woman', 'plumper girl', 'plumper milf', 'plumper wife', 'plumper housewife', 'plumper babe',
        'thick woman', 'thick girl', 'thick milf', 'thick wife', 'thick housewife', 'thick babe','plump girl',
        'Plump princess', 'Real curvy women', 'Plus size princess','Well nourished woman','sexy full-figure','buxom lady' , 'rubenesque',		
		],

# /*bust*/
'busty' : ['bbw','pawg','plumpers',
        'chubby tits', 'chubby tity', 'chubby titty', 'chubby boob', 'chubby boobs', 'chubby boobies',
        'big tits', 'big tity', 'big titty', 'big boob', 'big boobs', 'big boobies',
        'fat tits', 'fat tity', 'fat titty', 'fat boob', 'fat boobs', 'fat boobies',
        'fatty tits', 'fatty tity', 'fatty titty', 'fatty boob', 'fatty boobs', 'fatty boobies',
		'thick tits', 'thick tity', 'thick titty', 'thick boob', 'thick boobs', 'thick boobies',
        'chubby', 'curvy', 'fat', 'fatty', 'plumper', 'thick'],

# /*pawg*/
'pawg' : ['bbw','chubby','curvy','fat','fatty','busty', 'curves', 'plumper', 'plumpers','thick','plump',
        'chubby woman', 'chubby girl', 'chubby milf', 'chubby wife', 'chubby housewife', 'chubby babe',
        'curvy woman', 'curvy girl', 'curvy milf', 'curvy wife', 'curvy housewife', 'curvy babe',
        'fat woman', 'fat girl', 'fat milf', 'fat wife', 'fat housewife', 'fat babe',
        'fatty woman', 'fatty girl', 'fatty milf', 'fatty wife', 'fatty housewife', 'fatty babe',
        'busty woman', 'busty girl', 'busty milf', 'busty wife', 'busty housewife', 'busty babe',
        'plumper woman', 'plumper girl', 'plumper milf', 'plumper wife', 'plumper housewife', 'plumper babe',
        'thick woman', 'thick girl', 'thick milf', 'thick wife', 'thick housewife', 'thick babe'],

'bbbw' : ['bbw','pawg','chubby','curvy','fat','fatty','busty', 'curves', 'plumper', 'plumpers','thick', 'ssbbw', 'sbbw'],
'chubby' : ['pawg','bbw','curvy','fat','fatty','busty', 'curves', 'plumper', 'plumpers','thick','plump','chunky'],
'voluptuous' : ['pawg','bbw','curvy','fat','fatty','busty', 'curves', 'plumper', 'plumpers','thick','plump','chunky'],
'curvy' : ['pawg','chubby','bbw','fat','fatty','busty', 'curves', 'plumper', 'plumpers','thick','plump','chunky'],
'chunky' : ['pawg','chubby','bbw','fat','fatty','busty', 'curves', 'plumper', 'plumpers','thick','plump'],
'fat' : ['chubby','curvy','bbw','fatty','busty', 'curves', 'plumper', 'plumpers','thick','plump','chunky'],
'fatty' : ['chubby','curvy','fat','bbw','busty', 'curves', 'plumper', 'plumpers','thick','plump','chunky'],
'plump' : ['chubby','curvy','fat','bbw','busty', 'curves', 'plumper', 'plumpers','thick','chunky'],

'curves' : ['chubby','curvy','fat','fatty','busty', 'bbw', 'plumper', 'plumpers','thick'],
'plumper' : ['chubby','curvy','fat','fatty','busty', 'curves', 'bbw', 'plumpers','thick'],
'plumpers' : ['chubby','curvy','fat','fatty','busty', 'curves', 'plumper', 'bbw','thick'],
'thick' : ['chubby','curvy','fat','fatty','busty', 'curves', 'plumper', 'plumpers','bbw'],
'thicc' : ['chubby','curvy','fat','fatty','busty', 'curves', 'plumper', 'plumpers','bbw'],
'ssbbw' : ['bbbw','pawg','chubby','curvy','fat','fatty','busty', 'curves', 'plumper', 'plumpers','thick', 'bbw', 'sbbw'],
'sbbw' : ['bbbw','pawg','chubby','curvy','fat','fatty','busty', 'curves', 'plumper', 'plumpers','thick', 'ssbbw', 'bbw'],

'money' : ['cash','dollar','hard cash'],
'cash' : ['money','dollar','hard cash'],

'hotel' : ['motel', 'resort', 'hostel', 'inn', 'house', 'lodge', 'hangout', 'holiday spot', 'hideaway', 'hideout', 'bnb', 'airbnb'],
'motel' : ['hotel', 'resort', 'hostel', 'inn', 'house', 'lodge', 'hangout', 'holiday spot', 'hideaway', 'hideout', 'bnb', 'airbnb'],
'hostel' : ['hotel', 'resort', 'motel', 'inn', 'house', 'lodge', 'hangout', 'holiday spot', 'hideaway', 'hideout', 'bnb', 'airbnb'],
'resort' : ['hotel', 'hostel', 'motel', 'inn', 'house', 'lodge', 'hangout', 'holiday spot', 'hideaway', 'hideout', 'bnb', 'airbnb'],

'latina' : ['latino', 'cuban', 'colombiana','colombian','spanish','mexican','mexicana', 'latin'],
'latin' : ['latino', 'cuban', 'colombiana','colombian','spanish','mexican','mexicana', 'latin'],
'latino' : ['latina', 'cuban', 'colombiana','colombian','spanish','mexican','mexicana', 'latin'],
'cuban' : ['latina', 'latino', 'colombiana','colombian','spanish','mexican','mexicana', 'latin'],
'colombiana' : ['latina', 'cuban', 'latino','colombian','spanish','mexican','mexicana', 'latin'],
'colombian' : ['latina', 'cuban', 'latino','colombiana','spanish','mexican','mexicana', 'latin'],
'spanish' : ['latina', 'cuban', 'latino','colombiana','spanish','mexican','mexicana', 'latin'],
'mexican' : ['latina', 'cuban', 'latino','colombiana','spanish','mexican','mexicana', 'latin'],
'mexicana' : ['latina', 'cuban', 'latino','colombiana','spanish','mexican','mexicana', 'latin'],
'portuguese' : ['latina', 'cuban', 'latino','colombiana','spanish','mexican','mexicana', 'latin'],
'argentina' : ['latina', 'cuban', 'latino','colombiana','spanish','mexican','mexicana', 'latin'],


'indian' : ['indian','desi','arab','hindi','bangla','bengali','muslim','hindu', 'punjabi','pakistani','mallu','tamil','turkish','bangladeshi','persian','egyptian','lebanese','sri lankan','sri lanka','iranian','afghan','syrian','paki','arabian'],
'desi' : ['indian','desi','arab','hindi','bangla','bengali','muslim','hindu', 'punjabi','pakistani','mallu','tamil','turkish','bangladeshi','persian','egyptian','lebanese','sri lankan','sri lanka','iranian','afghan','syrian','paki','arabian'],
'arab' : ['indian','desi','arab','hindi','bangla','bengali','muslim','hindu', 'punjabi','pakistani','mallu','tamil','turkish','bangladeshi','persian','egyptian','lebanese','sri lankan','sri lanka','iranian','afghan','syrian','paki','arabian'],
'arabic' : ['indian','desi','arab','hindi','bangla','bengali','muslim','hindu', 'punjabi','pakistani','mallu','tamil','turkish','bangladeshi','persian','egyptian','lebanese','sri lankan','sri lanka','iranian','afghan','syrian','paki','arabian'],
'arabian' : ['indian','desi','arab','hindi','bangla','bengali','muslim','hindu', 'punjabi','pakistani','mallu','tamil','turkish','bangladeshi','persian','egyptian','lebanese','sri lankan','sri lanka','iranian','afghan','syrian','paki','arabian'],
'hindi' : ['indian','desi','arab','hindi','bangla','bengali','muslim','hindu', 'punjabi','pakistani','mallu','tamil','turkish','bangladeshi','persian','egyptian','lebanese','sri lankan','sri lanka','iranian','afghan','syrian','paki','arabian'],
'bangla' : ['indian','desi','arab','hindi','bangla','bengali','muslim','hindu', 'punjabi','pakistani','mallu','tamil','turkish','bangladeshi','persian','egyptian','lebanese','sri lankan','sri lanka','iranian','afghan','syrian','paki','arabian'],
'bengali' : ['indian','desi','arab','hindi','bangla','bengali','muslim','hindu', 'punjabi','pakistani','mallu','tamil','turkish','bangladeshi','persian','egyptian','lebanese','sri lankan','sri lanka','iranian','afghan','syrian','paki','arabian'],
'bangladeshi' : ['indian','desi','arab','hindi','bangla','bengali','muslim','hindu', 'punjabi','pakistani','mallu','tamil','turkish','bangladeshi','persian','egyptian','lebanese','sri lankan','sri lanka','iranian','afghan','syrian','paki','arabian'],
'muslim' : ['indian','desi','arab','hindi','bangla','bengali','muslim','hindu', 'punjabi','pakistani','mallu','tamil','turkish','bangladeshi','persian','egyptian','lebanese','sri lankan','sri lanka','iranian','afghan','syrian','paki','arabian'],
'hindu' : ['indian','desi','arab','hindi','bangla','bengali','muslim','hindu', 'punjabi','pakistani','mallu','tamil','turkish','bangladeshi','persian','egyptian','lebanese','sri lankan','sri lanka','iranian','afghan','syrian','paki','arabian'],
'punjabi' : ['indian','desi','arab','hindi','bangla','bengali','muslim','hindu', 'punjabi','pakistani','mallu','tamil','turkish','bangladeshi','persian','egyptian','lebanese','sri lankan','sri lanka','iranian','afghan','syrian','paki','arabian'],
'paki' : ['indian','desi','arab','hindi','bangla','bengali','muslim','hindu', 'punjabi','pakistani','mallu','tamil','turkish','bangladeshi','persian','egyptian','lebanese','sri lankan','sri lanka','iranian','afghan','syrian','paki','arabian'],
'pakistani' : ['indian','desi','arab','hindi','bangla','bengali','muslim','hindu', 'punjabi','pakistani','mallu','tamil','turkish','bangladeshi','persian','egyptian','lebanese','sri lankan','sri lanka','iranian','afghan','syrian','paki','arabian'],
'mallu' : ['indian','desi','arab','hindi','bangla','bengali','muslim','hindu', 'punjabi','pakistani','mallu','tamil','turkish','bangladeshi','persian','egyptian','lebanese','sri lankan','sri lanka','iranian','afghan','syrian','paki','arabian'],
'tamil' : ['indian','desi','arab','hindi','bangla','bengali','muslim','hindu', 'punjabi','pakistani','mallu','tamil','turkish','bangladeshi','persian','egyptian','lebanese','sri lankan','sri lanka','iranian','afghan','syrian','paki','arabian'],
'turkish' : ['indian','desi','arab','hindi','bangla','bengali','muslim','hindu', 'punjabi','pakistani','mallu','tamil','turkish','bangladeshi','persian','egyptian','lebanese','sri lankan','sri lanka','iranian','afghan','syrian','paki','arabian'],
'persian' : ['indian','desi','arab','hindi','bangla','bengali','muslim','hindu', 'punjabi','pakistani','mallu','tamil','turkish','bangladeshi','persian','egyptian','lebanese','sri lankan','sri lanka','iranian','afghan','syrian','paki','arabian'],
'egyptian' : ['indian','desi','arab','hindi','bangla','bengali','muslim','hindu', 'punjabi','pakistani','mallu','tamil','turkish','bangladeshi','persian','egyptian','lebanese','sri lankan','sri lanka','iranian','afghan','syrian','paki','arabian'],
'lebanese' : ['indian','desi','arab','hindi','bangla','bengali','muslim','hindu', 'punjabi','pakistani','mallu','tamil','turkish','bangladeshi','persian','egyptian','lebanese','sri lankan','sri lanka','iranian','afghan','syrian','paki','arabian'],
# /*'sri lankan' : ['indian','desi','arab','hindi','bangla','bengali','muslim','hindu', 'punjabi','pakistani','mallu','tamil','turkish','bangladeshi','persian','egyptian','lebanese','sri lankan','sri lanka','iranian','afghan','syrian','paki','arabian'],*/
# /*'sri lanka' : ['indian','desi','arab','hindi','bangla','bengali','muslim','hindu', 'punjabi','pakistani','mallu','tamil','turkish','bangladeshi','persian','egyptian','lebanese','sri lankan','sri lanka','iranian','afghan','syrian','paki','arabian'],*/
'iranian' : ['indian','desi','arab','hindi','bangla','bengali','muslim','hindu', 'punjabi','pakistani','mallu','tamil','turkish','bangladeshi','persian','egyptian','lebanese','sri lankan','sri lanka','iranian','afghan','syrian','paki','arabian'],
'afghan' : ['indian','desi','arab','hindi','bangla','bengali','muslim','hindu', 'punjabi','pakistani','mallu','tamil','turkish','bangladeshi','persian','egyptian','lebanese','sri lankan','sri lanka','iranian','afghan','syrian','paki','arabian'],
'syrian' : ['indian','desi','arab','hindi','bangla','bengali','muslim','hindu', 'punjabi','pakistani','mallu','tamil','turkish','bangladeshi','persian','egyptian','lebanese','sri lankan','sri lanka','iranian','afghan','syrian','paki','arabian'],
'malay' : ['indian','desi','arab','hindi','bangla','bengali','muslim','hindu', 'punjabi','pakistani','mallu','tamil','turkish','bangladeshi','persian','egyptian','lebanese','sri lankan','sri lanka','iranian','afghan','syrian','paki','arabian'],
'israeli' : ['indian','desi','arab','hindi','bangla','bengali','muslim','hindu', 'punjabi','pakistani','mallu','tamil','turkish','bangladeshi','persian','egyptian','lebanese','sri lankan','sri lanka','iranian','afghan','syrian','paki','arabian'],
'turkey' : ['indian','desi','arab','hindi','bangla','bengali','muslim','hindu', 'punjabi','pakistani','mallu','tamil','turkish','bangladeshi','persian','egyptian','lebanese','sri lankan','sri lanka','iranian','afghan','syrian','paki','arabian'],
'turkish' : ['indian','desi','arab','hindi','bangla','bengali','muslim','hindu', 'punjabi','pakistani','mallu','tamil','turkish','bangladeshi','persian','egyptian','lebanese','sri lankan','sri lanka','iranian','afghan','syrian','paki','arabian'],
'turk' : ['indian','desi','arab','hindi','bangla','bengali','muslim','hindu', 'punjabi','pakistani','mallu','tamil','turkish','bangladeshi','persian','egyptian','lebanese','sri lankan','sri lanka','iranian','afghan','syrian','paki','arabian'],


'milf' : ['milf','aunty','aunt','mature','mom','mommy','mother','step mom','step-mom','step mother','cougar','mature woman'],
'milfs' : ['milfs','aunties','aunts','matures','moms','mommies','mothers','step moms','step-moms','step mothers','cougars','mature women'],

'aunty' : ['milf','aunty','aunt','mature','mom','mommy','mother','step mom','step-mom','step mother','mother in-law','cougar','mature woman'],
'auntie' : ['milf','aunty','aunt','mature','mom','mommy','mother','step mom','step-mom','step mother','mother in-law','cougar','mature'],
'aunt' : ['milf','aunty','aunt','mature mom','step mommy','step mom','step-mom','step mother','mother in-law','cougar milf','mature woman'],

'cuckold' : ['cuckold','hotwife','cheating wife','cheater wife', 'cuck'],
'cuckolds' : ['cuckolds','hotwives','cheating wives','cheater wives', 'cucks'],
'cuck' : ['cuckold','hotwife','cheating wife','cheater wife', 'cuck'],
'cucks' : ['cuckolds','hotwives','cheating wives','cheater wives', 'cucks'],

'hotwife' : ['cuckold','hotwife','cheating wife','cheater wife', 'cuck'],
'hotwives' : ['cuckolds','hotwives','cheating wives','cheater wives', 'cucks'],

'cougar' : ['milf','aunty','aunt','mature','mom','mommy','mother','step mom','step-mom','step mother','cougar','mature woman'],

'perverted' : ['pervert', 'perverted','perv','pervs','pervy', 'perverts'],
'perv' : ['pervert', 'perverted','perv','pervs','pervy', 'perverts'],
'pervy' : ['pervert', 'perverted','perv','pervs','pervy', 'perverts'],
'pervert' : ['pervert', 'perverted','perv','pervs','pervy', 'perverts'],

'perverts' : ['pervert', 'perverted','perv','pervs','pervy', 'perverts'],
'pervs' : ['pervert', 'perverted','perv','pervs','pervy', 'perverts'],

'mature' : ['milf','aunty','aunt','mature','cougar','mature woman','experienced woman','aged woman'],


'girl' : ['girl','young woman','lady','young lady', 'chick', 'teenager', 'youngster'],
'girls' : ['girls','young women','ladies','young ladies', 'chicks', 'teenagers', 'youngsters'],

'gal' : ['girl','young woman','lady','young lady', 'chick', 'teenager', 'youngster'],
'gals' : ['girls','young women','ladies','young ladies', 'chicks', 'teenagers', 'youngsters'],


'chick' : ['girl','young woman','lady','young lady', 'chick', 'teenager', 'youngster'],
'chicks' : ['girls','young women','ladies','young ladies', 'chicks', 'teenagers', 'youngsters'],

'lady' : ['girl','woman','wife','wifey','housewife','house wife','lady','chick'],
'ladies' : ['girls','women','wives', 'housewives','house wives','ladies','chicks'],



'woman' : ['girl','woman','wife','wifey', 'hotwife','housewife','house wife','lady','chick'],
'women' : ['girls','women','wives', 'hotwives','housewives','house wives','ladies','chicks'],

'wife' : ['girl','woman','wife','wifey', 'housewife','house wife','lady','spouse'],
'wives' : ['girls','women','wives', 'housewives','house wives','ladies','spouses'],

'wifey' : ['girl','woman','wife','wifey', 'hotwife','housewife','house wife','lady','spouse'],

'housewife' : ['girl','woman','wife','wifey', 'hotwife','housewife','house wife','lady','spouse'],
'housewives' : ['girls','women','wives', 'hotwives','housewives','house wives','ladies','chicks'],

'female' : ['girl','woman','wife','wifey', 'hotwife','housewife','house wife','female','lady','chick'],
'females' : ['girls','women','wives','wifey', 'hotwives','housewives','house wives','ladies','chicks'],


'animation' : ['animation','animated', 'anime','manga','futanari', 'cartoon','hentai','3d','rule34','overwatch', 'ahegao','ecchi'],
'animated' : ['animation','animated', 'anime','manga','futanari', 'cartoon','hentai','3d','rule34','overwatch', 'ahegao','ecchi'],
'anime' : ['animation','animated', 'anime','manga','futanari', 'cartoon','hentai','3d','rule34','overwatch', 'ahegao','ecchi'],
'manga' : ['animation','animated', 'anime','manga','futanari', 'cartoon','hentai','3d','rule34','overwatch', 'ahegao','ecchi'],
'futanari' : ['animation','animated', 'anime','manga','futanari', 'cartoon','hentai','3d','rule34','overwatch', 'ahegao','ecchi'],
'cartoon' : ['animation','animated', 'anime','manga','futanari', 'cartoon','hentai','3d','rule34','overwatch', 'ahegao','ecchi'],
'toon' : ['animation','animated', 'anime','manga','futanari', 'cartoon','hentai','3d','rule34','overwatch', 'ahegao','ecchi'],
'hentai' : ['animation','animated', 'anime','manga','futanari', 'cartoon','hentai','3d','rule34','overwatch', 'ahegao','ecchi'],
'3d' : ['animation','animated', 'anime','manga','futanari', 'cartoon','hentai','3d','rule34','overwatch', 'ahegao','ecchi'],
'rule34' : ['animation','animated', 'anime','manga','futanari', 'cartoon','hentai','3d','rule34','overwatch', 'ahegao','ecchi'],
'overwatch' : ['animation','animated', 'anime','manga','futanari', 'cartoon','hentai','3d','rule34','overwatch', 'ahegao','ecchi'],
'ahegao' : ['animation','animated', 'anime','manga','futanari', 'cartoon','hentai','3d','rule34','overwatch', 'ahegao','ecchi'],
'ecchi' : ['animation','animated', 'anime','manga','futanari', 'cartoon','hentai','3d','rule34','overwatch', 'ahegao','ecchi'],


'hardcore' : ['hardcore','rough','intense','extreme','wild'],
'rough' : ['hardcore','rough','intense','extreme','wild','hard','insane'],
'intense' : ['hardcore','rough','intense','extreme','wild','hard','insane'],
'extreme' : ['hardcore','rough','intense','extreme','forced','wild','hard','insane'],
'forced' : ['hardcore','rough','intense','extreme','forced','wild','hard'],
'wild' : ['hardcore','rough','intense','extreme','wild','hard','insane'],
'insane' : ['insane','hardcore','rough','intense','extreme','wild','hard'],

# /*very difficult word*/
# /*'hard' : ['well','rough','solid','heavy','wild','hard','strong','tough'],*/
# /*'hard' : ['solid','heavy','hard','strong','tough'],*/
'hard' : ['hard'],

'brutal' : ['brutal', 'cruel', 'rude', 'forced', 'hardcore', 'rough','intense','extreme','wild'],
'cruel' : ['brutal', 'cruel', 'rude', 'forced', 'hardcore', 'rough','intense','extreme','wild'],
'rude' : ['brutal', 'cruel', 'rude', 'forced', 'hardcore', 'rough','intense','extreme','wild'],


'trans' : ['trans','femboyes','t-girls','tgirls', 'ladyboyes','shemales','trannies','ts','transsexual'],
'transsexual' : ['trans','femboy','t-girl','tgirl', 'ladyboy','shemale','ts','tranny','transsexual'],
'transexual' : ['trans','femboy','t-girl','tgirl', 'ladyboy','shemale','ts','tranny','transsexual'],
'transsexuals' : ['trans','femboys','t-girls','tgirls', 'ladyboys','shemales','ts','trannies','transsexuals'],
'femboy' : ['trans','femboy','t-girl','tgirl', 'ladyboy','shemale','ts','tranny','transsexual'],
'femboys' : ['trans','femboys','t-girls','tgirls', 'ladyboys','shemales','ts','trannies','transsexuals'],
't-girl' : ['trans','femboy','t-girl','tgirl', 'ladyboy','shemale','ts','tranny','transsexual'],
'tgirl' : ['trans','femboy','t-girl','tgirl', 'ladyboy','shemale','ts','tranny','transsexual'],
'tgirls' : ['trans','femboys','t-girls','tgirls', 'ladyboys','shemales','ts','trannies','transsexuals'],
'ladyboy' : ['trans','femboy','t-girl','tgirl', 'ladyboy','shemale','ts','tranny','transsexual'],
'ladyboys' : ['trans','femboys','t-girls','tgirls', 'ladyboys','shemales','ts','trannies','transsexuals'],
'shemale' : ['trans','femboy','t-girl','tgirl', 'ladyboy','shemale','ts','tranny','transsexual'],
'shemales' : ['trans','femboys','t-girls','tgirls', 'ladyboys','shemales','ts','trannies','transsexuals'],
'trannies' : ['trans','femboyes','t-girls','tgirls', 'ladyboyes','shemales','trannies','ts','transsexuals'],
'tranny' : ['trans','femboy','t-girl','tgirl', 'ladyboy','shemale','ts','tranny','transsexual'],
'ts' : ['trans','femboy','t-girl','tgirl', 'ladyboy','shemale', 'ts','tranny','transsexual'],
'shebabe' : ['trans babe','femboy beauty','babe t-girl','tgirl babe', 'sexy ladyboy','hottie shemale', 'ts babe','tranny babe','transsexual babe','shebabe'],


					  
'british' : ['british','english','uk','german','french','russian','usa','american','european','italian','australian','euro','canadian','swedish','romanian','hungarian','polish','ukrainian','dutch','irish','new zealand','greek','scottish','norwegian','swiss','danish','austrian'],
'brit' : ['british','english','uk','german','french','russian','usa','american','european','italian','australian','euro','canadian','swedish','romanian','hungarian','polish','ukrainian','dutch','irish','new zealand','greek','scottish','norwegian','swiss','danish','austrian'],
'english' : ['british','english','uk','german','french','russian','usa','american','european','italian','australian','euro','canadian','swedish','romanian','hungarian','polish','ukrainian','dutch','irish','new zealand','greek','scottish','norwegian','swiss','danish','austrian'],
'uk' : ['british','english','uk','german','french','russian','usa','american','european','italian','australian','euro','canadian','swedish','romanian','hungarian','polish','ukrainian','dutch','irish','new zealand','greek','scottish','norwegian','swiss','danish','austrian'],
'german' : ['british','english','uk','german','french','russian','usa','american','european','italian','australian','euro','canadian','swedish','romanian','hungarian','polish','ukrainian','dutch','irish','new zealand','greek','scottish','norwegian','swiss','danish','austrian'],
'french' : ['british','english','uk','german','french','russian','usa','american','european','italian','australian','euro','canadian','swedish','romanian','hungarian','polish','ukrainian','dutch','irish','new zealand','greek','scottish','norwegian','swiss','danish','austrian'],
'russian' : ['british','english','uk','german','french','russian','usa','american','european','italian','australian','euro','canadian','swedish','romanian','hungarian','polish','ukrainian','dutch','irish','new zealand','greek','scottish','norwegian','swiss','danish'],
'rus' : ['british','english','uk','german','french','russian','usa','american','european','italian','australian','euro','canadian','swedish','romanian','hungarian','polish','ukrainian','dutch','irish','new zealand','greek','scottish','norwegian','swiss','danish'],
'usa' : ['british','english','uk','german','french','russian','usa','american','european','italian','australian','euro','canadian','swedish','romanian','hungarian','polish','ukrainian','dutch','irish','new zealand','greek','scottish','norwegian','swiss','danish','austrian'],
'american' : ['british','english','uk','german','french','russian','usa','american','european','italian','australian','euro','canadian','swedish','romanian','hungarian','polish','ukrainian','dutch','irish','new zealand','greek','scottish','norwegian','swiss','danish','austrian'],
'european' : ['british','english','uk','german','french','russian','usa','american','european','italian','australian','euro','canadian','swedish','romanian','hungarian','polish','ukrainian','dutch','irish','new zealand','greek','scottish','norwegian','swiss','danish','austrian'],
'italian' : ['british','english','uk','german','french','russian','usa','american','european','italian','australian','euro','canadian','swedish','romanian','hungarian','polish','ukrainian','dutch','irish','new zealand','greek','scottish','norwegian','swiss','danish','austrian'],
'australian' : ['british','english','uk','german','french','russian','usa','american','european','italian','australian','euro','canadian','swedish','romanian','hungarian','polish','ukrainian','dutch','irish','new zealand','greek','scottish','norwegian','swiss','danish','austrian'],
'euro' : ['british','english','uk','german','french','russian','usa','american','european','italian','australian','euro','canadian','swedish','romanian','hungarian','polish','ukrainian','dutch','irish','new zealand','greek','scottish','norwegian','swiss','danish','austrian'],
'canadian' : ['british','english','uk','german','french','russian','usa','american','european','italian','australian','euro','canadian','swedish','romanian','hungarian','polish','ukrainian','dutch','irish','new zealand','greek','scottish','norwegian','swiss','danish','austrian'],
'swedish' : ['british','english','uk','german','french','russian','usa','american','european','italian','australian','euro','canadian','swedish','romanian','hungarian','polish','ukrainian','dutch','irish','new zealand','greek','scottish','norwegian','swiss','danish','austrian'],
'romanian' : ['british','english','uk','german','french','russian','usa','american','european','italian','australian','euro','canadian','swedish','romanian','hungarian','polish','ukrainian','dutch','irish','new zealand','greek','scottish','norwegian','swiss','danish','austrian'],
'hungarian' : ['british','english','uk','german','french','russian','usa','american','european','italian','australian','euro','canadian','swedish','romanian','hungarian','polish','ukrainian','dutch','irish','new zealand','greek','scottish','norwegian','swiss','danish','austrian'],
'polish' : ['british','english','uk','german','french','russian','usa','american','european','italian','australian','euro','canadian','swedish','romanian','hungarian','polish','ukrainian','dutch','irish','new zealand','greek','scottish','norwegian','swiss','danish','austrian'],
'ukrainian' : ['british','english','uk','german','french','russian','usa','american','european','italian','australian','euro','canadian','swedish','romanian','hungarian','polish','ukrainian','dutch','irish','new zealand','greek','scottish','norwegian','swiss','danish','austrian'],
'dutch' : ['british','english','uk','german','french','russian','usa','american','european','italian','australian','euro','canadian','swedish','romanian','hungarian','polish','ukrainian','dutch','irish','new zealand','greek','scottish','norwegian','swiss','danish','austrian'],
'irish' : ['british','english','uk','german','french','russian','usa','american','european','italian','australian','euro','canadian','swedish','romanian','hungarian','polish','ukrainian','dutch','irish','new zealand','greek','scottish','norwegian','swiss','danish','austrian'],
'greek' : ['british','english','uk','german','french','russian','usa','american','european','italian','australian','euro','canadian','swedish','romanian','hungarian','polish','ukrainian','dutch','irish','new zealand','greek','scottish','norwegian','swiss','danish','austrian'],
'scottish' : ['british','english','uk','german','french','russian','usa','american','european','italian','australian','euro','canadian','swedish','romanian','hungarian','polish','ukrainian','dutch','irish','new zealand','greek','scottish','norwegian','swiss','danish','austrian'],
'norwegian' : ['british','english','uk','german','french','russian','usa','american','european','italian','australian','euro','canadian','swedish','romanian','hungarian','polish','ukrainian','dutch','irish','new zealand','greek','scottish','norwegian','swiss','danish','austrian'],
'swiss' : ['british','english','uk','german','french','russian','usa','american','european','italian','australian','euro','canadian','swedish','romanian','hungarian','polish','ukrainian','dutch','irish','new zealand','greek','scottish','norwegian','swiss','danish','austrian'],
'danish' : ['british','english','uk','german','french','russian','usa','american','european','italian','australian','euro','canadian','swedish','romanian','hungarian','polish','ukrainian','dutch','irish','new zealand','greek','scottish','norwegian','swiss','danish','austrian'],
'austrian' : ['british','english','uk','german','french','russian','usa','american','european','italian','australian','euro','canadian','swedish','romanian','hungarian','polish','ukrainian','dutch','irish','new zealand','greek','scottish','norwegian','swiss','danish','austrian'],
'dominican' : ['british','english','uk','german','french','russian','usa','american','european','italian','australian','euro','canadian','swedish','romanian','hungarian','polish','ukrainian','dutch','irish','new zealand','greek','scottish','norwegian','swiss','danish','austrian'],
'bulgarian' : ['british','english','uk','german','french','russian','usa','american','european','italian','australian','euro','canadian','swedish','romanian','hungarian','polish','ukrainian','dutch','irish','new zealand','greek','scottish','norwegian','swiss','danish','austrian'],
'essex' : ['british','english','uk','german','french','russian','usa','american','european','italian','australian','euro','canadian','swedish','romanian','hungarian','polish','ukrainian','dutch','irish','new zealand','greek','scottish','norwegian','swiss','danish','austrian'],
'venezuelan' : ['venezuelan','british','english','uk','german','french','russian','usa','american','european','italian','australian','euro','canadian','swedish','romanian','hungarian','polish','ukrainian','dutch','irish','new zealand','greek','scottish','norwegian','swiss','danish','austrian'],


'doctor' : ['doctor', 'physician', 'gyno', 'gynecologist', 'medico', 'medic', 'therapist','doc'],
'physician' : ['doctor', 'physician', 'gyno', 'gynecologist', 'medico', 'medic', 'therapist','doc'],
'gynecologist' : ['doctor', 'physician', 'gyno', 'gynecologist', 'medico', 'medic', 'therapist','doc'],
'medico' : ['doctor', 'physician', 'gyno', 'gynecologist', 'medico', 'medic', 'therapist','doc'],
'therapist' : ['doctor', 'physician', 'gyno', 'gynecologist', 'medico', 'medic', 'therapist','doc'],
'gyno' : ['doctor', 'physician', 'gyno', 'gynecologist', 'medico', 'medic', 'therapist','doc'],
'doc' : ['doctor', 'physician', 'gyno', 'gynecologist', 'medico', 'medic', 'therapist','doc'],
'dr' : ['doctor', 'physician', 'gyno', 'gynecologist', 'medico', 'medic', 'therapist','doc'],

'doctors' : ['doctors', 'physicians', 'gynos', 'gynecologists', 'medicos', 'medics', 'therapists','docs'],
'docs' : ['doctors', 'physicians', 'gynos', 'gynecologists', 'medicos', 'medics', 'therapists','docs'],
'gynos' : ['doctors', 'physicians', 'gynos', 'gynecologists', 'medicos', 'medics', 'therapists','docs'],

'medical' : ['gyno', 'gynecologist'],
'nurse' : ['hospital nurse', 'hospital medic', 'female attendent', 'hospital attendent','paramedic'],
'paramedic' : ['hospital nurse', 'hospital medic', 'female attendent', 'hospital attendent','paramedic'],

'patient' : ['patient', 'sick patient'],

'exam' : ['examination','test','checkup','inspection','exam','check','autopsy','biopsy'],
'examination' : ['examination','test','checkup','inspection','exam','check','autopsy','biopsy'],
'checkup' : ['examination','test','checkup','inspection','exam','check','autopsy','biopsy'],
'inspection' : ['examination','test','checkup','inspection','exam','check','autopsy','biopsy'],
'autopsy' : ['examination','test','checkup','inspection','exam','check','autopsy','biopsy'],
'biopsy' : ['examination','test','checkup','inspection','exam','check','autopsy','biopsy'],

'check' : ['examination','test','checkup','inspection','exam','check'],

       


'vacation' : ['vacation','holiday','getaway','weekend'],
'holiday' : ['vacation','holiday','getaway','weekend'],
'weekend' : ['vacation','holiday','getaway','weekend'],


'want' : ['want','need','wish'],
'wants' : ['needs','wishes','wants'],
'wanted' : ['needed','wished','wanted'],
'need' : ['need','want','wish','require'],
'needs' : ['needs','wants','wishes','requirements'],
'wish' : ['wish','need','want','dream'],
'wishes' : ['needs','wants','requirements','dreams'],

'wanna' : ['wanna','want to','wish to','deam to','need to'],

 
'hijab' : ['hijab','muslim','arab','niqab','burka', 'headscarf', 'scarf'],
'muslim' : ['hijab girl','muslim','arab woman', 'niqab girl','burka woman', 'headscarf woman', 'scarf girl'],


# /*public, outdoor, outdoors, outside, open , street, road, roadside, , street side*/
'outdoor' : ['outdoor','outdoors','public','open', 'outside','street','road','roadside','street side'],
'outside' : ['outdoor','outdoors','in public','in open', 'outside','on roadside','on street side'],
'street' : ['outdoor','outdoors','public','open', 'outside','street','road','roadside','street side'],
'road' : ['outdoor','outdoors','public','open', 'outside','street','road','roadside','street side'],
'roadside' : ['outdoor','outdoors','public','open', 'outside','street','road','roadside','street side'],
'outdoors' : ['outdoor','outdoors','public','open', 'outside','street','road','roadside','street side'],
'streets' : ['outdoor','outdoors','public','open', 'outside','street','road','roadside','street side'],
'public' : ['outdoor','outdoors','public','open', 'outside','street','road','roadside','street side'],

# /*gay, faggot homosexual homo homophile same-sex, */
'gay' : ['gay','faggot','homosexual','homo','homophile','same-sex','twink'],
'gays' : ['gays','faggots','homosexuals','homos','homophiles','same-sexs','twinks'],
'faggot' : ['gay','faggot','homosexual','homo','homophile','same-sex','twink'],
'faggots' : ['gays','faggots','homosexuals','homos','homophiles','same-sexs','twinks'],
'twink' : ['gay','faggot','homosexual','homo','homophile','same-sex','twink'],
'twinks' : ['gays','faggots','homosexuals','homos','homophiles','same-sexs','twinks'],
'homosexual' : ['gay','faggot','homosexual','homo','homophile','same-sex'],
'homosexuals' : ['gays','faggots','homosexuals','homos','homophiles','same-sexs','twinks'],
'homophile' : ['gay','faggot','homosexual','homo','homophile','same-sex'],
'homophiles' : ['gays','faggots','homosexuals','homos','homophiles','same-sexs','twinks'],
'homo' : ['gay','faggot','homosexual','homo','homophile','same-sex'],
'homos' : ['gays','faggots','homosexuals','homos','homophiles','same-sexs','twinks'],

# /*'amateur','vouyer','homemade','home made','hobbyist', 'scandal', 'sex tape',  'mms', 'leaked tape', 'homevideo'*/
'amateur' : ['amateur','voyeur','homemade','home made','hobbyist', 'homevideo','peeping tom', 'peeper'],
'amateurs' : ['amateurs','voyeurs','hobbyists','peeping toms', 'peepers'],

'voyeur' : ['amateur','voyeur','stalker','bystander','spycam', 'hidden cam', 'scandal', 'onlooker','peeping tom', 'peeper'],
'voyeurs' : ['amateurs','voyeurs','stalkers','bystanders','onlookers','peeping toms', 'peepers'],

'homemade' : ['amateur','voyeur','homemade','home made','hobbyist', 'scandal', 'sex tape',  'mms', 'leaked tape', 'homevideo','peeping tom', 'peeper'],
'hobbyist' : ['amateur','voyeur','homemade','home made','hobbyist', 'scandal', 'sex tape',  'mms', 'leaked tape', 'homevideo','peeping tom', 'peeper'],
'scandal' : ['amateur','voyeur','homemade','home made','hobbyist', 'scandal', 'sex tape',  'mms', 'leaked tape', 'homevideo','peeping tom', 'peeper'],
'sextape' : ['amateur','voyeur','homemade','home made','hobbyist', 'scandal', 'sex tape',  'mms', 'leaked tape', 'homevideo','peeping tom', 'peeper'],
'mms' : ['amateur','voyeur','homemade','home made','hobbyist', 'scandal', 'sex tape',  'mms', 'leaked tape', 'homevideo','peeping tom', 'peeper'],
'homevideo' : ['amateur','voyeur','homemade','home made','hobbyist', 'scandal', 'sex tape',  'mms', 'leaked tape', 'homevideo','peeping tom', 'peeper'],

# /*pornstar, sexbomb, bombshell, firecracker , superstar, actress, model, goddess */
'pornstar' : ['pornstar','sexbomb','bombshell','firecracker','superstar','actress','model','goddess'],
'pornstars' : ['pornstars','sexbombs','bombshells','firecrackers','superstars','actresses','models','goddess'],
'sexbomb' : ['pornstar','sexbomb','bombshell','firecracker','superstar','actress','model','goddess'],
'bombshell' : ['pornstar','sexbomb','bombshell','firecracker','superstar','actress','model','goddess'],
'firecracker' : ['pornstar','sexbomb','bombshell','firecracker','superstar','actress','model','goddess'],
'superstar' : ['pornstar','sexbomb','bombshell','firecracker','superstar','actress','model','goddess'],
'actress' : ['pornstar','sexbomb','bombshell','firecracker','superstar','actress','model','goddess'],
'model' : ['pornstar','sexbomb','bombshell','firecracker','superstar','actress','model','goddess'],
'goddess' : ['pornstar','sexbomb','bombshell','firecracker','superstar','actress','model','goddess'],

# /*babe, babes*/
'babe' :  ['babe', 'pornstar', 'sexbomb', 'bombshell', 'firecracker' , 'superstar', 'actress', 'model', 'super beauty','diva'],
'diva' :  ['babe', 'pornstar', 'sexbomb', 'bombshell', 'firecracker' , 'superstar', 'actress', 'model', 'super beauty','diva'],
'beauty' :  ['babe', 'sexbomb', 'bombshell', 'firecracker' , 'model', 'super beauty'],
'babes' : ['babes', 'pornstars', 'sexbombs', 'bombshells', 'firecrackers', 'superstars', 'actresses', 'models', 'super beauties','divas'],

# /*titjob titfuck, tit fuck, titty fuck, TittyFuck, boobjob, boob job, melon fuck, breast fuck, breast job*/
'titjob' : ['titjob','titfuck','tit fuck','titty fuck','tittyFuck','boobjob','boob job','melon fuck','breast fuck','breast job'],
'titfuck' : ['titjob','titfuck','tit fuck','titty fuck','tittyFuck','boobjob','boob job','melon fuck','breast fuck','breast job'],


'' : ['','','','',''],
'' : ['','','','',''],
'' : ['','','','',''],
'' : ['','','','',''],
'' : ['','','','',''],
'' : ['','','','',''],
'' : ['','','','',''],
'' : ['','','','',''],


}
