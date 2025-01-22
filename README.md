# Automated ID Generation for Fair Contest Grading :sparkles:

<p align="center">
  <img src="https://i.gifer.com/origin/e6/e689257ceefe8a833c86d022de084df5.gif" width="400" alt="folder animation">
</p>

A simple tool to help examiners automatically generate **alternative IDs** for programming contest submissions. This prevents any unfair advantage by hiding the participant’s real ID from other graders.

## Table of Contents
1. [Background](#background)
2. [Features](#features)
3. [How It Works](#how-it-works)
4. [Prerequisites & Installation](#prerequisites--installation)
5. [Usage](#usage-rocket)
6. [Example Scenario](#example-scenario-sparkles)
7. [Acknowledgments](#acknowledgments-pray)
8. [License](#license-scroll)

---

## Background
In Vietnam, when participants submit code for a programming contest, their submissions are saved on a CD. Each participant’s submission is then placed into a main folder (**Folder A**), with each participant having a subfolder named `G<ID_NUMBER>` (e.g., `G001`).

To ensure fairness, the actual ID numbers are **masked**. This means:
- `G<ID_NUMBER>` becomes `P(<ID_NUMBER + offset>)`, which we call the **alternative number**.
- The head examiner creates a duplicate folder structure (**Folder C**) containing these new names (`P...`) and the files inside.

All ID numbers and their corresponding alternative numbers are stored in an Excel file, allowing the head examiner to see which alternative folder corresponds to which original ID. This system helps prevent biased grading by ensuring other examiners do not see real ID numbers.

---

## Features
- :heavy_check_mark: **Automatic Renaming**: Quickly renames subfolders from `G###` to `P###` with an offset.
- :heavy_check_mark: **Duplicate Folder Creation**: Creates a copy of the original folder structure (Folder C).
- :heavy_check_mark: **Excel Export**: Stores the mapping of original ID to the new ID in a handy spreadsheet.
- :heavy_check_mark: **Easy to Track**: Helps head examiners keep track of the original and alternative IDs effortlessly.

---

## How It Works
1. **Input Folder (Folder A)**: Contains all participant submissions with names in the format `G001`, `G002`, etc.
2. **Offset/Increment**: A numeric offset (e.g., `+ 100`) is used to transform `G001` into `P101`.
3. **Output Folder (Folder C)**: A newly created folder structure mirroring Folder A, but with renamed subfolders using the alternative ID format.
4. **Excel Mapping**: Simultaneously, an Excel file is generated listing the mapping between `G<ID>` and `P<ID>` (for record-keeping).

---

## Prerequisites & Installation
1. **Python 3** (or later).  
2. **Required Python libraries**: Make sure you install any necessary libraries mentioned in `requirements.txt` (if provided). Example:
   ```
   bash
   pip install -r requirements.txt
    ```

# Instructions

Below you will find all the necessary steps and details for setting up, running, and contributing to this project! We’ve added plenty of emojis to keep things lively. Enjoy! :tada:

---

## Cloning the Repository 

1. Open your terminal 
2. Clone the repository:
   ```bash
   git clone https://github.com/charlottenguyen05/test-number.git
   cd test-number
   ```
3. **Setting Up** 
   - Place your **Folder A** in the correct directory
   - Update paths in the script according to your setup  

---

## Usage :rocket:

### 1. Prepare Folder A :file_folder:
- Ensure you have a folder called **`A`** with subfolders named like **`G001`**, **`G002`**, etc.

### 2. Run the Script :running:
```bash
python test_number.py
```
> *Adjust the command above if your script has a different name.*

### 3. Follow the Prompts :mag_right:
- The program may ask for an offset number, the location of **Folder A**, and where to create **Folder C**.

### 4. Check the Results :white_check_mark:
- A new folder, **`C`**, is created with renamed subfolders (`P###`).  
- An **Excel file** is generated, mapping `G###` to `P###`.

---

## Example Scenario :sparkles:

Suppose we have these subfolders in **Folder A**:

```css
A
├── G001
│    └── solution.cpp
└── G002
     └── main.py
```

If you run the script with an **offset of `100`**, it will produce:

```css
C
├── P101
│    └── solution.cpp
└── P102
     └── main.py
```

And an Excel file (e.g., `Mapping.xlsx`) might look like:

| Original ID | Alternative ID |
|-------------|---------------|
| G001        | P101          |
| G002        | P102          |

---

## Acknowledgments :pray:

- **Inspiration**: This project is inspired by the difficulties teachers face in manually masking IDs for fair grading. :school_satchel:
- **Special Thanks**: To the teacher who shared this challenge, motivating the creation of this tool. :raised_hands:

---

## License :scroll:

This project is licensed under the [MIT License](LICENSE). Feel free to use it as you wish, but please provide appropriate attribution if you decide to fork and modify it. :memo:

