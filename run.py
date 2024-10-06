import wx
import wx.grid
import pandas as pd
import matplotlib
matplotlib.use('WXAgg')  # Use the WXAgg backend for wxPython
from matplotlib.backends.backend_wxagg import FigureCanvasWxAgg as FigureCanvas
from matplotlib.figure import Figure

from all_functions import search_data
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

        # Read the CSV file into a pandas DataFrame
        self.df = pd.read_csv(r"./Food_Nutrition_Dataset.csv")


        # Set the table data in the wxGrid
        self.table = DataTable(self.df)
        self.m_grid1.SetTable(self.table, takeOwnership=True)

        # Resize grid columns to fit content
        self.m_grid1.AutoSize()


        self.Show(True)
        self.Layout()

    def OnSearch(self, event):
        keyword = self.m_textCtrl1.GetValue()
        nutrient_name = self.m_textCtrl2.GetValue().strip()

        df = self.table.data

          # Ensure search_data is updated with the correct column name
        if keyword:
            loc = search_data(df, keyword)
            df = df[loc]
        if nutrient_name in df.columns:
            try:
                min_value = float(self.m_textCtrl3.GetValue())
                max_value = float(self.m_textCtrl4.GetValue())
            except ValueError:
                wx.MessageBox("Please enter valid numeric values for the range.", "Input Error", wx.OK | wx.ICON_ERROR)
                return

            #filter based on nutrient
            nutrient = df[nutrient_name]
            loc = (nutrient>=min_value) & (nutrient<=max_value)
            df = df.loc[loc]

        if not df.empty:
            tabl = DataTable(df)
            self.m_grid1.ClearGrid()
            self.m_grid1.SetTable(tabl, takeOwnership=True)
            self.m_grid1.AutoSize()
        else:
            wx.MessageBox(f"No data found for '{nutrient_name}' within the given range.", "No Results",
                          wx.OK | wx.ICON_INFORMATION)

    def Calculate(self, event):
        # BMI calculator
        calorie_intake = 0
        try:
            height = float(self.m_textCtrl111.GetValue()) / 100.0  # convert cm to meters
            weight = float(self.m_textCtrl121.GetValue())
            age = int(self.m_textCtrl14.GetValue())

            # Determine gender from checkbox
            if self.m_checkBox1.GetValue():
                gender = 'F'  # Female
            else:
                gender = 'M'  # Male

            # Calculate BMI
            bmi = weight / (height * height)

            # Estimate daily calorie intake (simple calculation)
            if gender == 'M':
                calorie_intake = 10 * weight + 6.25 * (height * 100) - 5 * age + 5
            elif gender == 'F':
                calorie_intake = 10 * weight + 6.25 * (height * 100) - 5 * age - 161
            else:
                self.bmi_result_label.SetLabel("Invalid gender input!")
                self.calculate_BMI.Layout()
                return calorie_intake

                # Show results
            self.bmi_result_label.SetLabel(
                f"Your BMI = {bmi:.2f}\n Based on your height and weight, your recommended daily calorie intake is {calorie_intake:.2f} kcal.")
            self.calculate_BMI.Layout()

        except ValueError:
            self.bmi_result_label.SetLabel("Please enter valid numeric values in the body information form.")
            self.calculate_BMI.Layout()
            return

#------------------ For nutrition calculations and barchart

        # For nutrition calculations and bar chart
        total_carbs = total_sugers = total_protein = total_fat = total_fiber = total_cal = 0

        # Function to get nutrient data
        def get_nutrient_data(food, amount):
            max_amount = 500
            if amount > max_amount:
                amount = max_amount
                wx.MessageBox(f"Amount is too large, clamping to {max_amount}g.", "Warning", wx.OK | wx.ICON_WARNING)

            if not food or amount <= 0:
                return 0, 0, 0, 0, 0, 0

            food_data = self.df[self.df['food'].str.lower() == food.lower()]
            if food_data.empty:
                wx.MessageBox(f"Food '{food}' not found in the dataset.", "Error", wx.OK | wx.ICON_ERROR)
                return 0, 0, 0, 0, 0, 0

            carbs_per_100g = food_data['Carbohydrates'].values[0]
            sugers_per_100g = food_data['Sugars'].values[0]
            protein_per_100g = food_data['Protein'].values[0]
            fat_per_100g = (
                    food_data['Fat'].values[0] +
                    food_data['Saturated Fats'].values[0] +
                    food_data['Monounsaturated Fats'].values[0] +
                    food_data['Polyunsaturated Fats'].values[0]
            )
            fiber_per_100g = food_data['Dietary Fiber'].values[0]
            cal_per_100g = food_data['Caloric Value'].values[0]

            return (
                (carbs_per_100g / 100) * amount,
                (sugers_per_100g / 100) * amount,
                (protein_per_100g / 100) * amount,
                (fat_per_100g / 100) * amount,
                (fiber_per_100g / 100) * amount,
                (cal_per_100g / 100) * amount
            )

        # Breakfast
        try:
            breakfast_amount = float(self.m_textCtrl8.GetValue()) if self.m_textCtrl8.GetValue() else 0
            total_carbs_b, total_sugers_b, total_protein_b, total_fat_b, total_fiber_b, total_cal_b = get_nutrient_data(
                self.m_textCtrl7.GetValue(), breakfast_amount)
            total_carbs += total_carbs_b
            total_sugers += total_sugers_b
            total_protein += total_protein_b
            total_fat += total_fat_b
            total_fiber += total_fiber_b
            total_cal += total_cal_b
        except ValueError:
            wx.MessageBox("Please enter a valid numeric value for breakfast amount.", "Error", wx.OK | wx.ICON_ERROR)
            return

        # Lunch
        try:
            lunch_amount = float(self.m_textCtrl12.GetValue()) if self.m_textCtrl12.GetValue() else 0
            total_carbs_l, total_sugers_l, total_protein_l, total_fat_l, total_fiber_l, total_cal_l = get_nutrient_data(
                self.m_textCtrl9.GetValue(), lunch_amount)
            total_carbs += total_carbs_l
            total_sugers += total_sugers_l
            total_protein += total_protein_l
            total_fat += total_fat_l
            total_fiber += total_fiber_l
            total_cal += total_cal_l
        except ValueError:
            wx.MessageBox("Please enter a valid numeric value for lunch amount.", "Error", wx.OK | wx.ICON_ERROR)
            return

        # Dinner
        try:
            dinner_amount = float(self.m_textCtrl11.GetValue()) if self.m_textCtrl11.GetValue() else 0
            total_carbs_d, total_sugers_d, total_protein_d, total_fat_d, total_fiber_d, total_cal_d = get_nutrient_data(
                self.m_textCtrl10.GetValue(), dinner_amount)
            total_carbs += total_carbs_d
            total_sugers += total_sugers_d
            total_protein += total_protein_d
            total_fat += total_fat_d
            total_fiber += total_fiber_d
            total_cal += total_cal_d
        except ValueError:
            wx.MessageBox("Please enter a valid numeric value for dinner amount.", "Error", wx.OK | wx.ICON_ERROR)
            return

        # Check if any nutrient data was entered
        if total_carbs == 0 and total_sugers == 0 and total_protein == 0 and total_fat == 0 and total_fiber == 0 and total_cal == 0:
            wx.MessageBox("Please enter valid food amounts.", "Error", wx.OK | wx.ICON_ERROR)
            return

        # Display total nutrition for the day
        wx.MessageBox(
            f"Total for the day:\nCarbohydrates: {total_carbs}g\nSugars: {total_sugers}g\nProtein: {total_protein}g\nFat: {total_fat}g\nFiber: {total_fiber}g",
            "Nutrition Summary", wx.OK | wx.ICON_INFORMATION)

        # Now drawing the nutrition bar chart inside the panel using matplotlib
        self.draw_nutrition_chart(total_carbs, total_sugers, total_protein, total_fat, total_fiber)
        self.draw_calorie_intake_chart(calorie_intake, total_cal)

    def draw_nutrition_chart(self, total_carbs, total_sugers, total_protein, total_fat, total_fiber):
        # Create a figure
        figure = Figure(figsize=(12, 10), dpi=100)
        axes = figure.add_subplot(111)

        # Nutrient data
        nutrients = ['Carbohydrates', 'Sugars', 'Protein', 'Fat', 'Fiber']
        values = [total_carbs, total_sugers, total_protein, total_fat, total_fiber]

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
        consumed_label = f'Consumed ({total_cal} kcal)'
        remaining_calories = calorie_intake - total_cal
        remaining_label = f'Remaining ({remaining_calories} kcal)'

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
