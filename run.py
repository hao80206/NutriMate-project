import wx
import wx.grid
import pandas as pd
import re
import matplotlib

matplotlib.use('WXAgg')  # allows Matplotlib to render plots within wxPython.
# to embed a Matplotlib figure into a wxPanel in a wxPython application.

from matplotlib.backends.backend_wxagg import FigureCanvasWxAgg
import matplotlib.pyplot as plt

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


if __name__ == "__main__":
    app = wx.App()
    frame = CalcFrame()
    app.MainLoop()
