from flask import Flask, render_template, request, jsonify
from agent.interaction import Interaction
import os
from werkzeug.utils import secure_filename

# 初始化 Flask 应用
app = Flask(__name__)

# 设置上传文件的存储路径和允许的文件类型
UPLOAD_FOLDER = os.path.join(os.path.dirname(__file__), 'docs')
ALLOWED_EXTENSIONS = {'pdf', 'png', 'jpg', 'jpeg', 'txt', 'docx', 'xlsx'}

# 配置上传文件夹
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# 初始化 Interaction 类，用于处理与 AI 的交互
knowledge_file = os.path.join(os.path.dirname(__file__), 'data', 'knowledge.json')
interaction = Interaction(knowledge_file=knowledge_file)


# 检查文件扩展名是否合法
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


# 渲染首页
@app.route('/')
def index():
    return render_template('index.html')


# 处理用户输入并获取 AI 的回复
@app.route('/ask', methods=['POST'])
def ask():
    user_input = request.json.get('user_input')
    if not user_input:
        return jsonify({"error": "没有输入内容"}), 400

    # 获取 AI 的回复
    response = interaction.interact(user_input)

    return jsonify({'response': response})


# 处理文件上传
@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return jsonify({'error': '没有选择文件'}), 400

    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': '没有选择文件'}), 400

    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(filepath)
        return jsonify({'message': f'文件上传成功，保存路径: {filepath}'}), 200
    else:
        return jsonify({'error': '不支持的文件类型'}), 400


if __name__ == '__main__':
    app.run(debug=True)
