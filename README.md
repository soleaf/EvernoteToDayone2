# EvernoteToDayone2
Move notes from Evernote to DayOne2 on Mac
It just simple python script.

## Requirement

- Python 2
- BeuatifulSoap(pip install beautifulsoup4)

## PROCEDURE

1. Open Evernote and select notes for export.
1. Right click and click 'Export Note...' to call 'Export Selected Notes' window.
1. Change Format to 'HTML' and save anywhere
1. To install DayOne2 CLI run 'sudo /Applications/Day\ One.app/Contents/Resources/install_cli.sh' on Terminal
1. Run 'python evernotehtml_to_dayone.py' on Terminal app
1. If you get some error for not found library 'BeautifulSoup', run 'pip install beautifulsoup4'
