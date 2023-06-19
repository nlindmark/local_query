'''
This file contains a simple shell for querying your index.
'''

import cmd
from llama_index import StorageContext, load_index_from_storage


class QueryShell(cmd.Cmd):
    '''
    A simple shell for querying your index.
    '''
    prompt = '> '

    def __init__(self, engine):
        super().__init__()
        self.query_engine = engine

    def do_query(self, line):
        """Type "query <question>" to make a query."""
        if line[-1] != '?':
            line += '?'
        result = self.query_engine.query(line)
        print(f'Result: {result}')

    do_q = do_query

    def do_quit(self):
        """Type "quit" to exit."""
        return True

if __name__ == '__main__':
    # rebuild storage context
    storage_context = StorageContext.from_defaults(persist_dir='./storage')
    # load index
    index = load_index_from_storage(storage_context)
    # Instantiate your query engine here, e.g.:
    query_engine = index.as_query_engine()

    # Pass the query engine to your shell
    shell = QueryShell(query_engine)
    shell.cmdloop()
