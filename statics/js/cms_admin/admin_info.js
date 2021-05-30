/**
 * 初始化管理员详情对话框
 */
var CmsAdminInfoDlg = {
    cmsAdminInfoData : {}
};

/**
 * 清除数据
 */
CmsAdminInfoDlg.clearData = function() {
    this.cmsAdminInfoData = {};
}

/**
 * 设置对话框中的数据
 *
 * @param key 数据的名称
 * @param val 数据的具体值
 */
CmsAdminInfoDlg.set = function(key, val) {
    this.cmsAdminInfoData[key] = (typeof val == "undefined") ? $("#" + key).val() : val;
    return this;
}

/**
 * 设置对话框中的数据
 *
 * @param key 数据的名称
 * @param val 数据的具体值
 */
CmsAdminInfoDlg.get = function(key) {
    return $("#" + key).val();
}

/**
 * 关闭此对话框
 */
CmsAdminInfoDlg.close = function() {
    parent.layer.close(window.parent.CmsAdmin.layerIndex);
}

/**
 * 收集数据
 */
CmsAdminInfoDlg.collectData = function() {
    this
    .set('id')
    .set('name')
    .set('password');
}

/**
 * 提交添加
 */
CmsAdminInfoDlg.addSubmit = function() {

    this.clearData();
    this.collectData();

    //提交信息
    var ajax = new $ax(Feng.ctxPath + "/cms_admin/save", function(data){
        Feng.success("添加成功!");
        window.parent.CmsAdmin.table.refresh();
        CmsAdminInfoDlg.close();
    },function(data){
        Feng.error("添加失败，请规范输入!");
    });
    ajax.set(this.cmsAdminInfoData);
    ajax.start();
}

/**
 * 提交修改
 */
CmsAdminInfoDlg.editSubmit = function() {

    this.clearData();
    this.collectData();

    //提交信息
    var ajax = new $ax(Feng.ctxPath + "/cms_admin/update", function(data){
        Feng.success("修改成功!");
        window.parent.CmsAdmin.table.refresh();
        CmsAdminInfoDlg.close();
    },function(data){
        Feng.error("修改失败，请规范输入!");
    });
    ajax.set(this.cmsAdminInfoData);
    ajax.start();
}

$(function() {

});
