

class MARKDOWN(object):
    """
    Will be used to write markdown reports.
    """

    def __init__(self):
        pass

    def separator(self):
        """"""
        return '**********'

    def title_lvl_1(self, string):
        """"""
        return '# {}'.format(string)

    def title_lvl_2(self, string):
        """"""
        return '## {}'.format(string)

    def title_lvl_3(self, string):
        """"""
        return '### {}'.format(string)

    def itemize_list(self, list_to_itemize):
        """"""
        return '\n-'.join(list_to_itemize)
