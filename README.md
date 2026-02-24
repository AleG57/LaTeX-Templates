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
Base and Basetwo templates are complete. Nevertheless, they are still simple to handle whereas the advanced one includes
bibliography for complex studies and projects.  

- [minimal](report/minimal/main.pdf)
- [base](report/base/main.pdf)
- [basetwo](report/basetwo/main.pdf)
- [advanced](report/advanced/main.pdf)

| Template | Custom commands | Code | Math expressions | Bibliography  |
|----------| --------------- |------|------------------|---------------|
| Minimal  |                 |      |                  |               |
| Base     |        X        |      |                  |               |
| Basetwo  |        X        |   X  |        X         |               |
| Advanced |        X        |   X  |        X         |       X       |

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

```bash
#!/bin/bash
# build.sh

set -e # Stop if error

pdflatex --shell-escape main.tex
bibtex main
pdflatex --shell-escape main.tex
pdflatex --shell-escape main.tex

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
This bash script allows you to run your .tex script once and once time since the bibtex package requires multiple runs of .tex files in order 
to work properly. Don't forget to make the file executable !
```bash
#!/bin/bash
chmod +x build.sh
```

**📝 Articles**
---

