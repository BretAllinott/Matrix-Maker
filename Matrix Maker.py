#These are game strategies. In format [[Columns],[Rows]]
headers=[[
    "A",
    "B",
    "C",
    "D",
    "E",
],
    ["A",
     "B",
     "C",
     "D",
]]
#Players of the game. In format [Player 1, Player 2]
players=["John","Joe"]

cols=len(headers[0])
rows=len(headers[1])
yheight=(rows-1)//2
header=r"""
\documentclass{article}
\usepackage{array}
\usepackage{float}

\begin{document}
\begin{table}[H]
\setlength{\extrarowheight}{2pt}
"""
ending=r"""
\end{tabular}
\end{table}
\end{document}
"""

print(header)
print("\\begin{tabular}{cc|"+ "|".join(["c"]*cols)+"|}")


print("& \\multicolumn{1}{c}{}",end=" ")
print("& \\multicolumn{"+str(cols)+"}{c}{"+players[1]+"}",end=" ")
print("\\\\")

print(" &\\multicolumn{1}{c}{}")
for col in headers[0]:
    print("& \\multicolumn{1}{c}{$"+col+"$}",end=" ")
print("\\\\" + "\\cline{"+str(3)+"-"+str(cols+2)+"}")

for row in range(rows):
    text = None
    if row is yheight:
        text = players[0]
    else:
        text = len(players[0]) * " "
    print(text +" ",end="")
    print("& ${}$ ".format(headers[1][row]),end="")
    for col in range(cols):
        print("& $ , $ ".format(row,col),end="")
    print("\\\\" + " \\cline{"+str((3))+"-"+str(cols+2)+"}")
print(ending)