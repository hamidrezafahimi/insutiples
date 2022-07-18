

### Installing LaTex Package

Install an almost full version of LaTex:

```
sudo apt install texlive-latex-extra
```

Also do this in order to avoid probable errors:
```
sudo apt-get update -y

sudo apt-get install -y texlive-science

sudo apt-get install texlive-latex-recommended

sudo apt install texlive-fonts-recommended

```


### Persian

```
sudo apt install texlive-xetex

sudo apt install texlive-lang-arabic 
```

You can add the folder containing your fonts to texhash:

```
# I assume that you've added your fonts to a folder named '~/.fonts'
texhash .fonts/
```

By clicking on any font file ('.ttf'), you can install it on ubuntu.

Then the font must be identified whether it is english or persian or ... .


### Check the Installation - Running .tex script without IDE

Make a simple latex script like:

```
\documentclass{article}
\usepackage{hyperref}
\begin{document}
Hello world \LaTeX
\end{document}
```

Name it hello-world.tex for example.

Compile it with `pdflatex`:

```
pdflatex hello-world.tex
```

See the pdf output:

```
evince hello-world.pdf
```

### Edit the '.tex' files in an editor

Install the texmaker this way:

```
sudo apt install texmaker
```

To compile english latex scripts, simply use 'pdflatex' or 'latex' build tools.

To compile persian latex scripts, use 'xelatex'. Also, remember to include the 'xepersian' package in your script.
