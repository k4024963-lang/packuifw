# packuifw

A tool for packing `.uifw` firmware from shell folders.
Part of the **Firmware Authority** project.

## What is .uifw

`.uifw` is a ZIP archive with the `.uifw` extension that contains a Windows shell:

```
my_shell.uifw
├── shell.json      metadata
├── launcher.exe    launches the shell
├── main.py         shell code
└── assets/         wallpapers, cursors, sounds
```

## Installation

```bash
pip install packuifw
```

## Usage

### CLI

```bash
pack_uifw <path_to_folder>
```

Creates `<folder_name>.uifw` next to the folder.

Example:

```bash
pack_uifw C:\shellpacks\win98
```

Creates `C:\shellpacks\win98.uifw`.

### GUI

Run `pack_uifw` without arguments to open the window:

```bash
pack_uifw
```

- Folder: shell folder (`shell.json`, `main.py`, `assets/`)
- Output: where to save `.uifw` (default — next to the folder)
- Pack: start packing

## Shell folder structure

```
my_shell/
├── shell.json      required (metadata)
├── launcher.exe    required (launches the shell)
├── main.py         shell code (Python)
└── assets/         wallpapers, cursors, sounds
    ├── wallpaper.jpg
    └── startup.wav
```

### shell.json

```json
{
    "key": "win98",
    "name": "Windows 98",
    "version": "1.0.0",
    "author": "dteamcorporation",
    "description": "Classic Windows 98 interface",
    "launcher": "launcher.exe",
    "entry": "main.py"
}
```

## Exclusions

The following are skipped during packing:

Files:

`app.py`, `bot.py`, `server.py`, `emergency.py`, `pack_uifw.py`, `submit_app.py`, `unpack_uifw.py`, `shell_manager_app.py`, `launcher_standalone.py`, `launcher.pyw`, `firmware.db`, `requests.db`, `emergency.log`, `pack_uifw.exe`, `unpack_uifw.exe`

Extensions:

`.db`, `.log`, `.pyc`

Directories:

`cache`, `__pycache__`, `installed_shells`, `.git`, `.idea`, `.vscode`

## Development

```bash
git clone https://github.com/k4024963-lang/packuifw.git
cd packuifw
pip install -e .
```

## License

MIT © fa_creepyr

## Links

- Firmware Authority: [firmware.authority.cloudpub.ru](https://firmware.authority.cloudpub.ru)
- TikTok: [@dteamcorporation](https://tiktok.com/@dteamcorporation)