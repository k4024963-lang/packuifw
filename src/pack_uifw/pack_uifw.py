import sys
import os
import json
import zipfile
from pathlib import Path

# --- EXCLUSION CONFIGURATION ---
EXCLUDE_NAMES = {
    'app.py', 'bot.py', 'server.py', 'firmware.db', 'requests.db',
    'emergency.py', 'launcher.pyw', 'pack_uifw.py', 'emergency.log',
    'submit_app.py', 'unpack_uifw.py', 'shell_manager_app.py',
    'launcher_standalone.py'
}
EXCLUDE_EXTS = {'.db', '.log', '.pyc'}
EXCLUDE_DIRS = {'cache', '__pycache__', 'installed_shells', '.git', '.idea', '.vscode'}


def should_skip(path):
    """Checks if a file or directory should be excluded from the archive."""
    if path.name in EXCLUDE_NAMES:
        return True
    if path.suffix.lower() in EXCLUDE_EXTS:
        return True
    for part in path.parts:
        if part in EXCLUDE_DIRS:
            return True
    return False


def pack_folder(folder_path, out_path=None):
    """Packs a shell folder into a .uifw archive."""
    folder = Path(folder_path).resolve()
    
    if not folder.exists() or not folder.is_dir():
        print("From folder err.")
        return False

    if out_path is None:
        out = folder.parent / f"{folder.name}.uifw"
    else:
        out = Path(out_path).resolve()

    meta_file = folder / 'shell.json'
    if not meta_file.exists():
        print('[!] Warning: shell.json not found in folder')

    # Remove existing archive to avoid appending
    if out.exists():
        try:
            out.unlink()
        except PermissionError:
            print(f"Cannot delete {out} — close File Explorer/archiver and try again.")
            return False

    count = 0
    try:
        with zipfile.ZipFile(out, 'w', zipfile.ZIP_DEFLATED) as z:
            for item in folder.rglob('*'):
                if item.is_dir():
                    continue
                if should_skip(item):
                    continue
                
                arcname = item.relative_to(folder)
                z.write(item, arcname)
                count += 1

        size_kb = out.stat().st_size // 1024
        firmware_key = folder.name
        print(f"Your firmware, named by {firmware_key}, builded in uifw. Success.")
        return True
        
    except Exception as e:
        print("Build err.")
        return False


def unpack_uifw(archive_path, dest_path=None):
    """Unpacks a .uifw archive into the specified folder."""
    archive = Path(archive_path).resolve()
    
    if not archive.exists():
        print("From folder err.")
        return False
        
    if dest_path is None:
        dest = archive.parent / f"{archive.stem}_unpacked"
    else:
        dest = Path(dest_path).resolve()
    
    try:
        dest.mkdir(parents=True, exist_ok=True)
        
        with zipfile.ZipFile(archive, 'r') as z:
            z.extractall(dest)
        
        print(f"Your firmware, named by {archive.stem}, unpacked. Success.")
        return True
        
    except Exception as e:
        print("Build err.")
        return False


def main():
    """Entry point for the CLI tool."""
    args = sys.argv[1:]
    
    if len(args) < 2:
        print("Usage:")
        print('  pack_uifw pack <folder_path> [output_path]')
        print('  pack_uifw unpack <file.uifw> [dest_folder]')
        return

    command = args[0].lower()
    target = args[1]
    optional_arg = args[2] if len(args) > 2 else None

    if command == 'pack':
        success = pack_folder(target, optional_arg)
    elif command == 'unpack':
        success = unpack_uifw(target, optional_arg)
    else:
        print(f"Unknown command: {command}")
        print("Use 'pack' or 'unpack'.")
        return

    if not success:
        sys.exit(1)


if __name__ == '__main__':
    main()