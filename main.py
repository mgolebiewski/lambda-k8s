'''
AWS Lambda function to list k8s pods running in default namespace

Authentication to k8s API is using bearer's token
The token is retrieved from AWS System Manager Parameter Store
k8s API access is restricted to its VPC

Boiler plate python Lambda code copied from:

https://aws.amazon.com/blogs/compute/sharing-secrets-with-aws-lambda-using-aws-systems-manager-parameter-store/

'''

import os
import kubernetes.client

url = os.environ['K8SAPI_URL']
token = os.environ['K8SAPI_TOKEN']

def list_pods(namespace="default"):
    """
    config for k8s client
    """
    k8sconf = kubernetes.client.Configuration()
    k8sconf.api_key['authorization'] = token
    k8sconf.api_key_prefix['authorization'] = 'Bearer'
    k8sconf.host = url
    # we've got no ca cert to verify against
    k8sconf.verify_ssl = False
    k8sconf.assert_hostname = False
    print ("bearer config set")

    # get new API object using our configuration
    api_instance = kubernetes.client.CoreV1Api(kubernetes.client.ApiClient(k8sconf))
    print ("new api instance created")

    # and call it
    pod_list = api_instance.list_namespaced_pod(namespace)
    print ("pod list obtained for namespace "+namespace)

    # print the results so that we know it worked
    for pod in pod_list.items:
        print("%s\t%s\t%s" % (pod.metadata.name,
                              pod.status.phase,
                              pod.status.pod_ip))

    del pod
    del pod_list
    del api_instance
    return


def lambda_handler(event, context):

    list_pods()

    return


# Below is the test harness
if __name__ == '__main__':
    request = {"None": "None"}

    lambda_handler(request, None)

