package com.lewic.entity;

import io.swagger.annotations.ApiModel;
import io.swagger.annotations.ApiModelProperty;
import lombok.Data;


/**
 * @author lewic
 * @since 2019/6/13 14:32
 **/

@Data
@ApiModel(value = "学生")
public class Student {

    @ApiModelProperty(value = "编号", name = "sid")
    private Integer sid;

    @ApiModelProperty(value = "姓名", name = "name", example = "张三")
    private String name;

    @ApiModelProperty(value = "手机号", name = "mobile", example = "18192871234")
    private String mobile;

}
