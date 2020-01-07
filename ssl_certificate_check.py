from cores.certificate import garther, cert, export


if __name__ == '__main__':
	

	report_file = '/home/hungdnv/Documents/Python-Check-SSL-Certificate/report.csv'
	domains_file = '/home/hungdnv/Documents/Python-Check-SSL-Certificate/cores/data/domains.conf'
	
	packages = []
	domains = [domain.rstrip('\n') for domain in open(domains_file)]

	for domain in domains:
		c = cert.Certificate(domain)
		c.get()
		package = {
			"domain": domain,
			"notBefore": c.notBefore(),
			"notAfter": c.notAfter(),
			"remaining": c.remaining(),
			"exception": c.get_exception(),
		}
		packages.append(package)

	#print (packages)


	export.csv_output(report_file, packages)
	export.table(report_file)

