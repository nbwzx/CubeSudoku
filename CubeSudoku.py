import numpy as np
import random


def transformation1(transformation1_a, transformation1_b, transformation1_c, transformation1_d):
    c[transformation1_a][transformation1_b] = a[transformation1_a][transformation1_b]
    a[transformation1_a][transformation1_b] = c[transformation1_c][transformation1_d]


def transformation2(transformation2_a, transformation2_b, transformation2_c, transformation2_d):
    c[transformation2_a][transformation2_b] = a[transformation2_a][transformation2_b]
    a[transformation2_a][transformation2_b] = a[transformation2_c][transformation2_d]


def f():
    for i in range(9):
        c[4][i] = a[4][i]
    a[4][0] = a[4][6]
    a[4][6] = a[4][8]
    a[4][8] = a[4][2]
    a[4][2] = c[4][0]
    a[4][1] = a[4][3]
    a[4][3] = a[4][7]
    a[4][7] = a[4][5]
    a[4][5] = c[4][1]
    for i in range(1, 4):
        transformation2(3 - 1, 3 * i - 1, 2 - 1, i - 1)
    for i in range(1, 4):
        transformation2(2 - 1, i - 1, 4 - 1, 10 - 3 * i - 1)
    for i in range(1, 4):
        transformation2(4 - 1, 3 * i - 2 - 1, 1 - 1, 6 + i - 1)
    for i in range(1, 4):
        transformation1(1 - 1, 6 + i - 1, 3 - 1, 12 - 3 * i - 1)


def x():
    for i in range(9):
        c[2][i] = a[2][i]
        c[3][i] = a[3][i]
    a[2][0] = a[2][2]
    a[2][2] = a[2][8]
    a[2][8] = a[2][6]
    a[2][6] = c[2][0]
    a[2][1] = a[2][5]
    a[2][5] = a[2][7]
    a[2][7] = a[2][3]
    a[2][3] = c[2][1]
    a[3][0] = a[3][6]
    a[3][6] = a[3][8]
    a[3][8] = a[3][2]
    a[3][2] = c[3][0]
    a[3][1] = a[3][3]
    a[3][3] = a[3][7]
    a[3][7] = a[3][5]
    a[3][5] = c[3][1]

    for i in range(1, 10):
        transformation2(6 - 1, i - 1, 1 - 1, 10 - i - 1)
    for i in range(1, 10):
        transformation1(2 - 1, i - 1, 6 - 1, 10 - i - 1)
    for i in range(1, 10):
        transformation1(5 - 1, i - 1, 2 - 1, i - 1)
    for i in range(1, 10):
        transformation1(1 - 1, i - 1, 5 - 1, i - 1)


def y():
    for i in range(9):
        c[1][i] = a[1][i]
        c[0][i] = a[0][i]
    a[1][0] = a[1][2]
    a[1][2] = a[1][8]
    a[1][8] = a[1][6]
    a[1][6] = c[1][0]
    a[1][1] = a[1][5]
    a[1][5] = a[1][7]
    a[1][7] = a[1][3]
    a[1][3] = c[1][1]
    a[0][0] = a[0][6]
    a[0][6] = a[0][8]
    a[0][8] = a[0][2]
    a[0][2] = c[0][0]
    a[0][1] = a[0][3]
    a[0][3] = a[0][7]
    a[0][7] = a[0][5]
    a[0][5] = c[0][1]
    for i in range(1, 10):
        transformation2(6 - 1, i - 1, 3 - 1, i - 1)
    for i in range(1, 10):
        transformation2(3 - 1, i - 1, 5 - 1, i - 1)
    for i in range(1, 10):
        transformation2(5 - 1, i - 1, 4 - 1, i - 1)
    for i in range(1, 10):
        a[4 - 1][i - 1] = c[6 - 1][i - 1]


def z():
    x()
    y()
    x()
    x()
    x()


def l():
    y()
    y()
    y()
    f()
    y()


def u():
    x()
    x()
    x()
    f()
    x()


def b():
    x()
    x()
    f()
    x()
    x()


def r():
    y()
    f()
    y()
    y()
    y()


def d():
    x()
    f()
    x()
    x()
    x()


def di():
    d()
    d()
    d()


def li():
    l()
    l()
    l()


def ri():
    r()
    r()
    r()


def fi():
    f()
    f()
    f()


def ui():
    u()
    u()
    u()


def bi():
    b()
    b()
    b()


def d2():
    d()
    d()


def l2():
    l()
    l()


def r2():
    r()
    r()


def f2():
    f()
    f()


def u2():
    u()
    u()


def b2():
    b()
    b()


def xr():
    l()
    x()


def xf():
    b()
    z()


def xu():
    d()
    y()


def xd():
    u()
    y()
    y()
    y()


def xl():
    r()
    x()
    x()
    x()


def xb():
    f()
    z()
    z()
    z()


def x2():
    x()
    x()


def y2():
    y()
    y()


def z2():
    z()
    z()


def xi():
    x()
    x()
    x()


def yi():
    y()
    y()
    y()


def zi():
    z()
    z()
    z()


def m():
    r()
    li()
    x()
    x()
    x()


def m2():
    r2()
    l2()
    x2()


def mi():
    x()
    l()
    r()
    r()
    r()


def s():
    f()
    f()
    f()
    b()
    z()


def s2():
    f2()
    b2()
    z2()


def si():
    z()
    z()
    z()
    b()
    b()
    b()
    f()


def e():
    u()
    d()
    d()
    d()
    y()
    y()
    y()


def e2():
    u2()
    d2()
    y2()


def ei():
    y()
    d()
    u()
    u()
    u()


def xr2():
    xr()
    xr()


def xf2():
    xf()
    xf()


def xu2():
    xu()
    xu()


def xd2():
    xd()
    xd()


def xl2():
    xl()
    xl()


def xb2():
    xb()
    xb()


def xri():
    xr()
    xr()
    xr()


def xfi():
    xf()
    xf()
    xf()


def xui():
    xu()
    xu()
    xu()


def xdi():
    xd()
    xd()
    xd()


def xli():
    xl()
    xl()
    xl()


def xbi():
    xb()
    xb()
    xb()


def operate(operate_char):
    if operate_char == "R":
        r()
    elif operate_char == "L":
        l()
    elif operate_char == "F":
        f()
    elif operate_char == "B":
        b()
    elif operate_char == "U":
        u()
    elif operate_char == "D":
        d()
    elif operate_char == "R2":
        r2()
    elif operate_char == "L2":
        l2()
    elif operate_char == "F2":
        f2()
    elif operate_char == "B2":
        b2()
    elif operate_char == "U2":
        u2()
    elif operate_char == "D2":
        d2()
    elif operate_char == "R'":
        ri()
    elif operate_char == "L'":
        li()
    elif operate_char == "F'":
        fi()
    elif operate_char == "B'":
        bi()
    elif operate_char == "U'":
        ui()
    elif operate_char == "D'":
        di()
    elif operate_char == "x":
        x()
    elif operate_char == "x2":
        x2()
    elif operate_char == "x'":
        xi()
    elif operate_char == "y":
        y()
    elif operate_char == "y2":
        y2()
    elif operate_char == "y'":
        yi()
    elif operate_char == "z":
        z()
    elif operate_char == "z2":
        z2()
    elif operate_char == "z'":
        zi()
    elif operate_char == "r":
        xr()
    elif operate_char == "r2":
        xr2()
    elif operate_char == "r'":
        xri()
    elif operate_char == "f":
        xf()
    elif operate_char == "f2":
        xf2()
    elif operate_char == "f'":
        xfi()
    elif operate_char == "u":
        xu()
    elif operate_char == "u2":
        xu2()
    elif operate_char == "u'":
        xui()
    elif operate_char == "d":
        xd()
    elif operate_char == "d2":
        xd2()
    elif operate_char == "d'":
        xdi()
    elif operate_char == "l":
        xl()
    elif operate_char == "l2":
        xl2()
    elif operate_char == "l'":
        xli()
    elif operate_char == "b":
        xb()
    elif operate_char == "b2":
        xb2()
    elif operate_char == "b'":
        xbi()
    elif operate_char == "S":
        s()
    elif operate_char == "S2":
        s2()
    elif operate_char == "S'":
        si()
    elif operate_char == "M":
        m()
    elif operate_char == "M2":
        m2()
    elif operate_char == "M'":
        mi()
    elif operate_char == "E":
        e()
    elif operate_char == "E2":
        e2()
    elif operate_char == "E'":
        ei()
    elif operate_char == "Rw":
        xr()
    elif operate_char == "Rw2":
        xr2()
    elif operate_char == "Rw'":
        xri()
    elif operate_char == "Fw":
        xf()
    elif operate_char == "Fw2":
        xf2()
    elif operate_char == "Fw'":
        xfi()
    elif operate_char == "Uw":
        xu()
    elif operate_char == "Uw2":
        xu2()
    elif operate_char == "Uw'":
        xui()
    elif operate_char == "Dw":
        xd()
    elif operate_char == "Dw2":
        xd2()
    elif operate_char == "Dw'":
        xdi()
    elif operate_char == "Lw":
        xl()
    elif operate_char == "Lw2":
        xl2()
    elif operate_char == "Lw'":
        xli()
    elif operate_char == "Bw":
        xb()
    elif operate_char == "Bw2":
        xb2()
    elif operate_char == "Bw'":
        xbi()
        # Other cases: Something wrong happens.


def getGs(s1):
    s1 = s1.replace("'2", "2")
    s1 = s1.replace("2'", "2")
    getGs_out = s1.split(" ")
    return getGs_out


def scramble(s1):
    arr = getGs(s1)
    for i in range(0, len(arr)):
        operate(arr[i])


def solveSudokucube(option, availableLimit):
    global blankNumber
    global availableNumber
    availableNumber = 0

    blank = []
    for i in range(6):
        for j in range(4):
            if board[i][j] == -1:
                blank.append((i, j))
    blankNumber = len(blank)

    def cornerPermutation(list):
        return [list[1], list[2], list[0]]

    def cornerCorrect():
        flip = 0
        flag = 0
        corner = [[0, 4, 2], [0, 3, 4], [0, 2, 5], [0, 5, 3],
                  [1, 2, 4], [1, 4, 3], [1, 5, 2], [1, 3, 5]]
        corfull = [[board[0][2], board[4][0], board[2][1]],
                   [board[0][3], board[3][0], board[4][1]],
                   [board[0][0], board[2][0], board[5][1]],
                   [board[0][1], board[5][0], board[3][1]],
                   [board[1][2], board[5][3], board[2][2]],
                   [board[1][3], board[3][3], board[5][2]],
                   [board[1][0], board[2][3], board[4][2]],
                   [board[1][1], board[4][3], board[3][2]]]
        for i in corfull:
            if -1 not in i:
                if i in corner:
                    flip = flip + 0
                    corner.remove(i)
                elif cornerPermutation(i) in corner:
                    flip = flip + 1
                    corner.remove(cornerPermutation(i))
                elif cornerPermutation(cornerPermutation(i)) in corner:
                    flip = flip + 2
                    corner.remove(cornerPermutation(cornerPermutation(i)))
                else:
                    return False
            else:
                flag = 1
        if flag == 0:
            if flip % 3 == 0:
                return True
            else:
                return False
        return True

    def edgePermutation(list):
        return [list[1], list[0]]

    def edgeCorrect():
        flip = 0
        flag = 0
        edge = [[0, 5], [0, 2], [0, 3], [0, 4], [1, 4], [1, 2],
                [1, 3], [1, 5], [4, 2], [4, 3], [5, 3], [5, 2]]
        edgefull = [[board[0][0], board[5][0]],
                    [board[0][1], board[2][0]],
                    [board[0][2], board[3][0]],
                    [board[0][3], board[4][0]],
                    [board[1][0], board[4][3]],
                    [board[1][1], board[2][3]],
                    [board[1][2], board[3][3]],
                    [board[1][3], board[5][3]],
                    [board[4][1], board[2][2]],
                    [board[4][2], board[3][1]],
                    [board[5][1], board[3][2]],
                    [board[5][2], board[2][1]]]
        for i in edgefull:
            if -1 not in i:
                if i in edge:
                    flip = flip + 0
                    edge.remove(i)
                elif edgePermutation(i) in edge:
                    flip = flip + 1
                    edge.remove(edgePermutation(i))
                else:
                    return False
            else:
                flag = 1
        if flag == 0:
            if flip % 2 == 0:
                return True
            else:
                return False
        return True

    def count(n):
        countNumber = 0
        for i in range(6):
            for j in range(4):
                if board[i][j] == n:
                    countNumber = countNumber + 1
        return countNumber

    def dfsEdge(n):
        global blankNumber
        global availableNumber
        if not (count(0) <= 4 and count(1) <= 4 and count(2) <= 4 and count(3) <= 4 and count(4) <= 4 and count(
                5) <= 4) or edgeCorrect() == False:
            return False
        if n == blankNumber:
            if count(0) == 4 and count(1) == 4 and count(2) == 4 and count(3) == 4 and count(4) == 4 and count(
                    5) == 4 and edgeCorrect():
                availableNumber = availableNumber + 1
                # print(board)
            return True
        for i in range(6):
            locationi, locationj = blank[n]
            board[locationi][locationj] = i
            dfsEdge(n + 1)
            if availableNumber > availableLimit:
                return 0  # pruning
            board[locationi][locationj] = -1

    def dfsCorner(n):
        global blankNumber
        global availableNumber
        if not (count(0) <= 4 and count(1) <= 4 and count(2) <= 4 and count(3) <= 4 and count(4) <= 4 and count(
                5) <= 4) or cornerCorrect() == False:
            return False
        if n == blankNumber:
            if count(0) == 4 and count(1) == 4 and count(2) == 4 and count(3) == 4 and count(4) == 4 and count(
                    5) == 4 and cornerCorrect():
                availableNumber = availableNumber + 1
                # print(board)
            return True
        for i in range(6):
            locationi, locationj = blank[n]
            board[locationi][locationj] = i
            dfsCorner(n + 1)
            if availableNumber > availableLimit:
                return 0  # pruning
            board[locationi][locationj] = -1

    if option == 1:
        dfsCorner(0)
    elif option == 0:
        dfsEdge(0)
    if availableNumber == availableLimit:
        return True
    else:
        return False


def scrambleGenerate(depthMax, depth, last1, last2, str):
    arr1 = ["U", "D", "R", "L", "F", "B", "U2", "D2", "R2",
            "L2", "F2", "B2", "U'", "D'", "R'", "L'", "F'", "B'"]
    arr2 = ["Rw", "Fw", "Rw'", "Fw'"]
    arr3 = ["Uw", "Uw'", "Uw2"]
    if depth == depthMax-2:
        i = random.randint(0, 5)
        if i <= 3:
            str = str+arr2[i]+" "
        depth = depth+1
    if depth == depthMax-1:
        i = random.randint(0, 2)
        str = str+arr3[i]+" "
        depth = depth+1
    if depth == depthMax:
        scramblelist.append(str)
        return
    if depth == 0:
        i = random.randint(0, 17)
        str = str+arr1[i]+" "
        scrambleGenerate(depthMax, depth+1, i, -1, str)
    if depth > 0:
        for _ in range(100000):
            i = random.randint(0, 17)
            if i % 2 == 0 and (not(i % 6 == last1 % 6 or (last2 >= 0 and i % 6 == (last1-1) % 6 and i % 6 == last2 % 6))):
                str = str+arr1[i]+" "
                break
            if i % 2 == 1 and (not(i % 6 == last1 % 6 or (last2 >= 0 and i % 6 == (last1+1) % 6 and i % 6 == last2 % 6))):
                str = str+arr1[i]+" "
                break
        scrambleGenerate(depthMax, depth+1, i, last1, str)


random.seed(1)
scramblelist = []
for scramblelistNum in range(100):
    scrambleGenerate(22, 0, -1, -1, "")

print("""\\documentclass[12pt]{article}
\\def\\filedate{2022/3/22}
\\usepackage{amssymb}
\\usepackage{geometry}  %Set the size of each part of the page
\\usepackage{fancyhdr}  %Set header, margin and footer
\\usepackage{ctex} %for Chinese
\\usepackage{tikz} %Draw
\\usepackage{hyperref}
\\newfontfamily\\newtime{Times New Roman}
%\\CTEXoptions[today=old]
\\topmargin=-0.6in
\\evensidemargin=0in
\\oddsidemargin=0in
\\textwidth=6.5in
\\textheight=9.0in
\\headsep=0.25in
\\linespread{1.3}
%\\pagestyle{fancy}
\\cfoot{\\thepage}
\\renewcommand\\headrulewidth{0.4pt}
\\renewcommand\\footrulewidth{0.4pt}
\\setlength\\parindent{2em}

\\begin{document}
\\begin{titlepage}
\\Large\\centering
\\vspace*{5cm}
\\centerline{\\huge\\bfseries 100 Rubik's Cube Sudoku Puzzles}
\\par\\noindent\\rule{\\textwidth}{4pt}\\\\
\\begin{tikzpicture}
\\shade[bottom color=lightgray,top color=white]
    (0,0) rectangle (\\textwidth, 1.5)
    node[midway] {\\textbf{\\large \\textit{Sudoku for cubers}}};
\\end{tikzpicture}
\\vspace*{2cm}
\\hspace{10cm} Made by \\textbf{Zixing Wang}
\\vfill\\small
\\end{titlepage}

\\centerline{\\textbf{\\Huge{Preface}}}
\\vspace*{1cm}
\\textbf{\\Large{Rules}}

Cube Sudoku is to fill colors in a 3$\\times$3$\\times$3 Rubik's cube with the \\href{https://www.speedsolving.com/wiki/index.php/Western_Color_Scheme}{Western color scheme}.  Once the puzzle is solved, this means that the state is solvable by legal moves (that is, without taking the cube apart again).

\\vspace{0.5cm}
\\textbf{\\Large{Western color scheme}}
\\vspace{0.5cm}
\\\\
\\begin{tikzpicture}[every node/.style={minimum size=0.5cm-\\pgflinewidth, outer sep=0pt},scale=0.5]
    \\node[fill=yellow] at (0.5,5.5) {};
    \\node[fill=yellow] at (1.5,5.5) {};
    \\node[fill=yellow] at (2.5,5.5) {};
    \\node[fill=yellow] at (0.5,4.5) {};
    \\node[fill=yellow] at (1.5,4.5) {};
    \\node[fill=yellow] at (2.5,4.5) {};
    \\node[fill=yellow] at (0.5,3.5) {};
    \\node[fill=yellow] at (1.5,3.5) {};
    \\node[fill=yellow] at (2.5,3.5) {};

    \\node[fill=blue] at (-2.5,2.5) {};
    \\node[fill=blue] at (-1.5,2.5) {};
    \\node[fill=blue] at (-0.5,2.5) {};
    \\node[fill=red] at (0.5,2.5) {};
    \\node[fill=red] at (1.5,2.5) {};
    \\node[fill=red] at (2.5,2.5) {};
    \\node[fill=green] at (3.5,2.5) {};
    \\node[fill=green] at (4.5,2.5) {};
    \\node[fill=green] at (5.5,2.5) {};
    \\node[fill=orange] at (6.5,2.5) {};
    \\node[fill=orange] at (7.5,2.5) {};
    \\node[fill=orange] at (8.5,2.5) {};

    \\node[fill=blue] at (-2.5,1.5) {};
    \\node[fill=blue] at (-1.5,1.5) {};
    \\node[fill=blue] at (-0.5,1.5) {};
    \\node[fill=red] at (0.5,1.5) {};
    \\node[fill=red] at (1.5,1.5) {};
    \\node[fill=red] at (2.5,1.5) {};
    \\node[fill=green] at (3.5,1.5) {};
    \\node[fill=green] at (4.5,1.5) {};
    \\node[fill=green] at (5.5,1.5) {};
    \\node[fill=orange] at (6.5,1.5) {};
    \\node[fill=orange] at (7.5,1.5) {};
    \\node[fill=orange] at (8.5,1.5) {};

    \\node[fill=blue] at (-2.5,0.5) {};
    \\node[fill=blue] at (-1.5,0.5) {};
    \\node[fill=blue] at (-0.5,0.5) {};
    \\node[fill=red] at (0.5,0.5) {};
    \\node[fill=red] at (1.5,0.5) {};
    \\node[fill=red] at (2.5,0.5) {};
    \\node[fill=green] at (3.5,0.5) {};
    \\node[fill=green] at (4.5,0.5) {};
    \\node[fill=green] at (5.5,0.5) {};
    \\node[fill=orange] at (6.5,0.5) {};
    \\node[fill=orange] at (7.5,0.5) {};
    \\node[fill=orange] at (8.5,0.5) {};

    \\node[fill=white] at (0.5,-0.5) {};
    \\node[fill=white] at (1.5,-0.5) {};
    \\node[fill=white] at (2.5,-0.5) {};
    \\node[fill=white] at (0.5,-1.5) {};
    \\node[fill=white] at (1.5,-1.5) {};
    \\node[fill=white] at (2.5,-1.5) {};
    \\node[fill=white] at (0.5,-2.5) {};
    \\node[fill=white] at (1.5,-2.5) {};
    \\node[fill=white] at (2.5,-2.5) {};

    \\draw[step=1cm,color=black, ultra thick] (-3,0) grid (9,3);
    \\draw[step=1cm,color=black, ultra thick] (0,-3) grid (3,0);
    \\draw[step=1cm,color=black, ultra thick] (0,3) grid (3,6);
\\end{tikzpicture}

\\vspace{0.5cm}
\\textbf{\\Large{Solutions}}

Each problem has only one solution. Solution can be accessed after each problem. You can apply the scramble in the solution to your Rubik's cube with yellow on the top and red on the front.

\\vspace{0.5cm}
\\textbf{\\Large{Acknowledgement}}

Thanks to Xi'an Jiao Tong University Rubik's Cube Club, for providing the idea of ``Cube Sudoku".

\\vspace{0.5cm}
\\textbf{\\Large{Github link}}

\\href{https://github.com/nbwzx/CubeSudoku}{https://github.com/nbwzx/CubeSudoku}

\\vspace{0.5cm}
\\textbf{\\Large{Contributors}}

\\href{https://github.com/nbwzx}{Zixing Wang}


\\vspace{0.5cm}
\\textbf{\\Large{License}}

MIT License
\\pagebreak
""")

for problemNumber in range(1, 101):
    a = [[0, 0, 0, 0, 0, 0, 0, 0, 0],
         [1, 1, 1, 1, 1, 1, 1, 1, 1],
         [2, 2, 2, 2, 2, 2, 2, 2, 2],
         [3, 3, 3, 3, 3, 3, 3, 3, 3],
         [4, 4, 4, 4, 4, 4, 4, 4, 4],
         [5, 5, 5, 5, 5, 5, 5, 5, 5]]
    c = [[0, 0, 0, 0, 0, 0, 0, 0, 0],
         [1, 1, 1, 1, 1, 1, 1, 1, 1],
         [2, 2, 2, 2, 2, 2, 2, 2, 2],
         [3, 3, 3, 3, 3, 3, 3, 3, 3],
         [4, 4, 4, 4, 4, 4, 4, 4, 4],
         [5, 5, 5, 5, 5, 5, 5, 5, 5]]
    randomNumber = 0
    if problemNumber <= 20:
        starNumber = "$\\bigstar$"
        deleteCorner = random.randint(2, 4)
        availableCorner = 1
        deleteEdge = random.randint(1, 3)
        availableEdge = 1
    if problemNumber <= 50 and problemNumber > 20:
        starNumber = "$\\bigstar\\bigstar$"
        deleteCorner = random.randint(5, 8)
        availableCorner = 1
        deleteEdge = random.randint(2, 4)
        availableEdge = 1
    if problemNumber <= 70 and problemNumber > 50:
        starNumber = "$\\bigstar\\bigstar\\bigstar$"
        deleteCorner = random.randint(8, 10)
        availableCorner = 1
        deleteEdge = random.randint(3, 5)
        availableEdge = 1
    if problemNumber <= 90 and problemNumber > 70:
        starNumber = "$\\bigstar\\bigstar\\bigstar\\bigstar$"
        randomNumber = random.randint(0, 7)
        if randomNumber > 1:
            deleteCorner = random.randint(10, 12)
            availableCorner = 1
            deleteEdge = random.randint(4, 6)
            availableEdge = 1
        if randomNumber == 0:
            deleteCorner = random.randint(10, 12)
            availableCorner = 2
            deleteEdge = random.randint(4, 6)
            availableEdge = 1
        if randomNumber == 1:
            deleteCorner = random.randint(10, 12)
            availableCorner = 1
            deleteEdge = random.randint(4, 6)
            availableEdge = 2
    if problemNumber <= 100 and problemNumber > 90:
        starNumber = "$\\bigstar\\bigstar\\bigstar\\bigstar\\bigstar$"
        randomNumber = random.randint(0, 3)
        if randomNumber == 0:
            deleteCorner = 14
            availableCorner = 2
            deleteEdge = 6
            availableEdge = 1
        if randomNumber == 1:
            deleteCorner = 13
            availableCorner = 1
            deleteEdge = 6
            availableEdge = 2
        if randomNumber == 2:
            deleteCorner = 13
            availableCorner = 2
            deleteEdge = 6
            availableEdge = 1
        if randomNumber == 3:
            deleteCorner = 13
            availableCorner = 1
            deleteEdge = 6
            availableEdge = 1
    for attempt in range(100000):
        board = [[0, 0, 0, 0],
                 [1, 1, 1, 1],
                 [2, 2, 2, 2],
                 [3, 3, 3, 3],
                 [4, 4, 4, 4],
                 [5, 5, 5, 5]]
        rnd = np.random.choice(24, deleteCorner, replace=False, p=None)
        for i in rnd:
            board[int(i / 4)][i % 4] = -1

        if solveSudokucube(1, availableCorner):
            # print(board)
            for i in range(6):
                for j in range(4):
                    if j == 0 or j == 1:
                        a[i][2 * j] = board[i][j]
                    if j == 2 or j == 3:
                        a[i][2 * j + 2] = board[i][j]
            break

    for attempt in range(100000):
        board = [[0, 0, 0, 0],
                 [1, 1, 1, 1],
                 [2, 2, 2, 2],
                 [3, 3, 3, 3],
                 [4, 4, 4, 4],
                 [5, 5, 5, 5]]
        rnd = np.random.choice(24, deleteEdge, replace=False, p=None)
        for i in rnd:
            board[int(i / 4)][i % 4] = -1

        if solveSudokucube(0, availableEdge):
            for i in range(6):
                for j in range(4):
                    a[i][2 * j + 1] = board[i][j]
            break

    scramble(scramblelist[problemNumber-1])
    fill = [["" for _ in range(9)] for _ in range(6)]
    gray = [["" for _ in range(9)] for _ in range(6)]
    sumGray = 0
    for i in range(6):
        for j in range(9):
            if a[i][j] == -1:
                fill[i][j] = "gray"
                gray[i][j] = "\Large \\textbf " + str(sumGray)
            if a[i][j] == 0:
                fill[i][j] = "yellow"
                gray[i][j] = ""
            if a[i][j] == 1:
                fill[i][j] = "white"
                gray[i][j] = ""
            if a[i][j] == 2:
                fill[i][j] = "blue"
                gray[i][j] = ""
            if a[i][j] == 3:
                fill[i][j] = "green"
                gray[i][j] = ""
            if a[i][j] == 4:
                fill[i][j] = "red"
                gray[i][j] = ""
            if a[i][j] == 5:
                fill[i][j] = "orange"
                gray[i][j] = ""

    order = [(0, 0), (0, 1), (0, 2), (0, 3), (0, 4), (0, 5), (0, 6), (0, 7), (0, 8),
             (2, 0), (2, 1), (2, 2), (4, 0), (4, 1), (4, 2), (3,
                                                              0), (3, 1), (3, 2), (5, 0), (5, 1), (5, 2),
             (2, 3), (2, 4), (2, 5), (4, 3), (4, 4), (4, 5), (3,
                                                              3), (3, 4), (3, 5), (5, 3), (5, 4), (5, 5),
             (2, 6), (2, 7), (2, 8), (4, 6), (4, 7), (4, 8), (3,
                                                              6), (3, 7), (3, 8), (5, 6), (5, 7), (5, 8),
             (1, 0), (1, 1), (1, 2), (1, 3), (1, 4), (1, 5), (1, 6), (1, 7), (1, 8)
             ]

    for i in order:
        if fill[i[0]][i[1]] == "gray":
            sumGray = sumGray + 1
            gray[i[0]][i[1]] = "\Large \\textbf " + str(sumGray)

    print("""
{\\noindent\\Large  \\newtime \\textbf{No. """ + str(problemNumber) + """\\qquad Difficulty: """ + starNumber + """}}
\\vspace{0.2cm}\\\\
\\begin{tikzpicture}[every node/.style={minimum size=1cm-\\pgflinewidth, outer sep=0pt}]
\\node[fill=""" + fill[0][0] + """] at (0.5,5.5) {""" + gray[0][0] + """};
\\node[fill=""" + fill[0][1] + """] at (1.5,5.5) {""" + gray[0][1] + """};
\\node[fill=""" + fill[0][2] + """] at (2.5,5.5) {""" + gray[0][2] + """};
\\node[fill=""" + fill[0][3] + """] at (0.5,4.5) {""" + gray[0][3] + """};
\\node[fill=""" + fill[0][4] + """] at (1.5,4.5) {""" + gray[0][4] + """};
\\node[fill=""" + fill[0][5] + """] at (2.5,4.5) {""" + gray[0][5] + """};
\\node[fill=""" + fill[0][6] + """] at (0.5,3.5) {""" + gray[0][6] + """};
\\node[fill=""" + fill[0][7] + """] at (1.5,3.5) {""" + gray[0][7] + """};
\\node[fill=""" + fill[0][8] + """] at (2.5,3.5) {""" + gray[0][8] + """};

\\node[fill=""" + fill[2][0] + """] at (-2.5,2.5) {""" + gray[2][0] + """};
\\node[fill=""" + fill[2][1] + """] at (-1.5,2.5) {""" + gray[2][1] + """};
\\node[fill=""" + fill[2][2] + """] at (-0.5,2.5) {""" + gray[2][2] + """};
\\node[fill=""" + fill[4][0] + """] at (0.5,2.5) {""" + gray[4][0] + """};
\\node[fill=""" + fill[4][1] + """] at (1.5,2.5) {""" + gray[4][1] + """};
\\node[fill=""" + fill[4][2] + """] at (2.5,2.5) {""" + gray[4][2] + """};
\\node[fill=""" + fill[3][0] + """] at (3.5,2.5) {""" + gray[3][0] + """};
\\node[fill=""" + fill[3][1] + """] at (4.5,2.5) {""" + gray[3][1] + """};
\\node[fill=""" + fill[3][2] + """] at (5.5,2.5) {""" + gray[3][2] + """};
\\node[fill=""" + fill[5][0] + """] at (6.5,2.5) {""" + gray[5][0] + """};
\\node[fill=""" + fill[5][1] + """] at (7.5,2.5) {""" + gray[5][1] + """};
\\node[fill=""" + fill[5][2] + """] at (8.5,2.5) {""" + gray[5][2] + """};

\\node[fill=""" + fill[2][3] + """] at (-2.5,1.5) {""" + gray[2][3] + """};
\\node[fill=""" + fill[2][4] + """] at (-1.5,1.5) {""" + gray[2][4] + """};
\\node[fill=""" + fill[2][5] + """] at (-0.5,1.5) {""" + gray[2][5] + """};
\\node[fill=""" + fill[4][3] + """] at (0.5,1.5) {""" + gray[4][3] + """};
\\node[fill=""" + fill[4][4] + """] at (1.5,1.5) {""" + gray[4][4] + """};
\\node[fill=""" + fill[4][5] + """] at (2.5,1.5) {""" + gray[4][5] + """};
\\node[fill=""" + fill[3][3] + """] at (3.5,1.5) {""" + gray[3][3] + """};
\\node[fill=""" + fill[3][4] + """] at (4.5,1.5) {""" + gray[3][4] + """};
\\node[fill=""" + fill[3][5] + """] at (5.5,1.5) {""" + gray[3][5] + """};
\\node[fill=""" + fill[5][3] + """] at (6.5,1.5) {""" + gray[5][3] + """};
\\node[fill=""" + fill[5][4] + """] at (7.5,1.5) {""" + gray[5][4] + """};
\\node[fill=""" + fill[5][5] + """] at (8.5,1.5) {""" + gray[5][5] + """};

\\node[fill=""" + fill[2][6] + """] at (-2.5,0.5) {""" + gray[2][6] + """};
\\node[fill=""" + fill[2][7] + """] at (-1.5,0.5) {""" + gray[2][7] + """};
\\node[fill=""" + fill[2][8] + """] at (-0.5,0.5) {""" + gray[2][8] + """};
\\node[fill=""" + fill[4][6] + """] at (0.5,0.5) {""" + gray[4][6] + """};
\\node[fill=""" + fill[4][7] + """] at (1.5,0.5) {""" + gray[4][7] + """};
\\node[fill=""" + fill[4][8] + """] at (2.5,0.5) {""" + gray[4][8] + """};
\\node[fill=""" + fill[3][6] + """] at (3.5,0.5) {""" + gray[3][6] + """};
\\node[fill=""" + fill[3][7] + """] at (4.5,0.5) {""" + gray[3][7] + """};
\\node[fill=""" + fill[3][8] + """] at (5.5,0.5) {""" + gray[3][8] + """};
\\node[fill=""" + fill[5][6] + """] at (6.5,0.5) {""" + gray[5][6] + """};
\\node[fill=""" + fill[5][7] + """] at (7.5,0.5) {""" + gray[5][7] + """};
\\node[fill=""" + fill[5][8] + """] at (8.5,0.5) {""" + gray[5][8] + """};

\\node[fill=""" + fill[1][0] + """] at (0.5,-0.5) {""" + gray[1][0] + """};
\\node[fill=""" + fill[1][1] + """] at (1.5,-0.5) {""" + gray[1][1] + """};
\\node[fill=""" + fill[1][2] + """] at (2.5,-0.5) {""" + gray[1][2] + """};
\\node[fill=""" + fill[1][3] + """] at (0.5,-1.5) {""" + gray[1][3] + """};
\\node[fill=""" + fill[1][4] + """] at (1.5,-1.5) {""" + gray[1][4] + """};
\\node[fill=""" + fill[1][5] + """] at (2.5,-1.5) {""" + gray[1][5] + """};
\\node[fill=""" + fill[1][6] + """] at (0.5,-2.5) {""" + gray[1][6] + """};
\\node[fill=""" + fill[1][7] + """] at (1.5,-2.5) {""" + gray[1][7] + """};
\\node[fill=""" + fill[1][8] + """] at (2.5,-2.5) {""" + gray[1][8] + """};

\\draw[step=1cm,color=black, ultra thick] (-3,0) grid (9,3);
\\draw[step=1cm,color=black, ultra thick] (0,-3) grid (3,0);
\\draw[step=1cm,color=black, ultra thick] (0,3) grid (3,6);
\\end{tikzpicture}
\\vspace{0.1cm}
\\\\
\\noindent\\normalsize \\newtime  \\textbf{Solution """ + str(problemNumber) + """: """ + scramblelist[problemNumber-1] + """}
\\vspace{1cm}

""")

print("""
\\end{document}
""")
