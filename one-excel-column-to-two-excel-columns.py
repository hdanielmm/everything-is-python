import pandas as pd

path = "resume-excel.xlsx"

# sheet_name = input("Sheet name: ")

xl = pd.ExcelFile(path)
print(xl.sheet_names)

for sheet_name in xl.sheet_names:
    df = pd.read_excel(path, sheet_name=sheet_name, header=None, names=["Variable"])

    name = df["Variable"].str.split("=", n=1, expand=True)
    name.columns = ["Variable", "Valor"]

    df = pd.DataFrame(name)
    df["Valor"] = df["Valor"].str.strip()
    df["Variable"] = df["Variable"].str.strip()


    print(df)

    # writer = pd.ExcelWriter("resume-excel-procesado2.xlsx")
    # df.to_excel(writer, sheet_name=sheet_name, index=False)

    with pd.ExcelWriter("resume-excel-procesado2.xlsx", mode="a") as writer:
        df.to_excel(writer, sheet_name=sheet_name, index=False)    


    # writer.close()


