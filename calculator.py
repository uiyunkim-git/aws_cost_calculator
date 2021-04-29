from cost import s3, aws_lambda, api_gateway
import matplotlib.pyplot as plt
import numpy as np

requests = 30000
s3_read_each_call_in_gigabyte = 0.0859375
s3_storage_usage_in_gigabyte = 5
lambda_memory = 2048
lambda_runtime = 24359

cost = 0
cost += s3.S3_COST_PER_GET_REQUEST(requests,False)
cost += s3.S3_COST_PER_PUT_REQUEST(requests,False)
cost += s3.S3_COST_STORED_AMOUNT(s3_storage_usage_in_gigabyte,False)
cost += s3.S3_COST_OUTBOUND_TRAFFIC(s3_read_each_call_in_gigabyte * requests,False)
cost += aws_lambda.LAMBDA_COST(requests,lambda_memory,lambda_runtime)
cost += api_gateway.API_GATEWAY_REST_REQUEST(requests,False)

print()
print(cost,"TOTAL")
# plt.plot([calculation(x) for x in np.linspace(0,requests,5,dtype=int)])
# plt.show()

