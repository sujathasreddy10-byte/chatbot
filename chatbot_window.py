import tkinter as tk
import random
from datetime import datetime


# =========================================================
# BASIC AI
# =========================================================

class BasicAI:

    def __init__(self):
        self.user_name = None

        self.responses = {
            "hello": [
                "Hello! 👋 How can I help you?",
                "Hi! 😊 Nice to meet you!",
                "Hey! What would you like to know?"
            ],

            "how are you": [
                "I'm doing great! 😊",
                "I'm good! Thanks for asking.",
                "I'm ready to help you!"
            ],

            "bye": [
                "Goodbye! 👋",
                "See you later!",
                "Have a great day! 😊"
            ],

            "thanks": [
                "You're welcome! 😊",
                "Happy to help!",
                "Anytime!"
            ]
        }

    def get_response(self, message):

        message = message.lower().strip()

        # ---------------------------------------------
        # EMPTY MESSAGE
        # ---------------------------------------------

        if not message:
            return "Please type something."


        # ---------------------------------------------
        # REMEMBER NAME
        # ---------------------------------------------

        if message.startswith("my name is "):

            self.user_name = message.replace(
                "my name is ",
                ""
            ).strip()

            return f"Nice to meet you, {self.user_name}! 😊"


        # ---------------------------------------------
        # ASK NAME
        # ---------------------------------------------

        if "what is my name" in message:

            if self.user_name:
                return f"Your name is {self.user_name}. 😊"

            return "I don't know your name yet."


        # ---------------------------------------------
        # TIME
        # ---------------------------------------------

        if "what time" in message or "current time" in message:

            current_time = datetime.now().strftime("%I:%M %p")

            return f"The current time is {current_time}."


        # ---------------------------------------------
        # DATE
        # ---------------------------------------------

        if "what date" in message or "today's date" in message:

            current_date = datetime.now().strftime(
                "%d %B %Y"
            )

            return f"Today's date is {current_date}."


        # ---------------------------------------------
        # JAVA
        # ---------------------------------------------

        if "what is java" in message:

            return (
                "Java is a high-level, object-oriented "
                "programming language. It is widely used "
                "for backend applications, Android development, "
                "enterprise applications and many other projects."
            )


        # ---------------------------------------------
        # PYTHON
        # ---------------------------------------------

        if "what is python" in message:

            return (
                "Python is a high-level programming language "
                "known for its simple syntax. It is commonly "
                "used for AI, machine learning, web development, "
                "automation and data science."
            )


        # ---------------------------------------------
        # DOCKER
        # ---------------------------------------------

        if "what is docker" in message:

            return (
                "Docker is a platform used to package and run "
                "applications inside containers. Containers "
                "make applications easier to develop, test "
                "and deploy."
            )


        # ---------------------------------------------
        # SPRING BOOT
        # ---------------------------------------------

        if "spring boot" in message:

            return (
                "Spring Boot is a Java framework used to build "
                "backend and REST API applications quickly. "
                "It simplifies configuration and application setup."
            )


        # ---------------------------------------------
        # HASHMAP
        # ---------------------------------------------

        if "hashmap" in message:

            return (
                "HashMap is a Java collection that stores data "
                "as key-value pairs. For example:\n\n"
                "HashMap<String, Integer> marks = new HashMap<>();"
            )


        # ---------------------------------------------
        # GREETING
        # ---------------------------------------------

        if message in ["hi", "hello", "hey", "hii", "hlo"]:

            return random.choice(
                self.responses["hello"]
            )


        # ---------------------------------------------
        # HOW ARE YOU
        # ---------------------------------------------

        if "how are you" in message:

            return random.choice(
                self.responses["how are you"]
            )


        # ---------------------------------------------
        # THANK YOU
        # ---------------------------------------------

        if (
            "thank you" in message
            or "thanks" in message
        ):

            return random.choice(
                self.responses["thanks"]
            )


        # ---------------------------------------------
        # GOODBYE
        # ---------------------------------------------

        if (
            message == "bye"
            or "goodbye" in message
        ):

            return random.choice(
                self.responses["bye"]
            )


        # ---------------------------------------------
        # SIMPLE MATH
        # ---------------------------------------------

        try:

            allowed = "0123456789+-*/(). "

            if all(
                character in allowed
                for character in message
            ):

                result = eval(
                    message,
                    {
                        "__builtins__": None
                    },
                    {}
                )

                return f"The answer is {result}"

        except:
            pass


        # ---------------------------------------------
        # DEFAULT RESPONSE
        # ---------------------------------------------

        return (
            "I'm still learning. 🤖\n\n"
            "Try asking me something like:\n"
            "• What is Java?\n"
            "• What is Python?\n"
            "• What is Docker?\n"
            "• What is HashMap?\n"
            "• What is Spring Boot?\n"
            "• What time is it?\n"
            "• My name is Anushree"
        )


# =========================================================
# CREATE AI
# =========================================================

ai = BasicAI()


# =========================================================
# SEND MESSAGE
# =========================================================

def send_message(event=None):

    message = input_box.get().strip()

    if not message:
        return "break"

    current_time = datetime.now().strftime("%H:%M")

    # Display user
    chat.config(state="normal")

    chat.insert(
        tk.END,
        f"You  •  {current_time}\n",
        "user_name"
    )

    chat.insert(
        tk.END,
        f"{message}\n\n",
        "user_message"
    )

    # Get AI response
    response = ai.get_response(message)

    # Display AI
    chat.insert(
        tk.END,
        f"AI  •  {datetime.now().strftime('%H:%M')}\n",
        "ai_name"
    )

    chat.insert(
        tk.END,
        f"{response}\n\n",
        "ai_message"
    )

    chat.config(state="disabled")

    chat.see(tk.END)

    input_box.delete(
        0,
        tk.END
    )

    return "break"


# =========================================================
# CLEAR CHAT
# =========================================================

def clear_chat():

    ai.user_name = None

    chat.config(
        state="normal"
    )

    chat.delete(
        "1.0",
        tk.END
    )

    chat.insert(
        tk.END,
        "AI  •  Now\n",
        "ai_name"
    )

    chat.insert(
        tk.END,
        "Hello! 👋 I'm your basic AI.\n"
        "Ask me something!\n\n",
        "ai_message"
    )

    chat.config(
        state="disabled"
    )

    input_box.focus_set()


# =========================================================
# WINDOW
# =========================================================

window = tk.Tk()

window.title(
    "Basic AI ChatBot"
)

window.geometry(
    "850x650"
)

window.minsize(
    700,
    500
)

window.configure(
    bg="#0f172a"
)


# =========================================================
# GRID
# =========================================================

window.grid_rowconfigure(
    1,
    weight=1
)

window.grid_columnconfigure(
    0,
    weight=1
)


# =========================================================
# HEADER
# =========================================================

header = tk.Frame(
    window,
    bg="#1e293b",
    height=90
)

header.grid(
    row=0,
    column=0,
    sticky="ew"
)

header.grid_propagate(False)


tk.Label(
    header,
    text="🤖",
    font=("Segoe UI Emoji", 30),
    bg="#1e293b",
    fg="white"
).pack(
    side="left",
    padx=(25, 12)
)


title_frame = tk.Frame(
    header,
    bg="#1e293b"
)

title_frame.pack(
    side="left",
    pady=15
)


tk.Label(
    title_frame,
    text="Basic AI ChatBot",
    font=("Segoe UI", 22, "bold"),
    bg="#1e293b",
    fg="white"
).pack(
    anchor="w"
)


tk.Label(
    title_frame,
    text="● Local AI • Ready to chat",
    font=("Segoe UI", 10),
    bg="#1e293b",
    fg="#22c55e"
).pack(
    anchor="w"
)


# =========================================================
# CHAT AREA
# =========================================================

chat_frame = tk.Frame(
    window,
    bg="#f1f5f9"
)

chat_frame.grid(
    row=1,
    column=0,
    sticky="nsew",
    padx=15,
    pady=15
)

chat_frame.grid_rowconfigure(
    0,
    weight=1
)

chat_frame.grid_columnconfigure(
    0,
    weight=1
)


chat = tk.Text(
    chat_frame,
    font=("Segoe UI", 12),
    bg="white",
    fg="#0f172a",
    wrap="word",
    relief="flat",
    bd=0,
    padx=20,
    pady=20
)

chat.grid(
    row=0,
    column=0,
    sticky="nsew"
)


# =========================================================
# SCROLLBAR
# =========================================================

scrollbar = tk.Scrollbar(
    chat_frame,
    command=chat.yview
)

scrollbar.grid(
    row=0,
    column=1,
    sticky="ns"
)

chat.config(
    yscrollcommand=scrollbar.set
)


# =========================================================
# TEXT STYLES
# =========================================================

chat.tag_configure(
    "user_name",
    foreground="#2563eb",
    font=("Segoe UI", 10, "bold")
)

chat.tag_configure(
    "user_message",
    foreground="#0f172a",
    font=("Segoe UI", 12)
)

chat.tag_configure(
    "ai_name",
    foreground="#059669",
    font=("Segoe UI", 10, "bold")
)

chat.tag_configure(
    "ai_message",
    foreground="#334155",
    font=("Segoe UI", 12)
)


# =========================================================
# WELCOME
# =========================================================

chat.insert(
    tk.END,
    "AI  •  Now\n",
    "ai_name"
)

chat.insert(
    tk.END,
    "Hello! 👋 I'm your basic AI.\n"
    "Ask me something!\n\n",
    "ai_message"
)

chat.config(
    state="disabled"
)


# =========================================================
# INPUT AREA
# =========================================================

bottom = tk.Frame(
    window,
    bg="#0f172a",
    height=75
)

bottom.grid(
    row=2,
    column=0,
    sticky="ew",
    padx=15,
    pady=(0, 5)
)

bottom.grid_propagate(False)


input_box = tk.Entry(
    bottom,
    font=("Segoe UI", 13),
    bg="white",
    fg="#0f172a",
    relief="flat",
    bd=0
)

input_box.pack(
    side="left",
    fill="both",
    expand=True,
    padx=5,
    pady=10,
    ipady=10
)


send_button = tk.Button(
    bottom,
    text="Send  ➤",
    font=("Segoe UI", 11, "bold"),
    bg="#2563eb",
    fg="white",
    activebackground="#1d4ed8",
    activeforeground="white",
    relief="flat",
    bd=0,
    cursor="hand2",
    padx=25,
    pady=10,
    command=send_message
)

send_button.pack(
    side="right",
    padx=5,
    pady=10
)


# =========================================================
# CLEAR BUTTON
# =========================================================

clear_button = tk.Button(
    window,
    text="Clear Chat",
    font=("Segoe UI", 9, "bold"),
    bg="#0f172a",
    fg="#94a3b8",
    activebackground="#0f172a",
    activeforeground="white",
    relief="flat",
    bd=0,
    command=clear_chat
)

clear_button.grid(
    row=3,
    column=0,
    pady=(0, 8)
)


# =========================================================
# ENTER KEY
# =========================================================

input_box.bind(
    "<Return>",
    send_message
)

input_box.focus_set()


# =========================================================
# START
# =========================================================

window.mainloop()