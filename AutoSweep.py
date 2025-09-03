# autoruns_sweep_win.py — list common startup entries on Windows
import os, subprocess, sys
from pathlib import Path
try:
    import winreg
except ImportError:
    print("Run on Windows (needs winreg)."); sys.exit(1)

def reg_enum(root, path):
    keys = []
    try:
        with winreg.OpenKey(root, path) as k:
            i = 0
            while True:
                try:
                    name, value, _ = winreg.EnumValue(k, i)
                    keys.append((path, name, value))
                    i += 1
                except OSError:
                    break
    except OSError:
        pass
    return keys

def main():
    targets = [
        (winreg.HKEY_CURRENT_USER, r"Software\Microsoft\Windows\CurrentVersion\Run"),
        (winreg.HKEY_CURRENT_USER, r"Software\Microsoft\Windows\CurrentVersion\RunOnce"),
        (winreg.HKEY_LOCAL_MACHINE, r"Software\Microsoft\Windows\CurrentVersion\Run"),
        (winreg.HKEY_LOCAL_MACHINE, r"Software\Microsoft\Windows\CurrentVersion\RunOnce"),
    ]
    print("== Registry Run/RunOnce ==")
    for root, path in targets:
        for p, name, val in reg_enum(root, path):
            print(f"[{p}] {name} -> {val}")

    print("\n== Startup folders ==")
    startup_dirs = [
        Path(os.getenv("APPDATA", "")) / "Microsoft/Windows/Start Menu/Programs/Startup",
        Path(os.getenv("PROGRAMDATA", "")) / "Microsoft/Windows/Start Menu/Programs/Startup",
    ]
    for d in startup_dirs:
        if d and d.exists():
            for f in d.iterdir():
                print(f"{d} -> {f.name}")

    print("\n== Scheduled tasks (top-level names) ==")
    try:
        out = subprocess.check_output(["schtasks", "/query", "/fo", "LIST", "/v"], text=True, errors="ignore")
        for line in out.splitlines():
            if line.startswith("TaskName:"):
                print(line.split(":",1)[1].strip())
    except Exception as e:
        print(f"Could not query scheduled tasks: {e}")

if __name__ == "__main__":
    main()
