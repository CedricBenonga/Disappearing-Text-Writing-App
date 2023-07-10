import math
from tkinter import *


# Screen
BG_COLOR = "#125B50"
window = Tk()
window.title("© Cedric Benonga")
window.minsize(width=900, height=450)
window.config(padx=50, pady=10, bg=BG_COLOR)


def blurry():

    # Restart counting down
    window.after_cancel(timer)
    star_button.grid_forget()
    disappear(6)


def disappear(count):

    global timer, placeholder_text
    time = math.floor(count - 1)

    if time == 5:

        # Changing label
        label.config(text="Keep typing!")

        # Displaying the typing box.
        typing_box.grid(row=3, column=0, padx=200, pady=50)  # padding inside grid creates margin
        typing_box.config(foreground="#000")

        # Saving the actual length
        text_length_5 = len(typing_box.get("1.0", END))
        with open("text_lgt.text", mode="w") as file:
            file.write(f"{text_length_5}")

    if time == 4:

        # Changing label
        label.config(text=f"You have {time} left!")
        # Displaying the typing box.
        typing_box.grid(row=3, column=0, padx=200, pady=50)

        # Counting the actual length
        text_length_4 = len(typing_box.get("1.0", END))

        # Checking the previous the length
        with open("text_lgt.text") as file:
            file_4 = file.read()  # The outcome is always a String, even if it's a number, just like "input" function
            file_4 = int(file_4)

        # Comparing both lengths
        if file_4 == text_length_4:
            typing_box.config(foreground="#555")

        else:
            # Stop counting while the user's typing
            window.after_cancel(timer)
            typing_box.config(foreground="#000")

            # Saving the new length
            with open("text_lgt.text", mode="w") as file:
                file.write(f"{text_length_4}")

                # Take the user back on the most clear screen if they type anything
                disappear(6)

    if time == 3:

        # Changing label
        label.config(text=f"You have {time} left!")
        # Displaying the typing box.
        typing_box.grid(row=3, column=0, padx=200, pady=50)

        # Counting the actual length
        text_length_3 = len(typing_box.get("1.0", END))

        # Checking the previous the length
        with open("text_lgt.text") as file:
            file_3 = file.read()  # The outcome is always a String, even if it's a number, just like "input" function
            file_3 = int(file_3)

        # Comparing both lengths
        if file_3 == text_length_3:
            typing_box.config(foreground="#999")

        else:
            # Stop counting while the user's typing
            window.after_cancel(timer)
            typing_box.config(foreground="#000")

            # Saving the new length
            with open("text_lgt.text", mode="w") as file:
                file.write(f"{text_length_3}")

                # Take the user back on the most clear screen if they type anything
                disappear(6)

    if time == 2:

        # Changing label
        label.config(text=f"You have {time} left!")
        # Displaying the typing box.
        typing_box.grid(row=3, column=0, padx=200, pady=50)

        # Counting the actual length
        text_length_2 = len(typing_box.get("1.0", END))

        # Checking the previous the length
        with open("text_lgt.text") as file:
            file_2 = file.read()  # The outcome is always a String, even if it's a number, just like "input" function
            file_2 = int(file_2)

        # Comparing both lengths
        if file_2 == text_length_2:
            typing_box.config(foreground="#DFDFDE")

        else:
            # Stop counting while the user's typing
            window.after_cancel(timer)
            typing_box.config(foreground="#000")

            # Saving the new length
            with open("text_lgt.text", mode="w") as file:
                file.write(f"{text_length_2}")

                # Take the user back on the most clear screen if they type anything
                disappear(6)

    if time == 1:

        # Changing label
        label.config(text=f"You have {time} left!")
        # Displaying the typing box.
        typing_box.grid(row=3, column=0, padx=200, pady=50)

        # Counting the actual length
        text_length_1 = len(typing_box.get("1.0", END))

        # Checking the previous the length
        with open("text_lgt.text") as file:
            file_1 = file.read()  # The outcome is always a String, even if it's a number, just like "input" function
            file_1 = int(file_1)

        # Comparing both lengths
        if file_1 == text_length_1:
            typing_box.config(foreground="#EEEEEE")

        else:
            # Stop counting while the user's typing
            window.after_cancel(timer)
            typing_box.config(foreground="#000")

            # Saving the new length
            with open("text_lgt.text", mode="w") as file:
                file.write(f"{text_length_1}")

                # Take the user back on the most clear screen if they type anything
                disappear(6)

    if time == 0:
        # Stop counting as the time is up and Take off the typing box.
        window.after_cancel(timer)
        typing_box.grid_forget()

        # Tell the user what happened.
        label.config(text="Oops! You're thinking too much!")

        # Give the user option to retry/restart from scratch and disregard their previous progres
        star_button.config(text="Retry")
        star_button.grid(column=0, row=4, padx=400)
        typing_box.delete("1.0", END)

        # Add some placeholder text
        typing_box.insert(END, placeholder_text)

        # text_length = int(len(typing_box.get("1.0", END)))
        # 
        # if text_length == 33:
        #     typing_box.config(insertontime=0)
        #
        # if text_length != 33:
        #     # typing_box.focus_set()
        #     typing_box.config(insertontime=1)

        typing_box.bind("<Button-1>", lambda event: typing_box.delete("1.0", END))

    timer = window.after(1000, disappear, count - 1)


timer = window.after(0, disappear, 0)

title = Label(text="5 seconds disappearing text App!", font=("Ariel", 20, "bold"), bg=BG_COLOR)
title.grid(row=1, column=0, padx=200, pady=10)

label = Label(text="Don't be inactive for 5 seconds!", font=("Ariel", 15, "bold"), bg=BG_COLOR)
label.grid(row=2, column=0, padx=200, pady=10)

typing_box = Text(height=10, width=50)
placeholder_text = "You only have 5 second to think."
typing_box.insert(END, placeholder_text)
typing_box.bind("<Button-1>", lambda event: typing_box.delete("1.0", END))


typing_box.grid_forget()

star_button = Button(text='Start', command=blurry)
star_button.config(padx=20)
star_button.grid(column=0, row=4, padx=400)

window.mainloop()
