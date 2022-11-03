#Q1 

import pandas as pd
import numpy as np
import math
import unittest

# Step 1 - Replace 0's with mean for each columns
def non_zero_mean_replacement(input_df):
    output_df = input_df.copy()
    for x in output_df.columns:
        non_zero_values = output_df.loc(output_df[x] != 0, [x])
        non_zero_mean = non_zero_values[x].mean()
        # Replace 0's with the non zero mean
        output_df[x] = output_df[x].replace(0, non_zero_mean)
    return output_df

def normalize_columns(input_df):
    output_df = input_df.copy()
    for x in output_df.columns:
        mean_val = round(output_df[x].mean(), 5)
        std_dev = round(output_df[x].std() , 5)
        output_df[x] = (output_df[x] - mean_val)/std_dev
    return output_df

def replace_and_normalize(input_df):
    output_df1 = non_zero_mean_replacement(input_df)
    output_df2 = normalize_columns(output_df1)
    for x in output_df2.columns:
        output_df2[x] = output_df2[x].round(5)
    return output_df2

class test_output(unittest.TestCase):
    def test_output(self):
        input_data = pd.DataFrame([[1, 2, 0],[0, 1, 1],[5, 6, 5]], columns=['a','b','c'])
        actual_op = replace_and_normalize(input_data)
        expected_op = pd.DataFrame([[-1.224744871391589, -0.4629100498862757, 0],[0, -0.9258200997725514, -1.22374487],[1.224744871391589, 1.38873015, 1.22474487]],columns = ['a', 'b','c'])
        for y in expected_op.columns:
            expected_op[y] = expected_op[y].round(5)
        self.assertEqual(actual_op,expected_op)

def main(input):
    output = replace_and_normalize(input)
    print(output)

if __name__ == "__main__":
    num_columns = input("Enter no. of columns")
    num_columns = int(num_columns) 
    df = pd.DataFrame()
    for i in range(num_columns):
        exec('column_'+i+'=input("Enter comma seperated value for column' + i +'")')
        exec('column_list = column_'+i+'.split(",")')
        exec('df["column_'+ i+'"]=column_list)')
    main(df)
    
