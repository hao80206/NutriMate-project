import wx
import wx.grid
import pandas as pd
import re

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
        self.df = pd.read_csv(r".\Food_Nutrition_Dataset.csv")


        # Set the table data in the wxGrid
        self.table = DataTable(self.df)
        self.m_grid1.SetTable(self.table, takeOwnership=True)

        # Resize grid columns to fit content
        self.m_grid1.AutoSize()
        self.min_val_ctrl = wx.TextCtrl(self, value="0")
        self.max_val_ctrl = wx.TextCtrl(self, value="1000")

        # Add a button to trigger the range filter
        self.filter_btn = wx.Button(self, label="Filter by Calories")
        self.filter_btn.Bind(wx.EVT_BUTTON, self.OnRangeFilter)

        self.Show(True)
        self.Layout()

    def OnSearch(self, event):

        keyword = self.m_textCtrl1.GetValue()
        nutrient = self.m_textCtrl2.GetValue()
        min_value = float(self.m_textCtrl3.GetValue())
        max_value = float(self.m_textCtrl4.GetValue())

        df = self.table.data
        loc = search_data(df, keyword)  # Ensure search_data is updated with the correct column name
        look = search_data(df, nutrient)
        search_result = df[loc, look]
        tabl = DataTable(search_result)



        # Clear and update the second grid with the search results
        self.m_grid1.ClearGrid()
        self.m_grid1.SetTable(tabl, takeOwnership=True)
        self.m_grid1.AutoSize()




if __name__ == "__main__":
    app = wx.App()
    frame = CalcFrame()
    app.MainLoop()
