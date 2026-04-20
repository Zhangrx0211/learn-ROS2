"""  
    需求：编写客户端，发送两个整型变量作为请求数据，并处理响应结果。
    步骤：
        1.导包；
        2.初始化 ROS2 客户端；
        3.定义节点类；
            3-1.创建客户端；
            3-2.等待服务连接；
            3-3.组织请求数据并发送；
        4.创建对象调用其功能，处理响应结果；
        5.释放资源。

"""
# 1.导包；
import sys
import rclpy
from rclpy.node import Node
from base_interfaces_demo.srv import Add
import sys

# 3.定义节点类； response.sum))
class MinimalClient(Node):
    

    def __init__(self):
        super().__init__('minimal_client_py')

        # ***3-1.创建客户端；
        self.cli = self.create_client(Add, 'add_ints')

        # ***3-2.等待服务连接；如果1秒内连接不上，循环下面的这个语句。
        while not self.cli.wait_for_service(timeout_sec=1.0):
            self.get_logger().info('服务连接中，请稍候...')
        

    # # 3-3.组织请求数据并发送；
    # def send_request(self):
    #     #创建Add接口的请求
    #     req = Add.Request()
    #     req.num1 = int(sys.argv[1])
    #     req.num2 = int(sys.argv[2])
    #     #发送请求
    #     self.future = self.cli.call_async(self.req)

        # 创建请求
        self.req = Add.Request()
        self.req.num1 = 3
        self.req.num2 = 5

       # 发送请求（异步）
        self.future = self.cli.call_async(self.req)

        # 设置回调，服务端处理完——执行callback
        self.future.add_done_callback(self.callback)
        
    #***接受结果
    def callback(self, future):
        result = future.result() #获取返回值
        self.get_logger().info(f'结果: {result.sum}')
 


def main():
    # 2.初始化 ROS2 客户端；
    rclpy.init()
    client = MinimalClient()

    rclpy.spin(client)

    # #发送请求
    # client.send_request()

    # # 负责接受服务端响应回来的结果。
    # rclpy.spin_until_future_complete(client,client.future)
    
    # try:
    #     response = client.future.result()
    # except Exception as e:
    #     client.get_logger().info('服务请求失败： %r' % (e,))
    # else:
    #     client.get_logger().info('响应结果： %d + %d = %d' %( response.sum))

    # # 5.释放资源。
    rclpy.shutdown()


if __name__ == '__main__':
    main()