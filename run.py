import wx
import wx.grid
import pandas as pd
import re
import matplotlib

matplotlib.use('WXAgg')  # allows Matplotlib to render plots within wxPython.
# to embed a Matplotlib figure into a wxPanel in a wxPython application.
import matplotlib
matplotlib.use('WXAgg')  # Use the WXAgg backend for wxPython
from matplotlib.backends.backend_wxagg import FigureCanvasWxAgg as FigureCanvas
from matplotlib.figure import Figure

from matplotlib.backends.backend_wxagg import FigureCanvasWxAgg
import matplotlib.pyplot as plt

from all_functions import search_data, prepare_macro_nutrient_data, prepare_micro_nutrient_data
from all_functions import search_data, calculate_bmi, calculate_nutrition
from all_functions import search_data, filter_nutrients, prepare_macro_nutrient_data, prepare_micro_nutrient_data
from template_frame import MyFrame1


class DataTable(wx.grid.GridTableBase):
    def __init__(self, data):
        wx.grid.GridTableBase.__init__(self)
        self.data = data
        self.col_labels = list(data.columns)
        self.row_count = len(data)
        self.col_count = len(self.col_labels)

    # Returns the number of rows in the DataFrame
    def GetNumberRows(self):
        return self.row_count

    # Returns the number of columns in the DataFrame
    def GetNumberCols(self):
        return self.col_count

    # Returns the value for a specific cell
    def GetValue(self, row, col):
        return str(self.data.iloc[row, col])

    # Returns the column label
    def GetColLabelValue(self, col):
        return self.col_labels[col]


class CalcFrame(MyFrame1):
    def __init__(self, parent=None):
        super().__init__(parent)

        # Set the size of the frame (width, height)
        self.SetSize(1500, 800)
        self.Centre()

        # Read the CSV file into a pandas DataFrame
        self.df = pd.read_csv(r"./Food_Nutrition_Dataset.csv")

        # Set the table data in the wxGrid
        self.table = DataTable(self.df)
        self.m_grid1.SetTable(self.table, takeOwnership=True)

        # Resize grid columns to fit content
        self.m_grid1.AutoSize()

        # Bind the grid selection event
        self.m_grid1.Bind(wx.grid.EVT_GRID_SELECT_CELL, self.on_select_food)

        self.Show(True)
        self.Layout()

    def OnSearch(self, event):
        keyword = self.m_textCtrl1.GetValue()
        nutrient_name = self.m_textCtrl2.GetValue().strip()
        nutrient_level = self.m_radioBox1.GetStringSelection().strip()  # Get selection level
        min_value_str = self.m_textCtrl3.GetValue().strip()  # Get min value as string
        max_value_str = self.m_textCtrl4.GetValue().strip()  # Get max value as string
        df = self.df

        # Search food
        if keyword:
            loc = search_data(df, keyword)
            df = df[loc]
            self.update_grid(df)

        # Filter nutrients using update
        if nutrient_name in df.columns:
            filter_df = filter_nutrients(df, nutrient_name,nutrient_level, min_value_str, max_value_str)
            self.update_grid(filter_df)

    def update_grid(self, df):
        if not isinstance(df, pd.DataFrame):
            wx.MessageBox("Data is not in the correct format.", "Error", wx.OK | wx.ICON_ERROR)
            return  # Exit the method if df is not a DataFrame
        if df.empty:  # If df is empty after filtering
            wx.MessageBox("No items found. Please try again.", "Information", wx.OK | wx.ICON_INFORMATION)
            self.m_grid1.ClearGrid()  # Clear the grid
        else:
            new_table = DataTable(df)
            self.m_grid1.ClearGrid()
            self.m_grid1.SetTable(new_table, takeOwnership=True)
            self.m_grid1.AutoSize()






    def on_select_food(self, event):
        df = self.table.data
        row = event.GetRow()
        selected_food_data = [self.m_grid1.GetCellValue(row, col) for col in range(self.m_grid1.GetNumberCols())]
        self.m_staticText15.SetLabel(selected_food_data[0].upper())

        macro_nutri_type, macro_nutri_value = prepare_macro_nutrient_data(df, selected_food_data)
        micro_nutri_type, micro_nutri_value = prepare_micro_nutrient_data(df, selected_food_data)

        nutri, (ax1, ax2) = plt.subplots(1, 2)
        ax1.barh(macro_nutri_type, macro_nutri_value) # using Horizontal bar plot
        ax1.set_title('Macro Nutrients Level', pad=20)
        ax1.text(0.5, 1.01, '*Fat includes Saturated Fat, Monounsaturated Fat, and Polyunsaturated Fat\n*Carbohydrate '
                            'includes Sugar', fontsize=5, ha='center', transform=ax1.transAxes)
        ax1.set_xlabel("Value (in gram)")

        colors = ['gold', 'yellowgreen', 'lightcoral', 'lightskyblue',
                  'tomato', 'mediumseagreen', 'slateblue', 'lightcoral', 'tomato']

        if sum(micro_nutri_value) == 0:
            ax2.pie(micro_nutri_value, labels=micro_nutri_type, colors=colors, autopct='%1.1f%%',
                    shadow=True)
            ax2.set_title("Contains No Micro Nutrients ")
        else:
            explode = (0.25,) + (0,) * (len(micro_nutri_value)-1) # only applied for the first two
            ax2.pie(micro_nutri_value, explode=explode, labels=micro_nutri_type, colors=colors, autopct='%1.1f%%',
                    shadow=True)
            ax2.set_title("Micro Nutrients Percentage")

        h, w = self.m_panel4.GetSize()
        nutri.set_size_inches(h / nutri.get_dpi(), w / nutri.get_dpi())
        canvas = FigureCanvasWxAgg(self.m_panel4, -1, nutri)
        canvas.SetSize(self.m_panel4.GetSize())
        self.Layout()


    def Calculate(self, event):
        # BMI calculator
        try:
            # Get height, weight, and age from text controls
            height = float(self.m_textCtrl111.GetValue()) / 100.0  # Convert cm to meters
            weight = float(self.m_textCtrl121.GetValue())
            age = int(self.m_textCtrl14.GetValue())

        except ValueError:
            self.bmi_result_label.SetLabel("Please enter valid numeric values for height, weight, and age.")
            self.calculate_BMI.Layout()
            return

        if height <= 0:
            self.bmi_result_label.SetLabel("Height must be greater than 0.")
            self.calculate_BMI.Layout()
            return

        if weight <= 0:
            self.bmi_result_label.SetLabel("Weight must be greater than 0.")
            self.calculate_BMI.Layout()
            return

        if age <= 0:
            self.bmi_result_label.SetLabel("Age must be a positive number.")
            self.calculate_BMI.Layout()
            return

        # Determine gender from checkbox
        if self.m_checkBox1.GetValue():
            gender = 'F'  # Female
        else:
            gender = 'M'  # Male

        try:
            # Call the calculate_bmi function to compute BMI and calorie intake
            bmi, calorie_intake = calculate_bmi(height, weight, age, gender)
            # Show results
            self.bmi_result_label.SetLabel(
                f"Your BMI = {bmi:.2f}\nBased on your height and weight, your recommended daily calorie intake is {calorie_intake:.2f} kcal."
            )
            self.calculate_BMI.Layout()

        except ValueError:
            self.bmi_result_label.SetLabel("Please enter valid numeric values in the body information form.")
            self.calculate_BMI.Layout()
            return
#------------------ For nutrition calculations and barchart
        # Nutrition calculations
        try:
            breakfast_amount = float(self.m_textCtrl8.GetValue()) if self.m_textCtrl8.GetValue() else 0
            lunch_amount = float(self.m_textCtrl12.GetValue()) if self.m_textCtrl12.GetValue() else 0
            dinner_amount = float(self.m_textCtrl11.GetValue()) if self.m_textCtrl11.GetValue() else 0

            breakfast_food = self.m_textCtrl7.GetValue()
            lunch_food = self.m_textCtrl9.GetValue()
            dinner_food = self.m_textCtrl10.GetValue()

            # Validate inputs for amounts and foods
            max_amount = 500
            if breakfast_amount > max_amount:
                breakfast_amount = max_amount
                wx.MessageBox(f"Breakfast amount is too large, clamping to {max_amount}g.", "Warning",
                            wx.OK | wx.ICON_WARNING)

            if lunch_amount > max_amount:
                lunch_amount = max_amount
                wx.MessageBox(f"Lunch amount is too large, clamping to {max_amount}g.", "Warning",
                                wx.OK | wx.ICON_WARNING)

            if dinner_amount > max_amount:
                dinner_amount = max_amount
                wx.MessageBox(f"Dinner amount is too large, clamping to {max_amount}g.", "Warning",
                                wx.OK | wx.ICON_WARNING)

            if not breakfast_food and not lunch_food and not dinner_food:
                wx.MessageBox("Please enter at least one valid meal with food and amount.", "Error",
                              wx.OK | wx.ICON_ERROR)
                return

            # Additional individual checks for the meals that were entered
            if breakfast_food and breakfast_amount <= 0:
                wx.MessageBox("Please enter a valid breakfast food and amount.", "Error", wx.OK | wx.ICON_ERROR)
                return

            if lunch_food and  lunch_amount <= 0:
                wx.MessageBox("Please enter a valid lunch food and amount.", "Error", wx.OK | wx.ICON_ERROR)
                return

            if dinner_food and dinner_amount <= 0:
                wx.MessageBox("Please enter a valid dinner food and amount.", "Error", wx.OK | wx.ICON_ERROR)
                return

            # Get nutrition data
            total_carbs, total_sugars, total_protein, total_fat, total_fiber, total_cal = 0, 0, 0, 0, 0, 0

            meals = [
                (breakfast_food, breakfast_amount),
                (lunch_food, lunch_amount),
                (dinner_food, dinner_amount)
            ]
            # Flag to check if at least one meal is provided
            meal_provided = False
            for meal_food, meal_amount in meals:
                if meal_food and meal_amount > 0:  # Only process if meal_food is provided and meal_amount is positive
                    meal_provided = True
                    food_data = self.df[self.df['food'].str.lower() == meal_food.lower()]

                    if food_data.empty:
                        wx.MessageBox(f"Food '{meal_food}' not found in the dataset.", "Error", wx.OK | wx.ICON_ERROR)
                        return

                    # Calculate nutritional values per 100g
                    carbs_per_100g = food_data['Carbohydrates'].values[0]
                    sugars_per_100g = food_data['Sugars'].values[0]
                    protein_per_100g = food_data['Protein'].values[0]
                    fat_per_100g = food_data['Fat'].values[0]
                    fiber_per_100g = food_data['Dietary Fiber'].values[0]
                    cal_per_100g = food_data['Caloric Value'].values[0]

                    # Calculate nutrients for the meal
                    carbs, sugars, fat, protein, fiber, cal = calculate_nutrition(carbs_per_100g, sugars_per_100g, fat_per_100g, protein_per_100g, fiber_per_100g,cal_per_100g, meal_amount)
                    # Accumulate totals
                    total_carbs += carbs
                    total_sugars += sugars
                    total_protein += protein
                    total_fat += fat
                    total_fiber += fiber
                    total_cal += cal

            # Check if at least one meal was provided
            if not meal_provided:
                wx.MessageBox("Please enter at least one valid meal with food and amount.", "Error",
                              wx.OK | wx.ICON_ERROR)
                return

            # Display total nutrition for the day
            wx.MessageBox(
                f"Total for the day:\nCarbohydrates: {total_carbs:.2f}g\nSugars: {total_sugars:.2f}g\nProtein: {total_protein:.2f}g\nFat: {total_fat:.2f}g\nFiber: {total_fiber:.2f}g",
                "Nutrition Summary", wx.OK | wx.ICON_INFORMATION
            )

            # Now draw the nutrition bar chart
            self.draw_nutrition_chart(total_carbs, total_sugars, total_protein, total_fat, total_fiber)
            self.draw_calorie_intake_chart(calorie_intake, total_cal)

        except ValueError:
            wx.MessageBox("Please enter a valid numeric value for amount.", "Error", wx.OK | wx.ICON_ERROR)
            return

    def draw_nutrition_chart(self, total_carbs, total_sugars, total_protein, total_fat, total_fiber):
        # Create a figure
        figure = Figure(figsize=(12, 10), dpi=100)
        axes = figure.add_subplot(111)

        # Nutrient data
        nutrients = ['Carbohydrates', 'Sugars', 'Protein', 'Fat', 'Fiber']
        values = [total_carbs, total_sugars, total_protein, total_fat, total_fiber]

        # Create bar chart
        axes.bar(nutrients, values, color=['lightcoral', 'lightblue', 'lightgreen', 'purple', 'grey'])

        # Set axis labels and title
        axes.set_xlabel("Nutrient", fontsize=12)
        axes.set_ylabel("Amount (g)", fontsize=12)
        axes.set_title("Nutritional Content", fontsize=14)

        # Clear the previous chart (if any) by resetting the panel
        for child in self.draw_nutritiousChart.GetChildren():
            child.Destroy()

        # Embed the figure into the wx.Panel
        canvas = FigureCanvas(self.draw_nutritiousChart, -1, figure)
        canvas.SetMinSize(self.draw_nutritiousChart.GetSize())
        self.draw_nutritiousChart.Layout()

    def draw_calorie_intake_chart(self, calorie_intake, total_cal):
        if calorie_intake <= 0 or total_cal <= 0:
            wx.MessageBox("Calorie intake or total calories must be greater than 0 to display the chart.", "Error",
                            wx.OK | wx.ICON_ERROR)
            return

        # Calculate the percentages
        consumed_percentage = (total_cal / calorie_intake) * 100
        remaining_percentage = 100 - consumed_percentage

        # Labels and values for the pie chart
        consumed_label = f'Consumed ({total_cal:.2f} kcal)'
        remaining_calories = calorie_intake - total_cal
        remaining_label = f'Remaining ({remaining_calories:.2f} kcal)'

        labels = [consumed_label, remaining_label]
        values = [consumed_percentage, remaining_percentage]

        # Create the figure for the pie chart
        figure = Figure(figsize=(13, 8), dpi=100)
        axes = figure.add_subplot(111)

        # Create the pie chart
        axes.pie(values, labels=labels, autopct='%1.1f%%', colors=['lightblue', 'lightgreen'], startangle=90)
        axes.axis('equal')  # Equal aspect ratio ensures that the pie is drawn as a circle.

        # Clear previous chart
        for child in self.drawCalorie_Intake.GetChildren():
            child.Destroy()

        # Embed the figure into the wx.Panel
        canvas = FigureCanvas(self.drawCalorie_Intake, -1, figure)
        canvas.SetMinSize(self.drawCalorie_Intake.GetSize())
        self.drawCalorie_Intake.Layout()


if __name__ == "__main__":
    app = wx.App()
    frame = CalcFrame()
    app.MainLoop()
