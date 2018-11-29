# isaham-skeleton
iSaham Skeleton is a mini framework for developing website.

## Notice
For any new iSaham member, you should learn python and version control management (We use [git](https://git-scm.com)). 

We assume you should be able to do some basic HTML, CSS and JavaScript coding. For beginner, we recommend to learn from [W3School](https://www.w3schools.com)

## Installation

Make sure your computer have python 2.xx installed
Use the package manager [pip](https://pip.pypa.io/en/stable/) to install BottlePy. You probably don't have to download pip if you already install python before. Download python 2.xx [here](https://www.python.org/downloads/)

```bash
pip install bottle
```

## Basic Usage

Clone the skeleton using git. If you don't have git program, just download and install from [here](https://git-scm.com/downloads)

```bash
git clone https://github.com/AmirinNS/isaham-skeleton.git
```
After finished, you can open any text editor such [Visual Code](https://code.visualstudio.com) or [Sublime](https://www.sublimetext.com)

Noted that all pages must be created within pages folder and you must create a specific folder for you project. You can't delete files that already exist in this skeleton. Any modification will be ignored and may lead to error during integration with actual server

## Advance Usage

You can explore React JS in this skeleton. Just head to react folder to play around. Install the dependency first. Oh we assume you already know what is npm is 😉

```bash
npm install
```

After that, run these script

```bash
npm run watch
```
Don't forget to run server.py too. Now we can harness the awesomeness of React and BottlePy server side rendering.
Lastly, build your react app after finished the code and copy over to pages folder

```bash
npm run build
```

## License
[MIT](https://choosealicense.com/licenses/mit/)
