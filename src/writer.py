

class MARKDOWN(object):
    """
    Will be used to write markdown reports.
    """

    def __init__(self):
        pass


    def write_string(self, string, file_name):
        """"""
        with open(file_name, 'a') as handler:
            handler.write('{}\n\n'.format(string))


    def separator(self):
        """"""
        return '**********\n'


    def title_lvl_1(self, string):
        """"""
        return '# {}\n'.format(string)


    def title_lvl_2(self, string):
        """"""
        return '## {}\n'.format(string)

    def write_title_lvl_2(self, string, file_name):
        """"""
        with open(file_name, 'a') as handler:
            handler.write('## {}\n\n'.format(string))


    def title_lvl_3(self, string):
        """"""
        return '### {}\n'.format(string)

    def write_title_lvl_3(self, string, file_name):
        """"""
        with open(file_name, 'a') as handler:
            handler.write('### {}\n\n'.format(string))


    def title_lvl_4(self, string):
        """"""
        return '#### {}\n'.format(string)

    def write_title_lvl_4(self, string, file_name):
        """"""
        with open(file_name, 'a') as handler:
            handler.write('#### {}\n\n'.format(string))


    def itemize_list(self, list_to_itemize):
        """"""
        return '- ' + '\n- '.join(list_to_itemize) + '\n'

    def write_itemize_list(self, list_to_itemize, file_name):
        """"""
        with open(file_name, 'a') as handler:
            handler.write('- ' + '\n- '.join(list_to_itemize) + '\n\n')
