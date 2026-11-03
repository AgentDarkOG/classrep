from pathlib import Path
import subprocess
import sys
import time

GAME_FILE = Path(__file__).with_name("first_class.py")
CHECK_INTERVAL = 0.5


def start_game():
    return subprocess.Popen([sys.executable, str(GAME_FILE)], cwd=GAME_FILE.parent)


def main():
    last_modified = GAME_FILE.stat().st_mtime_ns
    process = start_game()

    try:
        while True:
            time.sleep(CHECK_INTERVAL)
            current_modified = GAME_FILE.stat().st_mtime_ns

            if current_modified != last_modified:
                last_modified = current_modified
                process.terminate()
                process.wait()
                process = start_game()
                print("Code changed. Game restarted.")
            elif process.poll() is not None:
                print("Game closed. Save a code change to restart it.")
                while GAME_FILE.stat().st_mtime_ns == last_modified:
                    time.sleep(CHECK_INTERVAL)
                last_modified = GAME_FILE.stat().st_mtime_ns
                process = start_game()
    except KeyboardInterrupt:
        if process.poll() is None:
            process.terminate()
            process.wait()
        print("Auto-reload stopped.")


if __name__ == "__main__":
    main()
