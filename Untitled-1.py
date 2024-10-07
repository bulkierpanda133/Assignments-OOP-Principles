class BudgetCategory:
    def __init__(self, category_name, allocated_budget):
        # Private attributes
        self.__category_name = category_name
        self.__allocated_budget = allocated_budget
        self.__remaining_budget = allocated_budget  # Track remaining budget

    # Getter for category name
    def get_category_name(self):
        return self.__category_name

    # Setter for category name
    def set_category_name(self, name):
        self.__category_name = name

    # Getter for allocated budget
    def get_allocated_budget(self):
        return self.__allocated_budget

    # Setter for allocated budget with validation
    def set_allocated_budget(self, budget):
        if budget >= 0:
            self.__allocated_budget = budget
            self.__remaining_budget = budget  # Reset remaining budget
        else:
            raise ValueError("Budget must be a positive number.")

    # Method to add an expense to the category
    def add_expense(self, amount):
        if amount < 0:
            raise ValueError("Expense amount must be a positive number.")
        if amount > self.__remaining_budget:
            raise ValueError("Expense exceeds remaining budget.")
        
        self.__remaining_budget -= amount
        print(f"Expense of {amount} added. Remaining budget: {self.__remaining_budget}")

    # Method to display the budget category details
    def display_category_summary(self):
        print(f"Category: {self.__category_name}")
        print(f"Allocated Budget: {self.__allocated_budget}")
        print(f"Remaining Budget: {self.__remaining_budget}")

# Example usage
food_category = BudgetCategory("Food", 500)
food_category.add_expense(100)
food_category.display_category_summary()
