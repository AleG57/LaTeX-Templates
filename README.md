# $\LaTeX$ templates

From minimal to advanced $\LaTeX$ templates.

- 📄 [See eports](report)
- 🎓 [See thesis](thesis)
- 📝 [See articles](article)
- 🎤 [See beamers](beamer)


**🎤 Beamers**
---
For beamers, there is a minimal beamer including soft and simple presentation. Blue and red beamers are university-style templates
commonly used in academia. 

- [minimal](beamer/minimal/main.pdf)
- [red beamer](beamer/red/main.pdf)
- [blue beamer](beamer/blue/main.pdf)

```bash
#!/bin/bash
pdflatex main.tex
```
**📄 Reports**
---
Report includes a minimal template for soft and quick presentations, avoiding spending time on project's structure.
Base and Basetwo templates are complete. Nevertheless, they are still simple to handle. On the other side, the advanced template includes
bibliography and annexes management folder for complex studies and projects.  

- [minimal](report/minimal/main.pdf)
- [base](report/base/main.pdf)
- [basetwo](report/basetwo/main.pdf)
- [advanced](report/advanced/main.pdf)

These templates are basically a balance between how much time you wants to spend on the report's structure and the project itself. The basic ones 
are for tiny projects that didn't require a lot of structural comprehension whereas the advanced one is focused on optimizing the technical dept. 

| Template | Custom commands | Code | Math expressions | Bibliography  | Annexes |
|----------| --------------- |------|------------------|---------------|---------|
| Minimal  |                 |      |                  |               |         |
| Base     |        X        |      |                  |               |         |
| Basetwo  |        X        |   X  |        X         |               |         |
| Advanced |        X        |   X  |        X         |       X       |    X    |

The --shell-escape flag is mandatory for the use of minted (python code with colors)
```bash
#!/bin/bash
pdflatex --shell-escape main.tex
```
For the advanced one, you are provided a bash script that can be compiled using the following command :
```bash
#!/bin/bash
./build.sh
```
This bash script allows you to run your .tex script once and once time since the bibtex package requires multiple runs of .tex files in order 
to work properly. Don't forget to make the file executable !
```bash
#!/bin/bash
chmod +x build.sh
```

**🎓 Thesis**
---

The thesis template is unique and provide slightly sophisticated improvements on reports.  

- [Example](report/minimal/main.pdf)

Like for the report section, you are provided a bash script that can be compiled using the following command :
```bash
#!/bin/bash
./build.sh
```
This bash script allows you to compile your .tex scripts once and once time since the bibtex package requires multiple runs of .tex files in order 
to work properly. Don't forget to make the file executable !
```bash
#!/bin/bash
chmod +x build.sh
```
The thesis template allows you 

**📝 Articles**
---





For your information, the build.sh script is the following file 

```bash
#!/bin/bash
#!/bin/bash

# ------------ Init ------------ #

echo -e "\033[1;34m Removing auxiliary files \033[0m"
rm -rf _minted-* .minted-*
rm -f *.aux *.bbl *.blg *.log *.out *.toc *.lof *.lot *.fls *.fdb_latexmk *.synctex.gz

START_TIME=$SECONDS
LOG_FILE="build.log"
PDF_DIR="annexes/pdf"
SCRIPT_DIR="annexes/scripts"
TEX_DIR="annexes/tex"
OUTPUT_FILE="annexes.tex"

run_quiet() {
    local label="$1"
    shift
    echo -n "  $label ... "
    
    if ! "$@" > "$LOG_FILE" 2>&1; then
        echo -e "\033[1;31m[ÉCHEC]\033[0m"
        echo -e "\n\033[1;31m=== ERROR ===\033[0m\n"
        cat "$LOG_FILE"
        rm -f "$LOG_FILE"
        exit 1
    fi
    
    echo -e "\033[1;32m[OK]\033[0m"
}

shopt -s nocaseglob
set -e

echo -e "\033[1;34m Compilation of LaTeX document \033[0m"
echo -e "\033[1;34m Generating annexes.tex \033[0m"


# ------------ Annexes ------------ #

{
    echo "\begin{subappendices}"
    echo ""
    echo "\phantomsection\hypertarget{annexes_toc}{}"
    echo "\chapter*{Liste des Annexes}"
    echo "\addcontentsline{toc}{chapter}{Liste des Annexes}"
    echo ""
    echo "\begin{itemize}[label=\textbullet]"

    i=1

    # Sommaire PDF
    if [ -d "$PDF_DIR" ]; then
        for pdf_path in "$PDF_DIR"/*.pdf; do
            [ -e "$pdf_path" ] || continue
            clean_name=$(basename "$pdf_path" .pdf | tr '_' ' ')
            echo "  \item \hyperlink{annexe:$i}{\textbf{Annexe n°$i :} $clean_name}"
            ((i++))
        done
    fi

    # Sommaire TeX
    if [ -d "$TEX_DIR" ]; then
        while IFS= read -r tex_path; do
            [ -e "$tex_path" ] || continue
            filename=$(basename "$tex_path")
            clean_name=$(basename "$tex_path" .tex | tr '_' ' ')
            filename_echape=$(echo "$filename" | sed 's/_/\\_/g')
            echo "  \item \hyperlink{annexe:$i}{\textbf{Annexe n°$i :} $clean_name}"
            ((i++))
        done < <(find "$TEX_DIR" -type f -name "*.tex" | sort)
    fi

    # Sommaire Scripts
    if [ -d "$SCRIPT_DIR" ]; then
        while IFS= read -r script_path; do
            [ -e "$script_path" ] || continue
            filename_echape=$(basename "$script_path" | sed 's/_/\\_/g')
            echo "  \item \hyperlink{annexe:$i}{\textbf{Annexe n°$i :} \texttt{$filename_echape}}"
            ((i++))
        done < <(find "$SCRIPT_DIR" -type f | sort)
    fi

    echo "\end{itemize}"
    echo "\newpage"
    echo ""

    i=1

    # PDF
    if [ -d "$PDF_DIR" ]; then
        for pdf_path in "$PDF_DIR"/*.pdf; do
            [ -e "$pdf_path" ] || continue
            clean_name=$(basename "$pdf_path" .pdf | tr '_' ' ')
            echo "\phantomsection\hypertarget{annexe:$i}{}"
            echo "\thispagestyle{empty}\vspace*{\fill}\begin{center}\Huge\textbf{Annexe n°$i}\\\\[0.5cm]\Large $clean_name\end{center}\vspace*{\fill}\newpage"
            echo "\includepdf[pages=-, scale=1, pagecommand={\thispagestyle{plain}}]{$pdf_path}"
            ((i++))
        done
    fi

    # .tex files
    if [ -d "$TEX_DIR" ]; then
        while IFS= read -r tex_path; do
            [ -e "$tex_path" ] || continue
            clean_name=$(basename "$tex_path" .tex | tr '_' ' ')
            echo "\phantomsection\hypertarget{annexe:$i}{}"
            echo "\thispagestyle{empty}\vspace*{\fill}\begin{center}\Huge\textbf{Annexe n°$i}\\\\[0.5cm]\Large $clean_name\end{center}\vspace*{\fill}\newpage\pagestyle{fancy}"
            echo "\input{$tex_path}\newpage"
            ((i++))
        done < <(find "$TEX_DIR" -type f -name "*.tex" | sort)
    fi

    # scripts
    if [ -d "$SCRIPT_DIR" ]; then
        while IFS= read -r script_path; do
            [ -e "$script_path" ] || continue
            filename=$(basename "$script_path")
            ext="${filename##*.}"
            filename_echape=$(echo "$filename" | sed 's/_/\\_/g')

            langage="text"
            if [ "$ext" = "py" ]; then langage="python"; fi
            if [ "$ext" = "sh" ]; then langage="bash"; fi
            if [ "$ext" = "sql" ]; then langage="sql"; fi
            if [ "$ext" = "yaml" ] || [ "$ext" = "yml" ]; then langage="yaml"; fi

            echo "\phantomsection\hypertarget{annexe:$i}{}"
            echo "\thispagestyle{empty}\vspace*{\fill}\begin{center}\Huge\textbf{Annexe n°$i}\\\\[0.5cm]\Large \texttt{$filename_echape}\end{center}\vspace*{\fill}\clearpage\pagestyle{fancy}"
            echo "\inputminted[linenos=true, frame=lines, framesep=2mm, fontsize=\footnotesize, breaklines=true]{$langage}{$script_path}\newpage"
            ((i++))
        done < <(find "$SCRIPT_DIR" -type f | sort)
    fi

    echo "\end{subappendices}"
} > "$OUTPUT_FILE"

shopt -u nocaseglob

# ------------ Main ------------ #

echo -e "\033[1;34m Generating .pdf \033[0m"

run_quiet "[1/4] Generating LaTeX document" pdflatex -interaction=nonstopmode -halt-on-error --shell-escape main.tex
run_quiet "[2/4] Loading BibTeX citations" bibtex main
run_quiet "[3/4] Merging citations and LaTeX document" pdflatex -interaction=nonstopmode -halt-on-error --shell-escape main.tex
run_quiet "[4/4] Resolving cross-references" pdflatex -interaction=nonstopmode -halt-on-error --shell-escape main.tex

# Cleaning
rm -f "$LOG_FILE"

# ------------ Execution time ------------ #

ELAPSED=$(( SECONDS - START_TIME ))
MINUTES=$(( ELAPSED / 60 ))
SECONDS_LEFT=$(( ELAPSED % 60 ))

if [ $MINUTES -gt 0 ]; then
    TIME_FORMAT="${MINUTES}m ${SECONDS_LEFT}s"
else
    TIME_FORMAT="${SECONDS_LEFT}s"
fi

echo -e "\033[1;32m Compilation ended within $TIME_FORMAT \033[0m"
```
