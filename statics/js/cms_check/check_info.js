/**
 * 初始化管理员详情对话框
 */
var CmsCheckLogInfoDlg = {
    cmsCheckLogInfoData: {}
};

/**
 * 清除数据
 */
CmsCheckLogInfoDlg.clearData = function () {
    this.cmsCheckLogInfoData = {};
}

/**
 * 设置对话框中的数据
 *
 * @param key 数据的名称
 * @param val 数据的具体值
 */
CmsCheckLogInfoDlg.set = function (key, val) {
    this.cmsCheckLogInfoData[key] = (typeof val == "undefined") ? $("#" + key).val() : val;
    return this;
}

/**
 * 设置对话框中的数据
 *
 * @param key 数据的名称
 * @param val 数据的具体值
 */
CmsCheckLogInfoDlg.get = function (key) {
    return $("#" + key).val();
}

/**
 * 关闭此对话框
 */
CmsCheckLogInfoDlg.close = function () {
    parent.layer.close(window.parent.CmsCheckLog.layerIndex);
}

/**
 * 收集数据
 */
CmsCheckLogInfoDlg.collectData = function () {
    this
        .set('name')
        .set('temperature')
        .set('matter')
        .set('comment')
        .set('user_type')
        .set('user_id');
}

/**
 * 提交添加
 */
CmsCheckLogInfoDlg.addSubmit = function () {

    this.clearData();
    this.collectData();

    //提交信息
    var ajax = new $ax(Feng.ctxPath + "/cms_check/save", function (data) {
        Feng.success("欢迎进入本小区，请出示绿码!");
        window.parent.CmsCheckLog.table.refresh();
        CmsCheckLogInfoDlg.close();
    }, function (data) {
        Feng.error("添加失败,请规范输入!");
    });
    ajax.set(this.cmsCheckLogInfoData);
    ajax.start();
}

/**
 * 提交修改
 */
CmsCheckLogInfoDlg.editSubmit = function () {

    this.clearData();
    this.collectData();

    //提交信息
    var ajax = new $ax(Feng.ctxPath + "/cms_check/update", function (data) {
        Feng.success("修改成功!");
        window.parent.CmsCheckLog.table.refresh();
        CmsCheckLogInfoDlg.close();
    }, function (data) {
        Feng.error("修改失败，请规范输入!");
    });
    ajax.set(this.cmsCheckLogInfoData);
    ajax.start();
}

$(function () {

});
