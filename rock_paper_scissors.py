import tkinter as tk
import random

# ---------- VARIABLES ----------
choices = ["Rock", "Paper", "Scissors"]
user_score = 0
computer_score = 0

# ---------- GAME FUNCTION ----------
def play(user_choice):
    global user_score, computer_score

    computer_choice = random.choice(choices)

    user_label.config(text=f"You chose: {user_choice}")
    comp_label.config(text=f"Computer chose: {computer_choice}")

    # Game Logic
    if user_choice == computer_choice:
        result = "It's a Tie 🤝"

    elif (user_choice == "Rock" and computer_choice == "Scissors") or \
         (user_choice == "Paper" and computer_choice == "Rock") or \
         (user_choice == "Scissors" and computer_choice == "Paper"):
        result = "You Win 🎉"
        user_score += 1
    else:
        result = "Computer Wins 💻"
        computer_score += 1

    result_label.config(text=result)
    score_label.config(
        text=f"Score → You: {user_score} | Computer: {computer_score}"
    )

# ---------- RESET ----------
def reset_game():
    global user_score, computer_score
    user_score = 0
    computer_score = 0

    user_label.config(text="You chose: ")
    comp_label.config(text="Computer chose: ")
    result_label.config(text="Make your move!")
    score_label.config(text="Score → You: 0 | Computer: 0")

# ---------- WINDOW ----------
root = tk.Tk()
root.title("Rock Paper Scissors Game")
root.geometry("420x450")
root.config(bg="#f2f6ff")

# ---------- TITLE ----------
tk.Label(root,
         text="✊ Rock Paper Scissors ✋",
         font=("Arial",18,"bold"),
         bg="#4a7abc",
         fg="white",
         pady=10).pack(fill="x")

# ---------- INSTRUCTION ----------
tk.Label(root,
         text="Choose Rock, Paper or Scissors",
         font=("Arial",12),
         bg="#f2f6ff").pack(pady=15)

# ---------- BUTTONS ----------
btn_frame = tk.Frame(root, bg="#f2f6ff")
btn_frame.pack()

tk.Button(btn_frame, text="🪨 Rock", width=12,
          bg="#4CAF50", fg="white",
          command=lambda: play("Rock")).grid(row=0,column=0,padx=5,pady=5)

tk.Button(btn_frame, text="📄 Paper", width=12,
          bg="#2196F3", fg="white",
          command=lambda: play("Paper")).grid(row=0,column=1,padx=5,pady=5)

tk.Button(btn_frame, text="✂ Scissors", width=12,
          bg="#FF9800", fg="white",
          command=lambda: play("Scissors")).grid(row=0,column=2,padx=5,pady=5)

# ---------- DISPLAY ----------
user_label = tk.Label(root, text="You chose: ",
                      font=("Arial",12), bg="#f2f6ff")
user_label.pack(pady=10)

comp_label = tk.Label(root, text="Computer chose: ",
                      font=("Arial",12), bg="#f2f6ff")
comp_label.pack(pady=5)

result_label = tk.Label(root,
                        text="Make your move!",
                        font=("Arial",14,"bold"),
                        bg="#f2f6ff")
result_label.pack(pady=15)

# ---------- SCORE ----------
score_label = tk.Label(root,
                       text="Score → You: 0 | Computer: 0",
                       font=("Arial",12,"bold"),
                       bg="#f2f6ff")
score_label.pack(pady=10)

# ---------- PLAY AGAIN ----------
tk.Button(root,
          text="Play Again / Reset",
          bg="#f44336",
          fg="white",
          width=18,
          command=reset_game).pack(pady=20)

# ---------- RUN ----------
root.mainloop()
