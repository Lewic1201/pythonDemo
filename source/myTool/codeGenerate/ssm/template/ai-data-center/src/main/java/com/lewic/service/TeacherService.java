package com.lewic.service;

import com.lewic.common.Message;
import com.lewic.common.Page;
import com.lewic.entity.Teacher;
import com.lewic.mapper.Teacher2StudentMapper;
import com.lewic.mapper.TeacherMapper;
import lombok.extern.slf4j.Slf4j;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import java.util.List;


/**
 * @author lewic
 * @since 2019/6/13 15:22
 **/

@Service
@Slf4j
public class TeacherService {
    @Autowired
    TeacherMapper teacherMapper;
    @Autowired
    Teacher2StudentMapper teacher2StudentMapper;

    public Message listTeacher(String name, Integer pageNum, Integer pageSize) {
        Integer total = teacherMapper.getTeacherFilterCount(name);
        Page page = new Page(pageSize, pageNum, total);

        List<Teacher> teachers = teacherMapper.listTeacher(name, page);

        Message<List<Teacher>> msg = new Message<>();
        msg.setData(teachers);
        return msg;
    }


    public Message getTeacher(String id) {
        Teacher teacher = teacherMapper.getTeacher(id);

        Message<Teacher> msg = new Message<>();
        msg.setData(teacher);
        return msg;
    }


    public Message insertTeacher(Teacher teacher) {
        Message<String> msg = new Message<>();
        try {

            teacherMapper.insertTeacher(teacher);

            // 获取insert生成的id然后添加关联数据到中间表
            Integer autoId = teacher.getTid();
            teacher2StudentMapper.removeAllStudent(autoId);
            teacher2StudentMapper.addStudent(autoId, teacher.getStudents());

            msg.setData("insert success");
        } catch (Exception e) {
            msg.setMessage("insert failed, because: " + e.getMessage());
        }
        return msg;
    }

    public Message updateTeacher(Teacher teacher) {
        Message<String> msg = new Message<>();
        try {

            teacherMapper.updateTeacher(teacher);

            // 获取insert生成的id然后添加关联数据到中间表
            Integer tid = teacher.getTid();
            teacher2StudentMapper.removeAllStudent(tid);
            teacher2StudentMapper.addStudent(tid, teacher.getStudents());

            msg.setData("update success");
        } catch (Exception e) {
            msg.setMessage("update failed, because: " + e.getMessage());
        }
        return msg;
    }

    public Message deleteTeacher(String tid) {
        Message<String> msg = new Message<>();
        try {
            String[] tids = tid.split(",");
            teacherMapper.deleteTeacher(tids);
            msg.setData("delete success");
        } catch (Exception e) {
            msg.setMessage("delete failed, because:" + e.getMessage());
        }
        return msg;
    }

}
