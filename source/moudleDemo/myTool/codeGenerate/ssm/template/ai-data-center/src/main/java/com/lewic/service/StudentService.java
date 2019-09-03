package com.lewic.service;

import com.lewic.common.Message;
import com.lewic.common.Page;
import com.lewic.entity.Student;
import com.lewic.mapper.StudentMapper;
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
public class StudentService {

    @Autowired
    StudentMapper studentMapper;


    public Message listStudent(Integer pageNum, Integer pageSize) {
        Integer total = studentMapper.getStudentCount();
        Page page = new Page(pageSize, pageNum, total);

        List<Student> students = studentMapper.listStudent(page);

        Message<List> msg = new Message<>();
        msg.setData(students);
        return msg;
    }


    public Message<Student> getStudent(Integer id) {
        Student Student = studentMapper.getStudent(id);

        Message<Student> msg = new Message<>();
        msg.setData(Student);
        return msg;
    }


    public Message insertStudent(Student student) {
        Message<String> msg = new Message<>();
        try {
            studentMapper.insertStudent(student);
            msg.setData("insert success");
        } catch (Exception e) {
            msg.setMessage("insert failed, because: " + e.getMessage());
        }
        return msg;
    }

    public Message updateStudent(Student student) {
        Message<String> msg = new Message<>();
        try {
            studentMapper.updateStudent(student);
            msg.setData("update success");
        } catch (Exception e) {
            msg.setMessage("update failed, because: " + e.getMessage());
        }
        return msg;
    }

    public Message deleteStudent(String sid) {
        Message<String> msg = new Message<>();
        try {
            studentMapper.deleteStudent(sid);
            msg.setData("delete success");
        } catch (Exception e) {
            msg.setMessage("delete failed, because:" + e.getMessage());
        }
        return msg;
    }

}
