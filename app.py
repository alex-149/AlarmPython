import tkinter as tk
from tkinter import messagebox
import time
from playsound import playsound  # You can install playsound using: pip install playsound

class AlarmClock:
    def __init__(self, root):
        self.root = root
        self.root.title("Alarm Clock")

        self.label = tk.Label(root, text="Enter time (HH:MM):")
        self.label.pack(pady=10)

        self.entry = tk.Entry(root)
        self.entry.pack(pady=10)

        self.set_button = tk.Button(root, text="Set Alarm", command=self.set_alarm)
        self.set_button.pack(pady=10)

    def set_alarm(self):
        alarm_time = self.entry.get()
        try:
            hours, minutes = map(int, alarm_time.split(':'))
            now = time.localtime()
            alarm_timestamp = time.mktime((now.tm_year, now.tm_mon, now.tm_mday, hours, minutes, 0, 0, 0, now.tm_isdst))

            current_timestamp = time.mktime(time.localtime())

            if alarm_timestamp > current_timestamp:
                time_difference = alarm_timestamp - current_timestamp
                messagebox.showinfo("Alarm Set", f"Alarm set for {alarm_time}")
                self.root.after(int(time_difference * 1000), self.trigger_alarm)
            else:
                messagebox.showwarning("Invalid Time", "Please enter a future time.")

        except ValueError:
            messagebox.showerror("Invalid Format", "Please enter time in HH:MM format.")

    def trigger_alarm(self):
        messagebox.showinfo("Alarm", "Time's up!")
        playsound("path_to_alarm_sound.mp3")  # Replace with the path to your alarm sound file

if __name__ == "__main__":
    root = tk.Tk()
    alarm_clock = AlarmClock(root)
    root.mainloop()
