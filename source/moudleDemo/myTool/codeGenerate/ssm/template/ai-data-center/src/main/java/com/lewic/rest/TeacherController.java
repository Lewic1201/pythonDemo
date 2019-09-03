package com.lewic.rest;

import com.lewic.common.Message;
import com.lewic.common.Util;
import com.lewic.entity.Teacher;
import com.lewic.service.TeacherService;
import io.swagger.annotations.ApiOperation;
import io.swagger.annotations.ApiParam;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.validation.BindingResult;
import org.springframework.web.bind.annotation.*;

import javax.validation.Valid;


/**
 * @author lewic
 * @since 2019/6/13 15:22
 **/

@RestController
@RequestMapping("/api/v1.0")
public class TeacherController {
    @Autowired
    TeacherService teacherService;


    @ApiOperation("获取通知列表")
    @RequestMapping(value = "/teacher", method = RequestMethod.GET)
    public Message listTeacher(
            @ApiParam(value = "姓名") @RequestParam(required = false, value = "name") String name,
            @ApiParam(value = "第几页") @RequestParam(required = false, value = "pageNum", defaultValue = "1") Integer pageNum,
            @ApiParam(value = "每页条数") @RequestParam(required = false, value = "pageSize", defaultValue = "10") Integer pageSize
    ) {
        return teacherService.listTeacher(name, pageNum, pageSize);
    }

    @ApiOperation("根据id获取通知")
    @RequestMapping(value = "/teacher/{id}", method = RequestMethod.GET)
    public Message getTeacher(@PathVariable(value = "id") String tid) {
        return teacherService.getTeacher(tid);
    }

    @ApiOperation("新增通知")
    @RequestMapping(value = "/teacher", method = RequestMethod.POST)
    public Message insertTeacher(
            @ApiParam(value = "通知") @RequestBody @Valid Teacher teacher,
            BindingResult bindingResult
    ) {
        if (bindingResult.hasErrors()) {
            return Util.checkParam(bindingResult);
        }
        return teacherService.insertTeacher(teacher);
    }

    @ApiOperation("更新通知")
    @RequestMapping(value = "/teacher/{id}", method = RequestMethod.PUT)
    public Message updateTeacher(
            @PathVariable(value = "id") Integer tid,
            @ApiParam(value = "通知") @RequestBody @Valid Teacher teacher,
            BindingResult bindingResult
    ) {
        teacher.setTid(tid);
        if (bindingResult.hasErrors()) {
            return Util.checkParam(bindingResult);
        }
        return teacherService.updateTeacher(teacher);
    }

    @ApiOperation("删除通知")
    @RequestMapping(value = "/teacher/{id}", method = RequestMethod.DELETE)
    public Message deleteTeacher(@PathVariable(value = "id") String tid) {
        return teacherService.deleteTeacher(tid);
    }

}
