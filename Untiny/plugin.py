###
# Copyright (c) 2012, Valentin Lorentz
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are met:
#
#   * Redistributions of source code must retain the above copyright notice,
#     this list of conditions, and the following disclaimer.
#   * Redistributions in binary form must reproduce the above copyright notice,
#     this list of conditions, and the following disclaimer in the
#     documentation and/or other materials provided with the distribution.
#   * Neither the name of the author of this software nor the name of
#     contributors to this software may be used to endorse or promote products
#     derived from this software without specific prior written consent.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
# AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
# IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE
# ARE DISCLAIMED.  IN NO EVENT SHALL THE COPYRIGHT OWNER OR CONTRIBUTORS BE
# LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR
# CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF
# SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS
# INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN
# CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE)
# ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
# POSSIBILITY OF SUCH DAMAGE.

###

import json

import supybot.utils as utils
from supybot.commands import *
import supybot.plugins as plugins
import supybot.ircutils as ircutils
from supybot.utils.web import getUrlFd
import supybot.callbacks as callbacks
from supybot.i18n import PluginInternationalization, internationalizeDocstring

_ = PluginInternationalization('Untiny')

@internationalizeDocstring
class Untiny(callbacks.Plugin):
    """Add the help for "@plugin help Untiny" here
    This should describe *how* to use this plugin."""
    @internationalizeDocstring
    def untiny(self, irc, msg, args, url):
        """<url>

        Return the whole URL for a tiny URL."""
        data = json.load(getUrlFd(self.registryValue('service') % url))
        if 'org_url' in data:
            irc.reply(data['org_url'])
        elif 'error' in data:
            num, msg = data['error']
            messages = {
                    '0': _('Invalid URL'),
                    '1': _('Unsupported tinyurl service'),
                    '2': _('Connection to tinyurl service failed'),
                    '3': _('Unable to get the original URL'),
                    }
            irc.error(messages[num])
    untiny = wrap(untiny, ['text'])


Class = Untiny


# vim:set shiftwidth=4 softtabstop=4 expandtab textwidth=79:
