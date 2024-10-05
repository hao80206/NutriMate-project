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
                return

                # Show results
            self.bmi_result_label.SetLabel(
                f"Result: BMI = {bmi:.2f}, Daily Calorie Intake = {calorie_intake:.2f} kcal")
            self.calculate_BMI.Layout()

        except ValueError:
            self.bmi_result_label.SetLabel("Please enter valid numeric values.")
            self.calculate_BMI.Layout()
            return

        # For nutrition calculations and barchart

        total_carbs = total_sugers = total_protein = 0

        # Breakfast
        breakfast_food = self.m_textCtrl7.GetValue().lower()
        breakfast_amount = float(self.m_textCtrl8.GetValue()) if self.m_textCtrl8.GetValue() else 0

        if breakfast_amount > 0:
            food_data = self.df[self.df['food'].str.lower() == breakfast_food]
            if not food_data.empty:
                carbs_per_100g = food_data['Carbohydrates'].values[0]
                sugers_per_100g = food_data['Sugars'].values[0]
                protein_per_100g = food_data['Protein'].values[0]

                total_carbs += (carbs_per_100g / 100) * breakfast_amount
                total_sugers += (sugers_per_100g / 100) * breakfast_amount
                total_protein += (protein_per_100g / 100) * breakfast_amount

        # Lunch
        lunch_food = self.m_textCtrl9.GetValue().lower()
        lunch_amount = float(self.m_textCtrl12.GetValue()) if self.m_textCtrl12.GetValue() else 0

        if lunch_amount > 0:
            food_data = self.df[self.df['food'].str.lower() == lunch_food]
            if not food_data.empty:
                carbs_per_100g = food_data['Carbohydrates'].values[0]
                sugers_per_100g = food_data['Sugars'].values[0]
                protein_per_100g = food_data['Protein'].values[0]

                total_carbs += (carbs_per_100g / 100) * lunch_amount
                total_sugers += (sugers_per_100g / 100) * lunch_amount
                total_protein += (protein_per_100g / 100) * lunch_amount

        # Dinner
        dinner_food = self.m_textCtrl10.GetValue().lower()
        dinner_amount = float(self.m_textCtrl11.GetValue()) if self.m_textCtrl11.GetValue() else 0

        if dinner_amount > 0:
            food_data = self.df[self.df['food'].str.lower() == dinner_food]
            if not food_data.empty:
                carbs_per_100g = food_data['Carbohydrates'].values[0]
                sugers_per_100g = food_data['Sugars'].values[0]
                protein_per_100g = food_data['Protein'].values[0]

                total_carbs += (carbs_per_100g / 100) * dinner_amount
                total_sugers += (sugers_per_100g / 100) * dinner_amount
                total_protein += (protein_per_100g / 100) * dinner_amount

        # Check if any nutrient data was entered
        if total_carbs == 0 and total_sugers == 0 and total_protein == 0:
            wx.MessageBox("Please enter valid food amounts.", "Error", wx.OK | wx.ICON_ERROR)
            return

        # Display total nutrition for the day
        wx.MessageBox(
            f"Total for the day:\nCarbohydrates: {total_carbs}g\nSugars: {total_sugers}g\nProtein: {total_protein}g",
            "Nutrition Summary", wx.OK | wx.ICON_INFORMATION)

        # Now drawing the nutrition bar chart inside the panel using matplotlib
        self.draw_nutrition_chart(total_carbs, total_sugers, total_protein)

    def draw_nutrition_chart(self, total_carbs, total_sugers, total_protein):
        # Create a figure
        figure = Figure(figsize=(5, 4), dpi=100)
        axes = figure.add_subplot(111)

        # Nutrient data
        nutrients = ['Carbohydrates', 'Sugars', 'Protein']
        values = [total_carbs, total_sugers, total_protein]

        # Create bar chart
        axes.bar(nutrients, values, color=['lightcoral', 'lightblue', 'lightgreen'])

        # Clear the previous chart (if any) by resetting the panel
        for child in self.draw_nutritiousChart.GetChildren():
            child.Destroy()

        # Embed the figure into the wx.Panel
        canvas = FigureCanvas(self.draw_nutritiousChart, -1, figure)
        canvas.SetMinSize(self.draw_nutritiousChart.GetSize())
        self.draw_nutritiousChart.Layout()

if __name__ == "__main__":
    app = wx.App()
    frame = CalcFrame()
    app.MainLoop()
