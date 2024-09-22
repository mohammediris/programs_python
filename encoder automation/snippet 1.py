Notepad++ v8.6.9 bug-fixes & new enhancements:

 1. Make installation and updates easy & quiet by adding "Yes (Silent)" button.
 2. Add new options '/closeRunningNpp' & '/runNppAfterSilentInstall' in the installer.
 3. Fix crash of "Next Search Result" command on the empty search result.
 4. Fix the regression where the Find dialog size is not remembered across sessions.
 5. Fix the regression of content lost by using Encoding "Convert to..." commands. 
 6. Fix the regression of exception/crash on Windows Server Core 2022.
 7. Prevent DirectWrite from being enabled under Windows Sever.
 8. Enhance the quality of Fluent toolbar icon sets for different DPI settings.
 9. Improve the look & feel of tabbar close button in dark mode.
10. Improve the dark mode tab bar icon in the search results panel.
11. Add ability to pre-populate the predefined color sets for custom tones.
12. Add "Show All Character" popup menu on toolbar button.
13. Fix the rectangular selection copy-paste bug.
14. Allow opening shortcut files (*.lnk) directly if the file extension is changed.
15. Fix the lost panels issue.
16. Add Backspace unindent option.
17. Fix CSS more indentation bug.
18. Include F13-F24 keys in Shortcut Mapper.
19. Fix the problem where the last empty clean untitled tab cannot be closed after renaming.
20. Add plugin a command (NPPM_SETUNTITLEDNAME) to rename untitled tab.
21. Display a message box with information about disabled backward regex searching.
22. Fix the display glitch for unsaved tabs containing tab characters.
23. Fix status bar and tab bar flicker during the GUI updated (fixed only for dark mode).
24. Fix the issue with "Begin/End Select" command after deletion.
25. Resolve the integer overflow problem in the Column Editor.

''' snippet for reading all 8 input channels '''
    # you are already in input menu 
for i in range (8):
    writer.write(str(i)+'\n') 
    response = await reader.read(100000)
    # print(f"{response}") 
    matchMultiIP = re.findall(r"11.*: (\d{1,3}.\d{1,3}.\d{1,3}.\d{1,3})",response)
    matchMultiPort = re.findall(r"12.*: (\d{1,5})",response)
    print(f"Multicast config for input {str(i)} is {matchMultiIP[0]}:{matchMultiPort[0]}")
    writer.write('p\n')             # go back to encoder menu
    writer.write(str(i)+'p\n')      # go back to input menu