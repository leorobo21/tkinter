# importing modules
from tkinter import *
from tkinter.filedialog import askopenfilename
from tkinter import ttk

# defining main window
root = Tk()
root.geometry('710x600')
root.title('NVH Loads')


def open_file(text):
    file = askopenfilename(filetypes=[('all files', '*.*')], title="choose a file")
    text.set(file)
    return file


tab_parent = ttk.Notebook(root)

tab1 = Frame(tab_parent)
tab2 = Frame(tab_parent)

tab_parent.add(tab1, text="Road Loads")
tab_parent.add(tab2, text="Engine Loads")

tab_parent.grid(row=0, sticky=W)

global_frame = Frame(root, highlightbackground="grey", highlightcolor="grey", highlightthickness=1, bd=0)
global_frame.grid(row=1)

Engine_configuration_frame = LabelFrame(global_frame, text="Engine Configuration", fg="blue",
                                        highlightbackground="grey",
                                        highlightcolor="grey", highlightthickness=0, height=400, bd=1)
Engine_configuration_frame.grid(row=1, sticky=W)

type_of_engine_label = Label(Engine_configuration_frame, text='Type of Engine')
type_of_engine_label.grid(row=0, column=0, sticky=W)

type_of_engine_option = StringVar(Engine_configuration_frame)
type_of_engine_option.set("Inline")
type_of_engine_drop_down = ttk.Combobox(Engine_configuration_frame, textvariable=type_of_engine_option, width=12)
type_of_engine_drop_down['values'] = ("Inline", "Inclined")
type_of_engine_drop_down.grid(row=0, column=1, pady=3, padx=(1, 1))
# type_of_engine_drop_down.current(1)


num_of_cylinders_label = Label(Engine_configuration_frame, text='Number of Cylinders')
num_of_cylinders_label.grid(row=0, column=2, sticky=W, padx=(1, 1))

num_cylinders_option = StringVar(Engine_configuration_frame)
num_cylinders_option.set(4)
num_cylinders_drop_down = ttk.Combobox(Engine_configuration_frame, width=9, textvariable=num_cylinders_option)
num_cylinders_drop_down['values'] = (1, 2, 3, 4)
num_cylinders_drop_down.grid(row=0, column=3, padx=(1, 1), pady=3)
# num_cylinders_drop_down.current(3)s
# num_cylinders_drop_down.bind('<<ComboboxSelected>>',num_of_mountings)


firing_order_label = Label(Engine_configuration_frame, text='Firing Order')
firing_order_label.grid(row=0, column=4, sticky=W, padx=(9, 1))

firing_order_option = StringVar(Engine_configuration_frame)
firing_order_option.set('1-3-4-2')
num_cylinders_drop_down = ttk.Combobox(Engine_configuration_frame, width=9, textvariable=firing_order_option)
num_cylinders_drop_down['values'] = ('1-2-3-4', '2-4-5-6', '1-3-4-2')
num_cylinders_drop_down.grid(row=0, column=5, padx=(20, 20), pady=(3, 1))
# num_cylinders_drop_down.current(3)


entry_frame = ttk.Frame(Engine_configuration_frame)
entry_frame.grid(row=1, columnspan=4, pady=7)

combustion_profile_label = Label(entry_frame, text='Combustion Profile', justify='left')
combustion_profile_label.grid(row=0, column=0, sticky=W, padx=(7, 1))

path_text = StringVar()
load_icon = PhotoImage(file='open.png')
load_icon_resize = load_icon.subsample(3, 3)
load_entry = Entry(entry_frame, textvariable=path_text, width=9)
load_entry.grid(row=0, column=1, padx=(7, 1), ipadx=100)
load_button = Button(entry_frame, image=load_icon, height=10, width=15, command=lambda: open_file(path_text))
load_button.grid(row=0, column=2, padx=(1, 1))

# open_button = Button(entry_frame, text="Browse", command=lambda: open_file(path_text))
# open_button.grid(row=0, column=2, padx=(1, 1))


Engine_parameters_frame = LabelFrame(global_frame, text="Engine Parameters", fg="blue", highlightbackground="grey",
                                     highlightcolor="grey", highlightthickness=0, height=400, bd=1)
Engine_parameters_frame.grid(row=2, sticky=W, pady=4)

bore_diameter_label = Label(Engine_parameters_frame, text='Bore Diameter')
bore_diameter_label.grid(row=0, column=0, sticky=W, padx=(7, 7))
bore_diameter_entry = Entry(Engine_parameters_frame, textvariable=path_text, width=14)
bore_diameter_entry.grid(row=0, column=1, padx=(7, 1))
engine_stroke_label = Label(Engine_parameters_frame, text='Engine Stroke')
engine_stroke_label.grid(row=0, column=2, sticky=W, padx=(7, 7))
engine_stroke_entry = Entry(Engine_parameters_frame, textvariable=path_text, width=14)
engine_stroke_entry.grid(row=0, column=3, padx=(7, 1))
crank_pin_radius_label = Label(Engine_parameters_frame, text='Crank Pin Radius')
crank_pin_radius_label.grid(row=0, column=4, sticky=W, padx=(7, 7))
crank_pin_radius_entry = Entry(Engine_parameters_frame, textvariable=path_text, width=14)
crank_pin_radius_entry.grid(row=0, column=5, padx=(7, 1))

con_rod_len_label = Label(Engine_parameters_frame, text='Con. Rod Length')
con_rod_len_label.grid(row=1, column=0, sticky=W, padx=(7, 7), pady=4)
con_rod_len_entry = Entry(Engine_parameters_frame, textvariable=path_text, width=14)
con_rod_len_entry.grid(row=1, column=1, padx=(7, 1), pady=4)
con_rod_cg_label = Label(Engine_parameters_frame, text='Con. Rod CG')
con_rod_cg_label.grid(row=1, column=2, sticky=W, padx=(7, 7), pady=4)
con_rod_cg_entry = Entry(Engine_parameters_frame, textvariable=path_text, width=14)
con_rod_cg_entry.grid(row=1, column=3, padx=(7, 1), pady=4)
con_rod_mass_label = Label(Engine_parameters_frame, text='Con. Rod Mass')
con_rod_mass_label.grid(row=1, column=4, sticky=W, padx=(7, 7), pady=4)
con_rod_mass_entry = Entry(Engine_parameters_frame, textvariable=path_text, width=14)
con_rod_mass_entry.grid(row=1, column=5, padx=(7, 1), pady=4)

piston_mass_label = Label(Engine_parameters_frame, text='Piston Mass')
piston_mass_label.grid(row=2, column=0, sticky=W, padx=(7, 7), pady=4)
piston_mass_entry = Entry(Engine_parameters_frame, textvariable=path_text, width=14)
piston_mass_entry.grid(row=2, column=1, padx=(7, 1), pady=4)
crank_pin_mass_label = Label(Engine_parameters_frame, text='Crack Pin Mass')
crank_pin_mass_label.grid(row=2, column=2, sticky=W, padx=(7, 7), pady=4)
crank_pin_mass_entry = Entry(Engine_parameters_frame, textvariable=path_text, width=14)
crank_pin_mass_entry.grid(row=2, column=3, padx=(7, 1), pady=4)
crank_webs_button = Button(Engine_parameters_frame, text='Crank Webs & Counter Weights', width=30, bg='lightgreen')
crank_webs_button.grid(row=2, column=4, padx=(7, 1), pady=4, columnspan=2)

table_frame = Frame(Engine_parameters_frame)
table_frame.grid(row=3, columnspan=6)

head = ['Prop||WebNum', 1, 2, 3, 4, 5, 6, 7, 8]
# constant
engine_parameters_table_row_00 = Label(table_frame, text=head[0], width=19, relief=RAISED)
engine_parameters_table_row_00.grid(row=0, column=0, padx=(10, 1))
engine_parameters_table_row_01 = Label(table_frame, text=head[1], width=9, relief=SUNKEN)
engine_parameters_table_row_01.grid(row=0, column=1)
engine_parameters_table_row_02 = Label(table_frame, text=head[2], width=9, relief=SUNKEN)
engine_parameters_table_row_02.grid(row=0, column=2)
engine_parameters_table_row_03 = Label(table_frame, text=head[3], width=9, relief=SUNKEN)
engine_parameters_table_row_03.grid(row=0, column=3)
engine_parameters_table_row_04 = Label(table_frame, text=head[4], width=9, relief=SUNKEN)
engine_parameters_table_row_04.grid(row=0, column=4)
engine_parameters_table_row_05 = Label(table_frame, text=head[4], width=9, relief=SUNKEN)
engine_parameters_table_row_05.grid(row=0, column=5)
engine_parameters_table_row_06 = Label(table_frame, text=head[6], width=9, relief=SUNKEN)
engine_parameters_table_row_06.grid(row=0, column=6)
engine_parameters_table_row_07 = Label(table_frame, text=head[7], width=9, relief=SUNKEN)
engine_parameters_table_row_07.grid(row=0, column=7)
engine_parameters_table_row_08 = Label(table_frame, text=head[8], width=9, relief=SUNKEN)
engine_parameters_table_row_08.grid(row=0, column=8)

col_head = ['', 'CrankWebMass(kg)', 'CrankWebCG(mm)', 'CounterWeightMass(kg)', 'CounterWeightCG(mm)']

engine_parameters_table_col_10 = Label(table_frame, text=col_head[1], width=19, relief=SUNKEN)
engine_parameters_table_col_10.grid(row=1, column=0, padx=(10, 1))
engine_parameters_table_col_20 = Label(table_frame, text=col_head[2], width=19, relief=SUNKEN)
engine_parameters_table_col_20.grid(row=2, column=0, padx=(10, 1))
engine_parameters_table_col_30 = Label(table_frame, text=col_head[3], width=19, relief=SUNKEN)
engine_parameters_table_col_30.grid(row=3, column=0, padx=(10, 1))
engine_parameters_table_col_40 = Label(table_frame, text=col_head[4], width=19, relief=SUNKEN)
engine_parameters_table_col_40.grid(row=4, column=0, padx=(10, 1))

engine_parameters_table_entry_11 = Entry(table_frame, text="", width=9)
engine_parameters_table_entry_11.grid(row=1, column=1)
engine_parameters_table_entry_12 = Entry(table_frame, text="", width=9)
engine_parameters_table_entry_12.grid(row=1, column=2)
engine_parameters_table_entry_13 = Entry(table_frame, text="", width=9)
engine_parameters_table_entry_13.grid(row=1, column=3)
engine_parameters_table_entry_14 = Entry(table_frame, text="", width=9)
engine_parameters_table_entry_14.grid(row=1, column=4)
engine_parameters_table_entry_15 = Entry(table_frame, text="", width=9)
engine_parameters_table_entry_15.grid(row=1, column=5)
engine_parameters_table_entry_16 = Entry(table_frame, text="", width=9)
engine_parameters_table_entry_16.grid(row=1, column=6)
engine_parameters_table_entry_17 = Entry(table_frame, text="", width=9)
engine_parameters_table_entry_17.grid(row=1, column=7)
engine_parameters_table_entry_18 = Entry(table_frame, text="", width=9)
engine_parameters_table_entry_18.grid(row=1, column=8)
engine_parameters_table_entry_21 = Entry(table_frame, text="", width=9)
engine_parameters_table_entry_21.grid(row=2, column=1)
engine_parameters_table_entry_22 = Entry(table_frame, text="", width=9)
engine_parameters_table_entry_22.grid(row=2, column=2)
engine_parameters_table_entry_23 = Entry(table_frame, text="", width=9)
engine_parameters_table_entry_23.grid(row=2, column=3)
engine_parameters_table_entry_24 = Entry(table_frame, text="", width=9)
engine_parameters_table_entry_24.grid(row=2, column=4)
engine_parameters_table_entry_25 = Entry(table_frame, text="", width=9)
engine_parameters_table_entry_25.grid(row=2, column=5)
engine_parameters_table_entry_26 = Entry(table_frame, text="", width=9)
engine_parameters_table_entry_26.grid(row=2, column=6)
engine_parameters_table_entry_27 = Entry(table_frame, text="", width=9)
engine_parameters_table_entry_27.grid(row=2, column=7)
engine_parameters_table_entry_28 = Entry(table_frame, text="", width=9)
engine_parameters_table_entry_28.grid(row=2, column=8)
engine_parameters_table_entry_31 = Entry(table_frame, text="", width=9)
engine_parameters_table_entry_31.grid(row=3, column=1)
engine_parameters_table_entry_32 = Entry(table_frame, text="", width=9)
engine_parameters_table_entry_32.grid(row=3, column=2)
engine_parameters_table_entry_33 = Entry(table_frame, text="", width=9)
engine_parameters_table_entry_33.grid(row=3, column=3)
engine_parameters_table_entry_34 = Entry(table_frame, text="", width=9)
engine_parameters_table_entry_34.grid(row=3, column=4)
engine_parameters_table_entry_35 = Entry(table_frame, text="", width=9)
engine_parameters_table_entry_35.grid(row=3, column=5)
engine_parameters_table_entry_36 = Entry(table_frame, text="", width=9)
engine_parameters_table_entry_36.grid(row=3, column=6)
engine_parameters_table_entry_37 = Entry(table_frame, text="", width=9)
engine_parameters_table_entry_37.grid(row=3, column=7)
engine_parameters_table_entry_38 = Entry(table_frame, text="", width=9)
engine_parameters_table_entry_38.grid(row=3, column=8)
engine_parameters_table_entry_41 = Entry(table_frame, text="", width=9)
engine_parameters_table_entry_41.grid(row=4, column=1)
engine_parameters_table_entry_42 = Entry(table_frame, text="", width=9)
engine_parameters_table_entry_42.grid(row=4, column=2)
engine_parameters_table_entry_43 = Entry(table_frame, text="", width=9)
engine_parameters_table_entry_43.grid(row=4, column=3)
engine_parameters_table_entry_44 = Entry(table_frame, text="", width=9)
engine_parameters_table_entry_44.grid(row=4, column=4)
engine_parameters_table_entry_45 = Entry(table_frame, text="", width=9)
engine_parameters_table_entry_45.grid(row=4, column=5)
engine_parameters_table_entry_46 = Entry(table_frame, text="", width=9)
engine_parameters_table_entry_46.grid(row=4, column=6)
engine_parameters_table_entry_47 = Entry(table_frame, text="", width=9)
engine_parameters_table_entry_47.grid(row=4, column=7)
engine_parameters_table_entry_48 = Entry(table_frame, text="", width=9)
engine_parameters_table_entry_48.grid(row=4, column=8)

engine_parameters_table_button = Button(Engine_parameters_frame, text='Apply', width=9)
engine_parameters_table_button.grid(row=4, column=5, padx=(7, 1), pady=4, sticky=E)

analysis_parameters_frame = LabelFrame(global_frame, text="Analysis Parameters", fg="blue", highlightbackground="grey",
                                       highlightcolor="grey", highlightthickness=0, height=400, bd=1)
analysis_parameters_frame.grid(row=3, sticky=W, pady=4)

analysis_frame = ttk.Frame(analysis_parameters_frame)
analysis_frame.grid(column=0, row=0, pady=5)

choose_option = IntVar()
constant_rpm_option = ttk.Radiobutton(analysis_frame, text='Constant RPM', variable=choose_option, value=0)
constant_rpm_option.grid(row=0)
sweep_analysis_option = ttk.Radiobutton(analysis_frame, text='Sweep Analysis', variable=choose_option, value=1)
sweep_analysis_option.grid(row=1)

ttk.Separator(analysis_frame, orient=VERTICAL).grid(column=1, row=0, rowspan=3, sticky='ns')

analysis_frame2 = ttk.Frame(analysis_parameters_frame)
analysis_frame2.grid(row=0, column=2, pady=5, columnspan=5)

engine_rpm_label = Label(analysis_frame2, text='Engine RPM')
engine_rpm_label.grid(row=0, column=0, sticky=W, padx=(7, 7))
engine_rpm_entry = Entry(analysis_frame2, textvariable=path_text, width=14)
engine_rpm_entry.grid(row=0, column=1, padx=(7, 1))
num_cycles_label = Label(analysis_frame2, text='Num. Cycles')
num_cycles_label.grid(row=0, column=2, sticky=W, padx=(7, 7))
num_cycles_entry = Entry(analysis_frame2, textvariable=path_text, width=14)
num_cycles_entry.grid(row=0, column=3, padx=(7, 1))
num_cycles_or_points_label = Label(analysis_frame2, text='Num. Points/Cycles')
num_cycles_or_points_label.grid(row=0, column=4, sticky=W, padx=(7, 7))
num_cycles_or_points_entry = Entry(analysis_frame2, textvariable=path_text, width=14)
num_cycles_or_points_entry.grid(row=0, column=5, padx=(7, 1))

analysis_apply_button = Button(analysis_frame2, text='Apply', justify='center', width=10)
analysis_apply_button.grid(row=1, column=5, pady=4)

calculations_frame = LabelFrame(global_frame, text="Calculations", fg="blue", highlightbackground="grey",
                                highlightcolor="grey", highlightthickness=0, height=400, bd=1)
calculations_frame.grid(row=4, sticky=W, pady=4, columnspan=6)

sub_calculations_frame1 = ttk.Frame(calculations_frame)
sub_calculations_frame1.grid(column=0, row=0, pady=5)

check_button = IntVar()
time_domain_check_button = Checkbutton(sub_calculations_frame1, text='Time Domain', variable=check_button,
                                       justify='left')
time_domain_check_button.grid(row=0, sticky=W)
frequency_domain_check_button = Checkbutton(sub_calculations_frame1, text='Frequency Domain', variable=check_button,
                                            justify='left')
frequency_domain_check_button.grid(row=1, sticky=W)

ttk.Separator(sub_calculations_frame1, orient=VERTICAL).grid(column=1, row=0, rowspan=3, sticky='ns')

sub_calculations_frame2 = ttk.Frame(calculations_frame)
sub_calculations_frame2.grid(column=2, row=0, pady=5, columnspan=6)

time_domain_path_label = Label(sub_calculations_frame2, text='Time-Domain Results Location', justify='left')
time_domain_path_label.grid(row=0, column=0, sticky=W, padx=(7, 7), pady=3)

time_domain_path = StringVar()
load_icon1 = PhotoImage(file='open.png')
load_icon1_resize = load_icon.subsample(3, 3)
time_domain_path_entry = Entry(sub_calculations_frame2, textvariable=time_domain_path, width=9)
time_domain_path_entry.grid(row=0, column=1, padx=(7, 1), ipadx=125, columnspan=2, pady=3)
time_domain_path_button = Button(sub_calculations_frame2, image=load_icon, height=10, width=15)
time_domain_path_button.grid(row=0, column=4, padx=(1, 1), pady=3)

frequency_domain_path_label = Label(sub_calculations_frame2, text='Frequency-Domain Results Location', justify='left')
frequency_domain_path_label.grid(row=1, column=0, sticky=W, padx=(7, 7), pady=3)

frequency_domain_path = StringVar()
load_icon2 = PhotoImage(file='open.png')
load_icon2_resize = load_icon.subsample(3, 3)
frequency_domain_path_entry = Entry(sub_calculations_frame2, textvariable=time_domain_path, width=9)
frequency_domain_path_entry.grid(row=1, column=1, padx=(7, 1), ipadx=125, columnspan=2, pady=3)
frequency_domain_path_button = Button(sub_calculations_frame2, image=load_icon, height=10, width=15)
frequency_domain_path_button.grid(row=1, column=4, padx=(1, 1), pady=3)

interest_order_frame = Frame(global_frame)
interest_order_frame.grid(row=5, sticky=E, pady=4, columnspan=3)

interest_order_label = Label(interest_order_frame, text='Interest Order')
interest_order_label.grid(row=0, column=0, pady=3)
interest_order_entry = Entry(interest_order_frame, textvariable=time_domain_path, width=9)
interest_order_entry.grid(row=0, column=1, padx=(7, 1), pady=3)
interest_order_button = Button(interest_order_frame, text='Calculate')
interest_order_button.grid(row=0, column=2, padx=(7, 1), pady=3)

root.mainloop()
