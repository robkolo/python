import os

directory = r'/path/goes/here'

for root, dirs, files in os.walk(directory):
    print(f"root: {root}")
    print(f"dirs: {dirs}")
    print(f"files: {files}")

    for current_filename in files:
        new_filename = current_filename.replace('_', '-').lower()

        print(f"current filename: {current_filename}")
        print(f"    new filename: {new_filename}")

        os.rename(
            os.path.join(root, current_filename), 
            os.path.join(root, new_filename)
        )