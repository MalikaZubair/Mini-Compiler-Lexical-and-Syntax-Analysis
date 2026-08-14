import tkinter as tk
from tkinter import scrolledtext, messagebox

# ---------------- Compiler Phases ----------------

def lexical_analyzer(source):
    tokens = []
    current = ""

    for ch in source:
        if ch.isalnum():
            current += ch
        else:
            if current:
                tokens.append(current)
                current = ""
            if ch.strip():
                tokens.append(ch)

    if current:
        tokens.append(current)

    output = "[LEXICAL ANALYSIS]\n"
    for t in tokens:
        output += f"Token: {t}\n"

    return tokens, output


def syntax_analyzer(tokens):
    output = "[SYNTAX ANALYSIS]\n"

    if len(tokens) != 3:
        output += "Syntax Error: Expression must be operand operator operand\n"
        return output

    if tokens[1] not in ['+', '-', '*', '/']:
        output += "Syntax Error: Invalid operator\n"
        return output

    if not (tokens[0].isidentifier() or tokens[0].isdigit()):
        output += "Syntax Error: Invalid first operand\n"
        return output

    if not (tokens[2].isidentifier() or tokens[2].isdigit()):
        output += "Syntax Error: Invalid second operand\n"
        return output

    output += "Syntax is correct\n"
    return output


def semantic_analyzer(tokens):
    output = "[SEMANTIC ANALYSIS]\n"

    if len(tokens) != 3:
        output += "Semantic Error: Invalid expression\n"
        return output

    if tokens[1] == '/' and tokens[2].isdigit() and int(tokens[2]) == 0:
        output += "Semantic Error: Division by zero\n"
        return output

    output += "Semantic analysis successful\n"
    return output


def symbol_table(tokens):
    output = "[SYMBOL TABLE]\n"
    symbols = set()

    for t in tokens:
        if t.isidentifier():
            symbols.add(t)

    if not symbols:
        output += "No identifiers found\n"
    else:
        for s in symbols:
            output += f"{s} : identifier\n"

    return output


def intermediate_code(tokens):
    output = "[INTERMEDIATE CODE]\n"

    if len(tokens) == 3:
        output += f"t1 = {tokens[0]} {tokens[1]} {tokens[2]}\n"
    else:
        output += "Intermediate code cannot be generated\n"

    return output


def assembly_code(tokens):
    output = "[ASSEMBLY CODE]\n"

    if len(tokens) != 3:
        output += "Assembly code cannot be generated\n"
        return output

    var1, op, var2 = tokens
    output += f"MOV AX, {var1}\n"

    if op == '+':
        output += f"ADD AX, {var2}\n"
    elif op == '-':
        output += f"SUB AX, {var2}\n"
    elif op == '*':
        output += f"MUL {var2}\n"
    elif op == '/':
        output += f"DIV {var2}\n"

    output += "MOV t1, AX\n"
    return output


# ---------------- GUI Actions ----------------

def display_output(content):
    output_box.config(state='normal')
    output_box.delete("1.0", tk.END)

    for line in content.split("\n"):
        if "LEXICAL" in line:
            output_box.insert(tk.END, line + "\n", "lexical")
        elif "SYNTAX" in line:
            output_box.insert(tk.END, line + "\n", "syntax")
        elif "SEMANTIC" in line:
            output_box.insert(tk.END, line + "\n", "semantic")
        elif "SYMBOL" in line:
            output_box.insert(tk.END, line + "\n", "symbol")
        elif "INTERMEDIATE" in line:
            output_box.insert(tk.END, line + "\n", "intermediate")
        elif "ASSEMBLY" in line:
            output_box.insert(tk.END, line + "\n", "assembly")
        else:
            output_box.insert(tk.END, line + "\n")

    output_box.config(state='disabled')
    output_box.yview_moveto(0)


def copy_output():
    content = output_box.get("1.0", tk.END).strip()
    if content:
        root.clipboard_clear()
        root.clipboard_append(content)
        messagebox.showinfo("Copied", "Output copied to clipboard!")
    else:
        messagebox.showwarning("Empty", "No output to copy!")


def run_phase(phase):
    global tokens
    source = source_entry.get().strip()

    if not source:
        messagebox.showwarning("Input Error", "Please enter source code")
        return

    if phase == "Lexical":
        tokens, out = lexical_analyzer(source)
    elif phase == "Syntax":
        out = syntax_analyzer(tokens)
    elif phase == "Semantic":
        out = semantic_analyzer(tokens)
    elif phase == "Symbol":
        out = symbol_table(tokens)
    elif phase == "Intermediate":
        out = intermediate_code(tokens)
    elif phase == "Assembly":
        out = assembly_code(tokens)

    display_output(out)


def run_all():
    global tokens
    source = source_entry.get().strip()

    if not source:
        messagebox.showwarning("Input Error", "Please enter source code")
        return

    tokens, out1 = lexical_analyzer(source)
    out2 = syntax_analyzer(tokens)
    out3 = semantic_analyzer(tokens)
    out4 = symbol_table(tokens)
    out5 = intermediate_code(tokens)
    out6 = assembly_code(tokens)

    display_output(out1 + out2 + out3 + out4 + out5 + out6)


# ---------------- GUI Design ----------------

root = tk.Tk()
root.title("🌸 Malika's Compiler 🌸")
root.geometry("1000x750")
root.minsize(900, 700)
root.configure(bg="#fdf6e3")
root.grid_rowconfigure(3, weight=1)
root.grid_columnconfigure(0, weight=1)

title = tk.Label(
    root,
    text="💻 Modern Compiler",
    font=("Comic Sans MS", 24, "bold"),
    bg="#6c5ce7",
    fg="white",
    pady=15
)
title.grid(row=0, column=0, sticky='ew', padx=5, pady=5)

input_label = tk.Label(
    root,
    text="Enter Source Code:",
    font=("Arial", 12, "bold"),
    bg="#fdf6e3"
)
input_label.grid(row=1, column=0, sticky='w', padx=15)

source_entry = tk.Entry(
    root,
    font=("Arial", 12),
    bg="#ffeaa7"
)
source_entry.grid(row=1, column=0, sticky='ew', padx=15, pady=5)

btn_frame = tk.Frame(root, bg="#fdf6e3")
btn_frame.grid(row=2, column=0, sticky='ew', padx=15, pady=5)
btn_frame.grid_columnconfigure(tuple(range(7)), weight=1)

phases = ["Lexical", "Syntax", "Semantic", "Symbol", "Intermediate", "Assembly"]
colors = ["#74b9ff", "#ff7675", "#55efc4", "#fd79a8", "#ffeaa7", "#a29bfe"]

def on_enter(e):
    e.widget['background'] = "#dfe6e9"

def on_leave(e):
    e.widget['background'] = e.widget.default_bg

for i, (p, c) in enumerate(zip(phases, colors)):
    b = tk.Button(
        btn_frame,
        text=p,
        bg=c,
        fg="white",
        font=("Arial", 10, "bold"),
        relief="raised",
        bd=3,
        command=lambda phase=p: run_phase(phase),
        activebackground="#81ecec"
    )
    b.grid(row=0, column=i, padx=5, pady=5, sticky='ew')
    b.default_bg = c
    b.bind("<Enter>", on_enter)
    b.bind("<Leave>", on_leave)

run_all_btn = tk.Button(
    btn_frame,
    text="Run All",
    bg="#00b894",
    fg="white",
    font=("Arial", 10, "bold"),
    relief="raised",
    bd=3,
    command=run_all,
    activebackground="#81ecec"
)
run_all_btn.grid(row=1, column=0, columnspan=6, pady=5, sticky='ew')

copy_btn = tk.Button(
    btn_frame,
    text="Copy Output",
    bg="#636e72",
    fg="white",
    font=("Arial", 10, "bold"),
    relief="raised",
    bd=3,
    command=copy_output,
    activebackground="#b2bec3"
)
copy_btn.grid(row=2, column=0, columnspan=6, pady=5, sticky='ew')

output_box = scrolledtext.ScrolledText(
    root,
    state='disabled',
    wrap=tk.WORD,
    font=("Consolas", 11),
    bg="#dfe6e9",
    fg="#2d3436"
)
output_box.grid(row=3, column=0, sticky='nsew', padx=15, pady=10)

output_box.tag_config("lexical", foreground="#0984e3", font=("Consolas", 11, "bold"))
output_box.tag_config("syntax", foreground="#e17055", font=("Consolas", 11, "bold"))
output_box.tag_config("semantic", foreground="#00b894", font=("Consolas", 11, "bold"))
output_box.tag_config("symbol", foreground="#fd79a8", font=("Consolas", 11, "bold"))
output_box.tag_config("intermediate", foreground="#6c5ce7", font=("Consolas", 11, "bold"))
output_box.tag_config("assembly", foreground="#2d3436", font=("Consolas", 11, "bold"))

root.mainloop()
