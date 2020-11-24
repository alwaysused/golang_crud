func Msg_FindMsgByID(id uint) (Msg, error) {
	var msg Msg
	if err := g_DB.Model(&msg).Where("id = ?", id).First(&msg).Error; err != nil {
		return msg, err
	}
	return msg, nil
}
func Msg_SearchMsg(skip,limit int, info def.Msg_SearchMsg)([]Msg,int, error){
	var msgs []Msg
    var total int
    sqlStr := ""
    if info.StartTime != "" {
        sqlStr += fmt.Sprintf(" start_time > '%s'",info.StartTime)
    }
    if info.EndTime != "" {
        sqlStr += fmt.Sprintf("and end_time > '%s'",info.EndTime)
    }
    if info.Title != "" {
        sqlStr += fmt.Sprintf("and title like '%%%s%%'",info.Title)
    }
    if info.Type != 0 {
        sqlStr += fmt.Sprintf("and type=%d",info.Type)
    }
    if info.UserId != 0 {
        sqlStr += fmt.Sprintf("and user_id=%d",info.UserId)
    }

	if err := g_DB.Where(sqlStr). Count(&total) .Error; err != nil {
		return msgs, 0,err
	}

	if err := g_DB.Where(sqlStr).Offset(skip).Limit(limit).Find(&msgs).Error; err != nil {
		return msgs, 0,err
	}
	return msgs,total, nil
}
    
    
    func Msg_UpdateMsg(id uint, info def.Msg_UpdateMsg(Msg, error){
    msg := map[string]interface{} {
        "user_id": info.UserId,
        "status": info.Status,
        "products": info.Products,
        "scope": info.Scope,
        "scope_desc": info.ScopeDesc,
        "created_at": info.CreatedAt,
    var m Msg
    if err := g_DB.Update(&m).Where("id = ?", id).Updates(msg).Error; err !=nil{
        return Msg{}, err
    }
    return Msg_FindMsgByID(msg.ID)
}
func Msg_CreateMsg(info def.Msg_CreateMsg(Msg, error){
    msg := Msg {
        CustomModel:  CustomModel{},
        UserId: info.UserId,
        Status: info.Status,
        Products: info.Products,
        Scope: info.Scope,
        ScopeDesc: info.ScopeDesc,
        CreatedAt: info.CreatedAt,
    if err := g_DB.Create(&msg).Error; err !=nil{
        return Msg{}, err
    }
    return Msg_FindMsgByID(msg.ID)
}
func Msg_DeleteMsg(id uint)error{
	if err := g_DB.Where("id = ? ", id).Unscoped().Delete(&Msg{}).Error; err != nil {
		return err
	}
	return nil
}
