# importing modules
from tkinter import *
from tkinter.filedialog import askopenfilename
from tkinter import ttk

# defining main window
root = Tk()
root.geometry('780x770')
root.title('NVH Engine Mounting')


# for disable and enable
def filter_disable(condition):
    for i in range(5, len(rem_list)):
        rem_list[i].config(state=condition)
    for i in range(len(col_tab)):
        col_tab[i].config(state=condition)
    for i in range(len(mount_tab_row_inlined_head)):
        mount_tab_row_inlined_head[i].config(state=condition)
    for i in range(len(mount_tab_col_list)):
        mount_tab_col_list[i].config(state=condition)
    for i in range(len(mount_entry_tab)):
        mount_entry_tab[i].config(state=condition)
    for i in range(len(mount_row_head_inclined)):
        mount_row_head_inclined[i].config(state=condition)
    for i in range(len(axis_list)):
        axis_list[i].config(state=condition)
    for i in range(len(moment_axis_list)):
        moment_axis_list[i].config(state=condition)


def radiobutton_fun():
    if (Radiobutton_var.get() == 1):
        for i in range(0, 5):
            rem_list[i].config(state=NORMAL)
        filter_disable(DISABLED)

    if (Radiobutton_var.get() == 2):
        for i in range(0, 5):
            rem_list[i].config(state=DISABLED)
        filter_disable(NORMAL)


Radiobutton_var = IntVar()
# enter data via file radio button
load_radio_button = Radiobutton(root, text='Load Configuration File', pady=4, variable=Radiobutton_var, value=1,
                                command=radiobutton_fun)
load_radio_button.grid(row=0, column=0, sticky=W)


def ModifyWidgets(col_tab, mount_entry_tab, mount_row_head_inclined, mount_tab_row_inlined_head):
    for j in range(0, len(col_tab)):
        col_tab[j].grid_remove()
    for j in range(0, len(mount_entry_tab)):
        mount_entry_tab[j].grid_remove()
    for j in range(0, len(mount_row_head_inclined)):
        mount_row_head_inclined[j].grid_remove()
    for j in range(0, len(mount_tab_row_inlined_head)):
        mount_tab_row_inlined_head[j].grid_remove()


def open_file(text):
    file = askopenfilename(filetypes=[('all files', '*.*')], title="choose a file")
    text.set(file)
    return file


def inclined(y):
    if (y == 'Vertical'):
        for j in range(0, len(mount_tab_row_inlined_head)):
            mount_tab_row_inlined_head[j].grid_remove()
        for j in range(0, len(mount_row_head_inclined)):
            mount_row_head_inclined[j].grid_remove()
    if (y == 'Inclined'):
        for j in range(0, len(mount_tab_row_inlined_head)):
            mount_tab_row_inlined_head[j].grid()
        for j in range(0, (3 * no_mount_rows)):
            mount_row_head_inclined[j].grid()


def num_of_mountings(self):
    global no_mount_rows
    global mount_option1
    global mount_option2

    option1 = mount_option1.get()
    option2 = mount_option2.get()
    # for modifying the fildes
    ModifyWidgets(col_tab, mount_entry_tab, mount_row_head_inclined, mount_tab_row_inlined_head)

    def inner_table(x, y):
        if (option2 == 'Vertical'):
            for c in range(0, x):
                col_tab[c].grid()
            for i in range(0, (x * 6)):
                mount_entry_tab[i].grid()
            for j in range(0, len(mount_tab_row_inlined_head)):
                mount_tab_row_inlined_head[j].grid_remove()
            for j in range(0, len(mount_row_head_inclined)):
                mount_row_head_inclined[j].grid_remove()
        if (option2 == 'Inclined'):
            for c in range(0, x):
                col_tab[c].grid()
            for i in range(0, (x * 6)):
                mount_entry_tab[i].grid()
            for j in range(0, len(mount_tab_row_inlined_head)):
                mount_tab_row_inlined_head[j].grid()
            for j in range(0, (3 * no_mount_rows)):
                mount_row_head_inclined[j].grid()

    if (option1 == 'One' and option2 == 'Vertical'):
        no_mount_rows = 1
        return inner_table(1, 1)
    if (option1 == 'Two' and option2 == 'Vertical'):
        no_mount_rows = 2
        return inner_table(2, 2)
    if (option1 == 'Three' and option2 == 'Vertical'):
        no_mount_rows = 3
        return inner_table(3, 3)
    if (option1 == 'Four' and option2 == 'Vertical'):
        no_mount_rows = 4
        return inner_table(4, 4)

    if (option1 == 'One' and option2 == 'Inclined'):
        no_mount_rows = 1
        return inner_table(1, 1)
    if (option1 == 'Two' and option2 == 'Inclined'):
        no_mount_rows = 2
        return inner_table(2, 2)
    if (option1 == 'Three' and option2 == 'Inclined'):
        no_mount_rows = 3
        return inner_table(3, 3)
    if (option1 == 'Four' and option2 == 'Inclined'):
        no_mount_rows = 4
        return inner_table(4, 4)


# print(option1,option2)


global no_mount_rows
no_mount_rows = 4
# taking data via file
load_frame = Frame(root, highlightbackground="grey", highlightcolor="grey", highlightthickness=1, width=700, height=100,
                   bd=0, pady=4)
load_frame.grid(row=1, sticky=W)

load_label = Label(load_frame, text='Load Configuration File')
load_label.grid(row=0, column=0, padx=(1, 1), sticky=W)

path_text = StringVar()
# load_icon = PhotoImage(file = 'open2.png')
# load_icon_resize = load_icon.subsample(3,3)
load_entry = Entry(load_frame, textvariable=path_text)
load_entry.grid(row=0, column=1, ipadx=100)
# load_button = Button(load_frame,image = load_icon,height = 10,width = 15,command = lambda: open_file(path_text))
# load_button.grid(row = 0,column = 1,padx = (300,1))

open_button = Button(load_frame, text="Browse", command=lambda: open_file(path_text))
open_button.grid(row=0, column=2, padx=(1, 50))

load_button = Button(load_frame, text="Load", width=10)
load_button.grid(row=0, column=3, padx=(50, 2))

# enter data manually radio button
data_radio_button = Radiobutton(root, text='Enter Data Manually', pady=4, variable=Radiobutton_var, value=2,
                                command=radiobutton_fun)
data_radio_button.grid(row=2, column=0, sticky=W)

# manual data frame...............................frame1
global data_frame
data_frame = LabelFrame(root, text="Power Train Configuration", fg="blue", highlightbackground="grey",
                        highlightcolor="grey", highlightthickness=1, height=400, bd=0)
data_frame.grid(row=4, sticky=W)

# ................................................frame2
data_configuration_frame = Frame(data_frame, highlightbackground="grey", highlightcolor="grey", highlightthickness=1,
                                 height=100, bd=0)
data_configuration_frame.grid(row=1, sticky=W)

# power train configuration
data_heading1_label = Label(data_configuration_frame, text="Power Train Configuration")
data_heading1_label.grid(row=0, column=0, padx=(1, 1), pady=3, sticky=W)

data_heading2_label = Label(data_configuration_frame, text="Power Train Type")
data_heading2_label.grid(row=1, column=0, pady=3, sticky=W)

option = StringVar(data_configuration_frame)
option.set("Transverse")
data_heading2_drop_down = ttk.Combobox(data_configuration_frame, textvariable=option, width=12)
data_heading2_drop_down['values'] = ("Transverse", "Longitudinal")
data_heading2_drop_down.grid(row=1, column=0, pady=3, padx=(150, 1))
data_heading2_drop_down.current(1)

data_heading3_label = Label(data_configuration_frame, text="Power Train Mass (Kg)")
data_heading3_label.grid(row=2, column=0, pady=3, sticky=W)

data_heading3_entry = Entry(data_configuration_frame, width=12)
data_heading3_entry.grid(row=2, column=0, padx=(150, 1), pady=3)

# mount data
mount_data_heading1_label = Label(data_configuration_frame, text="Mount Data", justify='left')
mount_data_heading1_label.grid(row=0, column=1, padx=(1, 110), pady=3)

mount_data_heading2_label = Label(data_configuration_frame, text="Number of Engine Mount", justify='left')
mount_data_heading2_label.grid(row=1, column=1, padx=(1, 20), pady=3)

global mount_option1
# mount_option1 = StringVar(data_configuration_frame)
# mount_option1.set("Four")
global mount_option2
# mount_option2 = StringVar(data_configuration_frame)
# mount_option2.set("Inclined")
mount_option1 = StringVar(data_configuration_frame)
mount_option2 = StringVar(data_configuration_frame)
# mount_data_heading2_drop_down = OptionMenu(data_configuration_frame,mount_option1,"One","Two","Three","Four",command = num_of_mountings)
# mount_data_heading2_drop_down.grid(row = 1,column = 1,padx = (270, 1),pady = 3)
mount_data_heading2_drop_down = ttk.Combobox(data_configuration_frame, width=9, textvariable=mount_option1)
mount_data_heading2_drop_down['values'] = ("One", "Two", "Three", "Four")
mount_data_heading2_drop_down.grid(row=1, column=1, padx=(270, 1), pady=3)
mount_data_heading2_drop_down.current(3)
mount_data_heading2_drop_down.bind('<<ComboboxSelected>>', num_of_mountings)
print(mount_option1.get())

mount_data_heading3_drop_down = ttk.Combobox(data_configuration_frame, width=9, textvariable=mount_option2)
mount_data_heading3_drop_down['values'] = ("Vertical", "Inclined")
mount_data_heading3_drop_down.grid(row=2, column=1, padx=(270, 1), pady=3)
mount_data_heading3_drop_down.current(1)
mount_data_heading3_drop_down.bind('<<ComboboxSelected>>', num_of_mountings)

data_heading4_label = Label(data_configuration_frame, text="Mount Type", justify='left')
data_heading4_label.grid(row=2, column=1, padx=(1, 110), pady=3)

# data_heading4_label = Label(data_frame,text = "Power Train Centre of Gravity(mm)",fg = "blue")
# data_heading4_label.grid(row = 2,column = 0,padx = (1, 470),pady = 3)

# data_heading5_label = Label(data_frame,text = "Crank shaft/Load Axis Direction",fg = "blue")
# data_heading5_label.grid(row = 2,column = 0,padx = (1, 1),pady = 3)

# ...............................................frame3
data_gravity_main_frame = Frame(data_frame, width=600, height=90)
data_gravity_main_frame.grid(row=3, sticky=W)
data_gravity_frame1 = LabelFrame(data_gravity_main_frame, text="Power Train Centre of Gravity(mm)", fg="blue",
                                 highlightbackground="grey", highlightcolor="grey", highlightthickness=1, width=250,
                                 height=80, bd=0)
data_gravity_frame1.grid(row=0, column=0, pady=5, sticky=W)

x_axis_label = Label(data_gravity_frame1, text='X')
x_axis_label.grid(row=0, column=0, padx=(1, 180), pady=4)
y_axis_label = Label(data_gravity_frame1, text='Y')
y_axis_label.grid(row=0, column=0, padx=(1, 55), pady=4)
z_axis_label = Label(data_gravity_frame1, text='Z')
z_axis_label.grid(row=0, column=0, padx=(80, 1), pady=4)

x_axis_entry = Entry(data_gravity_frame1, width=8)
x_axis_entry.grid(row=1, column=0, padx=(1, 130), pady=(1, 10))
y_axis_entry = Entry(data_gravity_frame1, width=8)
y_axis_entry.grid(row=1, column=0, padx=(1, 1), pady=(1, 10))
z_axis_entry = Entry(data_gravity_frame1, width=8)
z_axis_entry.grid(row=1, column=0, padx=(130, 1), pady=(1, 10))

data_axis_frame2 = LabelFrame(data_gravity_main_frame, text="Crank shaft/Load Axis Direction", fg="blue",
                              highlightbackground="grey", highlightcolor="grey", highlightthickness=1, width=200,
                              height=80, bd=0)
data_axis_frame2.grid(row=0, column=1, pady=5, padx=(15, 1), columnspan=6)

x_axis_label1 = Label(data_axis_frame2, text='X')
x_axis_label1.grid(row=0, column=0, padx=(1, 180), pady=4)
y_axis_label1 = Label(data_axis_frame2, text='Y')
y_axis_label1.grid(row=0, column=0, padx=(1, 55), pady=4)
z_axis_label1 = Label(data_axis_frame2, text='Z')
z_axis_label1.grid(row=0, column=0, padx=(80, 1), pady=4)

x_axis_entry1 = Entry(data_axis_frame2, width=8)
x_axis_entry1.grid(row=1, column=0, padx=(1, 130), pady=(1, 10))
y_axis_entry1 = Entry(data_axis_frame2, width=8)
y_axis_entry1.grid(row=1, column=0, padx=(1, 1), pady=(1, 10))
z_axis_entry1 = Entry(data_axis_frame2, width=8)
z_axis_entry1.grid(row=1, column=0, padx=(130, 1), pady=(1, 10))

# data_heading6_label= Label(data_frame,text = 'Power Train Inertia(Kg-mm^2)',fg = "blue")
# data_heading6_label.grid(row = 4,column = 0,padx = (1,494),pady = 4)

# ....................................... inertia frmae..............#
data_inertia_frame = LabelFrame(data_frame, text='Power Train Inertia(Kg-mm^2)', fg="blue", highlightbackground="grey",
                                highlightcolor="grey", highlightthickness=1, width=600, height=100)
data_inertia_frame.grid(row=5, padx=(1, 450), sticky=W)

ixx_axis_label1 = Label(data_inertia_frame, text='Ixx')
ixx_axis_label1.grid(row=0, column=0, padx=(1, 180), pady=4)
ixy_axis_label1 = Label(data_inertia_frame, text='Ixy')
ixy_axis_label1.grid(row=0, column=0, padx=(1, 55), pady=4)
ixz_axis_label1 = Label(data_inertia_frame, text='Ixz')
ixz_axis_label1.grid(row=0, column=0, padx=(80, 1), pady=4)

ixx_axis_entry = Entry(data_inertia_frame, width=8)
ixx_axis_entry.grid(row=1, column=0, padx=(1, 130), pady=(1, 10))
ixy_axis_entry = Entry(data_inertia_frame, width=8)
ixy_axis_entry.grid(row=1, column=0, padx=(1, 1), pady=(1, 10))
ixz_axis_entry = Entry(data_inertia_frame, width=8)
ixz_axis_entry.grid(row=1, column=0, padx=(130, 1), pady=(1, 10))

# .........
iyx_axis_label1 = Label(data_inertia_frame, text='Iyx')
iyx_axis_label1.grid(row=2, column=0, padx=(1, 180), pady=4)
iyy_axis_label1 = Label(data_inertia_frame, text='Iyy')
iyy_axis_label1.grid(row=2, column=0, padx=(1, 55), pady=4)
iyz_axis_label1 = Label(data_inertia_frame, text='Iyz')
iyz_axis_label1.grid(row=2, column=0, padx=(80, 1), pady=4)

iyx_axis_entry = Entry(data_inertia_frame, width=8)
iyx_axis_entry.grid(row=3, column=0, padx=(1, 130), pady=(1, 10))
iyy_axis_entry = Entry(data_inertia_frame, width=8)
iyy_axis_entry.grid(row=3, column=0, padx=(1, 1), pady=(1, 10))
iyz_axis_entry = Entry(data_inertia_frame, width=8)
iyz_axis_entry.grid(row=3, column=0, padx=(130, 1), pady=(1, 10))

# ...............
izx_axis_label1 = Label(data_inertia_frame, text='Izx')
izx_axis_label1.grid(row=4, column=0, padx=(1, 180), pady=4)
izy_axis_label1 = Label(data_inertia_frame, text='Izy')
izy_axis_label1.grid(row=4, column=0, padx=(1, 55), pady=4)
izz_axis_label1 = Label(data_inertia_frame, text='Izz')
izz_axis_label1.grid(row=4, column=0, padx=(80, 1), pady=4)

izx_axis_entry = Entry(data_inertia_frame, width=8)
izx_axis_entry.grid(row=5, column=0, padx=(1, 130), pady=(1, 10))
izy_axis_entry = Entry(data_inertia_frame, width=8)
izy_axis_entry.grid(row=5, column=0, padx=(1, 1), pady=(1, 10))
izz_axis_entry = Entry(data_inertia_frame, width=8)
izz_axis_entry.grid(row=5, column=0, padx=(130, 1), pady=(1, 10))

# .............................Mounting system frame.....................
data_mounting_frame = LabelFrame(data_frame, text='Mounting System', fg="blue", width=600, height=200)
data_mounting_frame.grid(row=6, padx=(1, 230), pady=4)

# table column heading content # we need change for updation of col names
global col_head
col_head = ['', 'Mount1', 'Mount2', 'Mount3', 'Mount4']
global head
head = [' ', 'X(mm)', 'Y(mm)', 'Z(mm)', 'Kx(N/mm)', 'Ky(N/mm)', 'Kz(N/mm)']
global head2
head2 = ['Roll(Nm)', 'Pitch(Nm)', 'Yaw(Nm)']

global mount_table_col_10
global mount_table_col_20
global mount_table_col_30
global mount_table_col_40
global mount_table_entry_11
global mount_table_entry_12
global mount_table_entry_13
global mount_table_entry_14
global mount_table_entry_15
global mount_table_entry_16
global mount_table_entry_21
global mount_table_entry_22
global mount_table_entry_23
global mount_table_entry_24
global mount_table_entry_25
global mount_table_entry_26
global mount_table_entry_31
global mount_table_entry_32
global mount_table_entry_33
global mount_table_entry_34
global mount_table_entry_35
global mount_table_entry_36
global mount_table_entry_41
global mount_table_entry_42
global mount_table_entry_43
global mount_table_entry_44
global mount_table_entry_45
global mount_table_entry_46
global mount_table_row_07
global mount_table_row_08
global mount_table_row_09
global mount_table_entry_17
global mount_table_entry_18
global mount_table_entry_19
global mount_table_entry_27
global mount_table_entry_28
global mount_table_entry_29
global mount_table_entry_37
global mount_table_entry_38
global mount_table_entry_39
global mount_table_entry_47
global mount_table_entry_48
global mount_table_entry_49
# constant
mount_table_row_00 = Label(data_mounting_frame, text=head[0], width=9, relief=RAISED)
mount_table_row_00.grid(row=0, column=0)
mount_table_row_01 = Label(data_mounting_frame, text=head[1], width=9, relief=SUNKEN)
mount_table_row_01.grid(row=0, column=1)
mount_table_row_02 = Label(data_mounting_frame, text=head[2], width=9, relief=SUNKEN)
mount_table_row_02.grid(row=0, column=2)
mount_table_row_03 = Label(data_mounting_frame, text=head[3], width=9, relief=SUNKEN)
mount_table_row_03.grid(row=0, column=3)
mount_table_row_04 = Label(data_mounting_frame, text=head[4], width=9, relief=SUNKEN)
mount_table_row_04.grid(row=0, column=4)
mount_table_row_05 = Label(data_mounting_frame, text=head[4], width=9, relief=SUNKEN)
mount_table_row_05.grid(row=0, column=5)
mount_table_row_06 = Label(data_mounting_frame, text=head[6], width=9, relief=SUNKEN)
mount_table_row_06.grid(row=0, column=6)
# variable
mount_table_row_07 = Label(data_mounting_frame, text=head2[0], width=9, relief=SUNKEN)
mount_table_row_07.grid(row=0, column=7)
mount_table_row_08 = Label(data_mounting_frame, text=head2[1], width=9, relief=SUNKEN)
mount_table_row_08.grid(row=0, column=8)
mount_table_row_09 = Label(data_mounting_frame, text=head2[2], width=9, relief=SUNKEN)
mount_table_row_09.grid(row=0, column=9)
global mount_tab_row_inlined_head
mount_tab_row_inlined_head = [mount_table_row_07, mount_table_row_08, mount_table_row_09]
# variable
mount_table_col_00 = Label(data_mounting_frame, text=col_head[0])
mount_table_col_00.grid(row=0, column=0)
mount_table_col_10 = Label(data_mounting_frame, text=col_head[1], width=9, relief=RAISED)
mount_table_col_10.grid(row=1, column=0)
mount_table_col_20 = Label(data_mounting_frame, text=col_head[2], width=9, relief=RAISED)
mount_table_col_20.grid(row=2, column=0)
mount_table_col_30 = Label(data_mounting_frame, text=col_head[3], width=9, relief=RAISED)
mount_table_col_30.grid(row=3, column=0)
mount_table_col_40 = Label(data_mounting_frame, text=col_head[4], width=9, relief=RAISED)
mount_table_col_40.grid(row=4, column=0)

global col_tab
col_tab = [mount_table_col_10, mount_table_col_20, mount_table_col_30, mount_table_col_40]
# variable
mount_table_entry_11 = Entry(data_mounting_frame, text="", width=9)
mount_table_entry_11.grid(row=1, column=1)
mount_table_entry_12 = Entry(data_mounting_frame, text="", width=9)
mount_table_entry_12.grid(row=1, column=2)
mount_table_entry_13 = Entry(data_mounting_frame, text="", width=9)
mount_table_entry_13.grid(row=1, column=3)
mount_table_entry_14 = Entry(data_mounting_frame, text="", width=9)
mount_table_entry_14.grid(row=1, column=4)
mount_table_entry_15 = Entry(data_mounting_frame, text="", width=9)
mount_table_entry_15.grid(row=1, column=5)
mount_table_entry_16 = Entry(data_mounting_frame, text="", width=9)
mount_table_entry_16.grid(row=1, column=6)
mount_table_entry_21 = Entry(data_mounting_frame, text="", width=9)
mount_table_entry_21.grid(row=2, column=1)
mount_table_entry_22 = Entry(data_mounting_frame, text="", width=9)
mount_table_entry_22.grid(row=2, column=2)
mount_table_entry_23 = Entry(data_mounting_frame, text="", width=9)
mount_table_entry_23.grid(row=2, column=3)
mount_table_entry_24 = Entry(data_mounting_frame, text="", width=9)
mount_table_entry_24.grid(row=2, column=4)
mount_table_entry_25 = Entry(data_mounting_frame, text="", width=9)
mount_table_entry_25.grid(row=2, column=5)
mount_table_entry_26 = Entry(data_mounting_frame, text="", width=9)
mount_table_entry_26.grid(row=2, column=6)
mount_table_entry_31 = Entry(data_mounting_frame, text="", width=9)
mount_table_entry_31.grid(row=3, column=1)
mount_table_entry_32 = Entry(data_mounting_frame, text="", width=9)
mount_table_entry_32.grid(row=3, column=2)
mount_table_entry_33 = Entry(data_mounting_frame, text="", width=9)
mount_table_entry_33.grid(row=3, column=3)
mount_table_entry_34 = Entry(data_mounting_frame, text="", width=9)
mount_table_entry_34.grid(row=3, column=4)
mount_table_entry_35 = Entry(data_mounting_frame, text="", width=9)
mount_table_entry_35.grid(row=3, column=5)
mount_table_entry_36 = Entry(data_mounting_frame, text="", width=9)
mount_table_entry_36.grid(row=3, column=6)
mount_table_entry_41 = Entry(data_mounting_frame, text="", width=9)
mount_table_entry_41.grid(row=4, column=1)
mount_table_entry_42 = Entry(data_mounting_frame, text="", width=9)
mount_table_entry_42.grid(row=4, column=2)
mount_table_entry_43 = Entry(data_mounting_frame, text="", width=9)
mount_table_entry_43.grid(row=4, column=3)
mount_table_entry_44 = Entry(data_mounting_frame, text="", width=9)
mount_table_entry_44.grid(row=4, column=4)
mount_table_entry_45 = Entry(data_mounting_frame, text="", width=9)
mount_table_entry_45.grid(row=4, column=5)
mount_table_entry_46 = Entry(data_mounting_frame, text="", width=9)
mount_table_entry_46.grid(row=4, column=6)

mount_tab_col_list = [mount_table_row_00, mount_table_row_01, mount_table_row_02, mount_table_row_03,
                      mount_table_row_04,
                      mount_table_row_05, mount_table_row_06, mount_table_row_07, mount_table_row_08,
                      mount_table_row_09,
                      mount_table_col_00, mount_table_col_10, mount_table_col_20, mount_table_col_30,
                      mount_table_col_40]
global mount_entry_tab
mount_entry_tab = [mount_table_entry_11, mount_table_entry_12, mount_table_entry_13, mount_table_entry_14,
                   mount_table_entry_15, mount_table_entry_16,
                   mount_table_entry_21, mount_table_entry_22, mount_table_entry_23, mount_table_entry_24,
                   mount_table_entry_25, mount_table_entry_26,
                   mount_table_entry_31, mount_table_entry_32, mount_table_entry_33, mount_table_entry_34,
                   mount_table_entry_35, mount_table_entry_36,
                   mount_table_entry_41, mount_table_entry_42, mount_table_entry_43, mount_table_entry_44,
                   mount_table_entry_45, mount_table_entry_46,
                   ]

mount_table_entry_17 = Entry(data_mounting_frame, text="", width=9)
mount_table_entry_17.grid(row=1, column=7)
mount_table_entry_18 = Entry(data_mounting_frame, text="", width=9)
mount_table_entry_18.grid(row=1, column=8)
mount_table_entry_19 = Entry(data_mounting_frame, text="", width=9)
mount_table_entry_19.grid(row=1, column=9)
mount_table_entry_27 = Entry(data_mounting_frame, text="", width=9)
mount_table_entry_27.grid(row=2, column=7)
mount_table_entry_28 = Entry(data_mounting_frame, text="", width=9)
mount_table_entry_28.grid(row=2, column=8)
mount_table_entry_29 = Entry(data_mounting_frame, text="", width=9)
mount_table_entry_29.grid(row=2, column=9)
mount_table_entry_37 = Entry(data_mounting_frame, text="", width=9)
mount_table_entry_37.grid(row=3, column=7)
mount_table_entry_38 = Entry(data_mounting_frame, text="", width=9)
mount_table_entry_38.grid(row=3, column=8)
mount_table_entry_39 = Entry(data_mounting_frame, text="", width=9)
mount_table_entry_39.grid(row=3, column=9)
mount_table_entry_47 = Entry(data_mounting_frame, text="", width=9)
mount_table_entry_47.grid(row=4, column=7)
mount_table_entry_48 = Entry(data_mounting_frame, text="", width=9)
mount_table_entry_48.grid(row=4, column=8)
mount_table_entry_49 = Entry(data_mounting_frame, text="", width=9)
mount_table_entry_49.grid(row=4, column=9)

global mount_row_head_inclined
mount_row_head_inclined = [mount_table_entry_17, mount_table_entry_18, mount_table_entry_19,
                           mount_table_entry_27, mount_table_entry_28, mount_table_entry_29,
                           mount_table_entry_37, mount_table_entry_38, mount_table_entry_39,
                           mount_table_entry_47, mount_table_entry_48, mount_table_entry_49, ]

axis_list = [x_axis_label, y_axis_label, z_axis_label, x_axis_entry, y_axis_entry, z_axis_entry,
             x_axis_label1, y_axis_label1, z_axis_label1, x_axis_entry1, y_axis_entry1, z_axis_entry1]
moment_axis_list = [ixx_axis_label1, ixy_axis_label1, ixz_axis_label1, ixx_axis_entry, ixy_axis_entry, ixz_axis_entry,
                    iyx_axis_label1, iyy_axis_label1, iyz_axis_label1, iyx_axis_entry, iyy_axis_entry, iyz_axis_entry,
                    izx_axis_label1, izy_axis_label1, izz_axis_label1, izx_axis_entry, izy_axis_entry, izz_axis_entry]

rem_list = [load_entry, load_button, load_label, open_button, load_button, data_heading1_label, data_heading2_label,
            data_heading2_drop_down, data_heading3_label, data_heading3_entry, mount_data_heading1_label,
            mount_data_heading2_label, mount_data_heading2_drop_down, mount_data_heading3_drop_down,
            data_heading4_label]

visualize_button = Button(root, text='Visualize', width=10)
visualize_button.grid(row=7, column=0, sticky=W, pady=(4, 4))
save_button = Button(root, text='Save', width=10)
save_button.grid(row=7, column=0, pady=(4, 4), padx=(250, 1))
apply_button = Button(root, text='Apply', width=10)
apply_button.grid(row=7, column=0, pady=(4, 4), padx=(455, 1))

root.mainloop()
