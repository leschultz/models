import pandas as pd
import docker
import os


def predict(df, container_name):

    df.to_csv('/tmp/test.csv', index=False)
    client = docker.from_env()
    x = client.containers.run(
                              'leschultz/cmg:latest',
                              '/bin/bash run.sh',
                              volumes=['/tmp:/mnt'],
                              )

    df = pd.read_csv('/tmp/prediction.csv')

    return df


container_name = 'leschultz/cmg:latest'

X = [[1, 2], [2,3]]
X = pd.DataFrame(X)

y = predict(X, container_name)
print(y)
