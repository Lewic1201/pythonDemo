package com.sc.hoperun.common;

import java.io.Serializable;

/**
 * 
 * @author Administrator
 */
public class Page implements Serializable{

	private static final long serialVersionUID = 5790890024078772097L;
	
	//当前页
    private int pageNum =1;
    //总记录数
    private int total;
    //总页数
    private int pages;
    //每页多少
    private int pageSize = 10;
    //开始页码
    private int startRow;
    //结束页码
    private int endRow;

    public Page(){

    }

    public Page(int pageSize,int pageNum,int total){
        this.setPageSize(pageSize);
        this.setPageNo(pageNum);
        this.setTotalCount(total);
    }
    public int getPageNo() {
        return pageNum ;
    }

    public void setPageNo(int pageNo) {
        if (pageNo <= 0) pageNo = 1;
        this.pageNum = pageNo;
    }

    public int getTotalCount() {
        return total;
    }

    public void setTotalCount(int totalCount) {
        if (totalCount < pageSize) {
            if (pageNum  > 1) pageNum  = 1;
            startRow=0;
            endRow=totalCount;
			pages=1;
        }else{
            if(totalCount%pageSize==0){
				pages=totalCount/pageSize;
            }else{
				pages=totalCount/pageSize+1;
            }
            if(pageNum >= pages){
            	startRow=(pages-1)*pageSize;
				pageNum = pages;
            }else{
            	startRow=(pageNum -1)*pageSize;
            }
            endRow=startRow+pageSize;
        }
        this.total = totalCount;
    }

    public int getTotalPage() {
        return  pages;
    }

    public void setTotalPage(int totalPage) {
        this. pages = totalPage;
    }

    public int getPageSize() {
        if (pageSize <= 0) pageSize = 20;
        return pageSize;
    }

    public void setPageSize(int pageSize) {
        this.pageSize = pageSize;
    }

    public int getStartRow() {
        return startRow;
    }

    public void setStartRow(int startPage) {
        this.startRow = startPage;
    }

    public int getEndRow() {
        return endRow;
    }

    public void setEndPage(int endPage) {
        this.endRow = endPage;
    }

	@Override
	public int hashCode() {
		final int prime = 31;
		int result = 1;
		result = prime * result + endRow;
		result = prime * result + pageNum ;
		result = prime * result + pageSize;
		result = prime * result + startRow;
		result = prime * result + total;
		result = prime * result +  pages;
		return result;
	}

	@Override
	public boolean equals(Object obj) {
		if (this == obj)
			return true;
		if (obj == null)
			return false;
		if (getClass() != obj.getClass())
			return false;
		Page other = (Page) obj;
		if (endRow != other.endRow)
			return false;
		if (pageNum  != other.pageNum )
			return false;
		if (pageSize != other.pageSize)
			return false;
		if (startRow != other.startRow)
			return false;
		if (total != other.total)
			return false;
		if (total != other.pages)
			return false;
		return true;
	}

}
