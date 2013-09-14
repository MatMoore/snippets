#!/usr/bin/env python
"""
Dumb Archive eXtractor

Usage: dax.py file1 [file2...]
"""
import os
import subprocess
import sys
import re
import shutil
files = sys.argv[1:]

def extract_file(filename, dirpath):
	'''Extract an archive into its own directory'''
	rc = subprocess.call(['mkdir', '-p', dirpath])
	if rc:
		sys.exit(rc)
	os.chdir(dirpath)
	filename = os.path.join('..', filename)
	if filename.endswith('.zip'):
		rc = subprocess.call(['unzip', filename], stdout=sys.stdout, stderr=sys.stderr)
	else:
		rc = subprocess.call(['tar', '-x', '-v', '-f', filename], stdout=sys.stdout, stderr=sys.stderr)
		if rc:
			sys.exit(rc)
	os.chdir('..')

for filename in files:
	dirpath = '_' + re.sub(r'\.[^.]*$', '', filename).replace('.tar', '')
	if os.path.exists(dirpath):
		# WTF someone created a file here
		sys.exit(1)

	print 'Extracting into ' + dirpath
	extract_file(filename, dirpath)

	contents = os.listdir(dirpath)
	if len(contents) == 1 and os.path.isdir(os.path.join(dirpath, contents[0])):
		# Archive is packaged properly
		rootdir = contents[0]
		if os.path.exists(contents[0]):
			# TODO: compare existing directory and error if different
			# rsync --dry-run?
			if rootdir == dirpath:
				# Looks like we extracted this already LOL
				print rootdir + ' already exists: skipping'
				skip_file = True
			else:
				# Either we're extracting the same thing twice, or rootdir
				# is something stupid like 'src'
				# for now, just skip these as well.
				# TODO: avoid names matching certain patterns (use dirpath instead)
				print rootdir + ' already exists: skipping'
				skip_file = True
		else:
			print 'Found ' + contents[0]
			shutil.move(os.path.join(dirpath, contents[0]), '.')
		shutil.rmtree(dirpath)
	else:
		# Archive contains a bunch of crap
		if os.path.exists(dirpath[1:]):
			print dirpath[1:] + ' already exists: skipping'
			shutil.rmtree(dirpath)
		else:
			os.rename(dirpath, dirpath[1:])
