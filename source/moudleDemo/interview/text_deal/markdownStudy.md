# 这是一级标题
## 这是二级标题
### 这是三级标题
#### 这是四级标题
##### 这是五级标题
###### 这是六级标题





*字体加斜*
**字体加粗**
***字体加斜加粗***

~~这是加删除线的文字~~



>这是引用的内容
>>这是引用的内容
>>
>>>>>>>>>>这是引用的内容
>>>>>>>>>>这是引用的内容
>>>>>>>>>>
>>>>>>>>>>
>>
>>
>
>这是引用的内容



---
----
分隔线
***
*****



[简书]()  
[百度](http://baidu.com)
[超链接](http://link)  



<a href="https://linkAddress" target="_blank">超链接名</a>
- ##### 注：Markdown本身语法不支持链接在新页面中打开，貌似简书做了处理，是可以的。别的平台可能就不行了，如果想要在新页面中打开的话可以用html语言的a标签代替。  
  
   
  
* 无需列表
+ 无需列表
- 无需列表  
  
  
  

1. 有序列表
2. 有序列表
3. 有序列表 
4.  



- 列表嵌套,上一级和下一级之间敲两个空格即可
- 一级无序列表内容
  - 二级无序列表内容
  - 二级无序列表内容
    1. 三级有序列表内容
    2. 三级有序列表内容  



## 表格

表头|表头|表头
--|:--:|:---
内容|内容|内容
内容|内容|内容

```
第二行分割表头和内容。
- 有一个就行，为了对齐，多加了几个
文字默认居左
-两边加：表示文字居中
-右边加：表示文字居右
注：原生的语法两边都要用 | 包起来。此处省略
```





`单行代码`
``print 'hello world'``

```
代码块
```





### 流程图

```flow
st=>start: 开始
op=>operation: My Operation
cond=>condition: Yes or No?
e=>end
st->op->cond
cond(yes)->e
cond(no)->op
```

>>>只想说牛X  

```flow
st=>start: 开始
op=>operation: 输入信息
cond1=>condition: 有没有钱?
cond2=>condition: 帅否?
cond3=>condition: 高否?
fail=>operation: goodbye
success=>operation: 你好,高富帅
end=>end: 结束
e=>end
st->op->cond3->cond1->cond2->success->end
cond3(yes)->cond1
cond1(yes)->cond2
cond2(yes)->success
cond1(no)->fail
cond2(no)->fail
cond3(no)->fail
fail->op
```