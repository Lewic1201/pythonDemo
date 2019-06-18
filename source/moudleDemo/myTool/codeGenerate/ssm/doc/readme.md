- 所需参数

表名 table_name
表描述 table_name_ch
列名 column_name
列描述 column_name_ch

实体名 entity_name(默认表名的驼峰式)
变量名 param_name()

列类型 column(默认varchar)

需要生成sql建表语句

需要一个替换目标目录下将所有文件的某个字符串替换为新字符串的接口
需要一个统一替换文件名的接口
临时建一个备份文件,然后将备份文件重命名
待所有的表的增删改查建好后,设置标志是否删除源文件


复制模板文件到结果文件目录,然后根据文件名直接实行重命名,


对dao层文件仅需替换 table_name id