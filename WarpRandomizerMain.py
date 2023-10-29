"""
WarpRandomizerMain.py

Main function of the Warp Randomizer

Copyright (c) 2023 AtSign, XLuma, Turtleisaac

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>.
"""
import tempfile
import tkinter
from tkinter import ttk, TOP, TRUE, LEFT, W, E, Canvas, HORIZONTAL
from tkinter import filedialog
from tkinter import messagebox
from ttkthemes import ThemedTk
from nds.tableLocator import TableLocator
import activejson
import os
from RandomizerUtils import Definitions
from RandomizerUtils import Randomizer
import VerifyRom as verifier
from tkinter.ttk import *
from tkinter import *
from PIL import ImageTk, Image
from RandomizerUtils import Utils


class InfoWindow(Toplevel):

    def __init__(self, master=None):
        super().__init__(master=master)
        self.title("Warp Randomizer Info")
        self.geometry("250x200")
        label1 = Label(self, text="Supported Games:", font='Helvetica 16 bold')
        label2 = Label(self, text="Pokemon Emerald")
        label3 = Label(self, text="Pokemon Platinum")
        label4 = Label(self, text="Pokemon White2")
        label5 = Label(self, text="Pokemon FireRed")
        label6 = Label(self, text="Pokemon LeafGreen")
        label7 = Label(self, text="Pokemon HeartGold")
        label8 = Label(self, text="Pokemon SoulSilver")
        label1.pack()
        label2.pack()
        label3.pack()
        label4.pack()
        label5.pack()
        label6.pack()
        label7.pack()
        label8.pack()


root = ThemedTk(theme="breeze")
root.title('Universal Warp Randomizer V2.0')
root.resizable(False, False)
root.geometry('500x140')
ico = Image.open(Utils.resource_path(os.path.join('Resources', 'doodleDoorPoke.png')))
photo = ImageTk.PhotoImage(ico)
root.wm_iconphoto(False, photo)


top_frame = ttk.Frame(root)
top_frame.pack(side=TOP, pady=1)

style = ttk.Style()
style.configure("Hyperlink.TLabel", foreground="blue")

label1 = ttk.Label(top_frame, text="PointCrow's Universal Warp Randomizer", font='Helvetica 18 bold')
seed_entry = ttk.Entry(top_frame)
seed_label = ttk.Label(top_frame, text="Fixed Seed # (Optional)")
label2 = ttk.Label(top_frame, text="Created By XLuma, Turtleisaac, & AtSign", anchor="e", justify=LEFT)
info = ttk.Label(top_frame, text="Info", style="Hyperlink.TLabel", cursor="hand2")
progress_bar = ttk.Progressbar(top_frame, orient=HORIZONTAL, mode='indeterminate', length=400)
progress_bar['value'] = 0
pb_increase = [True]


def randomize():
    filetypes = [
        ('game file', '*.gba *.nds')
    ]
    # TODO put *.nds back to enable nds

    f_in = filedialog.askopenfile(title='Select ROM to Randomize', filetypes=filetypes, mode='r')
    if f_in is not None:
        filepath_input = os.path.abspath(f_in.name)
        f_in.close()
        verification_tuple = verifier.validate_rom(filepath_input)

        if verification_tuple is None:
            messagebox.showerror('Error', 'The provided rom at ' + filepath_input + ' is not valid. Warp '
                                                                                    'randomization aborted.')
            return

        f_out = filedialog.asksaveasfilename(defaultextension="." + verification_tuple[2])
        if f_out is None:  # asksaveasfile return `None` if dialog closed with "cancel".
            return
        filepath_output = f_out
        if filepath_input == filepath_output:
            messagebox.showerror('Error', 'You can\'t select the same file for both the input and the output. Please '
                                          'save as a new file.')
            return
        # f_out.close()
        fixed_seed = seed_entry.get()
        if fixed_seed == '':
            fixed_seed = -1
        else:
            try:
                fixed_seed = int(fixed_seed)
            except ValueError:
                pass
        complete = False

        seed_entry['state'] = 'disabled'
        open_button.grid_forget()
        progress_bar.grid(row=1, column=0, columnspan=2, pady=5)
        stored_seed = fixed_seed

        while True:
            set_randomize_gui(stored_seed)

            result = Randomizer.start_randomizer(filepath_input, filepath_output, Definitions.get_definition(
                int(verification_tuple[3])), fixed_seed, verification_tuple[4])
            stored_seed = result[1]
            if result[2]:
                messagebox.showerror('Error', 'Provided game is not supported. The list of supported games can be '
                                              'found in the Info window.')
                break
            if result[0]:
                complete = True
                break
            elif fixed_seed != -1:
                messagebox.showerror('Error', 'Seed unable to create valid randomization, please try different seed')
                break
        reset_gui()
        if complete:
            messagebox.showinfo(title='Randomizer', message='Warp Randomization Complete! Output can be found at:\n' +
                                                            filepath_output)


def set_randomize_gui(stored_seed):
    if stored_seed == -1:
        label2['text'] = 'Initializing'
    else:
        label2['text'] = 'Attempting Seed %s' % stored_seed

    if progress_bar['value'] == 0:
        pb_increase[0] = True
    elif progress_bar['value'] == 100:
        pb_increase[0] = False

    if pb_increase[0]:
        progress_bar['value'] += 20
    elif not pb_increase[0]:
        progress_bar['value'] -= 20
    root.update()


def reset_gui():
    progress_bar['value'] = 0
    progress_bar.grid_forget()
    open_button.grid(row=1, column=0, columnspan=2, pady=5)
    label2['text'] = 'Created By XLuma, Turtleisaac, & AtSign'
    seed_entry['state'] = 'enabled'
    root.update()


# open button
open_button = ttk.Button(
    top_frame,
    text='Randomize Warps',
    command=randomize,
    width=30,
    # font='Helvetica 12 bold'
)

label1.grid(row=0, column=0, columnspan=2)
open_button.grid(row=1, column=0, columnspan=2, pady=5)
seed_label.grid(row=2, column=0, sticky=E, columnspan=1, pady=5)
seed_entry.grid(row=2, column=1, sticky=W, columnspan=1, pady=5, padx=5)
info.grid(row=3, column=0, sticky=W, columnspan=1, pady=5)
info.bind("<Button-1>", lambda e: InfoWindow(root))
label2.grid(row=3, column=1, sticky=E, columnspan=1, pady=5)
top_frame.columnconfigure(0, weight=5, uniform='row')
top_frame.columnconfigure(1, weight=7, uniform='row')

root.eval('tk::PlaceWindow . center')

# Use this code to signal the splash screen removal.
if "NUITKA_ONEFILE_PARENT" in os.environ:
    splash_filename = os.path.join(
        tempfile.gettempdir(),
        "onefile_%d_splash_feedback.tmp" % int(os.environ["NUITKA_ONEFILE_PARENT"]),
    )

    if os.path.exists(splash_filename):
        os.unlink(splash_filename)

root.mainloop()
