# -*- coding: utf-8 -*-
"""
Created on Tue Feb 04 7:16:25 2025

@author: IAN CARTER KULANI

"""

import tkinter as tk
from tkinter import messagebox

# Function to calculate the residual energy
def calculate_residual_energy(initial_energy, total_consumed_energy):
    return initial_energy - total_consumed_energy

# Function to handle the button click event and perform the calculations
def calculate_energy():
    try:
        # Get the input values from the entry fields
        initial_energy = float(initial_energy_entry.get())
        total_consumed_energy = float(total_consumed_energy_entry.get())
        
        # Ensure that total consumed energy is not greater than initial energy
        if total_consumed_energy > initial_energy:
            messagebox.showerror("Input Error", "Total consumed energy cannot exceed initial energy!")
            return
        
        # Calculate residual energy
        residual_energy = calculate_residual_energy(initial_energy, total_consumed_energy)
        
        # Display the result
        result_label.config(text=f"Residual Energy: {residual_energy:.2f} Joules")
    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid numerical values.")

# Creating the main window
root = tk.Tk()
root.title("Residual Energy Calculator")
root.geometry("400x300")
root.configure(bg="yellow")

# Title Label
title_label = tk.Label(root, text="FANET Residual Energy Calculator", font=("Arial", 16), bg="yellow")
title_label.pack(pady=10)

# Initial Energy Entry
initial_energy_label = tk.Label(root, text="Enter Initial Energy (in Joules):", font=("Arial", 12), bg="yellow")
initial_energy_label.pack(pady=5)

initial_energy_entry = tk.Entry(root, font=("Arial", 12))
initial_energy_entry.pack(pady=5)

# Total Consumed Energy Entry
total_consumed_energy_label = tk.Label(root, text="Enter Total Consumed Energy (in Joules):", font=("Arial", 12), bg="yellow")
total_consumed_energy_label.pack(pady=5)

total_consumed_energy_entry = tk.Entry(root, font=("Arial", 12))
total_consumed_energy_entry.pack(pady=5)

# Calculate Button
calculate_button = tk.Button(root, text="Calculate Residual Energy", font=("Arial", 12), bg="yellow", command=calculate_energy)
calculate_button.pack(pady=20)

# Result Label
result_label = tk.Label(root, text="Residual Energy: ", font=("Arial", 12), bg="yellow")
result_label.pack(pady=10)

# Run the Tkinter event loop
root.mainloop()
