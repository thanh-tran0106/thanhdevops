# myapp/sftp_storage.py

import paramiko
from storages.backends.sftpstorage import SFTPStorage
import logging

logger = logging.getLogger(__name__)

class CustomSFTPStorage(SFTPStorage):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.client = self._get_sftp_client()

    def _get_sftp_client(self):
        """Create an SFTP client with custom host key policies."""
        logger.debug("Connecting to SFTP server at %s:%s", self.host, self.port)
        transport = paramiko.Transport((self.host, self.port))
        transport.connect(username=self.username, password=self.password)
        sftp = paramiko.SFTPClient.from_transport(transport)
        sftp.load_system_host_keys()
        sftp.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        return sftp

    def _open(self, name, mode='rb'):
        """Open a file on the SFTP server."""
        return self.client.open(name, mode)

    def _save(self, name, content):
        """Save a file to the SFTP server."""
        with self.client.open(name, 'wb') as f:
            for chunk in content.chunks():
                f.write(chunk)
        return name

    def delete(self, name):
        """Delete a file from the SFTP server."""
        self.client.remove(name)

    def exists(self, name):
        """Check if a file exists on the SFTP server."""
        try:
            self.client.stat(name)
            return True
        except FileNotFoundError:
            return False

    def url(self, name):
        """Return the URL of the file."""
        return f'{self.base_url}/{name}'
