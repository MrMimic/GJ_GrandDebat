

class MARKDOWN(object):
    """
    Will be used to write markdown reports.
    """

    def __init__(self):
        pass


    def write_blank_line(self, file_name):
        with open(file_name, 'a') as handler:
            handler.write('\n')


    def write_string(self, string, file_name):
        """"""
        with open(file_name, 'a') as handler:
            handler.write('{}\n\n'.format(string))

    def separator(self):
        """"""
        return '**********\n'

    def include_image(self, image_path, alt_text, file_name):
        """"""
        with open(file_name, 'a') as handler:
            handler.write('![{}]({})\n\n'.format(alt_text, image_path))

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

    def draw_table(self, header, data, file_name):
        """"""

        string = ''
        header_string = '|{}|'.format(('|').join(header))
        string = '{}\n{}'.format(string, header_string)
        formatter_string = '|{}|'.format(('|').join(['--' for head in header]))
        string = '{}\n{}'.format(string, formatter_string)

        for line in data:
            line_string = '|{}|'.format(('|').join([str(item) for item in line]))
            string = '{}\n{}'.format(string, line_string)

        string = '{}\n\n'.format(string)

        with open(file_name, 'a') as handler:
            handler.write(string)
