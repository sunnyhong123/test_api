#coding=utf-8
import csv
import os
import xlrd

# path = "F:\\test_vt_brand\\data\\"
# path_current = os.getcwd().split("public")[0]
path_current = os.path.dirname(os.path.dirname(__file__))
# print(path_current)
def reader_excel(file):
    wb = xlrd.open_workbook(filename=file)
    ws = wb.sheet_by_name('Sheet1')
    dataset = []
    for r in range(ws.nrows):
        col = []
        for c in range(ws.ncols):
            col.append(ws.cell(r, c).value)
        dataset.append(col)
    print(dataset)

def reader_csv(file):
    value_list =[]
    with open(path_current+file,"r") as f:
        value = csv.DictReader(f)
        for i in value:
            value_list.append(dict(i))

    return  value_list

def reader_text(file_path):
    try:
        r = open(path_current + file_path,"r")
        value =  r.read()
        r.close()
        return  value

    except Exception as e:
        return e


#读取文件,替换保存
def read_save_txt(file_path,email):
    try:
        r = open(path_current+file_path,"r")
        text = r.read()
        r.close()
        value = text.replace(text,email)
        s = open(path_current+file_path,"w")
        s.write(value)
        s.close()
    except Exception as e:
        return e




if __name__ == "__main__":
    # print(reader_csv(r"\data\register_testcase - 副本.csv"))
    # print(read_save_txt(r"\data\login_email.txt","9851355123@qq.com"))
    print(read_save_txt(r"\data\edit_id.txt",str(39)))

