/**
 * 初始化管理员详情对话框
 */
var CmsMigrantInfoDlg = {
    cmsMigrantInfoData : {}
};

/**
 * 清除数据
 */
CmsMigrantInfoDlg.clearData = function() {
    this.cmsMigrantInfoData = {};
}

/**
 * 设置对话框中的数据
 *
 * @param key 数据的名称
 * @param val 数据的具体值
 */
CmsMigrantInfoDlg.set = function(key, val) {
    this.cmsMigrantInfoData[key] = (typeof val == "undefined") ? $("#" + key).val() : val;
    return this;
}

/**
 * 设置对话框中的数据
 *
 * @param key 数据的名称
 * @param val 数据的具体值
 */
CmsMigrantInfoDlg.get = function(key) {
    return $("#" + key).val();
}

/**
 * 关闭此对话框
 */
CmsMigrantInfoDlg.close = function() {
    if(window.parent.CmsResident !== undefined){
        parent.layer.close(window.parent.CmsResident.layerIndex);
    }else {
        var index1 = parent.layer.getFrameIndex(window.name); //先得到当前iframe层的索引
        parent.layer.close(index1); //再执行关闭
    }
}

/**
 * 收集数据
 */
CmsMigrantInfoDlg.collectData = function() {
    this
    .set('id')
    .set('name')
    .set('age')
    .set('sex')
    .set('phone')
    .set('bce_user_id');
}

/**
 * 提交添加
 */
CmsMigrantInfoDlg.addSubmit = function() {

    this.clearData();
    this.collectData();

    //提交信息
    var ajax = new $ax(Feng.ctxPath + "/cms_migrant/save", function(data){
        Feng.success("添加成功!");
        localStorage.clear()
        localStorage.setItem("user_id", data.user_id)
        localStorage.setItem("type", data.type)
        localStorage.setItem("name", data.name)
        if(window.parent.CmsMigrant !== undefined){
            window.parent.CmsMigrant.table.refresh();
        }
        CmsMigrantInfoDlg.close();
    },function(data){
        Feng.error("添加失败，请规范输入!");
    });
    ajax.set(this.cmsMigrantInfoData);
    ajax.start();
}

/**
 * 提交修改
 */
CmsMigrantInfoDlg.editSubmit = function() {

    this.clearData();
    this.collectData();

    //提交信息
    var ajax = new $ax(Feng.ctxPath + "/cms_migrant/update", function(data){
        Feng.success("修改成功!");
        window.parent.CmsMigrant.table.refresh();
        CmsMigrantInfoDlg.close();
    },function(data){
        Feng.error("修改失败，请规范输入!");
    });
    ajax.set(this.cmsMigrantInfoData);
    ajax.start();
}

$(function() {

});
