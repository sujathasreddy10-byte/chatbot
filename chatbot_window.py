import tkinter as tk
from datetime import datetime


# =========================================================
# CHATBOT LOGIC
# =========================================================

def get_reply(message):
    message = message.lower().strip()

    if message in ["hello", "hi", "hey", "hii", "helo"]:
        return "Hello! 👋 Nice to meet you."

    elif "how are you" in message:
        return "I'm doing great! 😊 How can I help you?"

    elif "your name" in message or "who are you" in message:
        return "I'm My ChatBot 🤖. Nice to meet you!"

    elif "what can you do" in message:
        return "I can answer simple questions and have a conversation with you."

    elif "thank" in message:
        return "You're welcome! 😊"

    elif "good morning" in message:
        return "Good morning! ☀️ Have a great day!"

    elif "good night" in message:
        return "Good night! 🌙 Sleep well!"

    elif "bye" in message:
        return "Goodbye! 👋 See you again!"

    elif "python" in message:
        return "Python is a popular programming language used for AI, web development, automation and more."

    elif "college" in message:
        return "College is a great place to learn, build projects and develop your skills. 🎓"

    elif "help" in message:
        return "Sure! 😊 Tell me what you need help with."

    else:
        return "I'm still learning 🤔. Try asking me something else."


# =========================================================
# SEND MESSAGE
# =========================================================

def send_message(event=None):

    message = text_box.get().strip()

    if message == "":
        return "break"

    reply = get_reply(message)

    current_time = datetime.now().strftime("%H:%M")

    conversation.config(state="normal")

    # User message
    conversation.insert(
        tk.END,
        f"You  •  {current_time}\n",
        "user_name"
    )

    conversation.insert(
        tk.END,
        f"{message}\n\n",
        "user_message"
    )

    # Bot message
    conversation.insert(
        tk.END,
        f"Bot  •  {current_time}\n",
        "bot_name"
    )

    conversation.insert(
        tk.END,
        f"{reply}\n\n",
        "bot_message"
    )

    conversation.config(state="disabled")

    conversation.see(tk.END)

    # Clear input
    text_box.delete(0, tk.END)
    text_box.focus_set()

    # Prevent duplicate Enter message
    return "break"


# =========================================================
# CLEAR CHAT
# =========================================================

def clear_chat():

    conversation.config(state="normal")

    conversation.delete("1.0", tk.END)

    conversation.insert(
        tk.END,
        "Bot  •  Now\n",
        "bot_name"
    )

    conversation.insert(
        tk.END,
        "Hello! 👋 I'm My ChatBot.\n"
        "How can I help you today?\n\n",
        "bot_message"
    )

    conversation.config(state="disabled")

    conversation.see(tk.END)

    text_box.focus_set()


# =========================================================
# MAIN WINDOW
# =========================================================

window = tk.Tk()

window.title("My ChatBot")

# CHANGED SIZE
window.geometry("720x550")

# CHANGED MINIMUM SIZE
window.minsize(600, 500)

window.configure(bg="#0f172a")


# =========================================================
# HEADER
# =========================================================

header = tk.Frame(
    window,
    bg="#1e293b",
    height=80
)

header.pack(
    fill="x"
)

header.pack_propagate(False)


# Robot icon
bot_icon = tk.Label(
    header,
    text="🤖",
    font=("Segoe UI Emoji", 26),
    bg="#1e293b"
)

bot_icon.pack(
    side="left",
    padx=(20, 10)
)


# Title section
title_frame = tk.Frame(
    header,
    bg="#1e293b"
)

title_frame.pack(
    side="left",
    pady=10
)


title = tk.Label(
    title_frame,
    text="My ChatBot",
    font=("Segoe UI", 20, "bold"),
    fg="#f8fafc",
    bg="#1e293b"
)

title.pack(
    anchor="w"
)


status = tk.Label(
    title_frame,
    text="● Online • Ready to chat",
    font=("Segoe UI", 9),
    fg="#22c55e",
    bg="#1e293b"
)

status.pack(
    anchor="w"
)


# =========================================================
# CHAT AREA
# =========================================================

chat_frame = tk.Frame(
    window,
    bg="#0f172a"
)

chat_frame.pack(
    fill="both",
    expand=True,
    padx=15,
    pady=10
)


# Scrollbar
scrollbar = tk.Scrollbar(
    chat_frame,
    orient="vertical"
)

scrollbar.pack(
    side="right",
    fill="y"
)


# Conversation
conversation = tk.Text(
    chat_frame,
    font=("Segoe UI", 11),
    bg="#f8fafc",
    fg="#0f172a",
    relief="flat",
    bd=0,
    padx=15,
    pady=15,
    wrap="word",
    yscrollcommand=scrollbar.set
)

conversation.pack(
    side="left",
    fill="both",
    expand=True
)


scrollbar.config(
    command=conversation.yview
)


# =========================================================
# TEXT COLORS
# =========================================================

conversation.tag_configure(
    "user_name",
    foreground="#2563eb",
    font=("Segoe UI", 10, "bold")
)

conversation.tag_configure(
    "user_message",
    foreground="#1e293b",
    font=("Segoe UI", 11)
)

conversation.tag_configure(
    "bot_name",
    foreground="#059669",
    font=("Segoe UI", 10, "bold")
)

conversation.tag_configure(
    "bot_message",
    foreground="#334155",
    font=("Segoe UI", 11)
)


# =========================================================
# WELCOME MESSAGE
# =========================================================

conversation.insert(
    tk.END,
    "Bot  •  Now\n",
    "bot_name"
)

conversation.insert(
    tk.END,
    "Hello! 👋 I'm My ChatBot.\n"
    "How can I help you today?\n\n",
    "bot_message"
)

conversation.config(
    state="disabled"
)


# =========================================================
# INPUT AREA
# =========================================================

input_frame = tk.Frame(
    window,
    bg="#0f172a"
)

input_frame.pack(
    fill="x",
    padx=15,
    pady=(0, 5)
)


# Input box
text_box = tk.Entry(
    input_frame,
    font=("Segoe UI", 12),
    bg="white",
    fg="#0f172a",
    insertbackground="#2563eb",
    relief="flat",
    bd=0
)

text_box.pack(
    side="left",
    fill="x",
    expand=True,
    ipady=10,
    padx=(0, 10)
)


# =========================================================
# SEND BUTTON
# =========================================================

send_button = tk.Button(
    input_frame,
    text="Send  ➤",
    font=("Segoe UI", 11, "bold"),
    bg="#2563eb",
    fg="white",
    activebackground="#1d4ed8",
    activeforeground="white",
    relief="flat",
    bd=0,
    padx=20,
    pady=9,
    cursor="hand2",
    command=send_message
)

send_button.pack(
    side="right"
)


# =========================================================
# CLEAR BUTTON
# =========================================================

clear_button = tk.Button(
    window,
    text="Clear Chat",
    font=("Segoe UI", 9),
    bg="#0f172a",
    fg="#94a3b8",
    activebackground="#0f172a",
    activeforeground="white",
    relief="flat",
    bd=0,
    cursor="hand2",
    command=clear_chat
)

clear_button.pack(
    pady=(0, 8)
)


# =========================================================
# ENTER KEY
# =========================================================

text_box.bind(
    "<Return>",
    send_message
)


# =========================================================
# START
# =========================================================

text_box.focus_set()
window.mainloop()
