
import pandas as pd

df = pd.DataFrame({
    "emp_name" :["vj","bj", "cj", "vij","bij", "cij"] ,
    "emp_no" : [1, 2, 3, 4, 5,6],
    "age" : [32,34,45,56,33,36]}
                  )
df1 = pd.DataFrame({
    "emp_no": [1, 2, 3, 4, 5, 6],
    "salary": [20, 39, 34, 23 ,65, 48]
})

mer = pd.merge(df, df1, on="emp_no" )
right_join = pd.merge(df, df1, on="emp_no", how="right")
left_join  = pd.merge(df, df1, on="emp_no", how="left")
inner_join = pd.merge(df, df1, on="emp_no", how="inner")
outer_join = pd.merge(df, df1, on="emp_no", how="outer")

print(mer)
result = pd.concat([df, df1], axis=0 ) # Horizontal merge (column-wise)
df_final = pd.concat([df, df1], ignore_index=True) # Vertical merge (row-wise)

print(f"Median value of the salary list = {mer['salary'].median()}")
print(f"Sum of all values = {mer['salary'].sum()}")
print(f"Mean value = {mer['salary'].mean()}")
print(f"Number of non-null values = {mer['salary'].count()}")
print(f"Total number of rows = {mer['salary'].size}")

#Secound Heightest number
sorv= df1.sort_values("salary", ascending=False).iloc[2]
print(sorv)

mer['salary'].size      # total elements
mer['salary'].shape[0]  # number of rows

# execute n numer of 

df.agg({'salary': 'mean', 'age': 'max'})

# Remove duplicate

df.duplicated(keep=False)
df.duplicated(keep='last')
df.duplicated(keep='frist')
