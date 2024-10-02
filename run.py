import wx
import wx.grid
import pandas as pd
import re
import matplotlib

matplotlib.use('WXAgg')  # allows Matplotlib to render plots within wxPython.
# to embed a Matplotlib figure into a wxPanel in a wxPython application.

from matplotlib.backends.backend_wxagg import FigureCanvasWxAgg
import matplotlib.pyplot as plt

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

        # Set the size of the frame (width, height)
        self.SetSize(1000, 800)
        self.Centre()

        # Read the CSV file into a pandas DataFrame
        self.df = pd.read_csv(r".\Food_Nutrition_Dataset.csv")

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

            # filter based on nutrient
            nutrient = df[nutrient_name]
            loc = (nutrient >= min_value) & (nutrient <= max_value)
            df = df.loc[loc]

        if not df.empty:
            tabl = DataTable(df)
            self.m_grid1.ClearGrid()
            self.m_grid1.SetTable(tabl, takeOwnership=True)
            self.m_grid1.AutoSize()
        else:
            wx.MessageBox(f"No data found for '{nutrient_name}' within the given range.", "No Results",
                          wx.OK | wx.ICON_INFORMATION)

    def on_select_food(self, event):
        """Handles the selection of a food product from the grid."""
        row = event.GetRow()  # Get the selected row index
        selected_food_data = []

        # Get the data for the selected row (all columns)
        for col in range(self.m_grid1.GetNumberCols()):
            selected_food_data.append(self.m_grid1.GetCellValue(row, col))

        self.m_staticText15.SetLabel(selected_food_data[0])  # Display food name

        nutri = self.plot_data_line(selected_food_data)
        h, w = self.m_panel4.GetSize()
        # Resize the MatpotLib figure to fot within the m_panel4 dimensions
        nutri.set_size_inches(h / nutri.get_dpi(), w / nutri.get_dpi())

        # Create a FigureCanvasWxAgg object, which embeds the MatpotLib figure within the m_panel4 panel.
        canvas = FigureCanvasWxAgg(self.m_panel4, -1, nutri)

        # Sets the size of the canvas to match the size of the panel.
        canvas.SetSize(self.m_panel4.GetSize())

        # Adjust the layout again to ensure all components are correctly positioned after adding the canvas.
        self.Layout()

    def plot_data_line(self, selected_food_data):

        # macronutrients
        # X values:
        macro_nutri_type = ["Fat", "Protein", "Carbo", "Sugars", "Fiber"]
        # Y values:
        macro_nutri_value = [float(selected_food_data[2]), float(selected_food_data[8]), float(selected_food_data[6]),
                             float(selected_food_data[7]), float(selected_food_data[9])]


        # TODO: update Iron from g into mg!
        # TODO: update Iron from g into mg!
        # TODO: update Iron from g into mg!

        # Define the specific micronutrients and their corresponding values
        micronutrient_data = {
            "Cholesterol": float(selected_food_data[10]),
            "Sodium": float(selected_food_data[11]),
            "Vitamin A": float(selected_food_data[13]),
            "Vitamin C": float(selected_food_data[21]),
            "Calcium": float(selected_food_data[25]),
            "Iron": float(selected_food_data[27]),
            "Zinc": float(selected_food_data[33])
        }

        # Calculate others_value only for specified micronutrients below 1
        others_value = sum(value for nutrient, value in micronutrient_data.items() if value <= 1)

        # Filter out micronutrients that are below 1% and prepare lists for plotting
        micro_nutri_value = [value for value in micronutrient_data.values() if value > 1]
        micro_nutri_type = [nutrient for nutrient, value in micronutrient_data.items() if value > 1]

        # Add 'Others' to the lists if there are values to sum
        if others_value > 0:
            micro_nutri_type.append("Others")
            micro_nutri_value.append(others_value)

        nutri, (ax1, ax2) = plt.subplots(1, 2)

        ax1.bar(macro_nutri_type, macro_nutri_value)
        ax1.set_title(u'Macro Nutrition Level')
        ax1.set_xlabel("Nutrition")
        ax1.set_ylabel("Value (in gram)")

        explode = (0.1,) * len(micro_nutri_value)
        colors = ['gold', 'yellowgreen', 'lightcoral', 'lightskyblue', 'tomato', 'mediumseagreen', 'slateblue']

        ax2.pie(micro_nutri_value, explode=explode, labels=micro_nutri_type, colors=colors, autopct='%1.1f%%', shadow=True)
        ax2.set_title("Micro Nutrition Percentage")

        return nutri


if __name__ == "__main__":
    app = wx.App()
    frame = CalcFrame()
    app.MainLoop()
