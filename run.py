import wx
import wx.grid
import pandas as pd
import re
import matplotlib

matplotlib.use('WXAgg')  # allows Matplotlib to render plots within wxPython.
# to embed a Matplotlib figure into a wxPanel in a wxPython application.

from matplotlib.backends.backend_wxagg import FigureCanvasWxAgg
import matplotlib.pyplot as plt

from all_functions import search_data, prepare_macro_nutrient_data, prepare_micro_nutrient_data
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
        df = self.table.data
        row = event.GetRow()
        selected_food_data = [self.m_grid1.GetCellValue(row, col) for col in range(self.m_grid1.GetNumberCols())]
        self.m_staticText15.SetLabel(selected_food_data[0])

        macro_nutri_type, macro_nutri_value = prepare_macro_nutrient_data(df, selected_food_data)
        micro_nutri_type, micro_nutri_value = prepare_micro_nutrient_data(df, selected_food_data)

        nutri, (ax1, ax2) = plt.subplots(1, 2)
        ax1.barh(macro_nutri_type, macro_nutri_value) # using Horizontal bar plot
        ax1.set_title('Macro Nutrients Level')
        ax1.set_ylabel("Nutrients")
        ax1.set_xlabel("Value (in gram)")

        explode = (0.1,) * len(micro_nutri_value)
        colors = ['gold', 'yellowgreen', 'lightcoral', 'lightskyblue',
                  'tomato', 'mediumseagreen', 'slateblue', 'lightcoral', 'tomato']
        ax2.pie(micro_nutri_value, explode=explode, labels=micro_nutri_type, colors=colors, autopct='%1.1f%%',
                shadow=True)
        ax2.set_title("Micro Nutrients Percentage")

        h, w = self.m_panel4.GetSize()
        nutri.set_size_inches(h / nutri.get_dpi(), w / nutri.get_dpi())
        canvas = FigureCanvasWxAgg(self.m_panel4, -1, nutri)
        canvas.SetSize(self.m_panel4.GetSize())
        self.Layout()


if __name__ == "__main__":
    app = wx.App()
    frame = CalcFrame()
    app.MainLoop()
