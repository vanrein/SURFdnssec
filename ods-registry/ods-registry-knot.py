# Backend code for ods-registry, using Knot DNS as signer



#
# Start of code, imports
#
import os


#
# Return the set of zone names
#
def zonenames ():
	#
	# Run knotc to retrieve zone names
	zlist = os.popen ('/usr/sbin/knotc conf-read zone.domain', 'r')
	#
	# Collect the zone names mentioned in the zone list
	workset = set ()
	for zln in zlist:
		zln = zln.rstrip ()
		if zln == 'OK':
			# Overcome inconsistent reporting habits of Knot DNS
			continue
		if zln [:14] != 'zone.domain = ':
			raise Exception ('Found something else than a zone.domain property after "knotc conf-read zone.domain"')
		work = zln [14:]
		if work [-1:] == '.':
			work = work [:-1]
		workset.add (work)
	if zlist.close () is not None:
		raise Exception ('Knot DNS not available for registry zone listing')
	return workset

#
# Signal having seen the DS (not required for Knot DNS)
#
def seen_ds (zone, kid):
	return 0

