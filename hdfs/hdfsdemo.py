from hdfs3 import HDFileSystem

def read_File_Lines(hdfs_client):
    data = b'hello hadoop\ntest'
    with hdfs_client.open('/tmp/test/test2.txt','wb',replication=1) as f:
        f.write(data)
    with hdfs_client.open('/tmp/test/test2.txt') as f:
        out = f.readline()
        assert len(out) == 2
def path_is_exits(hdfs_client):
    path = '/tmp/test'
    if hdfs_client.exists(path):
        hdfs_client.rm(path)
    else:
        hdfs_client.makedirs(path)
def write_File(hdfs_client):
    text = b'hello hdfs' * 20
    with hdfs_client.open('/tmp/test/test.txt','wb',replication=1) as f:
        f.write(text)
    with hdfs_client.open('/tmp/test/test.txt') as f:
        out = f.read(len(text))
        assert text == out
if __name__ == '__main__':
    hdfs_client = HDFileSystem(host='localhost', port=9000)
    path_is_exits(hdfs_client)
    read_File_Lines(hdfs_client)
    hdfs_client.disconnect()
    print('-' * 20)
    print('success')
