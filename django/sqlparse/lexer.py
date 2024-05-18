import re
from threading import Lock
from io import TextIOBase

from django.sqlparse import tokens, keywords
from django.sqlparse.utils import consume


class Lexer:
    _default_instance = None
    _lock = Lock()

    @classmethod
    def get_default_instance(cls):
        """Returns the lexer instance used internally
        by the sqlparse core functions."""
        with cls._lock:
            if cls._default_instance is None:
                cls._default_instance = cls()
                cls._default_instance.default_initialization()
        return cls._default_instance

    def default_initialization(self):
        self.clear()
        self.set_SQL_REGEX(keywords.SQL_REGEX)
        self.add_keywords(keywords.KEYWORDS_COMMON)
        self.add_keywords(keywords.KEYWORDS_ORACLE)
        self.add_keywords(keywords.KEYWORDS_MYSQL)
        self.add_keywords(keywords.KEYWORDS_PLPGSQL)
        self.add_keywords(keywords.KEYWORDS_HQL)
        self.add_keywords(keywords.KEYWORDS_MSACCESS)
        self.add_keywords(keywords.KEYWORDS_SNOWFLAKE)
        self.add_keywords(keywords.KEYWORDS_BIGQUERY)
        self.add_keywords(keywords.KEYWORDS)

    def clear(self):
        self._SQL_REGEX = []
        self._keywords = []

    def set_SQL_REGEX(self, SQL_REGEX):
        FLAGS = re.IGNORECASE | re.UNICODE
        self._SQL_REGEX = [
            (re.compile(rx, FLAGS).match, tt)
            for rx, tt in SQL_REGEX
        ]

    def add_keywords(self, keywords):
        self._keywords.append(keywords)

    def is_keyword(self, value):
        val = value.upper()
        for kwdict in self._keywords:
            if val in kwdict:
                return kwdict[val], value
        else:
            return tokens.Name, value

    def get_tokens(self, text, encoding=None):
        if isinstance(text, TextIOBase):
            text = text.read()

        if isinstance(text, str):
            pass
        elif isinstance(text, bytes):
            if encoding:
                text = text.decode(encoding)
            else:
                try:
                    text = text.decode('utf-8')
                except UnicodeDecodeError:
                    text = text.decode('unicode-escape')
        else:
            raise TypeError("Expected text or file-like object, got {!r}".
                            format(type(text)))

        iterable = enumerate(text)
        for pos, char in iterable:
            for rexmatch, action in self._SQL_REGEX:
                m = rexmatch(text, pos)

                if not m:
                    continue
                elif isinstance(action, tokens._TokenType):
                    yield action, m.group()
                elif action is keywords.PROCESS_AS_KEYWORD:
                    yield self.is_keyword(m.group())

                consume(iterable, m.end() - pos - 1)
                break
            else:
                yield tokens.Error, char


def tokenize(sql, encoding=None):
    return Lexer.get_default_instance().get_tokens(sql, encoding)
