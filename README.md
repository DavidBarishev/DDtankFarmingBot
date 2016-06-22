# DDtank Farming Bot

## What is this repository for ? 
This repository is an semi automated bot , for the web flash game - DDtank.  
The repository is designed to be extendable , it run 'Farming modules' that are independent , and can be customizable by the user. 

## How is this repository designed ?
The tree of the repository is the following:

- Main Package
  - __init__ 
  - Main
  - Util
  - Logic
  - Imging
  - Globals
  - Exceptions 
  - Clicking
  - Modules
    - __init__  
    - TreasureFarm
    - TreasureMap
    - WealthTree
  - Images

In the global package , there are modules that provide the framework for the 'Farming Modules' , also it runs the modules.

## Dependencies 
- [pyautogui](https://pypi.python.org/pypi/PyAutoGUI)
- ~~OpenCV~~ not a dependency yet , but maybe in the future for faster image detection

## How to develope 'Farming Modules'
Check ou the wiki section for it [here](https://github.com/DavidBarishev/DDtankFarmingBot/wiki)

## Road Map

  - [x] Basic logging
  - [x] Basic Framwork
  - [ ] Develope as much 'Farming Modules'
  - [ ] Add combat farming - eg farming sports fights
  - [ ] Add PVE farming - eg farming botyard


## License
This software is protected under the  **GNU GENERAL PUBLIC LICENSE Version 3** , read the license.txt for more information 
