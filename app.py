# app.py

import tkinter as tk
from tkinter import ttk, messagebox
from recipes import RECIPES

class MealPlannerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Meal Planner App")
        
        self.dietary_pref = tk.StringVar()
        self.available_ingredients = tk.StringVar()
        
        self.create_welcome_screen()
        
    def create_welcome_screen(self):
        self.clear_screen()
        
        tk.Label(self.root, text="Welcome to the Meal Planner App! (only veg)", font=("Helvetica", 16)).pack(pady=10)
        
        tk.Label(self.root, text="Select your dietary preference:").pack(pady=5)
        self.dietary_pref_combo = ttk.Combobox(self.root, textvariable=self.dietary_pref)
        self.dietary_pref_combo['values'] = ('Vegetarian', 'Vegan', 'Gluten-Free')
        self.dietary_pref_combo.pack(pady=5)
        
        tk.Label(self.root, text="Enter available ingredients :").pack(pady=5)
        self.ingredients_entry = tk.Entry(self.root, textvariable=self.available_ingredients, width=50)
        self.ingredients_entry.pack(pady=5)
        
        tk.Button(self.root, text="Submit", command=self.submit_preferences).pack(pady=20)
    
    def submit_preferences(self):
        if not self.dietary_pref.get() or not self.available_ingredients.get():
            messagebox.showwarning("Input Error", "Please fill in all fields")
            return
        
        self.create_meal_plan_screen()
    
    def create_meal_plan_screen(self):
        self.clear_screen()
        
        meal_plan = self.generate_meal_plan()
        
        tk.Label(self.root, text="Your Weekly Meal Plan", font=("Helvetica", 16)).pack(pady=10)
        
        for day, meal in meal_plan.items():
            tk.Label(self.root, text=f"{day}: {meal['Dish']}").pack()
            tk.Label(self.root, text=f"Ingredients: {', '.join(meal['Ingredients'])}").pack(pady=5)
        
        tk.Button(self.root, text="Back", command=self.create_welcome_screen).pack(pady=20)
    
    def generate_meal_plan(self):
        # A simple implementation to get a meal plan based on dietary preference
        diet = self.dietary_pref.get()
        if diet in RECIPES:
            return RECIPES[diet]
        else:
            return {}
    
    def clear_screen(self):
        for widget in self.root.winfo_children():
            widget.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    app = MealPlannerApp(root)
    root.mainloop()
