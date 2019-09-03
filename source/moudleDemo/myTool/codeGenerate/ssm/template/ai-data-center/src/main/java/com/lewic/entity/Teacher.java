package com.lewic.entity;

import io.swagger.annotations.ApiModel;
import io.swagger.annotations.ApiModelProperty;
import lombok.Data;

import java.util.List;


/**
 * @author lewic
 * @since 2019/6/13 14:32
 **/

@Data
@ApiModel(value = "老师")
public class Teacher {

    @ApiModelProperty(value = "编号", name = "tid")
    private Integer tid;

    @ApiModelProperty(value = "姓名", name = "name", example = "王师")
    private String name;

    @ApiModelProperty(value = "学生列表", name = "students")
    private List<Student> students;

}
