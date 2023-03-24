import PySimpleGUI as sg
from pathlib import Path
import front

def first_window():
    layout = [
        [sg.Text('Choose XML files and Tag:')],
        [sg.Text('Enter directory', text_color='Red', key='_ENT_DIR_', visible=False)],
        [sg.Text('XML files:', size =(25, 1)), sg.Input(key='_FILES_'), sg.FilesBrowse(file_types = (("XML Files", "*.xml"), ("ALL Files", "*.*")), auto_size_button = False)],
        [sg.Text('Enter tag(s)', text_color='Red', key='_ENT_TAG_', visible=False)],
        [sg.Text('Tags (complete, case-sensitive, separate with ";", no spaces, only letters):', size =(25, 3)), sg.InputText(key='_TAG_')],
        [sg.Submit(), sg.Button('Restart'), sg.Cancel()]
    ]
    window = sg.Window('XML Tag Changer', layout)
    while True:
        event, values = window.read()
        if event == "Cancel" or event == sg.WIN_CLOSED:
            break
        if event == "Submit":
            if values['_FILES_'] != '':
                global paths
                paths = values['_FILES_'].split(';')
                if values['_TAG_'] != '':
                    global tags
                    tags = values['_TAG_'].split(';')
                    second_window()
                else:
                    window.Element('_ENT_TAG_').Update(visible=True)
            else:
                window.Element('_ENT_DIR_').Update(visible=True)
        if event == 'Restart':
            window.close()
            first_window()
    window.close()

def second_window():
    global path
    for path in paths:
        with open(path, 'r') as f:
            global data
            data = f.read()
        global tag
        for tag in tags:
            global open_tag
            global close_tag
            global idxs
            open_tag, close_tag, idxs = front.tag_counter(tag, data)
            global filename
            filename = Path(path).name
            global tags_in_file
            tags_in_file = front.tg_in_file(path)
            if open_tag in data and open_tag in tags_in_file:
                layout = [
                    [sg.Text('Match found in file Named "' + filename + '"')],
                    [sg.Text('Your old tag: "' + tag + '"')],
                    [sg.Text('(Tags in file: ' + str(tags_in_file) + ' )')],
                    [sg.Text('Enter tag(s)', text_color='Red', key='_ENT_NEW_TAG_', visible=False)],
                    [sg.Text('Enter a new tag (only one):', size =(20, 1)), sg.InputText(key='_NEW_TAG_')],
                    [sg.Submit(), sg.Cancel()]
                ]
                window = sg.Window("Confirmation", layout, modal=True)
                choice = None
                while True:
                    event, values = window.read()
                    if event == 'Submit':
                        global new_tag
                        if values != '':
                            new_tag = values['_NEW_TAG_']
                            window.close()
                            third_window()
                        else:
                            window.Element('_ENT_NEW_TAG_').Update(visible=True)
                    if event == "Cancel" or event == sg.WIN_CLOSED:
                        break
                    window.close()
            else:
                layout = [
                    [sg.Text('There is no tag "' + tag + '" in the file named "' + Path(path).name + '"')]
                ]
                window = sg.Window("Confirmation", layout, modal=True)
                choice = None
                while True:
                    event, values = window.read()
                    if event == "Cancel" or event == sg.WIN_CLOSED:
                        break
    window.close()

def third_window():
    new_tag_op = '<'+new_tag+'>'
    new_tag_cl = '</'+new_tag+'>'
    count = tags_in_file[open_tag]
    for idx in idxs:
        save_file_path = sg.Input(visible=False, enable_events=True, key='_SAVE_PATH_', expand_x=True)
        vis_flag = False
        do_save = False
        if count <= 1:
            do_save = True
        layout = [
            [sg.Text('"' + filename + '" includes tag "' + tag + '" ' + str(count) + ' time(s)')],
            [sg.Button("Show"), sg.Cancel()],
            [sg.Text(data[idx[0]:idx[0]+len(open_tag)+1], text_color='Red', visible=vis_flag, key='_t1_'),
             sg.Text(data[idx[0]+len(open_tag)+1:idx[1]-1], visible=vis_flag, key='_t2_'),
             sg.Text(data[idx[1]-1:idx[1]+len(close_tag)+1], text_color='Red', visible=vis_flag, key='_t3_')],
             [sg.Text('Change to:', visible=vis_flag, key='_t4_')],
             [sg.Text(new_tag_op, text_color='Red', visible=vis_flag, key='_t5_'),
              sg.Text(data[idx[0]+len(open_tag)+1:idx[1]-1], visible=vis_flag, key='_t6_'),
              sg.Text(new_tag_cl, text_color='Red', visible=vis_flag, key='_t7_')],
              [sg.Button("Yes, change", visible=vis_flag, key='_YES_'), sg.Button("No, don't change, next...", visible=vis_flag, key='_NO_')],
              [sg.Text("DON'T FORGET TO SAVE CHANCHES", text_color='Red', visible=do_save)],
              [save_file_path,
               sg.FileSaveAs(file_types=(("XML Files", "*.xml"), ("ALL Files", "*.*")), key='_SAVE_', visible=vis_flag)],
               [sg.Button("Next", visible=vis_flag, key='_NEXT_')]
        ]
        window = sg.Window('Accept and save', layout)
        while True:
            event, values = window.read()
            if event == "Cancel" or event == sg.WIN_CLOSED:
                count -= 1
                break
            if event == 'Show':
                vis_flag=True
                window.Element('_t1_').Update(visible=vis_flag)
                window.Element('_t2_').Update(visible=vis_flag)
                window.Element('_t3_').Update(visible=vis_flag)
                window.Element('_t4_').Update(visible=vis_flag)
                window.Element('_t5_').Update(visible=vis_flag)
                window.Element('_t6_').Update(visible=vis_flag)
                window.Element('_t7_').Update(visible=vis_flag)
                window.Element('_YES_').Update(visible=vis_flag)
                window.Element('_NO_').Update(visible=vis_flag)
            if event == "_YES_":
                acc_flag = 1
                save_data = front.replace_tag(data, new_tag, open_tag, acc_flag)
                window.Element('_SAVE_').Update(visible=vis_flag)
                window.Element('_YES_').Update(visible=False)
                window.Element('_NO_').Update(visible=False)
                window.Element('_NEXT_').Update(visible=vis_flag)
                if count <= 1:
                    do_save = True
                    window.Element('_SAVE_').Update(visible=vis_flag)
                    window.Element('_NEXT_').Update(visible=False)
            if event == '_SAVE_PATH_':
                file = open(save_file_path.get(), "w")
                file.write(save_data)
                file.close()
                window.close()
                break
            if event == "_NO_":
                acc_flag = 0
                front.replace_tag(data, new_tag, open_tag, acc_flag)
                window.Element('_NEXT_').Update(visible=vis_flag)
                if count <= 1:
                    do_save = True
                    window.Element('_SAVE_').Update(visible=vis_flag)
                    window.Element('_NEXT_').Update(visible=False)
            if event == '_NEXT_':
                count -= 1
                window.close()
                break
    window.close()

if __name__ == "__main__":
    first_window()
