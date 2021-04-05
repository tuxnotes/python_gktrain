# 用在哪里

# 注册

@route('index', methods=['GET','POST'])
def static_html():
    return render_template('index.html')

# 等效于
static_html = route('index', methods=['GET','POST'])(static_html)()

def route(rule, **options):
    def decorate(f):
        endpoint = options.pop('endpoint',None)
        # 使用类似字典的结构，以index为key，以method static_html 其他参数
        self.add_url_rule(rule, endpoint, f, **options)
        return f
    return decorate

######################
# 包装的形式用的最多
# 包装
def html_header(func):
    def decorate():
        return f'<html>{ func() }</html>'
    return decorate

def body_header(func):
    def decorate():
        return f'<body>{ func() }</body>'
    return decorate

@html_header
@body_header
def content():
    return 'Hello World!'

content()