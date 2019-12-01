package com.lewic.rest;

import com.lewic.common.Message;
import com.lewic.common.Util;
import com.lewic.entity.Student;
import com.lewic.service.StudentService;
import io.swagger.annotations.ApiOperation;
import io.swagger.annotations.ApiParam;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.validation.BindingResult;
import org.springframework.web.bind.annotation.*;

import javax.validation.Valid;


/**
 * @apiNote StudentController
 * @since 2019/6/14 19:55
 **/

@RestController
@RequestMapping("/api/v1.0")
public class StudentController {
    @Autowired
    StudentService studentService;


    @ApiOperation("获取学生列表")
    @RequestMapping(value = "/student", method = RequestMethod.GET)
    public Message listStudent(
            @ApiParam(value = "第几页") @RequestParam(required = false, value = "pageNum", defaultValue = "1") Integer pageNum,
            @ApiParam(value = "每页条数") @RequestParam(required = false, value = "pageSize", defaultValue = "10") Integer pageSize
    ) {
        return studentService.listStudent(pageNum, pageSize);
    }

    @ApiOperation("根据id获取学生")
    @RequestMapping(value = "/student/{id}", method = RequestMethod.GET)
    public Message getStudent(@PathVariable(value = "id") Integer sid) {
        return studentService.getStudent(sid);
    }

    @ApiOperation("新增学生")
    @RequestMapping(value = "/student", method = RequestMethod.POST)
    public Message insertStudent(
            @ApiParam(value = "学生") @RequestBody @Valid Student Student,
            BindingResult bindingResult
    ) {
        if (bindingResult.hasErrors()) {
            return Util.checkParam(bindingResult);
        }
        return studentService.insertStudent(Student);
    }

    @ApiOperation("更新学生")
    @RequestMapping(value = "/student/{id}", method = RequestMethod.PUT)
    public Message updateStudent(
            @PathVariable(value = "id") Integer sid,
            @ApiParam(value = "学生") @RequestBody @Valid Student student,
            BindingResult bindingResult
    ) {
        student.setSid(sid);
        if (bindingResult.hasErrors()) {
            return Util.checkParam(bindingResult);
        }
        return studentService.updateStudent(student);
    }

    @ApiOperation("删除学生")
    @RequestMapping(value = "/student/{id}", method = RequestMethod.DELETE)
    public Message deleteStudent(@PathVariable(value = "id") String sid) {
        return studentService.deleteStudent(sid);
    }

}
