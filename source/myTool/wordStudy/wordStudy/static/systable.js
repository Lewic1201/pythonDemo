/*
 * SYSUI-SYSTABLE插件（保留头部可免费使用）
 * 2018-11-26 version1.1
 * 799129700@qq.com SYSHUXL-化海天堂
 * Reserved head available commercial use
 * Universal background system interface framework
 * table表格功能 （排序，checkbox全选，表格列宽拖拽，按钮操作,分页）
 */
function extend(o, n, override) {
	for (var key in n) {
		if (n.hasOwnProperty(key) && (!o.hasOwnProperty(key) || override)) {
			o[key] = n[key];
		}
	}
	return o;
};
//简化document.getElementById方法
function TAB$(i) {
	return document.getElementById(i)
};
//简化document.createElement方法
function TABLAYER$(i) {
	return document.createElement(i)
};
// 插件构造函数 - 返回数组结构
function SYSTableSorter(options) {
	this._initial(options);
};
SYSTableSorter.prototype = {
	constructor: this,
	_initial: function(options) {
		var par = {
			TableName: '', //table表格名称
			btnArea: '', //执行table外的按钮操作区域
			paginName: '',
			curPage: 1,//默认显示当前页
			Sequence: [], //输入需要排序的位置排序
			RightClick: false, //是否允许右键
			ViewState: [], //无需设置
			Callback: function() {

			}, //回调table数据
			DeleteEvent: function() {

			}, //删除
			ModifyEvent: function() {

			}, //修改
			DetailedEvent: function() {

			}, //详细
			SaveEvent: function() {

			}, //保存提交事件
			CheckboxDeleteEvent: function() {

			}, //批量删除事件
			SearchEvent: function() {

			} //搜索事件
		};
		this.par = extend(par, options, true);
		//判断是否存在class属性方法
		this.hasClass = function(elements, cName) {
			return !!elements.className.match(new RegExp("(\\s|^)" + cName + "(\\s|$)"));
		}
		//添加class属性方法
		this.addClass = function(elements, cName) {
			if (!this.hasClass(elements, cName)) {
				elements.className += " " + cName;
			};
		};
		//删除class属性方法 elements当前结构  cName类名
		this.removeClass = function(elements, cName) {
			if (this.hasClass(elements, cName)) {
				elements.className = elements.className.replace(new RegExp("(\\s|^)" + cName + "(\\s|$)"), " "); // replace方法是替换
			};
		};
		//根据class类名条件筛选结构
		this.getByClass = function(oParent, sClass) { //根据class获取元素
			var oReasult = [];
			var oEle = oParent.getElementsByTagName("*");
			for (i = 0; i < oEle.length; i++) {
				if (oEle[i].className == sClass) {
					oReasult.push(oEle[i]);
				}
			};
			return oReasult;
		}
		this.show(this.par);
	},
	//方法
	show: function(callback) {
		var _this = this;
		var Table = TAB$(callback.TableName);
		var other = TAB$(callback.btnArea); //声明执行对象
		var args = callback.Sequence;
		// 设置表头的状态位，排序时根据状态判断升降序 
		for (var x = 0; x < Table.rows[0].cells.length; x++) {
			callback.ViewState[x] = false;
		};
		if (args != null) {
			if (args.length > 1) {
				for (var x = 1; x < args.length; x++) {
					if (args[x] > Table.rows[0].cells.length) {
						continue;
					} else {
						var newDiv = TABLAYER$("em");
						_this.addClass(newDiv, 'NormalCss');
						Table.rows[0].cells[args[x]].appendChild(newDiv);
						Table.rows[0].cells[args[x]].onclick = function() {
							for (var m = 1; m < args.length; m++) {
								_this.onSequence(Table, args[m]);
							}
						};
						Table.rows[0].cells[args[x]].style.cursor = "pointer";
					}
				}
			}
		};
		//checkbox全选选择操作，表格列宽拖拽
		var tTD;
		for (var x = 0; x < Table.rows[0].cells.length; x++) {
			var checkbox = Table.rows[0].cells[x].getElementsByTagName('input')[x];
			checkbox ? Table.rows[0].cells[x].onclick = function(e) {
					for (var m = 0; m < Table.rows[0].cells.length; m++) {
						_this.oncheckbox(Table, m)
					}
				} :'';
			//表格拖拽
			Table.rows[0].cells[x].onmousedown = function(e) {
				_this.Dragdrop(e, Table, tTD, this);
			}
			Table.rows[0].cells[x].onmouseup = function(e) {
				_this.onmouseupDrop(e, Table, tTD, this);

			}
			Table.rows[0].cells[x].onmousemove = function(e) {
				_this.onmousemoveDrop(e, Table, tTD, this);
			}
		};
		_this.callbackf(Table, _this);
		_this.Selectedbtnmethod(other, Table, _this);
	},
	 currentcheckbox:function(Table,index){
		 for (var x = 1; x < Table.rows.length; x++) {
		 	var checkbox = Table.rows[x].cells[0].getElementsByTagName('input')[0];
		 	checkbox ? Table.rows[x].cells[0].onclick = function() {
		 		for (var m = 1; m < Table.rows.length; m++) {
		 			index.onlikecheck(Table, m)
		 		}
		 	} : ''; //单选事件
		 };
	 },
	//回调table数据的方法
	callbackf: function(Table, obj) {
		var curPage = obj.par.curPage;
		obj.par.Callback(Table, obj, curPage);
		obj.ajaxObject(obj);
	},
	//设置一个提示框，编辑提示框，texts为提示文本 ，time为显示时间秒单位
	PromptBox: function(texts, time) {
		var _this = this;
		var b = document.body.querySelector(".box_Bullet");
		if (!b) {
			var box = document.createElement("div");
			document.body.appendChild(box).className = "box_Bullet";
			var boxcss = document.querySelector(".box_Bullet");
			var winWidth = window.innerWidth;
			document.body.appendChild(box).innerHTML = texts;
			var wblank = winWidth - boxcss.offsetWidth;
			box.style.cssText = "width:" + boxcss.offsetWidth + "px" + "; left:" + (wblank / 2) + "px" + ";" +
				"margin-top:" + (-boxcss.offsetHeight / 2) + "px";
			var int = setInterval(function() {
				time--;
				_this.endclearInterval(time, box, int);
			}, 1000);
		}
	},
	endclearInterval: function(time, box, int) {
		time > 0 ? time-- : clearInterval(int);
		if (time == 0) {
			clearInterval(int);
			document.body.removeChild(box);
			return
		}
	},
	//声明ajax方法.，用于判断浏览器是否支持ajax
	ajaxObject: function(obj) {
		var xmlHttp;
		try {
			// Firefox, Opera 8.0+, Safari
			xmlHttp = new XMLHttpRequest();
		} catch (e) {
			// Internet Explorer
			try {
				xmlHttp = new ActiveXObject("Msxml2.XMLHTTP");
			} catch (e) {
				try {
					xmlHttp = new ActiveXObject("Microsoft.XMLHTTP");
				} catch (e) {
					obj.PromptBox('您的浏览器不支持AJAX', 2);
					return false;
				}
			}
		}
		return xmlHttp;
	},
	//get请求
	ajaxGet: function(url, success) {
		var _this = this;
		var ajax = _this.ajaxObject();
		ajax.open("GET", url, true);
		ajax.onreadystatechange = function() {
			if (ajax.readyState == 4) {
				if (ajax.status == 200) {
					var json = ajax.responseText; //获取到json字符串，还需解析
					var jsonStr = JSON.parse(json); //将字符串转换为json数组
					success(jsonStr);
				} else {
					_this.PromptBox("HTTP请求错误！错误码：" + ajax.status, 2);
				}
			}
		};
		ajax.send();
	},
	//Post请求
	ajaxPost: function(url, data, evnet, layer) {
		var _this = this;
		var ajax = _this.ajaxObject();
		ajax.open("post", url, true);
		ajax.setRequestHeader("Content-Type", "application/x-www-form-urlencoded");
		ajax.onreadystatechange = function() {
			if (ajax.readyState == 4) {
				if (ajax.status == 200) {
					_this.PromptBox(ajax.responseText, 2);
				} else {
					_this.PromptBox("HTTP请求错误！错误码：" + ajax.status, 2);
					return;
				}
			} else {
				//_this.PromptBox("请稍等...",3);
			}
			_this.statusname(ajax.status, _this, evnet, layer);
		}
		typeof(data) != "undefined" ? ajax.send(data): '';
	},
	//状态类型判断
	statusname: function(status, set, evnet, layer) {
		//判断是的保存按钮操作
		if (evnet.name == "SaveEvent") {
			if (status == 404) {

			} else if (status == 200) {
				//保存信息返回原来状态
				var edit = set.getByClass(layer.parentNode, 'table-edit');
				for (var i = 0; i < edit.length; i++) {
					var text = edit[i].getElementsByTagName("input")[0].value;
					edit[i].innerHTML = text;
				}
				evnet.remove();
				layer.innerHTML += "<button class='btn btn-blue padding5' name='ModifyEvent'>修改</button>"
			}
		}
	},
	// table以外层按钮操作方法
	Selectedbtnmethod: function(other, Table, obj) {
		var btn = other.getElementsByTagName("a") || other.getElementsByTagName("button");
		for (var i = 0; i < btn.length; i++) {
			btn[i].onclick = function(e) {
				if (this.name == "DeleteCheckbox") {
					//判断是否存在checkbox选中栏目，
					var checkbox = document.getElementsByName('checkbox');
					var trm = Table.rows.length;
					for (var x = Table.rows.length - 1; x >= 1; x--) {
						if (checkbox[x].checked == true) {
							var id = checkbox[x].parentNode.parentNode.parentNode.getAttribute('data-id');
							var remove = checkbox[x].parentNode.parentNode.parentNode;
							obj.par.CheckboxDeleteEvent(obj, remove, id);
							var trm = Table.rows.length - 1;
						}
					};
					if (Table.rows.length == trm) {
						obj.PromptBox("请选择你要删除的信息！", 2);
					}
				} else if (this.name == "searchEvent") {
					//搜索方法操作
					var value = this.parentNode.getElementsByTagName('input')[0].value;
					if (value) {
						obj.par.SearchEvent(obj, value);
					} else {
						obj.PromptBox("请输入查询关键字！", 2);
					}
				}
			};
		}
	},
	//按钮操作事件方法
	BtnoperationMethod: function(Table, obj) {
		for (var x = 1; x < Table.rows.length; x++) {
			for (var c = 1; c < Table.rows[x].cells.length; c++) {
				var btn = Table.rows[x].cells[c].getElementsByTagName("button") || Table.rows[x].cells[c].getElementsByTagName(
					"a"); //获取按钮
				Table.rows[x].cells[c].onclick = function(e) {
					var evt = e || window.event;
					var tar = evt.target || evt.srcElement;
					if (tar.tagName.toLowerCase() == "button" || tar.tagName.toLowerCase() == "a") {
						var name = tar.name;
						var tr = this.parentNode;
						var id = tr.getAttribute("data-id");
						obj.btnclick(Table, id, this, name, tar);
					}
				}
			}
		}
	},
	//执行事件方法
	btnclick: function(Table, id, obj, name, e) {
		var _this = this;
		if (name == 'deleteEvent') {
			_this.par.DeleteEvent(obj, _this, id); //删除操作	
			return;
		} else if (name == 'modifyEvent') {
			_this.ModifyMethod(Table, id, obj, name, e);
			_this.par.ModifyEvent(obj, _this, id); //修改操作
			return;
		} else if (name == 'detailedEvent') {
			_this.par.DetailedEvent(obj, _this, id); //详细操作
			return;
		} else if (name == 'SaveEvent') {
			_this.SaveMethod(Table, id, obj, _this, e);
		}
	},
	//执行修改信息操作方法
	ModifyMethod: function(Table, id, obj, name, e) {
		var _this = this; //声明调用数组集合
		var edit = _this.getByClass(obj.parentNode, 'table-edit');
		if (edit != 0) {
			for (var i = 0; i < edit.length; i++) {
				var keyname = edit[i].getAttribute("data-value");
				var text = edit[i].innerText;
				edit[i].innerHTML = "<input type='text' class='edit-text' value='" + text + "' name='" + keyname + "' />";
			}
			e.remove();
			obj.innerHTML += "<button class='btn btn-blue padding5' name='SaveEvent'>保存</button>";
		} else {
			_this.PromptBox("抱歉，不支持直接修改信息，请点击详细进行操作", 2);
		}
	},
	//分页table
	pageTableMethod: function(html, curPage, pageTotal, pageSize, total) {
		var that = this;
		var Table = TAB$(that.par.TableName);
		var pagination = TAB$(that.par.paginName);
		if (pagination) {
			var ul = pagination.appendChild(TABLAYER$('ul'));
			//分页
			var number = document.getElementsByName('page-number')[0];
			if (number) {
				var pag = [];
				var number = document.getElementsByName('page-number');
				if (curPage < pageSize) {
					var i = Math.min(pageSize, pageTotal);
					while (i) {
						pag.unshift(i--);
					}
					for (var i = 0; i < number.length - 1; i++) {
						var ellipsis = number[i].parentNode.getElementsByTagName('span')[0];
						if(ellipsis){
							ellipsis.style.cssText = "display:block;";
						}
						
						that.getPage(curPage);
						var pages = parseInt(number[i].getAttribute("data-pages"));
						number[i].setAttribute("data-pages", pag[i]);
						number[i].innerHTML = pag[i];
						var ys = parseInt(number[i].innerHTML);
						if (ys == curPage) {
							that.addClass(number[i], 'active');
						} else {
							that.removeClass(number[i], 'active');
						}
					}
				} else {
					 if(pageTotal-curPage >1) {
						 var middle = (curPage - 1) - Math.floor(pageSize / 2),
						//从哪里开始
						i = pageSize;
					if (middle > pageTotal - pageSize) {
						middle = pageTotal - pageSize + 1;
					}
					while (i--) {
						pag.push(middle++);
					}
					for (var i = 0; i < number.length - 1; i++) {
						var ellipsis = number[i].parentNode.getElementsByTagName('span')[0];
						if(ellipsis){
								ellipsis.style.cssText = "display:none;";
						}
					
						var pages = parseInt(number[i].getAttribute("data-pages"));
						number[i].setAttribute("data-pages", pag[i]);
						number[i].innerHTML = pag[i];
						var ys = parseInt(number[i].innerHTML);
						if (ys == curPage) {
							that.addClass(number[i], 'active');
						} else {
							that.removeClass(number[i], 'active');
						}
					}
					 }else{
						 return;
					 }
				}
			} else {
				that.firstPage(ul, curPage,html,pageTotal); //首页
				that.lastPage(ul, curPage, html); //上一页
				for (var p = 0; p < pageTotal; p++) {
					var li = TABLAYER$('li');
					var atr = document.createAttribute("name");
					atr.nodeValue = "page-number";
					li.setAttributeNode(atr);
					if (p == curPage - 1) {
						li.className += ' active';
					} else {
						that.addClass(li, 'pages');
						that.getPage(curPage);
					}
					li.innerHTML = p + 1;
					var pages = document.createAttribute("data-pages");
					pages.nodeValue = p + 1;
					li.setAttributeNode(pages);
					ul.appendChild(li);
				};
				var number = document.getElementsByName('page-number');
				for (var i = 0; i < number.length; i++) {
					for (var e = 5; e < number.length; e++) {
						if (number.length == pageTotal) {
							var span = TABLAYER$('span');
							that.addClass(span, 'ellipsis');
							span.innerHTML = '...';
							ul.appendChild(span);
						}
						number[e].remove();
						li.innerHTML = pageTotal;
						that.removeClass(li,'pages');
						that.addClass(li,'mantissa');
						ul.appendChild(li);
					}
					number[i].index = i;
					number[i].onclick = function(e) {
						for (var n = 0; n < number.length; n++) {
							var classname=that.hasClass(li, 'mantissa');
							if(classname){
									var u=parseInt(li.getAttribute("data-pages"));
							}
							index = e.target.index;
							var curPage = parseInt(number[index].getAttribute("data-pages"));						
							var ym = parseInt(number[n].getAttribute("data-pages"));
							 if (ym == curPage) {
								that.addClass(number[n], 'active');
							} else {
								that.removeClass(number[n], 'active');
							}	
							if(u-curPage>1){	
								that.getPages(ul, curPage, pageTotal, pageSize);
							}
						}
						that.par.Callback(Table, that, curPage);//执行回调的方法
						var Pre = document.getElementsByName('Pre-page')[0];//设置
						that.lastPage(ul, curPage, html, Pre); //上一页
						var next = document.getElementsByName('Next-page')[0];
						that.nextPage(ul, curPage, pageTotal, html, next); //上一页
					}
				};
				//调用下一页
				that.nextPage(ul, curPage, pageTotal, html);
				//调用尾页
				that.finalPage(ul, curPage, pageTotal, html);
				//是否显示总页数,每页个数,数据
				that.showPageTotal(ul, pageTotal, total);
			}
		}
	},
	//当前页码数的方法
	getPage: function(page) {
          //暂无
	},
	//首页的方法
	firstPage: function(ul, curPage,html,pageTotal) {
		var that = this;
		var Table = TAB$(that.par.TableName);
		var li = TABLAYER$('li');
		li.innerHTML = '首页';
		ul.appendChild(li);
		li.onclick = function() {
			var val = parseInt(1);
			curPage = val;
			that.getPage(that.curPage);
			that.par.Callback(Table, that, curPage);
			that.addClass(li, 'active');
			var last = document.getElementsByName('last-page')[0];//设置
			that.removeClass(last, 'active');
			var Pre = document.getElementsByName('Pre-page')[0];//设置
			that.lastPage(ul, curPage, html, Pre); //上一页
			var next = document.getElementsByName('Next-page')[0];
			that.nextPage(ul, curPage, pageTotal, html, next); //下一页
			ul.remove();
		};
		var atr = document.createAttribute("name");
		atr.nodeValue = "home-page";
		li.setAttributeNode(atr);
	},
	//上一页的方法+
	lastPage: function(ul, curPage, html, obj) {
		var that = this;
		var Table = TAB$(that.par.TableName);
		var number = document.getElementsByName('page-number');
		var li = TABLAYER$('li');
		if (!obj) {
			li.innerHTML = '<';
			if (parseInt(curPage) == 1) {
				li.className = 'disabled';
			}
			var atr = document.createAttribute("name");
			atr.nodeValue = "Pre-page";
			li.setAttributeNode(atr);
			ul.appendChild(li);
		} else {
			if (parseInt(curPage) > 1) {
				obj.onclick = function() {
					curPage = parseInt(curPage - 1);
					if (curPage > 0) {
						that.par.Callback(Table, that, curPage);
						that.getPage(that.curPage);
					}
					if (curPage == 1) {
						that.addClass(obj, 'disabled');
					}
				}
				that.removeClass(obj, 'disabled');
			} else {
				for (var i = 0; i < number.length; i++) {
						var lastm = parseInt(number[i].getAttribute("data-pages"));
						if(curPage!=lastm){
						that.removeClass(number[i], 'active');
						}
				}
				that.addClass(obj, 'disabled');
			}
		}
	},
	//分页判断方法
	getPages: function(ul, curPage, pageTotal, pageSize) {
		var pag = [];
		var that = this;
		if (curPage <= pageTotal) {
			if (curPage < pageSize) {
				//当前页数小于显示条数
				var i = Math.min(pageSize, pageTotal);
				while (i) {
					pag.unshift(i--);
				}
			} else {
				//当前页数大于显示条数
				var middle = curPage - Math.floor(pageSize / 2),
					//从哪里开始
					i = pageSize;
				if (middle > pageTotal - pageSize) {
					middle = pageTotal - pageSize + 1;
				}
				while (i--) {
					pag.push(middle++);
				}
			}
		} else {
			that.PromptBox("当前页数不能大于总页数", 2);
		}
		if (!pageSize) {
			that.PromptBox("显示页数不能为空或者0", 2);
		}
		return pag;
	},
	Pagination: function(ul, pag, pageTotal, that) {
		var number = document.getElementsByName('page-number');
		var pagination = TAB$(that.par.paginName);
		for (var i = 0; i < number.length - 1; i++) {
			var li = TABLAYER$('li');
			number[i].innerHTML = pag[i];
			ul.appendChild(li);
			var m = pageTotal - 1;
			if (pag[i] == m) {}
		}
	},
	//下一页方法
	nextPage: function(ul, curPage, pageTotal, html, obj) {
		var that = this;
		var Table = TAB$(that.par.TableName);
		var li = TABLAYER$('li');
		var number = document.getElementsByName('page-number');
		if (!obj) {
			li.innerHTML = '>';
			if (parseInt(curPage + 1) < parseInt(pageTotal)) {
				li.onclick = function() {
					for (var i = 0; i < number.length - 1; i++) {
						var active = that.hasClass(number[i],'active');	
							if(active){
									var curPage = parseInt(number[i].getAttribute("data-pages"));		
							}
					}
					curPage = parseInt(curPage + 1);
					if(curPage>=pageTotal-1){
						li.className = 'disabled';
					}else{
						that.par.Callback(Table, that, curPage);
					that.getPage(that.curPage);
					var Pre = document.getElementsByName('Pre-page')[0];
					that.removeClass(Pre, 'disabled');
					}
				};
			} else {
				li.className = 'disabled';
			}
			var atr = document.createAttribute("name");
			atr.nodeValue = "Next-page";
			li.setAttributeNode(atr);
			ul.appendChild(li);
		} else {
			if (parseInt(curPage + 1) < parseInt(pageTotal)) {
				that.removeClass(obj, 'disabled');
				
			}else{
				for (var i = 0; i < number.length; i++) {
				  	var lastm = parseInt(number[i].getAttribute("data-pages"));
						if(curPage==lastm){
							that.addClass(number[i], 'active');
						}
				}
				that.addClass(obj, 'disabled');
			}		 
	  }
	},
	//是否显示总页数,每页个数,数据
	showPageTotal: function(ul, pageTotal, total) {
		var that = this;
		var li = TABLAYER$('li');
		li.innerHTML = '共&nbsp' + pageTotal + '&nbsp页';
		li.className = 'totalPage';
		ul.appendChild(li);
		var li2 = TABLAYER$('li');
		li2.innerHTML = '合计&nbsp' + total + '&nbsp条';
		li2.className = 'totalPage';
		ul.appendChild(li2);
	},
	//尾页方法
	finalPage: function(ul, curPage, pageTotal, html) {
		var that = this;
		var Table = TAB$(that.par.TableName);
		var li = TABLAYER$('li');
		li.innerHTML = '尾页';
		ul.appendChild(li);
		var pagination = TAB$(that.par.paginName);
		li.onclick = function() {
			var curPage = parseInt(pageTotal);
			that.getPage(curPage);
			that.par.Callback(Table, that, curPage);
			that.addClass(li, 'active');
			var last = document.getElementsByName('home-page')[0];//设置
			that.removeClass(last, 'active');
			var Pre = document.getElementsByName('Pre-page')[0];//设置
			that.lastPage(ul, curPage, html, Pre); //上一页
			var next = document.getElementsByName('Next-page')[0];
			that.nextPage(ul, curPage, pageTotal, html, next); //下一页
			ul.remove();
		};
		var atr = document.createAttribute("name");
		atr.nodeValue = "last-page";
		li.setAttributeNode(atr);
	},
	//执行保存的事件方法
	SaveMethod: function(Table, id, obj, _this, e) {
		var formData = "";
		var m = obj.parentNode.getElementsByTagName('td');
		for (var i = 0; i < m.length; i++) {
			var edit = _this.hasClass(m[i], 'table-edit');
			if (edit) {
				var keyname = m[i].getElementsByTagName("input")[0].name;
				var text = m[i].getElementsByTagName("input")[0].value;
				formData += keyname + "=" + text + "&";
			}
		}
		_this.par.SaveEvent(obj, _this, id, formData, e); //保存操作
	},
	onSequence: function(Table, col) {
		var _this = this;
		// 定义判断排序字段的一个标志位，数字排序(自己写)和字符排序(JavaScript内置函数) 
		var SortAsNumber = true;
		// 定义放置需要排序的行数组 
		var Sorter = [];
		for (var x = 1; x < Table.rows.length; x++) {
			Sorter[x - 1] = [Table.rows[x].cells[col].innerHTML, x];
			// 判断需要排序字段的类型，分为数字型和非数字型 
			SortAsNumber = SortAsNumber && _this.IsNumeric(Sorter[x - 1][0]);
		}
		// 如果是数字型采用下面的方法排序 
		if (SortAsNumber) {
			for (var x = 0; x < Sorter.length; x++) {
				for (var y = x + 1; y < Sorter.length; y++) {
					if (parseFloat(Sorter[y][0]) < parseFloat(Sorter[x][0])) {
						var tmp = Sorter[x];
						Sorter[x] = Sorter[y];
						Sorter[y] = tmp;
					}
				}
			}
		}
		// 如果是非数字型的可以采用内置方法sort()排序 
		else {
			Sorter.sort();
		}
		if (_this.par.ViewState[col]) {
			// JavaScript内置函数，用于颠倒数组中元素的顺序。 
			Sorter.reverse();
			_this.par.ViewState[col] = false;
			_this.addClass(Table.rows[0].cells[col].lastChild, 'SortDescCss');
		} else {
			_this.par.ViewState[col] = true;
			_this.removeClass(Table.rows[0].cells[col].lastChild, 'SortAscCss');
		}
		var Rank = [];
		for (var x = 0; x < Sorter.length; x++) {
			Rank[x] = _this.GetRowHtml(Table.rows[Sorter[x][1]]);
		}
		for (var x = 1; x < Table.rows.length; x++) {
			for (var y = 0; y < Table.rows[x].cells.length; y++) {
				Table.rows[x].cells[y].innerHTML = Rank[x - 1][y];
			}
		}
		_this.OnSorted(Table.rows[0].cells[col], _this.par.ViewState[col]);
	},
	onlikecheck: function(Table, col) {
		var table=this;
		for (var x = 0; x < Table.rows[0].cells.length; x++) {
			var checkbox = Table.rows[0].cells[x].getElementsByTagName('input')[x];
			if (checkbox) {
				if (checkbox.checked == true) {
					checkbox ? checkbox.checked = false : '';
				}
			}
			var zcheckbox = Table.rows[col].cells[0].getElementsByTagName('input')[x];
			if (zcheckbox) {
				if (zcheckbox.checked == true) {
					table.addClass(Table.rows[col],'active');
					//Table.rows[col].className = "active";

				} else {
					Table.rows[col].className = "";
				}
				for (var x = 1; x < Table.rows.length; x++) {
					var n = Table.querySelectorAll(".active").length;
					var t = Table.rows.length - 1;
					if (n == t) {
						checkbox ? checkbox.checked = true : '';
					}
				}
			}
		}
	},
	oncheckbox: function(Table, col) {
		for (var x = 1; x < Table.rows.length; x++) {
			var checkbox = Table.rows[x].cells[col].getElementsByTagName('input')[col];
			for (var y = 0; y < Table.rows[0].cells.length; y++) {
				var checkboxs = Table.rows[0].cells[y].getElementsByTagName('input')[y];
				if (checkboxs) {
					if (checkboxs.checked == false) {
						checkbox ? checkbox.checked = false : '';
						Table.rows[x].className = "";
					} else {
						checkbox ? checkbox.checked = true : '';
						Table.rows[x].className = "active";
					}
				}
			}
		}
	},
	//表格拖拽鼠标指针点击时发生
	Dragdrop: function(e, Table, tTD, obj) {
		var col = obj.cellIndex;
		var tTD = Table.rows[0].cells[col];
		if (e.offsetX > tTD.offsetWidth - 10) {
			tTD.mouseDown = true;
			tTD.oldX = e.x;
			tTD.oldWidth = tTD.offsetWidth;
		}
	},
	//表格拖拽鼠标按键被松开时发生
	onmouseupDrop: function(e, Table, tTD, obj) {
		var col = obj.cellIndex;
		if (tTD == undefined) tTD = Table.rows[0].cells[col];
		tTD.mouseDown = false;
		tTD.style.cursor = 'default';
	},
	//表格拖拽鼠标指针移动时发生
	onmousemoveDrop: function(e, Table, tTD, obj) {
		var col = obj.cellIndex;
		//更改鼠标样式
		if (e.offsetX > Table.rows[0].cells[col].offsetWidth - 5) {
			Table.rows[0].cells[col].style.cursor = 'e-resize';
		} else {
			Table.rows[0].cells[col].style.cursor = 'default';
		}
		//取出暂存的Table Cell
		if (tTD == undefined) tTD = Table.rows[0].cells[col];
		//调整宽度
		if (tTD.mouseDown != null && tTD.mouseDown == true) {
			tTD.style.cursor = 'default';
			if (tTD.oldWidth + (e.x - tTD.oldX) > 0)
				tTD.width = tTD.oldWidth + (e.x - tTD.oldX);
			//调整列宽
			tTD.style.width = tTD.width;
			tTD.style.cursor = 'e-resize';
			//调整该列中的每个Cell
			table = tTD;
			while (table.tagName != 'TABLE') table = table.parentElement;
			for (j = 0; j < table.rows.length; j++) {
				table.rows[j].cells[tTD.cellIndex].width = tTD.width;
			}
		}
	},
	// 取得指定行的内容. 
	GetRowHtml: function(row) {
		var result = [];
		for (var x = 0; x < row.cells.length; x++) {
			result[x] = row.cells[x].innerHTML;
		}
		return result;
	},
	OnSorted: function(cell, IsAsc) {
		return;
	},
	IsNumeric: function(num) {
		return /^\d+(\.\d+)?$/.test(num);
	}
};
