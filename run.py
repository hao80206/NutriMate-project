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

          # Ensure search_data is updated with the correct column name
        if keyword:
            loc = search_data(df, keyword)
            df = df[loc]
        if nutrient_name in df.columns:
            min_value = float(self.m_textCtrl3.GetValue())
            max_value = float(self.m_textCtrl4.GetValue())
            # filter based on nutrient
            nutrient = df[nutrient_name]
            range_filter = (nutrient >= min_value) & (nutrient <= max_value)
            df = df.loc[range_filter]

        #by level
        if nutrient_name in df.columns:
            nutrient_max = df[nutrient_name].max()
            low_threshold = nutrient_max * 0.33
            mid_threshold = nutrient_max * 0.66

            if nutrient_level == 'Low':
                loc = df[nutrient_name] < low_threshold
            elif nutrient_level == 'Mid':
                loc = (df[nutrient_name] >= low_threshold) & (df[nutrient_name] <= mid_threshold)
            elif nutrient_level == 'High':
                loc = df[nutrient_name] > mid_threshold
            df = df.loc[loc]
        if not df.empty:
            tabl = DataTable(df)
            self.m_grid1.ClearGrid()
            self.m_grid1.SetTable(tabl, takeOwnership=True)
            self.m_grid1.AutoSize()

if __name__ == "__main__":
    app = wx.App()
    frame = CalcFrame()
    app.MainLoop()
