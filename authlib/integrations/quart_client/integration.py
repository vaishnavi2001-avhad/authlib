from quart import current_app
# from quart.signals import Signal
from blinker import Signal

from ..base_client import FrameworkIntegration

# _signal = Signal()
# token_update = _signal.signal('token_update')
token_update = Signal('token_update')

class QuartIntegration(FrameworkIntegration):
    def update_token(self, token, refresh_token=None, access_token=None):
        token_update.send(
            current_app,
            name=self.name,
            token=token,
            refresh_token=refresh_token,
            access_token=access_token,
        )

    @staticmethod
    def load_config(oauth, name, params):
        rv = {}
        for k in params:
            conf_key = f'{name}_{k}'.upper()
            v = oauth.app.config.get(conf_key, None)
            if v is not None:
                rv[k] = v
        return rv