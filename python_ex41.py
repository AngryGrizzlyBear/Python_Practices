import random
from urllib import urlopen
import sys

WORD_URL = "http://learncodethehardway.org/words.txt"
WORDS = []

PHRASES = {
    "class %%%(%%%):":
        "Make a class named %%% that is -a %%%.",
    "class %%%(object):\n\tdef _int_(self, ***)" :
     "class %%% has-a _init_ that takes self and *** oaraneters.",
    "class %%%%(object): \n\tdef ***(self, @@@)":
     "class %%%% has -a function named *** that takes self and @@@ parameters.",
    "*** = %%%()":
    "Set *** to an instance of class %%%",
    "***.***(@@@)":
      "From *** get the *** function, and call it wit hparameters self, @@@.",
    "***.*** = '***":
      "From *** get the *** attribute and set it to '***'."
}

# Do they want to drill phases first
PRHASE_FIRST = False
if len(sys.argv) == 2 and sys.argv[1] == "english":
    PHRASE_FIRST = True

