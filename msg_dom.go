func Msg_FindMsgByID(id int)(model.Msg, error){
    return model.Msg_FindMsgByID(uint(id))
}
    
   
    func Msg_SearchMsg(info def.Msg_SearchMsg,skip,size int)([]model.Msg, int, error){
	return model.Msg_SearchMsg(skip, size,info)
}

    
    
    func Msg_UpdateMsg(id int,info def.Msg_UpdateMsg) (model.Msg, error) {
    m,_ := model.Msg_UpdateMsg(uint(id),info)

	return m, nil
}
    func Msg_CreateMsg(info def.Msg_CreateMsg(fMsg, error){
    m,err := model.Msg_CreateMsg(info)
    return m, err
}
func Msg_DeleteMsg(id int)error{
	return model.Msg_DeleteMsg(uint(id))
}
