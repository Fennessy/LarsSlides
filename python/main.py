import sys
import time
import subprocess
from pathlib import Path

MINUTES = 15
SCRIPTS_DIR = Path("python")

def setup_commands():
    version = sys.version_info.major
    commands = []

    if not SCRIPTS_DIR.exists():
        print(f"Error: directory '{SCRIPTS_DIR}' not found.")
        sys.exit(1)

    for file in SCRIPTS_DIR.iterdir():
        if  file.is_file() \
        and file.suffix == ".py" \
        and file.name != Path(__file__).name:

            print(f"Found {file.name}\n")
            commands.append([
                f"python{version}", str(file)
            ])
            commands.append([
                "python", str(file)
            ])
    return commands

def run_command(cmd):
    try:
        subprocess.run(cmd, check=True)
        return True
    except FileNotFoundError:
        return False
    except subprocess.CalledProcessError as e:
        print(f"Error running {' '.join(cmd)}: {e}")
        return True

def main():
    commands = setup_commands()

    while True:
        for i in range(0, len(commands), 2):
            if run_command(commands[i]):
                continue
            else:
                run_command(commands[i + 1])

        print("\nSuccessfully ran all the commands.")
        time.sleep(MINUTES * 60)

if __name__ == "__main__":
    main()
