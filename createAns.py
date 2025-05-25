import os
import sys
new_id = sys.argv[1].upper()

keys_folder = "keys"
ans_folder = "ans"

os.makedirs(ans_folder, exist_ok=True)

for filename in os.listdir(keys_folder):
    if filename.endswith(".lab"):
        old_id = filename.split('.')[0]

        if len(old_id) != len(new_id):
            continue

        input_path = os.path.join(keys_folder, filename)
        new_filename = filename.replace(old_id, new_id)
        output_path = os.path.join(ans_folder, new_filename)

        with open(input_path, "rb") as f:
            content = f.read()

        new_content = content.replace(old_id.encode(), new_id.encode())

        with open(output_path, "wb") as f:
            f.write(new_content)

        print(f"✅ {filename} ➜ {new_filename}")
