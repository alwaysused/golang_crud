func Msg_FindMsgByID(c *gin.Context){
    	id,_ := strconv.Atoi(c.Param("msg_id"))
    	ad,err := domain.Msg_FindMsgByID(id)
    	if err != nil {
    		response.GinBadReplyAsJson(c, http.StatusBadRequest, "获取失败", response.AtomcareError{Desc: err.Error()})
    		return
    	}
    	c.JSON(http.StatusOK, gin.H{"msg": "获取成功","value":ad})

}
func Msg_SearchMsg(c *gin.Context){

    var info def.Msg_SearchMsg
	skip,limit := util.GetPage(c)
	if err := c.ShouldBindJSON(&info);err != nil {
		response.GinBadReplyAsJson(c, http.StatusBadRequest, "广告上传失败", response.AtomcareError{Desc: "参数有误"})
	}
	

	ad, total,err := domain.Msg_SearchMsg(info, skip, limit)
	if err != nil {
		response.GinBadReplyAsJson(c, http.StatusBadRequest, "创建失败", response.AtomcareError{Desc: err.Error()})
		return
	}
	c.JSON(http.StatusOK, gin.H{"msg": "创建成功", "value": ad,"total":total})
}    
    func Msg_UpdateMsg(c *gin.Context){
	var info def.Msg_UpdateMsg
	if err := c.ShouldBindJSON(&info);err != nil {
		response.GinBadReplyAsJson(c, http.StatusBadRequest, "广告上传失败", response.AtomcareError{Desc: "参数有误"})

	}
	
	id,_ := strconv.Atoi(c.Param("msg_id"))
	ad, err := domain.Msg_UpdateMsg(id,info)
	if err != nil {
		response.GinBadReplyAsJson(c, http.StatusBadRequest, "创建失败", response.AtomcareError{Desc: err.Error()})
		return
	}
	c.JSON(http.StatusOK, gin.H{"msg": "创建成功", "value": ad})
}
func Msg_CreateMsg(info def.Msg_CreateMsg(fMsg, error)
    if err := c.ShouldBindJSON(&info);err != nil {
        response.GinBadReplyAsJson(c, http.StatusBadRequest, "广告上传失败", response.AtomcareError{Desc: "参数有误"})
	}
	ad, err := domain.Msg_CreateMsg(info)
    if err != nil {
		response.GinBadReplyAsJson(c, http.StatusBadRequest, "创建失败", response.AtomcareError{Desc: err.Error()})
		return
	}
	c.JSON(http.StatusOK, gin.H{"msg": "创建成功", "value": ad})
func Msg_DeleteMsg(c *gin.Context){
	id,_ := strconv.Atoi(c.Param("msg_id"))
	err := domain.Msg_DeleteMsg(id)
	if err != nil {
		response.GinBadReplyAsJson(c, http.StatusBadRequest, "删除失败", response.AtomcareError{Desc: err.Error()})
		return
	}
	c.JSON(http.StatusOK, gin.H{"msg": "删除成功"})

}
