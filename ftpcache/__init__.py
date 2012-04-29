#!/usr/bin/env
"""
FTP Cache

Mirrors a directory of a ftp server locally.  Only downloading new files.

"""

from ftplib import FTP

class FTPMirror:
	
	def __init__(self,url,localdir):
		"""Constructor
		
		Args:
		url - ftp url to mirror
		localdir - directory to keep in sync
		"""
		pass

	def __getremoteinfo(self):
		"""Get listing of remote file metadata.  Store in local metadata objects"""
		pass

	def __getlocalinfo(self):
		"""Get listing of local file metadata.  Store in local metadata ojects"""
		pass

	def mirror(self):
		"""Mirror """
		self.__getremoteinfo()
		self.__getlocalinfo()

		# Remove local files that are no longer present remotely

		# Update files that are newer on the remote
