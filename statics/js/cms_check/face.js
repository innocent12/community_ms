$(function () {

    // 完成上传   图片为base64
    $("#main__submit").click(function () {
        var ahis = $(this);
        ahis.hide();
        var d = {}
        $.ajax({
            url: "/cms_face/validate_face",
            data: {image: cropper.getDataURL()},
            method: "post",
            async: false,
            dataType: "json",
            success: function (data) {
                ahis.show();
                ahis.html("OK");
                // 解析图片获得的用户信息
                d = data
            }
        });
        addUser(d);
    })

    // 用户信息处理
    function addUser(data) {
        if (data.message === '照片不合格') {
            layer.msg(data.message, {icon: 2})
            return
        } else if (data.message === '人员登记') {
            var t_index = layer.open({
                content: "系统没有记录该用户信息，请进行人员信息登记",
                btn: ['业主登记', '外来人员登记', '取消'],
                yes: function (index, layero) {
                    // 业主登记页面跳转
                    layer.open({
                        type: 2,
                        method: 'get',
                        title: '业主登记',
                        area: ['800px', '420px'], //宽高
                        fix: false, //不固定
                        maxmin: true,
                        content: Feng.ctxPath + '/cms_resident/add',
                        success: function (layero, i) {
                            var body = layer.getChildFrame('body', i)
                            body.find('#bce_user_id').val(data.bce_user_id)
                            body.find('#user_type').val('业主')
                        },
                        end: function () {
                            if (localStorage.getItem('type') !== null) {
                                addLog();
                            }
                        }
                    });
                },
                btn2: function (index, layero) {
                    // 外来人员登记页面跳转
                    layer.open({
                        type: 2,
                        method: 'get',
                        title: '外来人员登记',
                        area: ['800px', '420px'], //宽高
                        fix: false, //不固定
                        maxmin: true,
                        content: Feng.ctxPath + '/cms_migrant/add',
                        success: function (layero, i) {
                            var body = layer.getChildFrame('body', i)
                            body.find('#bce_user_id').val(data.bce_user_id)
                        },
                        end: function () {
                            if (localStorage.getItem('type') !== null) {
                                addLog();
                            }
                        }
                    });
                },
                btn3: function () {
                    // 取消
                }
            });
            // parent.layer.close(t_index)
        } else {
            if (data.message === '业主'){
                var str = "姓名：" + data.name + ",上次体温：" + data.temperature +
                    "<br>住址：" + data.address +
                    "<br>手机号:" + data.phone

            }else if (data.message === '外来人员'){
                var str = "姓名：" + data.name + ",性别：" + data.sex +
                    "<br>手机号:" + data.phone
            }
            layer.open({
                content: str,
                title: data.message+'信息',
                area: ['200px', '220px'],
                yes: function () {
                    var index1 = parent.layer.getFrameIndex(window.name); //先得到当前iframe层的索引
                    parent.layer.close(index1); //再执行关闭
                    data['user_type'] = '业主'
                    window.parent.CmsCheckLog.openAddCmsCheckLog(data)
                }
            });
        }
    }

    // 添加Log记录
    function addLog() {
        //  关闭信息记录层
        var index1 = parent.layer.getFrameIndex(window.name); //先得到当前iframe层的索引
        parent.layer.close(index1); //再执行关闭
        if (localStorage.getItem('type') !== null) {
            // 关闭face页面
            console.log(localStorage.getItem('type'))
            // 关闭face页面
            var index1 = parent.layer.getFrameIndex(window.name); //先得到当前iframe层的索引
            parent.layer.close(index1); //再执行关闭
            var params = {
                'type': localStorage.getItem('type'),
                'name': localStorage.getItem('name'), 'user_id': localStorage.getItem('user_id')
            };
            window.parent.CmsCheckLog.openAddCmsCheckLog(params)
            localStorage.clear()
        }
    }

    Webcam.set({
        width: 320,
        height: 240,
        image_format: 'jpeg',
        jpeg_quality: 90
    });

    $("#open_media").click(function () {
        Webcam.attach("#open-power")
    })

    const options = {
        thumbBox: '.main__upload-left--thumbBox',
        spinner: '.main__upload-left--spinner',
        imgSrc: ''
    }
    let cropper = null;

    $("#main__confirm").click(function () {
        Webcam.freeze();
        Webcam.snap(function (data_uri) {
            options.imgSrc = data_uri;
            //注册裁剪组件
            cropper = $('#main__photo').cropbox(options);
            var onloadFn = cropper.image.onload;
            cropper.image.onload = function () {
                onloadFn();
                //初始化头像
                imgHtml();
            }
        });
    })

    $("#main__rop").on('click', function () {
        imgHtml();
    })

    $('#main__boost').on('click', function () {
        cropper.zoomIn();
    })

    $('#main__lessen').on('click', function () {
        cropper.zoomOut();
    })

    function imgHtml() {
        var img = cropper.getDataURL();
        var imgObj = $('.main__upload-right');
        imgObj.html('');
        imgObj.append('<img class="main__lager-photo" src="' + img + '" align="absmiddle"><p>180px*180px</p>');
        imgObj.append('<img class="main__small-photo" src="' + img + '" align="absmiddle"><p>128px*128px</p>');
        imgObj.append('<img class="main__mini-photo" src="' + img + '" align="absmiddle"><p>64px*64px</p>');
        $('#main__submit').show();
    }
});