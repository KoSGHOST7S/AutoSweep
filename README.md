AutoSweep is a lightweight blue-team auditing script for Windows that scans common persistence locations used by both legitimate software and malware.
It helps security professionals quickly spot suspicious autoruns, startup items, and scheduled tasks.

How It Works

Enumerates registry keys where apps configure auto-start.

Scans Windows startup folders for executables, scripts, and shortcuts.

Queries scheduled tasks and prints task names.

Reports results so you can distinguish normal startup apps vs. potential malware persistence.

HOW TO COPY THE REPO:
git clone https://github.com/KoSGHOST7S/AutoSweep.git
cd AutoSweep
