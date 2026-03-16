
PC@Kat MINGW64 ~ (main)
$ rm -r -Force C:\Users\PC\.git
rm: unknown option -- F
Try 'rm --help' for more information.

PC@Kat MINGW64 ~ (main)
$ cd C:\Users\PC\bank_widget
bash: cd: C:UsersPCbank_widget: No such file or directory

PC@Kat MINGW64 ~ (main)
$ ^C

PC@Kat MINGW64 ~ (main)
$ cd /c/Users/PC/bank_widget

PC@Kat MINGW64 ~/bank_widget (main)
$ git init
Initialized empty Git repository in C:/Users/PC/bank_widget/.git/

PC@Kat MINGW64 ~/bank_widget (main)
$ echo ".idea/" > .gitignore

PC@Kat MINGW64 ~/bank_widget (main)
$ echo "__pycache__/" >> .gitignore

PC@Kat MINGW64 ~/bank_widget (main)
$ echo "venv/" >> .gitignore

PC@Kat MINGW64 ~/bank_widget (main)
$ echo ".venv/" >> .gitignore

PC@Kat MINGW64 ~/bank_widget (main)
$ git add .gitignore
warning: in the working copy of '.gitignore', LF will be replaced by CRLF the next time Git touches it

PC@Kat MINGW64 ~/bank_widget (main)
$ git commit -m "Initial commit: add .gitignore"
[main (root-commit) 01d8098] Initial commit: add .gitignore
 1 file changed, 4 insertions(+)
 create mode 100644 .gitignore

PC@Kat MINGW64 ~/bank_widget (main)
$ git add src/masks.py

PC@Kat MINGW64 ~/bank_widget (main)
$ git commit -m "Add masks module"
[main 365e2f3] Add masks module
 1 file changed, 10 insertions(+)
 create mode 100644 src/masks.py

PC@Kat MINGW64 ~/bank_widget (main)
$ git add src/widget.py
fatal: pathspec 'src/widget.py' did not match any files

PC@Kat MINGW64 ~/bank_widget (main)
$

PC@Kat MINGW64 ~/bank_widget (main)
$ git commit -m "Add widget module"
On branch main
Untracked files:
  (use "git add <file>..." to include in what will be committed)
        .flake8
        bank_widget.zip
        main.py
        poetry.lock
        pyproject.toml
        src/__init__.py
        tests/

nothing added to commit but untracked files present (use "git add" to track)

PC@Kat MINGW64 ~/bank_widget (main)
$ git add src/masks.py main.py pyproject.toml .flake8

PC@Kat MINGW64 ~/bank_widget (main)
$ git commit -m "Add project structure and masks module"
[main 3275f99] Add project structure and masks module
 3 files changed, 49 insertions(+)
 create mode 100644 .flake8
 create mode 100644 main.py
 create mode 100644 pyproject.toml

PC@Kat MINGW64 ~/bank_widget (main)
$ git add src/widget.py
fatal: pathspec 'src/widget.py' did not match any files

PC@Kat MINGW64 ~/bank_widget (main)
$

PC@Kat MINGW64 ~/bank_widget (main)
$ git add src/widget.py
fatal: pathspec 'src/widget.py' did not match any files

PC@Kat MINGW64 ~/bank_widget (main)
$ ^C

PC@Kat MINGW64 ~/bank_widget (main)
$ touch src/masks.py

PC@Kat MINGW64 ~/bank_widget (main)
$ touch src/widget.py

PC@Kat MINGW64 ~/bank_widget (main)
$ ls src/
__init__.py  __pycache__/  masks.py  widget.py

PC@Kat MINGW64 ~/bank_widget (main)
$ git add src/widget.py

PC@Kat MINGW64 ~/bank_widget (main)
$ git commit -m "Add widget module with mask_account_card and get_date functions"
[main 8fdd16e] Add widget module with mask_account_card and get_date functions
 1 file changed, 0 insertions(+), 0 deletions(-)
 create mode 100644 src/widget.py

PC@Kat MINGW64 ~/bank_widget (main)
$ git log --oneline
8fdd16e (HEAD -> main) Add widget module with mask_account_card and get_date functions
3275f99 Add project structure and masks module
365e2f3 Add masks module
01d8098 Initial commit: add .gitignore

PC@Kat MINGW64 ~/bank_widget (main)
