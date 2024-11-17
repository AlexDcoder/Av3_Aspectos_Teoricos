from __future__ import annotations
from tkinter import END, messagebox
from typing import Tuple
import customtkinter


# Creating home configs
customtkinter.set_appearance_mode("Dark")


def alert_error(error_message):
    '''
        Show alert for error
    '''
    messagebox.showerror(title="Error founded", message=error_message)


def alert_information(information_message):
    '''
        Show alert for information
    '''
    messagebox.showinfo(message=information_message)


class Analyser(customtkinter.CTk):
    '''
        Creating the app for SQL code explainer
    '''

    def __init__(self, fg_color: str | Tuple[str, str] | None = None,
                 **kwargs):
        super().__init__(fg_color, **kwargs)

        self.title('Compiler')
        self.geometry("1466X868")

        self.app_name = customtkinter.CTkLabel(
            self, text="Compiler", font=customtkinter.CTkFont(
                family='Modern No. 20', size=32,
                weight='bold'))

        self.app_name.pack(pady=12)

        self._description_app = customtkinter.CTkLabel(
            self, text=('A portuguese language code compiler.'),
            font=customtkinter.CTkFont(
                family='Trebuchet MS', slant='italic'),
        )
        self._description_app.pack()

        self.input_output_frame = customtkinter.CTkFrame(
            self, fg_color=("gray100", "gray15"))
        self.input_output_frame.pack(pady=10)

        self.input_frame = customtkinter.CTkFrame(self.input_output_frame)
        self.input_frame.pack(padx=10, side="left")

        self.input_label = customtkinter.CTkLabel(
            self.input_frame, text="Context", font=customtkinter.CTkFont(
                family="Yu Gothic UI Semibold"))
        self.input_label.pack()

        self.input_textarea = customtkinter.CTkTextbox(
            self.input_frame, width=550, height=400,
            font=customtkinter.CTkFont(family="Yu Gothic UI Semibold"),
            corner_radius=0, wrap="none")

        placeholder_text = "Insert your code here."
        self.input_textarea.insert(1.0, placeholder_text)
        self.input_textarea.bind("<FocusIn>", self.clear_placeholder)
        self.input_textarea.bind(
            "<FocusOut>",
            lambda event: self.add_placeholder(event, placeholder_text))
        self.input_textarea.pack()

        self.compile_button = customtkinter.CTkButton(
            self.input_frame, text='Compile',
            fg_color=("green"), hover_color=('#19692c'),
            command=self.compile,
            font=customtkinter.CTkFont(family="@Yu Gothic UI", weight="bold"))
        self.compile_button.pack(side='right', pady=10, padx=10)

        self.clear_button = customtkinter.CTkButton(
            self.input_frame, text='Clear',
            fg_color='red',
            hover_color=("#DB3E39", "#821D1A"),
            command=self.clear_input,
            font=customtkinter.CTkFont(family="@Yu Gothic UI", weight="bold")
        )
        self.clear_button.pack(side="right", pady=10, padx=10)

        self.output_frame = customtkinter.CTkFrame(self.input_output_frame)
        self.output_frame.pack(padx=10, side="left")
        self.output_label = customtkinter.CTkLabel(
            self.output_frame, text="Output", font=customtkinter.CTkFont(
                family="Yu Gothic UI Semibold"))
        self.output_label.pack()

        self.output_textbox = customtkinter.CTkTextbox(
            self.output_frame, 550, 400,
            fg_color=("transparent")
        )
        self.output_textbox.configure(state='disabled')
        self.output_textbox.pack()

        self.copy_output = customtkinter.CTkButton(
            self.output_frame,
            text='Copy',
            command=self.copy,
            font=customtkinter.CTkFont(family="@Yu Gothic UI", weight="bold")
        )
        self.copy_output.pack(side="right", pady=10, padx=10)

    def clear_placeholder(self, event):
        if self.input_textarea.get("1.0", "end-1c") == "Insert your code here.":
            self.input_textarea.delete("1.0", END)

    def add_placeholder(self, event, placeholder_text):
        if not self.input_textarea.get("1.0", "end-1c").strip():
            self.input_textarea.insert("1.0", placeholder_text)

    def compile(self):
        self.output_textbox.configure(state='normal')
        self.output_textbox.delete("1.0", END)
        self.output_textbox.insert("1.0", "oi")

    def clear_input(self):
        '''
            Clear context from input textarea
        '''
        if self.input_textarea.get("1.0", "end-1c") != \
                "Insert your code here.":
            self.input_textarea.delete("0.0", END)

    def copy(self):
        self.output_textbox.configure(state='normal')
        result = self.output_textbox.get("1.0", END)
        self.clipboard_append(result)
        self.add_placeholder(None, "Insert your code here.")


if __name__ == '__main__':
    analyser = Analyser()
    analyser.mainloop()
