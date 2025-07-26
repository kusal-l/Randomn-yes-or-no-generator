# Randomn-yes-or-no-generator
Generates yes or no responces randomly as much as you prefer

## ✅ Features
- Generates a customizable number of random "yes"/"no" values.
- Uses weighted probability: **95% yes**, **5% no**.
- Outputs results both in the console and in a text file (`random_yes_no_output.txt`).

## 📂 Output
- Console: Displays all generated values line by line.
- File: Results are written to **`random_yes_no_output.txt`** in the same directory.

## ⚙️ How It Works
- The script uses Python's `random` module.
- `generate_yes_no()` returns `"yes"` 95% of the time and `"no"` 5% of the time.
- Modify the number inside the brackets `[generate_yes_no() for _ in range(10)]` to generate more or fewer outputs.

## 🔧 Customization
- To change the number of results, edit this line in the script

    <img width="427" height="29" alt="image" src="https://github.com/user-attachments/assets/dae1e2e2-85ab-418d-bafa-398053378b2a" />

- Replace _10_ with any number you need.
