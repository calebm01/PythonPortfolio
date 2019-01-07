import time

#Hangman Game
#Eric Broadbent
#11/26/18
#The classic game of Hangman. The computer picks a random word and the player wrong to guess it
# one letter at a time. If the player can't guess the word in time, the stick figure gets hanged.

HANGMAN = (
"""
 ------
 |   |
 |
 |
 |
 |
 |
 |
 |
 |
 |
 |

 -------------
 """
,

"""
 ------
 |   |
 |   O
 |
 |
 |
 |
 |
 |
 |
 |
 |

 -------------

 """
,

"""
 ------
 |   |
 |   O
 |   |
 |
 |
 |
 |
 |
 |
 |
 |

 -------------

 """
,
"""
------
 |   |
 |   O
 |   |/
 |
 |
 |
 |
 |
 |
 |
 |

 -------------
 """
,
"""
------
 |   |
 |   O
 |  \\|/
 |
 |
 |
 |
 |
 |
 |
 |

 -------------
 """
,
"""
------
 |   |
 |   O
 |  \|/
 |    \\
 |
 |
 |
 |
 |
 |
 |

 -------------

 """
,
"""
------
 |   |
 |   O
 |  \\|/
 |  / \\
 |
 |
 |
 |
 |
 |
 |

 -------------
 """)

MAX_WRONG = len(HANGMAN)-1

for i in range(len(HANGMAN)):
    print(HANGMAN[i])
    time.sleep(1)
