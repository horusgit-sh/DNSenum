#!/usr/bin/env python3

import dns.zone as dz
import dns.query as dq
import dns.resolver as dr
import argparse

NS = dr.Resolver()

# Target domain
Domain = 'inlanefreight.com'

NS.nameservers = ['ns1.inlanefreight.com', 'ns2.inlanefreight.com']

Subdomains = []

def AXFR(domain, nameserver):

        try:
                axfr = dz.from_xfr(dq.xfr(nameserver, domain))

                if axfr:
                        print('[*] Successful Zone Transfer from {}'.format(nameserver))

                        for record in axfr:
                            sub = '{}.{}'.format(record.to_text(), domain)
                            if sub not in Subdomains:
                                Subdomains.append(sub)

        except Exception as error:
                print(error)
                pass

if __name__=="__main__":

        for nameserver in NS.nameservers:

                AXFR(Domain, nameserver)

        if Subdomains is not None:
                print('-------- Found Subdomains:')

                for subdomain in Subdomains:
                        print('{}'.format(subdomain))

        else:
                print('No subdomains found.')
                exit()         