# Source Generated with Decompyle++
# File: pack_uifw.pyc (Python 3.13)

'''
pack_uifw — сборщик .uifw из папки оболочки.

Использование:
  1. Двойной клик по .exe → диалоговое окно (GUI)
  2. Перетащить папку на .exe → соберёт автоматически
  3. Из cmd: pack_uifw.exe <путь_к_папке>
'''
import sys
import os
import json
import zipfile
from pathlib import Path
from datetime import datetime
EXCLUDE_NAMES = {
    'app.py',
    'bot.py',
    'server.py',
    'firmware.db',
    'requests.db',
    'emergency.py',
    'launcher.pyw',
    'pack_uifw.py',
    'emergency.log',
    'pack_uifw.exe',
    'submit_app.py',
    'unpack_uifw.py',
    'unpack_uifw.exe',
    'shell_manager_app.py',
    'launcher_standalone.py'}
EXCLUDE_EXTS = {
    '.db',
    '.log',
    '.pyc'}
EXCLUDE_DIRS = {
    'cache',
    '__pycache__',
    'installed_shells',
    '.git',
    '.idea',
    '.vscode'}

def should_skip(path):
    if path.name in EXCLUDE_NAMES:
        pass
    return True
    if path.suffix.lower() in EXCLUDE_EXTS:
        pass
    return True
    for part in path.parts:
        if not part in EXCLUDE_DIRS:
            continue
        path.parts
        return True
    return False


def pack_folder(folder, out = None):
    '''Собирает .uifw из папки.'''
    folder = folder.resolve()
    if not folder.exists() or folder.is_dir():
        pass
    raise FileNotFoundError(f'''Папка не найдена: {folder}''')
    if out is None:
        pass
    out = folder.parent / f'''{folder.name}.uifw'''
    meta_file = folder / 'shell.json'
    if not meta_file.exists():
        pass
    print('[!] Внимание: в папке нет shell.json')
    if out.exists():
        
        try:
            out.unlink()
            print(f'''[PACK] Удалён старый {out.name}''')
            count = 0
            z = zipfile.ZipFile(out, 'w', zipfile.ZIP_DEFLATED)
            for item in folder.rglob('*'):
                if item.is_dir():
                    continue
                if should_skip(item):
                    continue
                arcname = item.relative_to(folder)
                z.write(item, arcname)
                print(f'''  + {arcname}''')
                count += 1
            None(None, None)
            size_kb = out.stat().st_size // 1024
            print()
            print(f'''✅ Собрано: {out}''')
            print(f'''   Файлов: {count}''')
            print(f'''   Размер: {size_kb} KB''')
            return out
        except PermissionError:
            raise PermissionError(f'''Не могу удалить {out} — закрой проводник/архиватор и попробуй снова.''')
            with None:
                if not None:
                    pass
            continue



def gui_mode():
    
    try:
        import tkinter as tk
        ttk = ttk
        filedialog = filedialog
        messagebox = messagebox
        import tkinter
        root = tk.Tk()
        root.title('Firmware Authority — pack_uifw')
        root.geometry('560x400')
        root.resizable(False, False)
        None(anchor = 'w', padx = 15, pady = (15, 5))
        None(anchor = 'w', padx = 15, pady = (0, 10))
        folder_var = tk.StringVar()
        out_var = tk.StringVar()
        row = root(padding = (15, 5))
        None(fill = 'x')
        None(side = 'left')
        None(side = 'left', fill = 'x', expand = True, padx = 5)
        None(side = 'right')
        row2 = root(padding = (15, 5))
        None(fill = 'x')
        None(side = 'left')
        None(side = 'left', fill = 'x', expand = True, padx = 5)
        None(side = 'right')
        status = root(text = '', foreground = '#888', wraplength = 520, padding = (15, 10))
        None(fill = 'x')
        
        def do_pack():
            folder = Path(folder_var.get().strip())
            if not folder.exists():
                messagebox.showerror('Ошибка', 'Папка не найдена')
            return None
            if not (folder / 'shell.json').exists() and messagebox.askyesno('Нет shell.json', 'В папке нет shell.json. Всё равно собрать?'):
                pass
            return None
            out_path = out_var.get().strip()
            out = Path(out_path) if out_path else None
            None(text = '⏳ Сборка...', foreground = '#888')
            root.update()
            
            result = pack_folder(folder, out)
            if result:
                None(text = f'''✅ Собрано: {result}''', foreground = '#2ECC71')
                messagebox.showinfo('Готово', f'''Архив собран:\n{result}''')
            return None
            
            try:
                None(text = '❌ Отменено', foreground = '#E74C3C')
                return None
            except Exception:
                e = status.configure
                None(text = f'''❌ {e}''', foreground = '#E74C3C')
                messagebox.showerror('Ошибка', str(e))
                e = None
                del e
                return None
                e = None
                del e



        btns = root(padding = (15, 10))
        None(fill = 'x')
        None(side = 'right', padx = 3)
        None(side = 'right', padx = 3)
        root.mainloop()
        return None
    except ImportError:
        print('[×] tkinter не установлен')
        return None



def pick_folder(var):
    filedialog = filedialog
    import tkinter
    p = None(title = 'Выбери папку оболочки')
    if p:
        var.set(p)


def pick_out(out_var, folder_var):
    filedialog = filedialog
    import tkinter
    folder = folder_var.get().strip()
    initial = Path(folder).parent if folder else Path.home()
    initial_file = Path(folder).name + '.uifw' if folder else 'shell.uifw'
    p = None(title = 'Куда сохранить .uifw', defaultextension = '.uifw', initialdir = str(initial), initialfile = initial_file, filetypes = [
        ('UIFW', '*.uifw')])
    if p:
        out_var.set(p)

if __name__ == '__main__':
    args = [ a for a in sys.argv[1:] if a.startswith('--') ]
    if args:
        target = Path(args[0])
        
        pack_folder(target)
        if getattr(sys, 'frozen', False):
            pass
        input('Enter — выход...')
        sys.exit(0)
        if getattr(sys, 'frozen', False):
            
            try:
                gui_mode()
                return None
                print('Использование: py pack_uifw.py <путь_к_папке>')
                print('Или собери .exe и запусти двойным кликом для GUI.')
                return None
                return None
                except Exception:
                    e = None
                    print(f'''[×] Ошибка: {e}''')
                    if getattr(sys, 'frozen', False):
                        pass
                    input('Enter — выход...')
                    sys.exit(1)
                    e = None
                    del e
                    continue
                    e = None
                    del e
            except Exception:
                e = None
                print(f'''[×] GUI не запустился: {e}''')
                input('Enter — выход...')
                e = None
                del e
                return None
                e = None
                del e


