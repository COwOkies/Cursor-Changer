import psutil
import configparser
import tkinter as tk

config = configparser.ConfigParser()
config.read('config.ini')

w_name = config.get('values','Program')
timesleep = config.getfloat('values','TimeSleep')
DefaultCursor = config.get('values','DefaultCursorName')
NewCursor = config.get('values','NewCursorName')

w_name += ".exe"
isdefault=True
list_proc = []

pid = None
for proc in psutil.process_iter():
    if proc.name() not in list_proc:
        list_proc.append(proc.name())
list_proc.sort()

root = tk.Tk()
root.geometry("400x300")
root.title('Setup Config.ini')
root.resizable(False, False)
root.configure(bg='white')

texte = tk.Label(root, text="Program",bg='white')
texte.place(x=175,y=10)

options = list_proc
selected_option = tk.StringVar()
if w_name in options:
    selected_option.set(w_name)
else:
    selected_option.set(options[0])
    
option_menu = tk.OptionMenu(root, selected_option,*options)
option_menu.config(border=0,font=('bold',10),bg='white',width=27,highlightthickness=0)
option_menu.place(x=85,y=35)

texte2 = tk.Label(root, text="Time Sleep",bg='white')
texte2.place(x=167,y=70)

spinbox = tk.Spinbox(root, from_=0, to=5, increment=0.1, format="%.1f",width=3,border=0,font=('bold',10))
spinbox.delete(0, tk.END)
spinbox.insert(0, timesleep)
spinbox.place(x=183,y=95)


texte3 = tk.Label(root, text="Default Cursor Name",bg='white')
texte3.place(x=141,y=118)


entry_name = tk.PhotoImage(file='buttons/input.png')
entry_image = tk.Label(root,image=entry_name,border=0,bg='white')
entry_image.place(x=81,y=140)

entry = tk.Entry(root,width=27,border=0,font=('bold',11),justify='center')
entry.insert(0, DefaultCursor)
entry.place(x=88,y=144)


texte4 = tk.Label(root, text="New Cursor Name",bg='white')
texte4.place(x=148,y=168)


entry2_name = tk.PhotoImage(file='buttons/input.png')
entry2_image = tk.Label(root,image=entry_name,border=0,bg='white')
entry2_image.place(x=81,y=190)

entry2 = tk.Entry(root,width=27,border=0,font=('bold',11),justify='center')
entry2.insert(0, NewCursor)
entry2.place(x=88,y=194)

    
def config_ini():
    w_name = selected_option.get()[:-4]
    timesleep = spinbox.get()
    DefaultCursor = entry.get()
    NewCursor = entry2.get()

    config = configparser.ConfigParser()

    config.read('config.ini')

    config['values']['Program'] = w_name
    config['values']['DefaultCursorName'] = DefaultCursor
    config['values']['NewCursorName'] = NewCursor
    config['values']['TimeSleep'] = timesleep
    
    with open('config.ini', 'w') as configfile:
        config.write(configfile)
    

butimage = tk.PhotoImage(file="buttons/button.png")
bouton = tk.Button(root,image=butimage, text="Apply", command=config_ini,bg='white',border='0')
bouton.place(x=122,y=230)

root.mainloop()



    
