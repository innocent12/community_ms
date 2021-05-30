/**
 * 管理员管理初始化
 */
var CmsCheckLog = {
    id: "CmsCheckLogTable",	//表格id
    selectItem: null,		//选中的条目
    table: null,
    layerIndex: -1
};

/**
 * 初始化表格的列
 */
CmsCheckLog.initColumn = function () {
    return [
        {field: 'selectItem', radio: true},
            {title: '序号', field: 'id', visible: true, align: 'center', valign: 'middle'},
            {title: '姓名', field: 'name', visible: true, align: 'center', valign: 'middle'},
            {title: '用户编号', field: 'user_id', visible: true, align: 'center', valign: 'middle'},
            {title: '职业', field: 'user_type', visible: true, align: 'center', valign: 'middle'},
            {title: '温度', field: 'temperature', visible: true, align: 'center', valign: 'middle'},
            {title: '登记时间', field: 'sign_time', visible: true, align: 'center', valign: 'middle'},
            {title: '事宜', field: 'matter', visible: true, align: 'center', valign: 'middle'},
        {title: '备注', field: 'comment', visible: true, align: 'center', valign: 'middle'}
    ];
};

/**
 * 检查是否选中
 */
CmsCheckLog.check = function () {
    var selected = $('#' + this.id).bootstrapTable('getSelections');
    if(selected.length == 0){
        Feng.info("请先选中表格中的某一记录！");
        return false;
    }else{
        CmsCheckLog.selectItem = selected[0];
        return true;
    }
};

/**
 * 点击添加出入记录
 */
CmsCheckLog.openAddCmsCheckLog = function (params) {
    var test = "12563"
    var index = layer.open({
        type: 2,
        method: 'get',
        title: '出入登记',
        area: ['800px', '420px'], //宽高
        fix: false, //不固定
        maxmin: true,
        content: Feng.ctxPath + '/cms_check/add',
        success: function (layero, i) {
            if(params !== undefined){
                var body = layer.getChildFrame('body', i)
                body.find('#user_id').val(params['user_id'])
                body.find('#name').val(params['name'])
                body.find('#user_type').val(params['user_type'])
            }
        }
    });
    this.layerIndex = index;
};

/**
 * 打开查看管理员详情
 */
CmsCheckLog.openCmsCheckLogDetail = function () {
    if (this.check()) {
        var index = layer.open({
            type: 2,
            title: '管理员详情',
            area: ['800px', '420px'], //宽高
            fix: false, //不固定
            maxmin: true,
            content: Feng.ctxPath + '/cms_check/edit/' + CmsCheckLog.selectItem.id
        });
        this.layerIndex = index;
    }
};

/**
 * 删除管理员
 */
CmsCheckLog.delete = function () {
    if (this.check()) {
        var ajax = new $ax(Feng.ctxPath + "/cms_check/delete", function (data) {
            Feng.success("删除成功!");
            CmsCheckLog.table.refresh();
        }, function (data) {
            Feng.error("删除失败!");
        });
        ajax.set("cmsCheckLogId",this.selectItem.id);
        ajax.start();
    }
};

/**
 * 启动摄像头
 */
CmsCheckLog.openCapture = function (){
    var index = layer.open({
        type: 2,
        method: 'get',
        title: '人脸识别',
        area: ['1100px', '520px'], //宽高
        fix: false, //不固定
        maxmin: true,
        content: Feng.ctxPath + '/cms_face/video'
    });
    this.layerIndex = index;
};



$(function () {
    var defaultColumns = CmsCheckLog.initColumn();
    var table = new BSTable(CmsCheckLog.id, "/cms_check/list", defaultColumns);
    table.setPaginationType("client");
    CmsCheckLog.table = table.init();
});
