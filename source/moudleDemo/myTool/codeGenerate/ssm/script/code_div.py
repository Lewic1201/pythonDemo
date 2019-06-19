#!/usr/bin/env python
# -- coding: utf-8 --
"""
@author: Lewic
@file: code_div
@time: 2019/6/18 18:46
@desc:
"""
import datetime
from script.dataStructure import TableFields

txt00 = 'com.sc.hoperun'
txt01 = '规则模板'
txt02 = '@Date 2019/6/14 15:38'
txt03 = 'RuleDetail'
txt04 = 'ruleDetail'
txt05 = 'ruleId'
txt06 = '    // 规则名称\n' \
        '    private String ruleName;\n' \
        '    // 描述\n' \
        '    private String description;'
txt07 = '        this.ruleName = ruleName;\n' \
        '        this.description = description;'
txt08 = '        this.ruleName = ruleName;\n' \
        '        this.description = description;'
txt09 = 'String ruleName, String description'
txt10 = 'String ruleId, String ruleName, String description'
txt11 = '@ApiParam(value = "规则名称") @RequestParam(value = "ruleName") String ruleName,\n' \
        '            @ApiParam(value = "描述") @RequestParam(value = "description") String description'
txt12 = 'ruleName, description'
txt13 = 'ruleId, ruleName, description'
txt14 = 'rule_detail'
txt15 = 'rule_name,\n        description'
txt16 = '#{ruleName,jdbcType=VARCHAR},\n                #{description,jdbcType=VARCHAR}'
txt17 = 'rule_name      = #{ruleName,jdbcType=VARCHAR},\n            description    = #{description,jdbcType=VARCHAR}'
txt18 = '        <result column="rule_name" jdbcType="VARCHAR" property="ruleName"/>\n' \
        '        <result column="description" jdbcType="VARCHAR" property="description"/>'


def get_now_time(formats='%Y-%m-%d %H:%M:%S'):
    now_time = datetime.datetime.now().strftime(formats)
    return now_time


def create_replace_map(table_fields):
    if not isinstance(table_fields, TableFields):
        raise Exception('type error')

    # 添加[:]浅拷贝
    new00 = table_fields.package_pre[:]
    new01 = table_fields.table_name_ch[:]
    new02 = '@Date %s' % get_now_time('%Y/%m/%d %H:%M')[:]
    new03 = table_fields.class_name[:]
    new04 = table_fields.entity_name[:]
    new05 = table_fields.column_id[:]
    new14 = table_fields.table_name[:]

    columns = table_fields.get_columns()
    new06 = ''
    new07 = ''
    new08 = ''
    new09 = ''
    new10 = ''
    new11 = ''
    new12 = ''
    new13 = ''
    new15 = ''
    new16 = ''
    new17 = ''
    new18 = ''
    is_first = True

    for col in columns:
        new06 += '    ' + '// ' + col['column_name_ch'] + '\n' + '    private ' + col['param_type'] + ' ' + col[
            'param_name'] + ';\n'

        new09 += col['param_type'] + ' ' + col['param_name'] + ', '
        new11 += '            @ApiParam(value = "%s") @RequestParam(value = "%s") %s %s,\n' % (
            col['column_name_ch'], col['param_name'], col['param_type'], col['param_name'])
        new12 += col['param_name'] + ', '
        new16 += '                #{%s,jdbcType=%s},\n' % (col['param_name'], col['jdbc_type'])
        new17 += '            %s = #{%s,jdbcType=%s},\n' % (col['column_name'], col['param_name'],
                                                            col['jdbc_type'])
        new18 += '        <result column="%s" jdbcType="%s" property="%s"/>\n' % (
            col['column_name'], col['jdbc_type'], col['param_name'])

        new08 += '        this.' + col['param_name'] + ' = ' + col['param_name'] + ';\n'
        new15 += '        ' + col['column_name'] + ',\n'

    new08 = new08[:]
    new09 = new09[:-2]
    new11 = new11[12:-2]
    new12 = new12[:-2]
    new15 = new15[8:-2]
    new16 = new16[16:-2]
    new17 = new17[12:-2]

    res = [

        [txt06, new06],
        [txt08, new08],
        [txt11, new11],
        [txt15, new15],
        [txt07, new07],
        [txt09, new09],
        [txt12, new12],
        [txt16, new16],
        [txt17, new17],
        [txt00, new00],
        [txt01, new01],
        [txt03, new03],
        [txt04, new04],
        [txt05, new05],
        [txt14, new14],
        [txt02, new02],
        [txt18, new18],
    ]

    return res


if __name__ == '__main__':
    tf = TableFields('client_link', '客户资料', 'com.hoperun', 'clientId')
    tf.add_column('user_name', '用户名')
    tf.add_column('password', '密码')
    tf.add_column('create_time', '创建时间', 'datetime')
    tf.add_column('level', '权限级别', 'int')

    maps = create_replace_map(tf)
    print(maps)
