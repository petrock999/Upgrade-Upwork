import tkinter as tk
from tkinter import ttk

# Initialize the root window
root = tk.Tk()
root.title("Job Selector")

# Choices for the main and sub dropdowns
main_choices = ["Web Development", "Social Media Marketing", "Marketing Strategy", "Mobile App Development", "3D Modeling"]
sub_choices = {
    "Web Development": ["WordPress", "Web Design", "Shopify"],
    "Social Media Marketing": ["Marketing Strategy", "Facebook", "Instagram"],
    "Marketing Strategy": ["Social Media Marketing", "Internet Marketing", "Email Marketing"],
    "Mobile App Development": ["Android App Development", "iOS Development", "Android"],
    "3D Modeling": ["3D Design", "3D Rendering", "3D Animation"]
}

# Custom job titles and descriptions
custom_jobs = {
    ("3D Modeling", "3D Design"): {"title": "Unreal Engine Expert", "description": "Create 3D models for Unreal Engine."},
    # Add other combinations here
}

# Function to update the sub-choice dropdown
def update_subchoices(*args):
    chosen_category = main_choice.get()
    sub_choice_dropdown['values'] = sub_choices[chosen_category]

# Function to update job title and description based on custom selections
def update_job_info():
    main = main_choice.get()
    sub = sub_choice.get()
    job_info = custom_jobs.get((main, sub), {"title": "N/A", "description": "N/A"})
    job_title_label.config(text=f"Job Title: {job_info['title']}")
    job_desc_label.config(text=f"Job Description: {job_info['description']}")

# Main choice dropdown
main_choice = tk.StringVar()
main_choice_dropdown = ttk.Combobox(root, textvariable=main_choice, values=main_choices)
main_choice_dropdown.grid(column=0, row=0, padx=10, pady=10)
main_choice_dropdown.bind('<<ComboboxSelected>>', update_subchoices)

# Sub choice dropdown
sub_choice = tk.StringVar()
sub_choice_dropdown = ttk.Combobox(root, textvariable=sub_choice)
sub_choice_dropdown.grid(column=1, row=0, padx=10, pady=10)

# Button to update job info
update_button = ttk.Button(root, text="Update Job Info", command=update_job_info)
update_button.grid(column=0, row=1, columnspan=2, pady=10)

# Labels for job title and description
job_title_label = ttk.Label(root, text="Job Title: ")
job_title_label.grid(column=0, row=2, padx=10, pady=10, sticky="w")

job_desc_label = ttk.Label(root, text="Job Description: ")
job_desc_label.grid(column=0, row=3, padx=10, pady=10, sticky="w")

# Start the GUI loop
root.mainloop()
