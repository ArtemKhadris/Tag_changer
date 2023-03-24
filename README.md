# Tag changer (GUI)
## Description
XML tag changer
Currently works with XML files, other file formats (PHP, HTML etc.) will be added in the future.

Before starting, you need to install PySimpleGUI.

Initial install for Windows:
```
python -m pip install PySimpleGUI
```
Initial install for Linux and MacOS:
```
python3 -m pip install PySimpleGUI
```

## Manual
### 1

In the first window you need to select a XML file and enter the tag(s) you want to replace (through ";", completely, without spaces and with the same case as they are written in the file).

Click SUBMIT to continue.

To restart the program, press RESTART.

To cancel and close, press CANCEL.

If you have not entered a directory or tags, the program will warn you.

If the entered tag is missing in the file, the program will warn you.

![image](https://user-images.githubusercontent.com/106828028/227540033-993821ac-0ff6-4167-9c85-310f031e52ac.png)

### 2

In the next window, you will be informed about the matches found, indicate all the tags used in the file and ask you to enter a new tag (only one).

![image](https://user-images.githubusercontent.com/106828028/227542921-d48ffaec-6228-4f39-bd26-3ffa908b7ca9.png)

### 3

In the next window, you will be told how many times the selected tag occurs in the file, if several, then you will need to select which tag should be replaced.

![image](https://user-images.githubusercontent.com/106828028/227544740-a4caf5bb-a1bc-44fd-bb52-3fc0a166f6c9.png)

Press SHOW to continue.

If you need to replace this tag, click YES, CHANGE, if not, click NO, DON'T CHANGE, NEXT...

![image](https://user-images.githubusercontent.com/106828028/227546345-057bb357-b2e3-401e-a3d4-bec8089ae2b6.png)

When the tag is last encountered in the file, you will be prompted to save your changes. Save the file however you like.

![image](https://user-images.githubusercontent.com/106828028/227548004-beb21af1-99d1-42ad-a849-58bce72090ff.png)

## Thanks for using.

If any errors and incorrect operation of the application are found, please report to the mail artem.hadris@gmail.com .

