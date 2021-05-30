/**
 * 管理员管理初始化
 */
var Admin = {
    id: "CmsAdminTable",	//表格id
    selectItem: null,		//选中的条目
    table: null,
    layerIndex: -1
};

/**
 * 初始化表格的列
 */
Admin.initColumn = function () {
    return [
        {field: 'selectItem', radio: true},
            {title: '序号', field: 'id', visible: true, align: 'center', valign: 'middle'},
            {title: '用户名', field: 'name', visible: true, align: 'center', valign: 'middle'},
            {title: '密码', field: 'password', visible: true, align: 'center', valign: 'middle'},
        {title: '创建时间', field: 'create_time', visible: true, align: 'center', valign: 'middle'}
    ];
};

/**
 * 检查是否选中
 */
Admin.check = function () {
    var selected = $('#' + this.id).bootstrapTable('getSelections');
    if(selected.length == 0){
        Feng.info("请先选中表格中的某一记录！");
        return false;
    }else{
        Admin.selectItem = selected[0];
        return true;
    }
};

/**
 * 点击添加管理员
 */
Admin.openAddCmsAdmin = function () {
    var index = layer.open({
        type: 2,
        method: 'get',
        title: '添加管理员',
        area: ['800px', '420px'], //宽高
        fix: false, //不固定
        maxmin: true,
        content: Feng.ctxPath + '/cms_admin/cmsAdmin_add'
    });
    this.layerIndex = index;
};

/**
 * 打开查看管理员详情
 */
Admin.openCmsAdminDetail = function () {
    if (this.check()) {
        var index = layer.open({
            type: 2,
            title: '管理员详情',
            area: ['800px', '420px'], //宽高
            fix: false, //不固定
            maxmin: true,
            content: Feng.ctxPath + '/cms_admin/cmsAdmin_edit/' + Admin.selectItem.id
        });
        this.layerIndex = index;
    }
};

/**
 * 删除管理员
 */
Admin.delete = function () {
    if (this.check()) {
        var ajax = new $ax(Feng.ctxPath + "/cms_admin/delete", function (data) {
            Feng.success("删除成功!");
            Admin.table.refresh();
        }, function (data) {
            Feng.error("删除失败!" + data.responseJSON.message + "!");
        });
        ajax.set("cmsAdminId",this.selectItem.id);
        ajax.start();
    }
};

$(function () {
    var defaultColunms = Admin.initColumn();
    var table = new BSTable(Admin.id, "/cms_admin/list", defaultColunms);
    table.setPaginationType("client");
    Admin.table = table.init();
});
