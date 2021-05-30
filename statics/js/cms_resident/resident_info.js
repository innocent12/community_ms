/**
 * 初始化管理员详情对话框
 */
var CmsResidentInfoDlg = {
    cmsResidentInfoData: {}
};

/**
 * 清除数据
 */
CmsResidentInfoDlg.clearData = function () {
    this.cmsResidentInfoData = {};
}

/**
 * 设置对话框中的数据
 *
 * @param key 数据的名称
 * @param val 数据的具体值
 */
CmsResidentInfoDlg.set = function (key, val) {
    this.cmsResidentInfoData[key] = (typeof val == "undefined") ? $("#" + key).val() : val;
    return this;
}

/**
 * 设置对话框中的数据
 *
 * @param key 数据的名称
 * @param val 数据的具体值
 */
CmsResidentInfoDlg.get = function (key) {
    return $("#" + key).val();
}

/**
 * 关闭此对话框
 */
CmsResidentInfoDlg.close = function () {
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
CmsResidentInfoDlg.collectData = function () {
    this
        .set('id')
        .set('name')
        .set('age')
        .set('sex')
        .set('phone')
        .set('address')
        .set('job')
        .set('bce_user_id');
}

/**
 * 提交添加
 */
CmsResidentInfoDlg.addSubmit = function () {

    this.clearData();
    this.collectData();

    //提交信息
    var ajax = new $ax(Feng.ctxPath + "/cms_resident/save", function (data) {
        Feng.success("添加成功!");
        localStorage.clear()
        localStorage.setItem("user_id", data.user_id)
        localStorage.setItem("type", data.type)
        localStorage.setItem("name", data.name)
        if(window.parent.CmsResident !== undefined){
            window.parent.CmsResident.table.refresh();
        }
        CmsResidentInfoDlg.close();
    }, function (data) {
        Feng.error("添加失败，请规范输入!");
    });
    ajax.set(this.cmsResidentInfoData);
    ajax.start();
}

/**
 * 提交修改
 */
CmsResidentInfoDlg.editSubmit = function () {

    this.clearData();
    this.collectData();

    //提交信息
    var ajax = new $ax(Feng.ctxPath + "/cms_resident/update", function (data) {
        Feng.success("修改成功!");
        window.parent.CmsResident.table.refresh();
        CmsResidentInfoDlg.close();
    }, function (data) {
        Feng.error("修改失败，请规范输入!");
    });
    ajax.set(this.cmsResidentInfoData);
    ajax.start();
}

$(function () {

});
