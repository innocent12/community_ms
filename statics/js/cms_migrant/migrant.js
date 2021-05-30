/**
 * 管理员管理初始化
 */
var CmsMigrant = {
    id: "CmsMigrantTable",	//表格id
    selectItem: null,		//选中的条目
    table: null,
    layerIndex: -1
};

/**
 * 初始化表格的列
 */
CmsMigrant.initColumn = function () {
    return [
        {field: 'selectItem', radio: true},
            {title: '序号', field: 'id', visible: true, align: 'center', valign: 'middle'},
            {title: '姓名', field: 'name', visible: true, align: 'center', valign: 'middle'},
            {title: '年龄', field: 'age', visible: true, align: 'center', valign: 'middle'},
            {title: '性别', field: 'sex', visible: true, align: 'center', valign: 'middle'},
            {title: '手机号', field: 'phone', visible: true, align: 'center', valign: 'middle'},
        {title: '人脸识别编号', field: 'bce_user_id', visible: true, align: 'center', valign: 'middle'},
        {title: '记录时间', field: 'log_time', visible: true, align: 'center', valign: 'middle'}
    ];
};

/**
 * 检查是否选中
 */
CmsMigrant.check = function () {
    var selected = $('#' + this.id).bootstrapTable('getSelections');
    if(selected.length == 0){
        Feng.info("请先选中表格中的某一记录！");
        return false;
    }else{
        CmsMigrant.selectItem = selected[0];
        return true;
    }
};

/**
 * 点击添加管理员
 */
CmsMigrant.openAddCmsMigrant = function () {
    var index = layer.open({
        type: 2,
        method: 'get',
        title: '添加管理员',
        area: ['800px', '420px'], //宽高
        fix: false, //不固定
        maxmin: true,
        content: Feng.ctxPath + '/cms_migrant/add'
    });
    this.layerIndex = index;
};

/**
 * 打开查看管理员详情
 */
CmsMigrant.openCmsMigrantDetail = function () {
    if (this.check()) {
        var index = layer.open({
            type: 2,
            title: '管理员详情',
            area: ['800px', '420px'], //宽高
            fix: false, //不固定
            maxmin: true,
            content: Feng.ctxPath + '/cms_migrant/edit/' + CmsMigrant.selectItem.id
        });
        this.layerIndex = index;
    }
};

/**
 * 删除管理员
 */
CmsMigrant.delete = function () {
    if (this.check()) {
        var ajax = new $ax(Feng.ctxPath + "/cms_migrant/delete", function (data) {
            Feng.success("删除成功!");
            CmsMigrant.table.refresh();
        }, function (data) {
            Feng.error("删除失败!" + data.responseJSON.message + "!");
        });
        ajax.set("cmsMigrantId",this.selectItem.id);
        ajax.start();
    }
};

$(function () {
    var defaultColunms = CmsMigrant.initColumn();
    var table = new BSTable(CmsMigrant.id, "/cms_migrant/list", defaultColunms);
    table.setPaginationType("client");
    CmsMigrant.table = table.init();
});
