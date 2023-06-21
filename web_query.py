from flask import Flask, render_template, request
from llama_index import StorageContext, load_index_from_storage

app = Flask(__name__)

# rebuild storage context
storage_context = StorageContext.from_defaults(persist_dir='./storage')
# load index
index = load_index_from_storage(storage_context)
# Instantiate your query engine here, e.g.:
query_engine = index.as_query_engine()

@app.route('/', methods=['GET', 'POST'])
def index():
    result = ''
    if request.method == 'POST':
        question = request.form.get('question')
        if question[-1] != '?':
            question += '?'
        result = query_engine.query(question)
    return render_template('index.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)
