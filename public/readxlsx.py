#coding=utf-8
import xlrd
import os

class GetDate(object):
    def __init__(self,dr):
        self.driver = dr
        self.cur_dir = os.path.split(os.path.dirname(__file__))[0]

    def get_date(self,path_dir,sheet_name):
        try:
            date_list = []
            get_file = xlrd.open_workbook(self.cur_dir + path_dir)
            get_sheet = get_file.sheet_by_name(sheet_name)
            get_rows = get_sheet.nrows
            print(get_rows)
            for i in range(get_rows):
                if i > 0:
                   date_list.append(get_sheet.row_values(i))
            return date_list
        except Exception as e:
            return e

    def read_doc(self,path_dir):
        try:
            r = open(self.cur_dir+path_dir,"r")
            value = r.read()
            r.close()
            return  value
        except Exception as e :
            return e

    def save_doc(self,path_dir,value):
        try:
            w = open(self.cur_dir+path_dir,"w")
            w.write(value)
            w.close()
        except Exception as e :
            return  e

# a = GetDate()
# b = a.get_date("\\databases\\Purchase_Management\\purchase_supplier.xlsx","Sheet1")
# p = b[random.randrange(0,len(b))]
# m = p[0]
# print(m)
































# if __name__=="__main__":
#     #excel文件全路径
#     excelpath = r'C:\Users\Administrator\Desktop\【高铁】2019年团体火车票订票站点.xlsx'
#     #用于读取excel文件
#     tableopen = xlrd.open_workbook(excelpath)
#     #获取excel工作簿数
#     count = len(tableopen.sheets())
#     print(u"工作簿数为%s"%count)
#     #获取表数据的行、列数
#     table = tableopen.sheet_by_name('01-节前去程')
#     h = table.nrows
#     l = table.ncols
#     print(u"表数据的行数为%s,列数为%s"%(h,l))
#     # 循环读取数据
#     for i in range(0,h):
#         rowValues = table.row_values(i) #按行读取数据
#         # 输出读取的数据
#         for data in rowValues:
#             print(data,'   ',)
#         print('')
