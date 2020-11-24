base = "msg"
daxie = "Msg"
fushu = "msgs"
baseid = "msg_id"
createParamName =  f"{daxie}_Create{daxie}"
findidParamNamae = f"{daxie}_Find{daxie}ByID"
deleteFuncName = f"{daxie}_Delete{daxie}"
searchFuncName = f"{daxie}_Search{daxie}"
updateFuncName  =f"{daxie}_Update{daxie}"

indent= "    "
#member = []

api = open(f"{base}_api.go","w", encoding="utf-8")
dom = open(f"{base}_dom.go","w", encoding="utf-8")
model = open(f"{base}_model.go","w", encoding="utf-8")


def w():
    apif = [g_get_detail_api,g_search_api,g_update_api,g_zeng_api,g_delete_api]
    domf = [g_get_detail_domain,g_search_domain,g_update_domain,g_zeng_domain,g_delete_domain]
    modelf = [g_get_detail_model,g_search_model,g_update_model,g_zeng_model,g_delete_model]
    #modelf = []

    for f in apif:
        api.write(f())
    for f in domf:
        dom.write(f())
    for f in modelf:
        model.write(f())
    
def snakeWords(inp):
    s = ""
    c  = 0
    for i in inp :
        if str.islower(i):
            pass
        elif c != 0:
            s += "_"
        s += str.lower(i)
        c +=1
    return s
def init_create(member):
    with   open("create.txt")as f:
        d = f.readlines()
        for line in d:
            member.append(line.split()[0])
def init_update(member):
    with   open("update.txt")as f:
        d = f.readlines()
        for line in d:
            member.append(line.split()[0])
def init_search(member):
    with   open("search.txt")as f:
        d = f.readlines()
        for line in d:
            member.append(line.split())
def g_zeng_model():
    member = []
    init_create(member)
    p=[]
    func_declare = "func " + createParamName + f"(info def.{createParamName}({daxie}, error){{"
    p.append(func_declare)
    line1 = indent +f"{base} := {daxie} " +"{"
    p.append(line1)
    jichuchengyuan=indent * 2+"CustomModel:  CustomModel{},"
    p.append(jichuchengyuan)
    for i in member:
        p.append(indent * 2+ f"{i}: info.{i},")
    database =indent + f"if err := g_DB.Create(&{base}).Error; err !=nil" + "{"
    db2 = indent *2+ f"return {daxie}"+"{}, err\n    }"
    returns = indent+ "return " + findidParamNamae +f"({base}.ID)\n}}"
    p.append(database)
    p.append(db2)
    p.append(returns)
    s="\n".join(p) + "\n"
    return s
    

def g_zeng_domain():
    p=[]
    func_declare = "func " + createParamName + f"(info def.{createParamName}(f{daxie}, error){{"
    diaoyongmodel = f"    m,err := model.{createParamName}(info)"

    returns = "    return m, err\n}"

    p.append(func_declare)
    p.append(diaoyongmodel)
    p.append(returns)
    return "\n".join(p) + "\n"

def g_zeng_api():
    p=[]
    func_declare = "func " + createParamName + f"(info def.{createParamName}(f{daxie}, error)"
    l1 = "    if err := c.ShouldBindJSON(&info);err != nil {"
    l2 = "        response.GinBadReplyAsJson(c, http.StatusBadRequest, \"广告上传失败\", response.AtomcareError{Desc: \"参数有误\"})"

    l3 = "	}"

    l4 = f'''	ad, err := domain.{createParamName}(info)'''
    l5= '''    if err != nil {
		response.GinBadReplyAsJson(c, http.StatusBadRequest, "创建失败", response.AtomcareError{Desc: err.Error()})
		return
	}
	c.JSON(http.StatusOK, gin.H{"msg": "创建成功", "value": ad})'''
    p.append(func_declare)

    p.append(l1)
    p.append(l2)
    p.append(l3)
    p.append(l4)
    p.append(l5)
    return "\n".join(p) + "\n"

def g_update_api():
    s=f'''func {updateFuncName}(c *gin.Context){{
	var info def.{updateFuncName}
	if err := c.ShouldBindJSON(&info);err != nil {{
		response.GinBadReplyAsJson(c, http.StatusBadRequest, "广告上传失败", response.AtomcareError{{Desc: "参数有误"}})

	}}
	
	id,_ := strconv.Atoi(c.Param("{baseid}"))
	ad, err := domain.{updateFuncName}(id,info)
	if err != nil {{
		response.GinBadReplyAsJson(c, http.StatusBadRequest, "创建失败", response.AtomcareError{{Desc: err.Error()}})
		return
	}}
	c.JSON(http.StatusOK, gin.H{{"msg": "创建成功", "value": ad}})
}}\n'''
    return s



def g_update_domain():
    s = f'''func {updateFuncName}(id int,info def.{updateFuncName}) (model.{daxie}, error) {{
    m,_ := model.{updateFuncName}(uint(id),info)

	return m, nil
}}
    '''

    return s
def g_update_model():
    member=[]
    init_create(member)
    p = []
    func_declare = "func " + updateFuncName + f"(id uint, info def.{updateFuncName}({daxie}, error){{"
    p.append(func_declare)
    line1 = indent + f"{base} := map[string]interface{{}} " + "{"
    p.append(line1)
    #jichuchengyuan = indent * 2 + "CustomModel:  CustomModel{},"
    #p.append(jichuchengyuan)
    for i in member:
        dbc = snakeWords(i)
        p.append(indent * 2 + f'"{dbc}": info.{i},')
    s1 = indent +f"var m {daxie}"
    database = indent + f"if err := g_DB.Model(&{daxie}{{}}).Update(&m).Where(\"id = ?\", id).Updates({base}).Error; err !=nil" + "{"
    db2 = indent * 2 + f"return {daxie}" + "{}, err\n    }"
    returns = indent + "return " + findidParamNamae + f"({base}.ID)\n}}"
    p.append(s1 )
    p.append(database)
    p.append(db2)
    p.append(returns)
    return "\n".join(p) + "\n"

def g_delete_model():
    s = f'''func {deleteFuncName}(id uint)error{{
	if err := g_DB.Where("id = ? ", id).Unscoped().Delete(&{daxie}{{}}).Error; err != nil {{
		return err
	}}
	return nil
}}\n'''
    return s

def g_delete_domain():
    s='''func Msg_DeleteMsg(id int)error{
	return model.Msg_DeleteMsg(uint(id))
}\n'''
    return s
def g_delete_api():
    s  =  f'''func {deleteFuncName}(c *gin.Context){{
	id,_ := strconv.Atoi(c.Param("{baseid}"))
	err := domain.{daxie}_Delete{daxie}(id)
	if err != nil {{
		response.GinBadReplyAsJson(c, http.StatusBadRequest, "删除失败", response.AtomcareError{{Desc: err.Error()}})
		return
	}}
	c.JSON(http.StatusOK, gin.H{{"msg": "删除成功"}})

}}\n'''
    return s

# g_zeng_model()
# g_zeng_domain()
# g_zeng_api()
#
# g_update_api()
# g_update_domain()
# g_update_model()

def g_search_api():
    s = f'''func {searchFuncName}(c *gin.Context){{

    var info def.{searchFuncName}
	skip,limit := util.GetPage(c)
	if err := c.ShouldBindJSON(&info);err != nil {{
		response.GinBadReplyAsJson(c, http.StatusBadRequest, "广告上传失败", response.AtomcareError{{Desc: "参数有误"}})
	}}
	

	ad, total,err := domain.Msg_SearchMsg(info, skip, limit)
	if err != nil {{
		response.GinBadReplyAsJson(c, http.StatusBadRequest, "创建失败", response.AtomcareError{{Desc: err.Error()}})
		return
	}}
	c.JSON(http.StatusOK, gin.H{{"msg": "创建成功", "value": ad,"total":total}})
}}    
    '''
    return s
def g_search_domain():
    s = f'''func {searchFuncName}(info def.{searchFuncName},skip,size int)([]model.{daxie}, int, error){{
	return model.{searchFuncName}(skip, size,info)
}}

    
    
    '''
    return s




def g_search_model():
    p = []

    init_search(p)
    s = f'''func {searchFuncName}(skip,limit int, info def.{searchFuncName})([]{daxie},int, error){{
	var {fushu} []{daxie}
    var total int
    sqlStr := ""
'''
    for i in p:
        dbcolumn = snakeWords(i[0])
        if i[1] == "string" and i[0].endswith("Time") is False:
                s += f"    if info.{i[0]} != \"\" {{\n"
                s += f"        sqlStr += fmt.Sprintf(\"and {dbcolumn} like '%%%s%%%'\",info.{i[0]})\n"
                s += "    }\n"
        elif i[1] == "int" or i[1] == "uint":
            s += f"    if info.{i[0]} != 0 {{\n"
            s += f"        sqlStr += fmt.Sprintf(\"and {dbcolumn}=%d\",info.{i[0]})\n"
            s += "    }\n"

        elif i[1] == "*bool":
            s += f"    if *info.{i[0]} != nil {{\n"
            s += f"        sqlStr += fmt.Sprintf(\"and {dbcolumn}= %v \",*info.{i[0]})\n"
            s += "    }\n"
        elif  i[1] == "string" and i[0].endswith("Time") is True:
            s += f"    if info.{i[0]} != \"\" {{\n"
            s += f"        sqlStr += fmt.Sprintf(\"and {dbcolumn} > '%s'\",info.{i[0]})\n"
            s += "    }\n"
    s += f'''
	if err := g_DB.Where(sqlStr). Count(&total) .Error; err != nil {{
		return {fushu}, 0,err
	}}

	if err := g_DB.Where(sqlStr).Offset(skip).Limit(limit).Find(&{fushu}).Error; err != nil {{
		return {fushu}, 0,err
	}}
	return {fushu},total, nil
}}
    
    
    '''

    return s

def g_get_detail_api():
    s = f'''func {findidParamNamae}(c *gin.Context){{
    	id,_ := strconv.Atoi(c.Param("{baseid}"))
    	ad,err := domain.{findidParamNamae}(id)
    	if err != nil {{
    		response.GinBadReplyAsJson(c, http.StatusBadRequest, "获取失败", response.AtomcareError{{Desc: err.Error()}})
    		return
    	}}
    	c.JSON(http.StatusOK, gin.H{{"msg": "获取成功","value":ad}})

}}\n'''
    return s

def g_get_detail_model():
    s = f'''func {findidParamNamae}(id uint) (Msg, error) {{
	var {base} {daxie}
	if err := g_DB.Model(&{base}).Where("id = ?", id).First(&{base}).Error; err != nil {{
		return {base}, err
	}}
	return {base}, nil
}}\n'''
    return s

def g_get_detail_domain():
    s = f'''func {findidParamNamae}(id int)(model.{daxie}, error){{
    return model.{findidParamNamae}(uint(id))
}}
    
   
    '''
    return s

# g_get_detail_api()
# g_get_detail_domain()
# g_get_detail_model()

w()