
import os
import shutil
DIRS_TO_CLEAN = ["data", "features", "models", "results", "__pycache__"]
def clean():
    for d in DIRS_TO_CLEAN:
        if os.path.exists(d):
            print(f"Removing {d}...")
            try:
                if os.path.isfile(d):
                    os.remove(d)
                else:
                    shutil.rmtree(d)
                print(f"Removed {d}")
            except Exception as e:
                print(f"Error removing {d}: {e}")
        else:
            print(f"{d} does not exist.")

if __name__ == "__main__":
    clean()
