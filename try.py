#%%
import os
import main as mn

import PySimpleGUI as sg

sg.theme('Dark Blue 3')  # please make your windows colorful

sg.set_options(font = 'Default 18', keep_on_top=True)


max_filename_length = int(20)

name_list = ['bolt_cmvu3e',
            'bolt_cddcb2az',
            'bolt_kveirbh',
            'doodad_pcawexfc',
            'doodad_qpv9213',
            'doodad_mbnqlgd37',
            'doodad_mwgeg',
            'whirlygig_vkbwbw',
            'whirlygig_qkenfiv3',
            'whirlygig_bnejkw0',
            'whirlygig_rrmew',
            'whirlygig_vmecq3']



mn.create_files_for_test(name_list)

name_table =    [
                    ['bolt_cmvu3e.txt','bolt_Sample1.txt'],
                    ['bolt_cddcb2az.txt','bolt_Sample2.txt']
                ]
name_table_headings = ['current name','new name']

initial_table = [[]]

# table = sg.Table(name_table, name_table_headings,enable_events=True,key='-TABLE-')
table = sg.Table(initial_table, enable_events=True,key='-TABLE-')



layout = [
            [sg.FolderBrowse(button_text='Select folder', key='-FOLDER-'), sg.Text()],
            # [table],
            [sg.Text(size = (max_filename_length,1), key='-HEADER1-'), sg.Text(size = (max_filename_length,1), key='-HEADER2-'), sg.Text(size = (max_filename_length,1), key='-HEADER3-')],
            [sg.Text(size = (max_filename_length,1), key='-NAME1-'), sg.Input(size = (max_filename_length,1), key='-IN1-', enable_events=True), sg.Text(size = (max_filename_length,1), key='-OUT1-')],
            # [sg.Text('Your typed chars appear here:'), sg.Text(size=(20,1), )],
            # [sg.Input(key='-IN-')],
            [sg.Button('read filenames in folder')],
            [sg.Button('copy input to output')],
            [sg.Button('Exit')]
        ]

window = sg.Window('File Rename', layout)



while True:  # Event Loop
    event, values = window.read()
    print(event, values)
    if event == sg.WIN_CLOSED or event == 'Exit':
        break
    elif event == 'read filenames in folder':
        if os.path.exists(values['-FOLDER-']):
            old_names_col = os.listdir(values['-FOLDER-'])
            no_rows = len(old_names_col)
            """create layout with no_rows.  each row should have names displayed"""
            table.update(old_names_col)
        else:
            print("The system cannot find the path specified: ''")
    elif event == '-IN1-':
        window['-OUT1-'].update(values['-IN1-'])
        print()
    elif event == 'copy input to output':
        window['-OUT1-'].update(values['-IN1-'])
window.close()
# %%
