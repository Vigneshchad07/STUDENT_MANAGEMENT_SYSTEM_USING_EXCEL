import csv, os

PATH = r"D:\Python\Python Codes\Student Management using Excel.csv"

def read_data():
    if not os.path.exists(PATH): return [], []
    with open(PATH, 'r', encoding='utf-8') as f:
        rows = list(csv.reader(f))
    h_idx = next((i for i, r in enumerate(rows) if any('ID' in c for c in r)), -1)
    if h_idx == -1: return [], []
    indices = [i for i, c in enumerate(rows[h_idx]) if c.strip()]
    header = [rows[h_idx][i].strip() for i in indices]
    data = [{h: (r[i].strip() if i < len(r) else "") for i, h in zip(indices, header)} 
            for r in rows[h_idx+1:] if any(r)]
    return header, data

def write_data(header, data):
    with open(PATH, 'w', newline='', encoding='utf-8') as f:
        w = csv.writer(f)
        w.writerow(["Student Management"] + [""]*25)
        pad = lambda items: [x for item in items for x in (item, "", "", "")]
        w.writerow(pad(header))
        for r in data: w.writerow(pad([r.get(h, "") for h in header]))
    print("Changes Saved.")

def append_record(h, d):
    d.append({c: input(f"New {c}: ") for c in h})
    write_data(h, d)

def remove_record(h, d):
    sid = input("ID to remove: ")
    new_d = [r for r in d if r[h[0]] != sid]
    if len(new_d) < len(d): write_data(h, new_d)
    else: print("Not found.")

def read_rows(h, d):
    col = next((c for c in h if c.lower() == input("Search by which column? ").lower()), None)
    if not col: return print("Invalid.")
    val = input(f"Search for value in '{col}': ").lower()
    for r in d:
        if val in r[col].lower(): print(f"Row: {r}")

def read_columns(h, d):
    search = input("Enter column name(s) (e.g. Name, Group): ").split(',')
    v_cols = [c for c in h if any(c.lower() == s.strip().lower() for s in search)]
    if not v_cols: return print("No valid columns.")
    print("\n" + " | ".join(v_cols) + "\n" + "-"*30)
    for r in d: print(" | ".join(r.get(c, "") for c in v_cols))

def menu():
    opts = {
        '1': ("Read All Data", lambda h, d: [print(r) for r in d]),
        '2': ("Append Record", append_record),
        '3': ("Remove Record", remove_record),
        '4': ("Read by Rows (Search)", read_rows),
        '5': ("Read by Columns (Access)", read_columns),
        '6': ("Save Manual State", write_data),
        '7': ("Exit", None)
    }
    while True:
        h, d = read_data()
        print(f"\n{'='*25}\n STUDENT MANAGER MENU \n{'='*25}")
        for k, v in opts.items(): print(f"{k}. {v[0]}")
        c = input("> ")
        if c == '7': break
        if c in opts: 
            if h: opts[c][1](h, d)
            else: print("Error: CSV structure not recognized.")
        else: print("Invalid option.")

if __name__ == "__main__": menu()
