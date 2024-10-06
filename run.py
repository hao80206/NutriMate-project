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

        self.Show(True)
        self.Layout()

    def OnSearch(self, event):
        keyword = self.m_textCtrl1.GetValue()
        nutrient_name = self.m_textCtrl2.GetValue().strip()
        nutrient_level = self.m_radioBox1.GetStringSelection().strip()

        df = self.table.data

        # Search food
        if keyword:
            loc = search_data(df, keyword)
            df = df[loc]

        # Check if nutrient name is provided
        # Check if both min and max values are provided
            min_value_str = self.m_textCtrl3.GetValue().strip()  # Get min value as string
            max_value_str = self.m_textCtrl4.GetValue().strip()  # Get max value as string

            # If min or max are not provided, filter by level
            else:
                level_filter = None
                if nutrient_level:  # Check if nutrient level is selected




                    # print(f"nutrient_max: {nutrient_max}, low_threshold: {low_threshold}, mid_threshold: {mid_threshold}")



                    df = df.loc[level_filter]
                    # print(f"level_filter ({nutrient_level}): {level_filter.sum()} items found")

        if df.empty:  # If df is empty after filtering
            self.m_grid1.ClearGrid()  # Clear the grid again to ensure it's empty
            print("No items found. The grid has been cleared.")
        else:
            tabl = DataTable(df)
            self.m_grid1.ClearGrid()
            self.m_grid1.SetT able(tabl, takeOwnership=True)
            self.m_grid1.AutoSize()


if __name__ == "__main__":
    app = wx.App()
    frame = CalcFrame()
    app.MainLoop()
