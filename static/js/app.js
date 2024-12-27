$(document).ready(function() {
    // 页面加载时将焦点放在输入框
    $('#user-input').focus();

    // 防止重复发送请求：按下发送按钮后禁用按钮，避免多次点击
    let isRequesting = false;

    // 监听回车键提交
    $('#user-input').keydown(function(event) {
        if (event.key === "Enter") {
            $('#send-btn').click();
        }
    });

    // 发送按钮点击事件
    $('#send-btn').click(function() {
        if (isRequesting) return;  // 如果正在请求中，则不再触发点击事件

        var userInput = $('#user-input').val().trim();
        if (userInput !== "") {
            appendMessage('您', userInput, 'user');
            $('#user-input').val("");  // 清空输入框

            // 显示加载提示
            appendLoadingMessage();

            // 设置请求状态为进行中
            isRequesting = true;

            // 发送请求到后端 Flask
            $.ajax({
                url: '/ask',
                type: 'POST',
                contentType: 'application/json',
                data: JSON.stringify({ 'user_input': userInput }),
                success: function(response) {
                    var botResponse = response.response;
                    appendMessage('OmniAI', botResponse, 'bot');
                    scrollToBottom();  // 滚动到底部

                    // 删除加载提示
                    removeLoadingMessage();
                },
                error: function(xhr, status, error) {
                    console.error("请求失败:", error);
                    appendMessage('OmniAI', "对不起，出现了错误，请稍后再试。", 'bot');
                    removeLoadingMessage();  // 删除加载提示
                },
                complete: function() {
                    // 请求完成，恢复按钮可用状态
                    isRequesting = false;
                }
            });
        }
    });

    // 向聊天框添加消息
    function appendMessage(sender, message, type) {
        var messageElement = $('<div class="message ' + type + '">')
            .html('<strong>' + sender + ':</strong> ' + message);
        $('#chat-box').append(messageElement);
        scrollToBottom();
    }

    // 向聊天框添加加载提示
    function appendLoadingMessage() {
        var loaderElement = $('<div id="loading-message" class="message bot">')
            .html('<strong>OmniAI:</strong> <span class="loading-text">正在思考中...</span>');
        $('#chat-box').append(loaderElement);
    }

    // 删除加载提示
    function removeLoadingMessage() {
        $('#loading-message').remove();  // 删除加载提示元素
    }

    // 滚动到聊天框底部
    function scrollToBottom() {
        var chatBox = $('#chat-box');
        // 只有在用户滚动到最底部时才自动滚动
        if (chatBox[0].scrollHeight - chatBox.scrollTop() === chatBox.outerHeight()) {
            chatBox.animate({ scrollTop: chatBox[0].scrollHeight }, 500);
        }
    }

    // 上传按钮点击事件
    $('#upload-btn').click(function() {
        $('#file-input').click();  // 点击按钮时触发文件选择框
    });

    // 文件选择变化时触发上传
    $('#file-input').change(function(event) {
        var fileInput = event.target;
        var file = fileInput.files[0];

        if (file) {
            var formData = new FormData();
            formData.append("file", file);

            // 发送文件到服务器
            $.ajax({
                url: '/upload',
                type: 'POST',
                data: formData,
                contentType: false,
                processData: false,
                success: function(response) {
                    console.log("文件上传成功", response);
                    // 显示上传成功提示框
                    $('#upload-success').fadeIn().addClass('fade-out').delay(3000).fadeOut();
                },
                error: function(xhr, status, error) {
                    console.error("文件上传失败", error);
                }
            });
        }
    });
});
