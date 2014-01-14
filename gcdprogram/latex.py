# -*- coding: utf-8 -*-
latexDoc = """
\documentclass[a4paper,10pt]{{article}}
\usepackage[utf8]{{inputenc}}
\usepackage[T1]{{fontenc}}
\usepackage[english]{{babel}}
\\title{{Den udvidede euklidiske algoritme}}
\\author{{Foo bar\\\\ \\rule{{5.5cm}}{{0.5mm}}}}
\\begin{{document}}
\\maketitle
\\noindent Vi starter med at udfylde tabellen for $gcd({a},{b})$. \\\\
\\begin{{tabular}}{{| c || c | c | l |}} 
    \hline
    $i$ & $r_i$ & $q_i$ & Forklaring \\\\
    \hline
    {gcdtable}
    \hline
\end{{tabular}} \\\\
Og da resten nu er nul er GCD vores sidste $r$-værdi eller $r_{lasti} = 
{lastr}$.
{coprime}
\end{{document}}
    """
