# lambda-k8s
Access k8s API from AWS Lambda

Example code to test read-only access to k8s API from an AWS Lambda function.

Code: Python with official Kubernetes Python client library
Authentication: bearer's token
Environment: k8s runs inside a VPC

Test by running from a shell:
```bash
$ export K8SAPI_URL=https://api.k8s.my.domain
$ export K8SAPI_TOKEN=bearers-token
$ python main.py 
bearer config set
new api instance created
/opt/conda/lib/python3.6/site-packages/urllib3/connectionpool.py:858: InsecureRequestWarning: Unverified HTTPS request is being made. Adding certificate verification is strongly advised. See: https://urllib3.readthedocs.io/en/latest/advanced-usage.html#ssl-warnings
  InsecureRequestWarning)
pod list obtained for namespace default
busybox-test	Running	100.xxx.xxx.xxx
jenkins-b4c9ff566-hkpnz	Running	100.xxx.xxx.xxx
lego-kube-lego-7f4cd5c859-zwpv8	Running	100.xxx.xxx.xxx
my-nginx-nginx-ingress-controller-7b5c9566d4-hkclk	Running	100.xxx.xxx.xxx
my-nginx-nginx-ingress-default-backend-69fbf794d9-pm69w	Running	100.xxx.xxx.xxx
$
```


