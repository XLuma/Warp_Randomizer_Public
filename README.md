# PointCrow's Universal Warp Randomizer

**This is the repo for the official warp randomizer used in PointCrow's Twitch streams**

**Created by XLuma, Turtleisaac, AtSign**

# Usage

* To run a compiled build, please download one from the **Releases** tab here on GitHub and double click the application.

* To run from source, run `WarpRandomizerMain.py`

## Compiling

# Dependencies

* On Windows, you will need to install python 3.9, git, make, pip and Microsoft Visual Studio (at least 2019).
* On MacOS, you will need to install python 3.9, git, make, pip and a C compiler if for some reason your computer doesnt have one. By default, MacOS has clang installed.
* On Linux, you will need to install python 3.9, git, make, python-pip, python3-tk, patchelf and gcc (if for some reason, your distro doesnt come with gcc already installed).
  
* On MacOS systems, brew may be needed to install tkinter, which is a dependency accross all systems. Once brew is installed, run `brew install python-tk`.
* On Windows systems, tkinter can be installed when installing Python. dont miss it, or you're going to do a little bit of googling to get it back up. `pip install python-tk` should be fine... maybe.

# Building the project

1. Clone the repo `git clone https://github.com/AtSign8877/PointCrow_Universal_Warp_Randomizer.git`
2. access the directory via cd in a terminal
3. Install the python dependencies required. Make sure pip is installed. `pip install -r requirements.txt`. On linux system, you might have to try python-pip or python3-pip.
4. Run `make onefile`. A WarpRandomizerMain.dist will appear, in which you can check if the required data files are being copied correctly. In the root of the project, Windows
users will find an executable. Mac and Linux users will find a .bin file, which will need its permissions adjusted to be executed with `chmod 777 WarpRandomizerMain.bin`.

# License
This project is made available under the GPL-V3 license. See `LICENSE.md` for more details.

