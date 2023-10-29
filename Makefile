RED= \033[0;31m
NC= \033[0m
GREEN = \033[0;32m
COMPILING = @printf "$(GREEN)Compiling...\n$(NC)"
SLEEP= @sleep 1
UNAME := $(shell uname -s)
WINDOWS := $(findstring "MSYS_NT", $(UNAME))
all:
	$(SLEEP)
	$(COMPILING)
	$(SLEEP)
	@echo $(UNAME)
#	pyinstaller --windowed --noconsole --clean --onefile WarpRandomizerMain.spec old command
	@if [ "$(UNAME)" = "Darwin" ]; then make mac ; fi
	@if [ "$(UNAME)" = "Linux" ]; then make lin ; fi
	@if [ "$(WINDOWS)" = "MSYS_NT" ]; then make win ; fi
	@if [ "$(UNAME)" = "Darwin" ]; then chmod 777 $(shell pwd)/WarpRandomizerMain.dist/WarpRandomizerMain ; fi
	@if [ "$(UNAME)" = "Linux" ]; then chmod 777 $(shell pwd)/WarpRandomizerMain.dist/WarpRandomizerMain.bin ; fi

onefile:
	$(SLEEP)
	$(COMPILING)
	$(SLEEP)
	@echo $(UNAME)
	@if [ "$(UNAME)" = "Darwin" ]; then make mac_onefile ; fi
	@if [ "$(UNAME)" = "Linux" ]; then make lin_onefile ; fi
	@if [ "$(WINDOWS)" = "MSYS_NT" ]; then make win_onefile ; fi

mac:
	python3 -m nuitka --follow-imports --standalone --include-package-data=ttkthemes --include-data-dir=Resources=Resources WarpRandomizerMain.py

mac_onefile:
	#python3 -m nuitka --follow-imports --standalone --include-package-data=ttkthemes --include-data-dir=Resources=Resources --enable-plugin=numpy --macos-create-app-bundle --onefile WarpRandomizerMain.py
	pyinstaller WarpRandomizerMain.spec
	#mv WarpRandomizerMain.bin WarpRandomizer

lin:
	python3 -m nuitka --follow-imports --standalone --enable-plugin=tk-inter --include-package-data=ttkthemes --include-data-dir=Resources=Resources WarpRandomizerMain.py

lin_onefile:
	python3 -m nuitka --follow-imports --standalone --enable-plugin=tk-inter --include-package-data=ttkthemes --include-data-dir=Resources=Resources --onefile WarpRandomizerMain.py

win:
	python -m nuitka --follow-imports --standalone --enable-plugin=tk-inter --enable-plugin=numpy --include-package-data=ttkthemes --include-data-dir=Resources=Resources --windows-icon-from-ico=Resources/doodleDoorPoke.png --onefile-windows-splash-screen-image=Resources/doodleDoorPoke.png WarpRandomizerMain.py

win_onefile:
	python -m nuitka --follow-imports --standalone --enable-plugin=tk-inter --enable-plugin=numpy --include-package-dat=ttkthemes --include-data-dir=Resources=Resources --windows-icon-from-ico=Resources/doodleDoorPoke.png --windows-disable-console --onefile-windows-splash-screen-image=Resources/doodleDoorPoke.png --onefile WarpRandomizerMain.py

