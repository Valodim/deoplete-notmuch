import re
import subprocess
from subprocess import CalledProcessError
from .base import Base


class Source(Base):
    COLON_PATTERN = re.compile(r':\s?')
    COMMA_PATTERN = re.compile(r'.+,\s?')
    HEADER_PATTERN = re.compile(r'^(Bcc|Cc|From|Reply-To|To):(\s?|.+,\s?)')

    def __init__(self, vim):
        super().__init__(vim)

        self.rank = 75  # default is 100, give deoplete-abook priority
        self.name = 'notmuch'
        self.mark = ''
        self.min_pattern_length = 0
        self.filetypes = ['mail', 'notmuch-compose']
        self.matchers = ['matcher_length', 'matcher_full_fuzzy']
        self.is_volatile = False
        self.max_candidates = 10000
        self.addresscache = None

    def on_init(self, context):
        self.command = context['vars'].get('deoplete#sources#notmuch#command',
                                           ['notmuch', 'address',
                                            '--format=text',
                                            '--deduplicate=address',
                                            '*' ])

    def get_complete_position(self, context):
        colon = self.COLON_PATTERN.search(context['input'])
        comma = self.COMMA_PATTERN.search(context['input'])
        return max(colon.end() if colon is not None else -1,
                   comma.end() if comma is not None else -1)

    def gather_candidates(self, context):
        if self.HEADER_PATTERN.search(context['input']) is None:
            return

        if self.addresscache is None:
            try:
                command_results = subprocess.check_output(self.command, universal_newlines=True).split('\n')
            except CalledProcessError:
                return

            self.addresscache = list(command_results)

        return self.addresscache
