from country_list import available_languages, countries_for_language


class Enumerations:
    @property
    def media_types(self):
        return {
            'json': {
                'names': ['application/json'],
                'extensions': ['.json'],
                'title': 'JavaScript Object Notation'
            },
            'xml': {
                'names': ['application/xml', 'text/xml'],
                'extensions': ['.xml'],
                'title': 'Extensible Markup Language'
            },
            'pdf': {
                'names': ['application/pdf'],
                'extensions': ['.pdf'],
                'title': 'Portable Document Format'
            },
            'doc': {
                'names': ['application/msword'],
                'extensions': ['.doc'],
                'title': 'Word Processing Document'
            },
            'docx': {
                'names': ['application/vnd.openxmlformats-officedocument.wordprocessingml.document'],
                'extensions': ['.docx'],
                'title': 'Open Office Word Processing Document'
            },
            'odt': {
                'names': ['application/vnd.oasis.opendocument.text'],
                'extensions': ['.odt'],
                'title': 'Open Document Word Processing Format'
            },
            'htm': {
                'names': ['text/html'],
                'extensions': ['.html', '.htm'],
                'title': 'Hypertext Markup Language'
            },
            'csv': {
                'names': ['text/csv'],
                'extensions': ['.csv', '.tsv'],
                'title': 'Comma Separated Values'
            },
            'txt': {
                'names': ['text/plain'],
                'extensions': ['.txt'],
                'title': 'Plain Text'
            },
        }

    @property
    def languages(self):
        return available_languages()

    def countries(self, language_code:str):
        return countries_for_language(language_code)
