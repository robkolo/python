import os

directory = r'/Users/rkolodzi/Code/CloudFormationBackup'

for root, dirs, files in os.walk(directory):
    print(f"root: {root}")
    print(f"dirs: {dirs}")
    print(f"files: {files}")

    for current_filename in files:
        lc_filename = current_filename.lower().replace('_', '-')

        print(f"current filename: {current_filename}")
        print(f"new filename: {lc_filename}")

        os.rename(
            os.path.join(root, current_filename), 
            os.path.join(root, lc_filename)
        )