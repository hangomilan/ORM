from sql_helper import Functions


TABLENAME = "customers"
FILENAME = "customers.csv"


class Customer:
    def caller(self):
        datas = Functions.data_reader(FILENAME)
        for j in range(1, len(datas)):
            sql = "INSERT INTO `orm`.`" + TABLENAME + "` VALUES("
            for i in range(len(datas[j].split(";"))):
                if i != len(datas[j].split(";"))-1:
                    sql += "'" + datas[j].split(";")[i] + "',"
                else:
                    sql += "'" + datas[j].split(";")[i] + "'"
            sql += ");"
            sql_executer(sql)
            print(sql)


test = Customer()
test.caller()