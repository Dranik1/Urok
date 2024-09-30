bibliothek={
    "termcolor2",
    "wikipedia"

}

'''from termcolor2 import c
print(c("Some text").blue.on_white.underline)'''


import wikipedia
wikipedia.set_lang("lv")
print(wikipedia.summary('Riga'))
