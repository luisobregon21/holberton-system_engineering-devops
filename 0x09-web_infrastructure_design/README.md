# 0x09. Web infrastructure design
## Concepts: 
  * Network basics
  * Server
  * Web server
  * DNS
  * Load balancer
  * Monitoring
  * What is a database
  * What’s the difference between a web server and an app server?
  * DNS record types[]()
  * Single point of failure
  * How to avoid downtime when deploying new code
  * High availability cluster (active-active/active-passive)
  * What is HTTPS
  * What is a firewall

## Notes On Concepts

### **DNS**  
  * DNS is, in simple words, the technology that translates text-based domain names into machine-adapted numerical IPs 
  * When you type a websites name on your web browser, like "foobar.com”, the computer first searches in the **web browser DNS** cache if it knows what IP address “foobar.com” is.  Then if the web browser doesn’t know, it searches in the **Operating System** cache. If that also fails, the request for the IP address that belongs to “foobar.com” is sent to the resolver.
 * ** The RESOLVER ** is outside of your computer, the resolver checks on its cache to see if it knows the IP address for “foobar.com”, if it’s not on its cache it goes to the **“ROOT”.**
  *  All Resolvers must know how to **locate the root server**, this server knows how to find the ".COM", which is a TOP-LEVEL-DOMAIN(TLD).
  *  After the resolver visits the ROOT it stores the information of said request so it doesn’t have to do it again.
* Once it reaches the TLD for ".com" domains, if that specific TLD doesn’t know the answer, then it gives the resolver the name servers for that “foobar.com” website. The resolver stores the name servers for later. So it doesn’t need to do all of these requests all over again.
* Once the resolver reaches the name server, the Resolver finds its answer to which IP address corresponds to “foobar.com” because when you register a new domain, like “foobar.com” you have to manually register the name and communicate it to the TLD registry.

## DNS Drawing
![](images/DNS.jpeg)
